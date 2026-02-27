#!/usr/bin/env python3
"""
Docs Improver - Technical Documentation Analysis, Generation, and Improvement
Analyzes documentation quality, generates missing docs, checks consistency, and provides improvement suggestions.
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict


# ============================================================================
# Data Models
# ============================================================================

@dataclass
class DocQualityReport:
    """Documentation quality assessment"""
    overall_score: int = 0
    completeness_score: int = 0
    accuracy_score: int = 0
    clarity_score: int = 0
    structure_score: int = 0
    maintainability_score: int = 0
    
    issues: List[Dict] = field(default_factory=list)
    critical_issues: List[Dict] = field(default_factory=list)
    major_issues: List[Dict] = field(default_factory=list)
    minor_issues: List[Dict] = field(default_factory=list)
    
    recommendations: Dict[str, List[str]] = field(default_factory=lambda: {
        'quick_wins': [],
        'short_term': [],
        'long_term': []
    })


@dataclass
class DocInventory:
    """Inventory of existing documentation"""
    files: List[Dict] = field(default_factory=list)
    missing_docs: List[str] = field(default_factory=list)
    outdated_docs: List[str] = field(default_factory=list)
    
    # Doc types
    readme: Optional[str] = None
    api_docs: Optional[str] = None
    architecture_docs: Optional[str] = None
    deployment_guide: Optional[str] = None
    dev_guide: Optional[str] = None
    changelog: Optional[str] = None
    contributing: Optional[str] = None


@dataclass
class ConsistencyIssue:
    """Documentation consistency issue"""
    type: str  # api_mismatch, code_example_outdated, diagram_mismatch, etc.
    severity: str  # critical, major, minor
    location: str
    description: str
    expected: str
    actual: str
    fix_suggestion: str


@dataclass
class GeneratedDoc:
    """Generated documentation"""
    filename: str
    content: str
    doc_type: str
    auto_generated: bool = True
    sections: List[str] = field(default_factory=list)


# ============================================================================
# Documentation Analyzer
# ============================================================================

class DocsAnalyzer:
    """Analyze documentation quality and completeness"""
    
    ESSENTIAL_DOCS = [
        'README.md',
        'README.rst',
        'README.txt'
    ]
    
    IMPORTANT_DOCS = [
        'CHANGELOG.md',
        'CONTRIBUTING.md',
        'LICENSE',
        'INSTALL.md',
        'DEPLOYMENT.md',
        'ARCHITECTURE.md',
        'API.md',
        'docs/',
        'documentation/'
    ]
    
    def __init__(self, path: str):
        self.root_path = Path(path).resolve()
        self.inventory = DocInventory()
        self.quality_report = DocQualityReport()
        
    def scan_documentation(self) -> DocInventory:
        """Scan for existing documentation"""
        print(f"📚 Scanning documentation in: {self.root_path}")
        
        # Check root directory
        for item in self.root_path.iterdir():
            if item.is_file():
                self._analyze_file(item)
            elif item.is_dir() and item.name in ['docs', 'documentation', 'doc']:
                self._scan_docs_directory(item)
        
        # Identify missing docs
        self._identify_missing_docs()
        
        return self.inventory
    
    def _analyze_file(self, file_path: Path):
        """Analyze a documentation file"""
        name = file_path.name
        
        file_info = {
            'path': str(file_path.relative_to(self.root_path)),
            'name': name,
            'size': file_path.stat().st_size,
            'lines': 0,
            'last_modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
        }
        
        # Count lines
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                file_info['lines'] = len(content.split('\n'))
                file_info['has_code_examples'] = '```' in content or '    ' in content
                file_info['has_images'] = any(ext in content.lower() for ext in ['.png', '.jpg', '.gif', '.svg'])
                file_info['has_links'] = 'http' in content or 'www.' in content
        except:
            pass
        
        self.inventory.files.append(file_info)
        
        # Categorize
        if name in ['README.md', 'README.rst', 'README.txt']:
            self.inventory.readme = file_info['path']
        elif name in ['CHANGELOG.md', 'HISTORY.md', 'NEWS.md']:
            self.inventory.changelog = file_info['path']
        elif name in ['CONTRIBUTING.md', 'CONTRIBUTE.md']:
            self.inventory.contributing = file_info['path']
        elif name in ['API.md', 'api.md', 'API.rst']:
            self.inventory.api_docs = file_info['path']
        elif name in ['ARCHITECTURE.md', 'architecture.md', 'DESIGN.md']:
            self.inventory.architecture_docs = file_info['path']
        elif name in ['DEPLOYMENT.md', 'deployment.md', 'DEPLOY.md', 'deploy.md']:
            self.inventory.deployment_guide = file_info['path']
        elif name in ['INSTALL.md', 'install.md', 'INSTALLATION.md', 'SETUP.md']:
            self.inventory.dev_guide = file_info['path']
    
    def _scan_docs_directory(self, docs_dir: Path):
        """Scan docs directory"""
        for file_path in docs_dir.rglob('*'):
            if file_path.is_file() and file_path.suffix in ['.md', '.rst', '.txt', '.adoc']:
                self._analyze_file(file_path)
    
    def _identify_missing_docs(self):
        """Identify missing essential documentation"""
        if not self.inventory.readme:
            self.inventory.missing_docs.append('README.md')
        
        # Check for code to determine what docs are needed
        has_api = self._detect_api_code()
        if has_api and not self.inventory.api_docs:
            self.inventory.missing_docs.append('API.md')
        
        has_complex_architecture = self._detect_complex_architecture()
        if has_complex_architecture and not self.inventory.architecture_docs:
            self.inventory.missing_docs.append('ARCHITECTURE.md')
    
    def _detect_api_code(self) -> bool:
        """Detect if project has API code"""
        api_patterns = ['@app.route', '@router.', 'def api_', 'class ApiController', 'FastAPI', 'Flask', 'Express']
        
        for file_path in self.root_path.rglob('*'):
            if file_path.is_file() and file_path.suffix in ['.py', '.js', '.ts', '.java', '.go', '.rs']:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(10000)  # First 10KB
                        if any(pattern in content for pattern in api_patterns):
                            return True
                except:
                    pass
        return False
    
    def _detect_complex_architecture(self) -> bool:
        """Detect if project has complex architecture"""
        # Check for multiple services/modules
        src_dirs = [d for d in self.root_path.iterdir() if d.is_dir() and d.name in ['src', 'app', 'services', 'modules']]
        return len(src_dirs) > 0 or len(list(self.root_path.iterdir())) > 10
    
    def assess_quality(self, file_path: Optional[str] = None) -> DocQualityReport:
        """Assess documentation quality"""
        print("📊 Assessing documentation quality...")
        
        files_to_assess = []
        if file_path:
            files_to_assess = [f for f in self.inventory.files if f['path'] == file_path]
        else:
            files_to_assess = self.inventory.files
        
        if not files_to_assess:
            self.quality_report.overall_score = 0
            self.quality_report.critical_issues.append({
                'type': 'no_documentation',
                'description': 'No documentation files found',
                'fix': 'Create README.md with project overview'
            })
            return self.quality_report
        
        # Assess each file
        scores = []
        for file_info in files_to_assess:
            score = self._assess_file_quality(file_info)
            scores.append(score)
        
        # Calculate overall score
        if scores:
            self.quality_report.overall_score = sum(s['overall'] for s in scores) // len(scores)
            self.quality_report.completeness_score = sum(s['completeness'] for s in scores) // len(scores)
            self.quality_report.accuracy_score = sum(s['accuracy'] for s in scores) // len(scores)
            self.quality_report.clarity_score = sum(s['clarity'] for s in scores) // len(scores)
            self.quality_report.structure_score = sum(s['structure'] for s in scores) // len(scores)
            self.quality_report.maintainability_score = sum(s['maintainability'] for s in scores) // len(scores)
        
        # Generate recommendations
        self._generate_recommendations()
        
        return self.quality_report
    
    def _assess_file_quality(self, file_info: Dict) -> Dict:
        """Assess quality of a single file"""
        scores = {
            'overall': 0,
            'completeness': 0,
            'accuracy': 0,
            'clarity': 0,
            'structure': 0,
            'maintainability': 0
        }
        
        file_path = self.root_path / file_info['path']
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            return scores
        
        # Completeness (30%)
        completeness_checks = [
            ('has_title', '#' in content or len(content.split('\n')[0]) < 100),
            ('has_description', len(content) > 200),
            ('has_installation', 'install' in content.lower() or 'setup' in content.lower()),
            ('has_usage', 'usage' in content.lower() or 'example' in content.lower()),
            ('has_code_examples', '```' in content),
        ]
        scores['completeness'] = sum(1 for _, check in completeness_checks if check) * 20
        
        if not any(check for _, check in completeness_checks[:2]):
            self.quality_report.critical_issues.append({
                'type': 'missing_basics',
                'location': file_info['path'],
                'description': 'Missing title or project description',
                'fix': 'Add clear project title and description at the top'
            })
        
        # Clarity (25%)
        clarity_checks = [
            ('has_sections', content.count('#') >= 3),
            ('has_lists', '-' in content or '*' in content or '1.' in content),
            ('readable_length', 200 < len(content) < 50000),
        ]
        scores['clarity'] = sum(1 for _, check in clarity_checks if check) * 33
        
        # Structure (20%)
        structure_score = 0
        if content.count('#') >= 5:
            structure_score += 40
        if '## ' in content:
            structure_score += 30
        if '### ' in content:
            structure_score += 30
        scores['structure'] = structure_score
        
        # Maintainability (15%)
        maintainability_checks = [
            ('has_toc', '## Contents' in content or '## Table' in content or '[toc]' in content.lower()),
            ('has_links', 'http' in content or '](' in content),
            ('not_too_long', len(content) < 30000),
        ]
        scores['maintainability'] = sum(1 for _, check in maintainability_checks if check) * 33
        
        # Accuracy (10%) - Hard to assess automatically
        scores['accuracy'] = 70  # Default, would need code comparison
        
        # Overall weighted score
        scores['overall'] = int(
            scores['completeness'] * 0.30 +
            scores['accuracy'] * 0.10 +
            scores['clarity'] * 0.25 +
            scores['structure'] * 0.20 +
            scores['maintainability'] * 0.15
        )
        
        return scores
    
    def _generate_recommendations(self):
        """Generate improvement recommendations"""
        report = self.quality_report
        
        # Quick wins
        if report.completeness_score < 60:
            report.recommendations['quick_wins'].append('Add project description and badges to README')
        if not any(f.get('has_code_examples') for f in self.inventory.files):
            report.recommendations['quick_wins'].append('Add code examples to show usage')
        
        # Short term
        if self.inventory.missing_docs:
            report.recommendations['short_term'].append(f'Create missing docs: {", ".join(self.inventory.missing_docs[:3])}')
        if report.structure_score < 60:
            report.recommendations['short_term'].append('Improve document structure with clear sections')
        
        # Long term
        report.recommendations['long_term'].append('Set up automated documentation generation')
        report.recommendations['long_term'].append('Create architecture diagrams')
        report.recommendations['long_term'].append('Establish documentation review process')


# ============================================================================
# Documentation Generator
# ============================================================================

class DocsGenerator:
    """Generate documentation from code"""
    
    def __init__(self, path: str):
        self.root_path = Path(path).resolve()
        self.generated_docs: List[GeneratedDoc] = []
        
    def generate_readme(self) -> GeneratedDoc:
        """Generate README.md"""
        print("📝 Generating README.md...")
        
        # Gather project info
        project_name = self.root_path.name
        description = self._extract_description()
        install_steps = self._detect_install_steps()
        usage_examples = self._find_usage_examples()
        
        content = f"""# {project_name.title().replace('-', ' ')}

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

