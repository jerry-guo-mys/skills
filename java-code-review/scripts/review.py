#!/usr/bin/env python3
"""
Java Code Review - Automatic code review tool for Java projects
"""

import argparse
import re
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict


class JavaCodeReviewer:
    """Java code review engine"""
    
    def __init__(self, path: str):
        self.root_path = Path(path)
        self.issues = defaultdict(list)
        self.stats = {
            'files': 0,
            'lines': 0,
            'classes': 0,
            'methods': 0
        }
    
    def scan(self) -> list:
        """Scan Java files"""
        print(f"🔍 扫描 Java 项目：{self.root_path}")
        
        java_files = list(self.root_path.rglob('*.java'))
        print(f"  找到 {len(java_files)} 个 Java 文件")
        
        for file_path in java_files:
            self._review_file(file_path)
        
        return java_files
    
    def _review_file(self, file_path: Path):
        """Review a single Java file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
            
            self.stats['files'] += 1
            self.stats['lines'] += len(lines)
            
            # Run all checks
            self._check_naming(file_path, content, lines)
            self._check_code_smell(file_path, content, lines)
            self._check_security(file_path, content, lines)
            self._check_performance(file_path, content, lines)
            self._check_concurrency(file_path, content, lines)
            
        except Exception as e:
            print(f"  ⚠️ 读取失败 {file_path}: {e}")
    
    def _check_naming(self, file_path: Path, content: str, lines: list):
        """Check naming conventions"""
        filename = file_path.name
        
        # Class name should match filename
        class_match = re.search(r'public\s+class\s+(\w+)', content)
        if class_match:
            class_name = class_match.group(1)
            if class_name != filename.replace('.java', ''):
                self.issues['major'].append({
                    'type': '命名规范',
                    'location': str(file_path),
                    'description': f'类名 {class_name} 与文件名不匹配',
                    'suggestion': '类名应与文件名保持一致'
                })
        
        # Check method names (should be camelCase)
        for i, line in enumerate(lines, 1):
            if re.search(r'\b(public|private|protected)\s+\w+\s+[a-z]\w*\s*\(', line):
                # Good - camelCase
                pass
            elif re.search(r'\b(public|private|protected)\s+\w+\s+[A-Z]\w*\s*\(', line):
                self.issues['minor'].append({
                    'type': '命名规范',
                    'location': f'{file_path}:{i}',
                    'description': '方法名应使用 camelCase',
                    'line': line.strip()
                })
    
    def _check_code_smell(self, file_path: Path, content: str, lines: list):
        """Check code smells"""
        # Check method length
        method_pattern = r'(public|private|protected).*?\s+(\w+)\s*\([^)]*\)\s*\{'
        for match in re.finditer(method_pattern, content):
            method_name = match.group(2)
            start = match.end()
            
            # Count braces to find method end
            brace_count = 1
            end = start
            for i in range(start, len(content)):
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        end = i
                        break
            
            method_lines = content[start:end].count('\n')
            if method_lines > 50:
                self.issues['major'].append({
                    'type': '代码异味',
                    'location': f'{file_path}',
                    'description': f'方法过长：{method_name}() ({method_lines}行)',
                    'suggestion': '拆分为多个小方法（建议<50 行）'
                })
        
        # Check class length
        if len(lines) > 500:
            self.issues['major'].append({
                'type': '代码异味',
                'location': str(file_path),
                'description': f'类过大 ({len(lines)}行)',
                'suggestion': '按职责拆分（建议<500 行）'
            })
        
        # Check parameter count
        param_pattern = r'\w+\s*\(([^)]+)\)'
        for match in re.finditer(param_pattern, content):
            params = match.group(1).split(',')
            if len(params) > 5 and 'class' not in match.group(0):
                self.issues['minor'].append({
                    'type': '代码异味',
                    'location': f'{file_path}',
                    'description': f'方法参数过多 ({len(params)}个)',
                    'suggestion': '使用参数对象或 Builder 模式'
                })
    
    def _check_security(self, file_path: Path, content: str, lines: list):
        """Check security vulnerabilities"""
        # SQL Injection
        sql_pattern = r'["\']SELECT.*?\+.*?["\']|["\']INSERT.*?\+.*?["\']|["\']UPDATE.*?\+.*?["\']|["\']DELETE.*?\+.*?["\']'
        for i, line in enumerate(lines, 1):
            if re.search(sql_pattern, line, re.IGNORECASE):
                self.issues['critical'].append({
                    'type': '安全',
                    'location': f'{file_path}:{i}',
                    'description': 'SQL 注入风险 - 字符串拼接 SQL',
                    'line': line.strip(),
                    'suggestion': '使用 PreparedStatement 或参数化查询'
                })
        
        # Hardcoded passwords
        password_pattern = r'(password|passwd|pwd|secret)\s*[=:]\s*["\'][^"\']+["\']'
        for i, line in enumerate(lines, 1):
            if re.search(password_pattern, line, re.IGNORECASE):
                self.issues['critical'].append({
                    'type': '安全',
                    'location': f'{file_path}:{i}',
                    'description': '硬编码密码/密钥',
                    'line': line.strip(),
                    'suggestion': '使用环境变量或配置中心'
                })
        
        # XSS - unescaped user input
        xss_pattern = r'\.getParameter\([^)]+\)|request\([^)]+\)'
        for i, line in enumerate(lines, 1):
            if re.search(xss_pattern, line):
                if 'escape' not in line and 'encode' not in line:
                    self.issues['major'].append({
                        'type': '安全',
                        'location': f'{file_path}:{i}',
                        'description': '潜在的 XSS 风险 - 用户输入未转义',
                        'line': line.strip(),
                        'suggestion': '对用户输入进行 HTML 转义'
                    })
    
    def _check_performance(self, file_path: Path, content: str, lines: list):
        """Check performance issues"""
        # N+1 query in loop
        loop_pattern = r'for\s*\([^)]+\)\s*\{[^}]*\.find\([^)]*\)|for\s*\([^)]+\)\s*\{[^}]*\.get\([^)]*\)'
        for i, line in enumerate(lines, 1):
            if re.search(loop_pattern, line, re.IGNORECASE):
                self.issues['major'].append({
                    'type': '性能',
                    'location': f'{file_path}:{i}',
                    'description': 'N+1 查询风险 - 循环中查询数据库',
                    'line': line.strip(),
                    'suggestion': '使用批量查询或 JOIN'
                })
        
        # Resource not closed
        resource_pattern = r'(new\s+FileInputStream|new\s+FileOutputStream|new\s+BufferedReader|new\s+InputStreamReader)\s*\('
        for i, line in enumerate(lines, 1):
            if re.search(resource_pattern, line):
                # Check if in try-with-resources
                context_start = max(0, i - 5)
                context = '\n'.join(lines[context_start:i])
                if 'try (' not in context and 'try(' not in context:
                    self.issues['major'].append({
                        'type': '性能',
                        'location': f'{file_path}:{i}',
                        'description': '资源未关闭 - 可能导致内存泄漏',
                        'line': line.strip(),
                        'suggestion': '使用 try-with-resources'
                    })
        
        # String concatenation in loop
        concat_pattern = r'for\s*\([^)]+\)\s*\{[^}]*\+=[^}]*\}'
        for i, line in enumerate(lines, 1):
            if 'String' in line and '+=' in line:
                self.issues['minor'].append({
                    'type': '性能',
                    'location': f'{file_path}:{i}',
                    'description': '字符串拼接性能问题',
                    'line': line.strip(),
                    'suggestion': '使用 StringBuilder'
                })
    
    def _check_concurrency(self, file_path: Path, content: str, lines: list):
        """Check concurrency issues"""
        # Non-thread-safe collection
        unsafe_pattern = r'(HashMap|ArrayList|HashSet)\s*<[^>]+>\s+\w+\s*='
        for i, line in enumerate(lines, 1):
            if re.search(unsafe_pattern, line):
                # Check if it's static or shared
                if 'static' in line or 'public' in line:
                    self.issues['major'].append({
                        'type': '并发',
                        'location': f'{file_path}:{i}',
                        'description': '线程安全问题 - 使用非线程安全集合',
                        'line': line.strip(),
                        'suggestion': '使用 ConcurrentHashMap/CopyOnWriteArrayList'
                    })
        
        # Synchronized method (potential performance issue)
        sync_pattern = r'public\s+synchronized\s+\w+'
        for i, line in enumerate(lines, 1):
            if re.search(sync_pattern, line):
                self.issues['minor'].append({
                    'type': '并发',
                    'location': f'{file_path}:{i}',
                    'description': '同步方法 - 可能影响性能',
                    'line': line.strip(),
                    'suggestion': '考虑使用更细粒度的锁或无锁设计'
                })
    
    def generate_report(self, output: str):
        """Generate review report"""
        total_issues = sum(len(v) for v in self.issues.values())
        
        # Calculate score
        score = 100
        score -= len(self.issues['critical']) * 10
        score -= len(self.issues['major']) * 5
        score -= len(self.issues['minor']) * 2
        score = max(0, min(100, score))
        
        report = f"""# Java 代码审查报告

