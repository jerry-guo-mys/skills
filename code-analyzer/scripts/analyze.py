#!/usr/bin/env python3
"""
Code Analyzer Pro - Advanced codebase analysis with AI-powered insights
Generates comprehensive reports with issues, recommendations, and quality scores.
"""

import os
import sys
import ast
import json
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from datetime import datetime
import re


# ============================================================================
# Data Classes for Analysis Results
# ============================================================================

@dataclass
class CodeIssue:
    """Represents a code quality issue"""
    severity: str  # critical, major, minor
    category: str  # architecture, complexity, security, etc.
    title: str
    description: str
    location: str
    impact: str
    recommendation: str
    priority: int = 1  # 1-5, 1 is highest


@dataclass
class QualityMetrics:
    """Quality metrics for a codebase"""
    maintainability_score: int = 0
    testability_score: int = 0
    documentation_score: int = 0
    complexity_score: int = 0
    overall_score: int = 0
    
    def calculate_overall(self):
        weights = {
            'maintainability_score': 0.35,
            'testability_score': 0.25,
            'documentation_score': 0.20,
            'complexity_score': 0.20
        }
        self.overall_score = int(
            self.maintainability_score * weights['maintainability_score'] +
            self.testability_score * weights['testability_score'] +
            self.documentation_score * weights['documentation_score'] +
            self.complexity_score * weights['complexity_score']
        )


@dataclass
class ModuleInfo:
    """Information about a code module"""
    name: str
    path: str
    lines: int = 0
    functions: List[str] = field(default_factory=list)
    classes: List[str] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    complexity: int = 0
    dependencies: List[str] = field(default_factory=list)
    dependents: List[str] = field(default_factory=list)


@dataclass
class AnalysisReport:
    """Complete analysis report"""
    timestamp: str = ""
    path: str = ""
    total_files: int = 0
    total_lines: int = 0
    languages: Dict[str, int] = field(default_factory=dict)
    
    # Analysis results
    modules: List[ModuleInfo] = field(default_factory=list)
    issues: List[CodeIssue] = field(default_factory=list)
    metrics: QualityMetrics = field(default_factory=QualityMetrics)
    
    # Architecture
    architecture_style: str = ""
    entry_points: List[str] = field(default_factory=list)
    circular_dependencies: List[List[str]] = field(default_factory=list)
    
    # Recommendations
    quick_wins: List[str] = field(default_factory=list)
    short_term: List[str] = field(default_factory=list)
    long_term: List[str] = field(default_factory=list)


# ============================================================================
# Advanced Code Analyzer
# ============================================================================

