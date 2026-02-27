#!/usr/bin/env python3
"""
GitHub Issues Collector - Automatically collect feedback from GitHub Issues
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path


def collect_github_issues(repo: str, token: str = None, output: str = 'github-feedback.md'):
    """Collect issues from GitHub"""
    
    print(f"🐙 从 GitHub 收集反馈：{repo}")
    
    # Try to use GitHub API if token provided
    issues = []
    
    if token:
        # Use GitHub API
        import urllib.request
        import urllib.error
        
        url = f"https://api.github.com/repos/{repo}/issues?state=all&per_page=100"
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {token}'
        }
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                issues = data[:50]  # Limit to 50 issues
                print(f"  ✅ 获取到 {len(issues)} 个 Issues")
        except Exception as e:
            print(f"  ⚠️ API 请求失败：{e}")
            print(f"  📝 使用模板模式")
    else:
        print(f"  ℹ️ 未提供 GitHub Token，使用模板模式")
        print(f"  💡 获取 Token: https://github.com/settings/tokens")
    
    # Generate report
    report = f"""# GitHub Issues 反馈收集

**仓库:** {repo}  
**收集时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Issues 数量:** {len(issues)}

---

## 📊 统计信息

| 状态 | 数量 | 占比 |
|------|------|------|
| **Open** | {sum(1 for i in issues if i.get('state') == 'open')} | {sum(1 for i in issues if i.get('state') == 'open') * 100 // max(1, len(issues))}% |
| **Closed** | {sum(1 for i in issues if i.get('state') == 'closed')} | {sum(1 for i in issues if i.get('state') == 'closed') * 100 // max(1, len(issues))}% |

---

## 🔴 严重问题 (P0)

"""
    
    # Categorize issues
    critical = [i for i in issues if any(label in str(i.get('labels', [])) for label in ['bug', 'critical', 'P0'])]
    major = [i for i in issues if any(label in str(i.get('labels', [])) for label in ['enhancement', 'P1'])]
    minor = [i for i in issues if i.get('state') == 'open' and i not in critical + major]
    
    if critical:
        for issue in critical[:5]:
            report += f"""### #{issue['number']} {issue['title']}

**状态:** {'🟢 已解决' if issue['state'] == 'closed' else '🔴 待解决'}  
**创建时间:** {issue['created_at'][:10]}  
**标签:** {[l['name'] for l in issue.get('labels', [])]}  
**链接:** {issue['html_url']}

**描述:**
{issue.get('body', '无描述')[:500]}

---

"""
    else:
        report += "*暂无严重问题*\n\n---\n\n"
    
    report += f"""## 🟡 主要问题 (P1)

"""
    
    if major:
        for issue in major[:5]:
            report += f"""### #{issue['number']} {issue['title']}

**状态:** {'🟢 已解决' if issue['state'] == 'closed' else '🟡 待解决'}  
**创建时间:** {issue['created_at'][:10]}  
**链接:** {issue['html_url']}

---

"""
    else:
        report += "*暂无主要问题*\n\n---\n\n"
    
    report += f"""## 🟢 其他问题 (P2/P3)

"""
    
    if minor:
        for issue in minor[:10]:
            report += f"- #{issue['number']} {issue['title']} - {issue['html_url']}\n"
    else:
        report += "*暂无其他问题*\n"
    
    report += f"""
---

## 📈 趋势分析

### 月度 Issue 趋势

| 月份 | 新增 | 已解决 | 待解决 |
|------|------|--------|--------|
| 2026-02 | {len(issues)} | {sum(1 for i in issues if i.get('state') == 'closed')} | {sum(1 for i in issues if i.get('state') == 'open')} |

### 标签分布

| 标签 | 数量 |
|------|------|
| bug | {sum(1 for i in issues if any('bug' in str(l) for l in i.get('labels', [])))} |
| enhancement | {sum(1 for i in issues if any('enhancement' in str(l) for l in i.get('labels', [])))} |
| documentation | {sum(1 for i in issues if any('documentation' in str(l) for l in i.get('labels', [])))} |

---

## 💡 改进建议

### 立即处理
- [ ] 解决所有 P0 严重问题
- [ ] 回复所有未回复的 Issues

### 近期改进
- [ ] 处理 P1 主要问题
- [ ] 添加 Issue 模板
- [ ] 建立 Issue 分类规则

### 长期优化
- [ ] 建立 Issue 自动化流程
- [ ] 定期 Issue 清理
- [ ] 用户反馈闭环机制

---

## 🔗 相关链接

- [GitHub Issues](https://github.com/{repo}/issues)
- [反馈收集](反馈收集.md)
- [改进计划](改进计划.md)
"""
    
    output_path = Path(output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ GitHub Issues 报告已生成：{output_path}")
    print(f"\n💡 提示:")
    print(f"1. 提供 GitHub Token 可获取完整数据")
    print(f"2. Token 权限：repo (私有仓库) 或 public_repo (公开仓库)")
    print(f"3. 运行命令：python3 {__file__} --repo user/repo --token YOUR_TOKEN")


def main():
    parser = argparse.ArgumentParser(description='Collect GitHub Issues')
    parser.add_argument('--repo', '-r', required=True, help='GitHub repository (user/repo)')
    parser.add_argument('--token', '-t', help='GitHub Personal Access Token')
    parser.add_argument('--output', '-o', default='github-issues.md', help='Output file')
    
    args = parser.parse_args()
    
    collect_github_issues(args.repo, args.token, args.output)


if __name__ == '__main__':
    main()