**审查时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**审查路径:** {self.root_path}  
**审查文件:** {self.stats['files']} 个  
**总代码行数:** {self.stats['lines']:,}

---

## 📊 总体评分：{score}/100 {'✅' if score >= 80 else '⚠️' if score >= 60 else '❌'}

| 类型 | 问题数 | 占比 |
|------|--------|------|
| 🔴 严重 | {len(self.issues['critical'])} | {len(self.issues['critical']) * 100 // max(1, total_issues)}% |
| 🟡 主要 | {len(self.issues['major'])} | {len(self.issues['major']) * 100 // max(1, total_issues)}% |
| 🟢 次要 | {len(self.issues['minor'])} | {len(self.issues['minor']) * 100 // max(1, total_issues)}% |

---

"""
        
        if self.issues['critical']:
            report += "## 🔴 严重问题 ({})\n\n".format(len(self.issues['critical']))
            for i, issue in enumerate(self.issues['critical'][:10], 1):
                report += f"### {i}. [{issue['type']}] {issue['description']}\n"
                report += f"**位置:** `{issue['location']}`\n"
                if 'line' in issue:
                    report += f"**代码:**\n```java\n{issue['line']}\n```\n"
                if 'suggestion' in issue:
                    report += f"**建议:** {issue['suggestion']}\n"
                report += "\n"
        
        if self.issues['major']:
            report += "## 🟡 主要问题 ({})\n\n".format(len(self.issues['major']))
            for i, issue in enumerate(self.issues['major'][:10], 1):
                report += f"### {i}. [{issue['type']}] {issue['description']}\n"
                report += f"**位置:** `{issue['location']}`\n"
                if 'suggestion' in issue:
                    report += f"**建议:** {issue['suggestion']}\n"
                report += "\n"
        
        if self.issues['minor']:
            report += "## 🟢 次要问题 ({})\n\n".format(len(self.issues['minor']))
            for i, issue in enumerate(self.issues['minor'][:10], 1):
                report += f"{i}. **[{issue['type']}]** {issue['description']} - `{issue['location']}`\n"
        
        report += f"""
---

## 📋 改进建议

### 立即修复
"""
        if self.issues['critical']:
            report += "- [ ] 修复所有严重安全问题\n"
            report += "- [ ] 修复资源泄漏问题\n"
        
        report += """
### 短期优化
- [ ] 重构过长的方法
- [ ] 优化性能问题
- [ ] 修复线程安全问题

### 长期改进
- [ ] 引入代码审查 checklist
- [ ] 配置 CI 自动检查
- [ ] 建立代码规范文档
"""
        
        output_path = Path(output)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ 审查报告已生成：{output_path}")
        print(f"📊 总体评分：{score}/100")
        print(f"🔴 严重：{len(self.issues['critical'])} | 🟡 主要：{len(self.issues['major'])} | 🟢 次要：{len(self.issues['minor'])}")


def main():
    parser = argparse.ArgumentParser(description='Java Code Review Tool')
    parser.add_argument('--path', '-p', default='.', help='Path to Java source code')
    parser.add_argument('--output', '-o', default='代码审查报告.md', help='Output file')
    parser.add_argument('--check', '-c', choices=['all', 'security', 'performance', 'naming'], 
                       default='all', help='Check type')
    
    args = parser.parse_args()
    
    reviewer = JavaCodeReviewer(args.path)
    reviewer.scan()
    reviewer.generate_report(args.output)


if __name__ == '__main__':
    main()