class CodeAnalyzerPro:
    """Advanced code analyzer with deep insights"""
    
    SUPPORTED_EXTENSIONS = {
        '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
        '.java': 'java', '.go': 'go', '.rs': 'rust',
        '.c': 'c', '.cpp': 'cpp', '.h': 'c', '.hpp': 'cpp',
        '.cs': 'csharp', '.rb': 'ruby', '.php': 'php', '.swift': 'swift',
        '.sh': 'shell', '.sql': 'sql', '.yaml': 'yaml', '.yml': 'yaml',
        '.json': 'json', '.md': 'markdown', '.toml': 'toml'
    }
    
    def __init__(self, path: str, exclude_patterns: List[str] = None):
        self.root_path = Path(path).resolve()
        self.exclude_patterns = exclude_patterns or [
            'node_modules', 'vendor', '.git', '__pycache__',
            '.venv', 'venv', 'dist', 'build', '.idea', '.vscode',
            'target', 'bin', 'obj', '.DS_Store'
        ]
        self.files = []
        self.modules: Dict[str, ModuleInfo] = {}
        self.issues: List[CodeIssue] = []
        self.report = AnalysisReport()
    
    def should_include(self, file_path: Path) -> bool:
        """Check if file should be included"""
        path_str = str(file_path)
        for pattern in self.exclude_patterns:
            if pattern in path_str:
                return False
        return file_path.suffix in self.SUPPORTED_EXTENSIONS
    
    def discover_files(self) -> List[Path]:
        """Discover all relevant files"""
        self.files = []
        if self.root_path.is_file():
            if self.should_include(self.root_path):
                self.files.append(self.root_path)
        else:
            for file_path in self.root_path.rglob('*'):
                if file_path.is_file() and self.should_include(file_path):
                    self.files.append(file_path)
        return self.files
    
    def analyze_file(self, file_path: Path) -> ModuleInfo:
        """Analyze a single file"""
        rel_path = str(file_path.relative_to(self.root_path))
        module = ModuleInfo(name=file_path.stem, path=rel_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                module.lines = len(lines)
                
                lang = self.SUPPORTED_EXTENSIONS.get(file_path.suffix, 'unknown')
                
                if lang == 'python':
                    self._analyze_python(content, module)
                elif lang in ['javascript', 'typescript']:
                    self._analyze_js(content, module)
                elif lang == 'java':
                    self._analyze_java(content, module)
                elif lang == 'go':
                    self._analyze_go(content, module)
                elif lang == 'rust':
                    self._analyze_rust(content, module)
        
        except Exception as e:
            module.dependencies.append(f"Error: {str(e)}")
        
        return module
    
    def _analyze_python(self, content: str, module: ModuleInfo):
        """Analyze Python code"""
        # Imports
        import_pattern = r'^(?:from\s+(\S+)\s+import|import\s+(\S+))'
        for match in re.finditer(import_pattern, content, re.MULTILINE):
            imp = match.group(1) or match.group(2)
            if imp:
                module.imports.append(imp.split('.')[0])
        
        # Functions
        func_pattern = r'^def\s+(\w+)\s*\('
        module.functions = re.findall(func_pattern, content, re.MULTILINE)
        
        # Classes
        class_pattern = r'^class\s+(\w+)'
        module.classes = re.findall(class_pattern, content, re.MULTILINE)
        
        # Complexity
        module.complexity = self._calculate_complexity(content)
    
    def _analyze_js(self, content: str, module: ModuleInfo):
        """Analyze JavaScript/TypeScript"""
        import_pattern = r"(?:import|require)\s*\(?['\"]([^'\"]+)['\"]"
        module.imports = re.findall(import_pattern, content)
        
        func_patterns = [
            r'function\s+(\w+)',
            r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?\(',
        ]
        for pattern in func_patterns:
            module.functions.extend(re.findall(pattern, content))
        
        class_pattern = r'class\s+(\w+)'
        module.classes = re.findall(class_pattern, content)
        module.complexity = self._calculate_complexity(content)
    
    def _analyze_java(self, content: str, module: ModuleInfo):
        """Analyze Java"""
        import_pattern = r'^import\s+(\S+)'
        module.imports = re.findall(import_pattern, content, re.MULTILINE)
        
        class_pattern = r'(?:public\s+|private\s+)?class\s+(\w+)'
        module.classes = re.findall(class_pattern, content)
        
        method_pattern = r'(?:public|private|protected)\s+\w+\s+(\w+)\s*\('
        module.functions = re.findall(method_pattern, content)
        module.complexity = self._calculate_complexity(content)
    
    def _analyze_go(self, content: str, module: ModuleInfo):
        """Analyze Go"""
        import_pattern = r'["\']([^"\']+)["\']'
        module.imports = re.findall(import_pattern, content)
        
        func_pattern = r'^func\s+(?:\([^)]+\)\s+)?(\w+)'
        module.functions = re.findall(func_pattern, content, re.MULTILINE)
        
        struct_pattern = r'type\s+(\w+)\s+struct'
        module.classes = re.findall(struct_pattern, content)
        module.complexity = self._calculate_complexity(content)
    
    def _analyze_rust(self, content: str, module: ModuleInfo):
        """Analyze Rust"""
        use_pattern = r'^use\s+([^;]+)'
        module.imports = re.findall(use_pattern, content, re.MULTILINE)
        
        func_pattern = r'^fn\s+(\w+)'
        module.functions = re.findall(func_pattern, content, re.MULTILINE)
        
        struct_pattern = r'struct\s+(\w+)'
        module.classes = re.findall(struct_pattern, content)
        module.complexity = self._calculate_complexity(content)
    
    def _calculate_complexity(self, content: str) -> int:
        """Calculate cyclomatic complexity"""
        complexity = 1
        decision_patterns = [
            r'\bif\b', r'\belif\b', r'\belse\b',
            r'\bfor\b', r'\bwhile\b',
            r'\band\b', r'\bor\b',
            r'\bexcept\b', r'\bcatch\b',
            r'\?\.', r'\?\?'  # Optional chaining
        ]
        for pattern in decision_patterns:
            complexity += len(re.findall(pattern, content))
        return min(complexity, 50)
    
    def detect_architecture(self) -> str:
        """Detect architecture style"""
        patterns = {
            'MVC': ['controller', 'model', 'view', 'controllers', 'models', 'views'],
            'Clean Architecture': ['domain', 'application', 'infrastructure', 'presentation'],
            'Microservices': ['service', 'gateway', 'api', 'microservice'],
            'Layered': ['api', 'service', 'repository', 'data'],
            'Hexagonal': ['adapter', 'port', 'domain', 'application']
        }
        
        dir_names = set()
        for file_path in self.files:
            rel_path = str(file_path.relative_to(self.root_path))
            parts = rel_path.split(os.sep)
            if len(parts) > 1:
                dir_names.add(parts[0].lower())
        
        detected = []
        for arch, keywords in patterns.items():
            matches = sum(1 for kw in keywords if kw in dir_names)
            if matches >= 2:
                detected.append(arch)
        
        return detected[0] if detected else 'Unknown/Mixed'
    
    def find_circular_dependencies(self) -> List[List[str]]:
        """Find circular dependencies"""
        # Build dependency graph
        graph = defaultdict(set)
        for name, module in self.modules.items():
            for imp in module.imports:
                graph[name].add(imp)
        
        # Find cycles using DFS
        cycles = []
        visited = set()
        rec_stack = set()
        path = []
        
        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    # Found cycle
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    cycles.append(cycle)
            
            path.pop()
            rec_stack.remove(node)
            return False
        
        for node in graph:
            if node not in visited:
                dfs(node)
        
        return cycles[:10]  # Limit to 10 cycles
    
    def identify_issues(self):
        """Identify code quality issues"""
        self.issues = []
        
        for name, module in self.modules.items():
            # High complexity
            if module.complexity > 20:
                self.issues.append(CodeIssue(
                    severity='major',
                    category='complexity',
                    title=f'High complexity in {module.name}',
                    description=f'Complexity score: {module.complexity}',
                    location=module.path,
                    impact='Hard to understand, test, and maintain',
                    recommendation='Break down into smaller functions/classes',
                    priority=2
                ))
            
            # Large files
            if module.lines > 500:
                self.issues.append(CodeIssue(
                    severity='minor',
                    category='maintainability',
                    title=f'Large file: {module.name}',
                    description=f'{module.lines} lines of code',
                    location=module.path,
                    impact='Difficult to navigate and understand',
                    recommendation='Split into smaller modules',
                    priority=3
                ))
            
            # Too many imports (potential god module)
            if len(module.imports) > 20:
                self.issues.append(CodeIssue(
                    severity='major',
                    category='architecture',
                    title=f'Too many dependencies: {module.name}',
                    description=f'{len(module.imports)} imports',
                    location=module.path,
                    impact='High coupling, hard to test',
                    recommendation='Consider dependency injection or facade pattern',
                    priority=2
                ))
        
        # Circular dependencies
        cycles = self.find_circular_dependencies()
        for cycle in cycles:
            self.issues.append(CodeIssue(
                severity='critical',
                category='architecture',
                title='Circular dependency detected',
                description=' → '.join(cycle),
                location=cycle[0],
                impact='Cannot test modules independently, tight coupling',
                recommendation='Introduce interface/abstraction layer',
                priority=1
            ))
        
        # Sort by priority
        self.issues.sort(key=lambda x: x.priority)
    
    def calculate_metrics(self) -> QualityMetrics:
        """Calculate quality metrics"""
        metrics = QualityMetrics()
        
        if not self.modules:
            return metrics
        
        # Maintainability: based on complexity and file size
        avg_complexity = sum(m.complexity for m in self.modules.values()) / len(self.modules)
        avg_lines = sum(m.lines for m in self.modules.values()) / len(self.modules)
        
        metrics.maintainability_score = max(0, 100 - int(avg_complexity * 2) - int(avg_lines / 50))
        
        # Testability: based on modularity
        avg_imports = sum(len(m.imports) for m in self.modules.values()) / len(self.modules)
        metrics.testability_score = max(0, 100 - int(avg_imports * 3))
        
        # Documentation: check for docstrings/comments
        doc_count = 0
        for file_path in self.files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if '"""' in content or "'''" in content or '//' in content or '#' in content:
                        doc_count += 1
            except:
                pass
        
        metrics.documentation_score = int((doc_count / len(self.files)) * 100) if self.files else 0
        
        # Complexity score (inverse)
        metrics.complexity_score = max(0, 100 - int(avg_complexity * 3))
        
        metrics.calculate_overall()
        return metrics
    
    def generate_recommendations(self):
        """Generate improvement recommendations"""
        report = self.report
        
        # Quick wins (can be done in hours)
        report.quick_wins = [
            "Add type hints to public functions",
            "Add docstrings to modules and classes",
            "Remove unused imports",
            "Add .gitignore for generated files"
        ]
        
        # Short term (1-2 weeks)
        critical_issues = [i for i in self.issues if i.severity == 'critical']
        major_issues = [i for i in self.issues if i.severity == 'major']
        
        if critical_issues:
            report.short_term.append("Fix circular dependencies")
        if major_issues:
            report.short_term.append("Refactor high-complexity modules")
        report.short_term.extend([
            "Add unit tests for core modules",
            "Set up CI/CD pipeline",
            "Configure linting rules"
        ])
        
        # Long term (1-3 months)
        report.long_term = [
            "Consider architectural refactoring",
            "Improve test coverage to >80%",
            "Add comprehensive API documentation",
            "Implement code review process"
        ]
    
    def run(self, output: Optional[str] = None) -> AnalysisReport:
        """Run complete analysis"""
        print(f"🔍 Analyzing: {self.root_path}")
        
        # Discover and analyze files
        self.discover_files()
        print(f"📁 Found {len(self.files)} files")
        
        for file_path in self.files:
            module = self.analyze_file(file_path)
            self.modules[module.name] = module
        
        # Build report
        self.report.timestamp = datetime.now().isoformat()
        self.report.path = str(self.root_path)
        self.report.total_files = len(self.files)
        self.report.total_lines = sum(m.lines for m in self.modules.values())
        
        # Languages
        lang_count = defaultdict(int)
        for module in self.modules.values():
            ext = Path(module.path).suffix
            lang = self.SUPPORTED_EXTENSIONS.get(ext, 'unknown')
            lang_count[lang] += 1
        self.report.languages = dict(lang_count)
        
        # Architecture
        self.report.architecture_style = self.detect_architecture()
        self.report.modules = list(self.modules.values())
        
        # Issues and metrics
        self.identify_issues()
        self.report.issues = self.issues
        self.report.metrics = self.calculate_metrics()
        
        # Recommendations
        self.generate_recommendations()
        
        # Entry points
        for module in self.modules.values():
            if any(p in module.name.lower() for p in ['main', 'index', 'app', 'cli']):
                self.report.entry_points.append(module.path)
        
        print("✅ Analysis complete")
        
        # Output
        if output:
            self.export_report(output)
            print(f"📝 Report saved to: {output}")
        
        return self.report
    
    def export_report(self, output_path: str):
        """Export report as Markdown"""
        report = self.report
        
        md = []
        md.append("# 🔍 Code Analysis Report\n")
        md.append(f"**Generated:** {report.timestamp}\n")
        md.append(f"**Path:** {report.path}\n")
        
        # Executive Summary
        md.append("\n## 📊 Executive Summary\n")
        md.append(f"- **Overall Score:** {report.metrics.overall_score}/100")
        md.append(f"- **Total Files:** {report.total_files}")
        md.append(f"- **Total Lines:** {report.total_lines:,}")
        md.append(f"- **Architecture:** {report.architecture_style}")
        md.append(f"- **Issues Found:** {len(report.issues)}\n")
        
        # Quality Metrics
        md.append("\n## 📈 Quality Metrics\n")
        md.append("| Metric | Score | Status |")
        md.append("|--------|-------|--------|")
        md.append(f"| Maintainability | {report.metrics.maintainability_score}/100 | {self._status(report.metrics.maintainability_score)} |")
        md.append(f"| Testability | {report.metrics.testability_score}/100 | {self._status(report.metrics.testability_score)} |")
        md.append(f"| Documentation | {report.metrics.documentation_score}/100 | {self._status(report.metrics.documentation_score)} |")
        md.append(f"| Complexity | {report.metrics.complexity_score}/100 | {self._status(report.metrics.complexity_score)} |")
        
        # Issues
        if report.issues:
            md.append("\n## ⚠️ Issues Found\n")
            by_severity = defaultdict(list)
            for issue in report.issues:
                by_severity[issue.severity].append(issue)
            
            for severity in ['critical', 'major', 'minor']:
                if severity in by_severity:
                    md.append(f"\n### {severity.upper()} ({len(by_severity[severity])})\n")
                    for issue in by_severity[severity][:5]:  # Top 5
                        md.append(f"**{issue.title}**\n")
                        md.append(f"- Location: `{issue.location}`")
                        md.append(f"- Impact: {issue.impact}")
                        md.append(f"- Recommendation: {issue.recommendation}\n")
        
        # Recommendations
        md.append("\n## 🎯 Recommendations\n")
        
        md.append("\n### Quick Wins (Hours)\n")
        for item in report.quick_wins:
            md.append(f"- [ ] {item}")
        
        md.append("\n### Short Term (1-2 Weeks)\n")
        for item in report.short_term:
            md.append(f"- [ ] {item}")
        
        md.append("\n### Long Term (1-3 Months)\n")
        for item in report.long_term:
            md.append(f"- [ ] {item}")
        
        # Write file
        with open(output_path, 'w') as f:
            f.write('\n'.join(md))
    
    def _status(self, score: int) -> str:
        """Get status emoji for score"""
        if score >= 80:
            return "✅ Excellent"
        elif score >= 60:
            return "⚠️ Needs Improvement"
        else:
            return "❌ Critical"


# ============================================================================
# Main Entry Point
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='Code Analyzer Pro')
    parser.add_argument('--path', '-p', default='.', help='Path to codebase')
    parser.add_argument('--output', '-o', help='Output file (Markdown)')
    parser.add_argument('--exclude', '-e', help='Exclude patterns (comma-separated)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    exclude = args.exclude.split(',') if args.exclude else None
    analyzer = CodeAnalyzerPro(args.path, exclude_patterns=exclude)
    report = analyzer.run(output=args.output)
    
    if not args.output:
        # Print summary to console
        print("\n" + "="*60)
        print(f"Overall Score: {report.metrics.overall_score}/100")
        print(f"Files: {report.total_files} | Lines: {report.total_lines:,}")
        print(f"Issues: {len(report.issues)}")
        
        if report.issues:
            print("\nTop Issues:")
            for issue in report.issues[:3]:
                print(f"  - [{issue.severity.upper()}] {issue.title}")


if __name__ == '__main__':
    main()