## 📖 Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Development](#development)
- [Contributing](#contributing)

## 📝 About

{description if description else 'A brief description of the project goes here.'}

## 🚀 Installation

```bash
{install_steps if install_steps else '# Clone the repository\ngit clone <repository-url>\n\n# Install dependencies\n# (Add your installation steps here)'}
```

## 💡 Usage

{usage_examples if usage_examples else '```python\n# Example usage\n# Add your usage examples here\n```'}

## 🔌 API

<!-- API documentation will be generated by api-docs.py -->

## 🛠️ Development

```bash
# Setup development environment
# Add your development setup steps here
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) first.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- List any acknowledgments here

"""
        
        doc = GeneratedDoc(
            filename='README.md',
            content=content,
            doc_type='readme',
            sections=['About', 'Installation', 'Usage', 'API', 'Development', 'Contributing']
        )
        
        self.generated_docs.append(doc)
        return doc
    
    def _extract_description(self) -> str:
        """Extract project description from various sources"""
        # Try package.json
        pkg_json = self.root_path / 'package.json'
        if pkg_json.exists():
            try:
                with open(pkg_json) as f:
                    data = json.load(f)
                    if 'description' in data:
                        return data['description']
            except:
                pass
        
        # Try setup.py
        setup_py = self.root_path / 'setup.py'
        if setup_py.exists():
            try:
                with open(setup_py, 'r') as f:
                    content = f.read()
                    match = re.search(r'description=[\'"]([^\'"]+)[\'"]', content)
                    if match:
                        return match.group(1)
            except:
                pass
        
        # Try README if exists
        readme = self.root_path / 'README.md'
        if readme.exists():
            try:
                with open(readme, 'r') as f:
                    lines = f.readlines()
                    # Get first paragraph after title
                    for i, line in enumerate(lines[1:], 1):
                        if line.strip() and not line.startswith('#'):
                            return line.strip()
            except:
                pass
        
        return ''
    
    def _detect_install_steps(self) -> str:
        """Detect installation steps from project files"""
        steps = []
        
        # Check for package.json (Node.js)
        if (self.root_path / 'package.json').exists():
            steps.append('# Install dependencies')
            steps.append('npm install')
        
        # Check for requirements.txt (Python)
        if (self.root_path / 'requirements.txt').exists():
            steps.append('# Install dependencies')
            steps.append('pip install -r requirements.txt')
        
        # Check for Cargo.toml (Rust)
        if (self.root_path / 'Cargo.toml').exists():
            steps.append('# Build the project')
            steps.append('cargo build')
        
        # Check for go.mod (Go)
        if (self.root_path / 'go.mod').exists():
            steps.append('# Download dependencies')
            steps.append('go mod download')
        
        return '\n'.join(steps) if steps else ''
    
    def _find_usage_examples(self) -> str:
        """Find usage examples in code"""
        examples = []
        
        # Look for example files
        for pattern in ['examples/', 'example/', 'demo/', 'sample/']:
            examples_dir = self.root_path / pattern
            if examples_dir.exists():
                for file_path in examples_dir.glob('*'):
                    if file_path.is_file():
                        try:
                            with open(file_path, 'r') as f:
                                content = f.read(2000)
                                examples.append(f"```{file_path.suffix[1:]}\n{content}\n```")
                        except:
                            pass
                break
        
        return '\n\n'.join(examples[:2]) if examples else ''
    
    def generate_api_docs(self) -> GeneratedDoc:
        """Generate API documentation"""
        print("📝 Generating API documentation...")
        
        endpoints = self._extract_api_endpoints()
        
        content = f"""# API Documentation

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

This document describes the API endpoints available in this project.

## Endpoints

"""
        
        if endpoints:
            for endpoint in endpoints:
                content += f"""
### {endpoint.get('method', 'GET')} {endpoint.get('path', '/unknown')}

{endpoint.get('description', 'No description available.')}

**Parameters:**

{self._format_params(endpoint.get('params', []))}

**Response:**

```json
{json.dumps(endpoint.get('response_example', {}), indent=2)}
```

"""
        else:
            content += "\n*No API endpoints detected automatically. Please add API documentation manually.*\n"
        
        doc = GeneratedDoc(
            filename='API.md',
            content=content,
            doc_type='api',
            sections=['Overview', 'Endpoints']
        )
        
        self.generated_docs.append(doc)
        return doc
    
    def _extract_api_endpoints(self) -> List[Dict]:
        """Extract API endpoints from code"""
        endpoints = []
        
        # Python - Flask/FastAPI
        for file_path in self.root_path.rglob('*.py'):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    
                    # Flask routes
                    for match in re.finditer(r'@app\.route\([\'"]([^\'"]+)[\'"](?:,\s*methods=\[([^\]]+)\])?\)', content):
                        path = match.group(1)
                        methods = match.group(2) if match.group(2) else "'GET'"
                        endpoints.append({
                            'method': methods.strip().strip("'\""),
                            'path': path,
                            'file': str(file_path.relative_to(self.root_path)),
                            'description': 'API endpoint',
                            'params': [],
                            'response_example': {}
                        })
                    
                    # FastAPI routes
                    for match in re.finditer(r'@(?:app|router)\.(get|post|put|delete|patch)\([\'"]([^\'"]+)[\'"]', content):
                        method = match.group(1).upper()
                        path = match.group(2)
                        endpoints.append({
                            'method': method,
                            'path': path,
                            'file': str(file_path.relative_to(self.root_path)),
                            'description': 'API endpoint',
                            'params': [],
                            'response_example': {}
                        })
            except:
                pass
        
        return endpoints[:20]  # Limit to 20 endpoints
    
    def _format_params(self, params: List) -> str:
        """Format parameters for documentation"""
        if not params:
            return "*No parameters*"
        
        formatted = []
        for param in params:
            if isinstance(param, dict):
                formatted.append(f"- `{param.get('name', 'unknown')}` ({param.get('type', 'any')}): {param.get('description', '')}")
            else:
                formatted.append(f"- `{param}`")
        
        return '\n'.join(formatted)
    
    def save_all(self, output_dir: Optional[str] = None):
        """Save all generated documents"""
        target_dir = Path(output_dir) if output_dir else self.root_path
        
        for doc in self.generated_docs:
            output_path = target_dir / doc.filename
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(doc.content)
            print(f"✅ Generated: {output_path}")


# ============================================================================
# Consistency Checker
# ============================================================================

class ConsistencyChecker:
    """Check documentation consistency with code"""
    
    def __init__(self, path: str):
        self.root_path = Path(path).resolve()
        self.issues: List[ConsistencyIssue] = []
    
    def check_all(self) -> List[ConsistencyIssue]:
        """Run all consistency checks"""
        print("🔍 Checking documentation consistency...")
        
        self._check_api_docs()
        self._check_code_examples()
        self._check_links()
        
        return self.issues
    
    def _check_api_docs(self):
        """Check API documentation matches actual API"""
        # Find API documentation
        api_docs = None
        for doc_name in ['API.md', 'api.md', 'docs/api.md']:
            doc_path = self.root_path / doc_name
            if doc_path.exists():
                api_docs = doc_path
                break
        
        if not api_docs:
            return
        
        # Extract documented endpoints
        with open(api_docs, 'r') as f:
            doc_content = f.read()
        
        documented_endpoints = set(re.findall(r'(?:GET|POST|PUT|DELETE|PATCH)\s+(/\S+)', doc_content, re.IGNORECASE))
        
        # Extract actual endpoints from code
        actual_endpoints = set()
        for file_path in self.root_path.rglob('*.py'):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    for match in re.finditer(r'@(?:app|router)\.(?:get|post|put|delete|patch)\([\'"]([^\'"]+)[\'"]', content, re.IGNORECASE):
                        actual_endpoints.add(match.group(1))
            except:
                pass
        
        # Find mismatches
        missing_in_docs = actual_endpoints - documented_endpoints
        if missing_in_docs:
            for endpoint in list(missing_in_docs)[:5]:
                self.issues.append(ConsistencyIssue(
                    type='api_mismatch',
                    severity='major',
                    location=str(api_docs),
                    description=f'API endpoint {endpoint} exists in code but not documented',
                    expected='Endpoint should be documented',
                    actual='Not found in API documentation',
                    fix_suggestion=f'Add documentation for {endpoint}'
                ))
    
    def _check_code_examples(self):
        """Check if code examples in docs are up to date"""
        # Look for code examples in markdown files
        for md_file in self.root_path.rglob('*.md'):
            try:
                with open(md_file, 'r') as f:
                    content = f.read()
                
                # Extract code blocks
                code_blocks = re.findall(r'```(?:\w+)?\n(.*?)```', content, re.DOTALL)
                
                for code in code_blocks[:5]:  # Check first 5 code blocks
                    # Check if referenced functions/classes exist
                    for match in re.finditer(r'def\s+(\w+)', code):
                        func_name = match.group(1)
                        if not self._function_exists(func_name):
                            self.issues.append(ConsistencyIssue(
                                type='code_example_outdated',
                                severity='minor',
                                location=str(md_file),
                                description=f'Function {func_name} in code example may not exist',
                                expected='Function should exist in codebase',
                                actual=f'Function {func_name} not found',
                                fix_suggestion='Update or remove the code example'
                            ))
            except:
                pass
    
    def _check_links(self):
        """Check for broken links (basic check)"""
        for md_file in self.root_path.rglob('*.md'):
            try:
                with open(md_file, 'r') as f:
                    content = f.read()
                
                # Extract links
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                
                for text, link in links:
                    if link.startswith('http'):
                        # External link - skip for now (would need HTTP check)
                        pass
                    elif not link.startswith('#'):
                        # Internal link - check if file exists
                        link_path = self.root_path / link.split('#')[0]
                        if not link_path.exists() and link_path.is_absolute() == False:
                            self.issues.append(ConsistencyIssue(
                                type='broken_link',
                                severity='minor',
                                location=str(md_file),
                                description=f'Link to {link} may be broken',
                                expected='Link should point to existing file',
                                actual=f'File not found: {link}',
                                fix_suggestion='Update or remove the link'
                            ))
            except:
                pass
    
    def _function_exists(self, func_name: str) -> bool:
        """Check if a function exists in the codebase"""
        for file_path in self.root_path.rglob('*.py'):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    if f'def {func_name}(' in content:
                        return True
            except:
                pass
        return False


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='Docs Improver - Analyze, Generate, and Improve Documentation')
    parser.add_argument('--path', '-p', default='.', help='Path to project')
    parser.add_argument('--mode', '-m', default='all', 
                       choices=['analyze', 'generate', 'check', 'all'],
                       help='Operation mode')
    parser.add_argument('--output', '-o', help='Output directory for generated docs')
    parser.add_argument('--report', '-r', help='Output file for quality report')
    
    args = parser.parse_args()
    
    print(f"📚 Docs Improver - Analyzing: {args.path}\n")
    
    if args.mode in ['analyze', 'all']:
        # Analyze documentation
        analyzer = DocsAnalyzer(args.path)
        analyzer.scan_documentation()
        report = analyzer.assess_quality()
        
        print("\n📊 Documentation Quality Report")
        print("=" * 60)
        print(f"Overall Score: {report.overall_score}/100")
        print(f"\nDimension Scores:")
        print(f"  - Completeness: {report.completeness_score}/100")
        print(f"  - Accuracy: {report.accuracy_score}/100")
        print(f"  - Clarity: {report.clarity_score}/100")
        print(f"  - Structure: {report.structure_score}/100")
        print(f"  - Maintainability: {report.maintainability_score}/100")
        
        print(f"\n📁 Documentation Inventory:")
        print(f"  - Files found: {len(analyzer.inventory.files)}")
        print(f"  - Missing: {len(analyzer.inventory.missing_docs)}")
        
        if analyzer.inventory.missing_docs:
            print(f"\n⚠️  Missing Documentation:")
            for doc in analyzer.inventory.missing_docs:
                print(f"    - {doc}")
        
        if report.critical_issues:
            print(f"\n🔴 Critical Issues ({len(report.critical_issues)}):")
            for issue in report.critical_issues[:5]:
                print(f"    - {issue['description']}")
        
        if report.recommendations['quick_wins']:
            print(f"\n💡 Quick Wins:")
            for rec in report.recommendations['quick_wins'][:3]:
                print(f"    - {rec}")
        
        # Save report
        if args.report:
            save_report(report, analyzer.inventory, args.report)
            print(f"\n✅ Report saved to: {args.report}")
    
    if args.mode in ['generate', 'all']:
        # Generate documentation
        generator = DocsGenerator(args.path)
        generator.generate_readme()
        generator.generate_api_docs()
        generator.save_all(args.output)
    
    if args.mode in ['check', 'all']:
        # Check consistency
        checker = ConsistencyChecker(args.path)
        issues = checker.check_all()
        
        if issues:
            print(f"\n🔍 Consistency Issues Found: {len(issues)}")
            for issue in issues[:10]:
                print(f"\n  [{issue.severity.upper()}] {issue.type}")
                print(f"  Location: {issue.location}")
                print(f"  Issue: {issue.description}")
                print(f"  Fix: {issue.fix_suggestion}")
        else:
            print(f"\n✅ No consistency issues found!")


def save_report(report: DocQualityReport, inventory: DocInventory, output_path: str):
    """Save quality report to file"""
    content = f"""# Documentation Quality Report

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overall Score: {report.overall_score}/100

## Dimension Scores

| Dimension | Score | Status |
|-----------|-------|--------|
| Completeness | {report.completeness_score}/100 | {'✅' if report.completeness_score >= 70 else '⚠️'} |
| Accuracy | {report.accuracy_score}/100 | {'✅' if report.accuracy_score >= 70 else '⚠️'} |
| Clarity | {report.clarity_score}/100 | {'✅' if report.clarity_score >= 70 else '⚠️'} |
| Structure | {report.structure_score}/100 | {'✅' if report.structure_score >= 70 else '⚠️'} |
| Maintainability | {report.maintainability_score}/100 | {'✅' if report.maintainability_score >= 70 else '⚠️'} |

## Documentation Inventory

- **Files Found:** {len(inventory.files)}
- **Missing Docs:** {len(inventory.missing_docs)}

### Missing Documentation

"""
    
    for doc in inventory.missing_docs:
        content += f"- {doc}\n"
    
    if report.critical_issues:
        content += f"\n## Critical Issues ({len(report.critical_issues)})\n\n"
        for issue in report.critical_issues:
            content += f"- **{issue['type']}**: {issue['description']}\n"
            content += f"  - Fix: {issue['fix']}\n\n"
    
    content += "\n## Recommendations\n\n"
    
    content += "### Quick Wins\n\n"
    for rec in report.recommendations['quick_wins']:
        content += f"- [ ] {rec}\n"
    
    content += "\n### Short Term\n\n"
    for rec in report.recommendations['short_term']:
        content += f"- [ ] {rec}\n"
    
    content += "\n### Long Term\n\n"
    for rec in report.recommendations['long_term']:
        content += f"- [ ] {rec}\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    main()
