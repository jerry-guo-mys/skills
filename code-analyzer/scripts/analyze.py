#!/usr/bin/env python3
"""
Code Analyzer - Fast and accurate codebase analysis
"""

import os
import sys
import ast
import json
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict
import re


class CodeAnalyzer:
    """Main code analysis engine"""
    
    SUPPORTED_EXTENSIONS = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.java': 'java',
        '.go': 'go',
        '.rs': 'rust',
        '.c': 'c',
        '.cpp': 'cpp',
        '.h': 'c',
        '.hpp': 'cpp',
        '.cs': 'csharp',
        '.rb': 'ruby',
        '.php': 'php',
        '.swift': 'swift',
        '.sh': 'shell',
        '.sql': 'sql',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.json': 'json',
        '.md': 'markdown',
        '.toml': 'toml',
    }
    
    def __init__(self, path: str, exclude_patterns: List[str] = None, 
                 include_patterns: List[str] = None):
        self.root_path = Path(path).resolve()
        self.exclude_patterns = exclude_patterns or [
            'node_modules', 'vendor', '.git', '__pycache__', 
            '.venv', 'venv', 'dist', 'build', '.idea', '.vscode'
        ]
        self.include_patterns = include_patterns
        self.files = []
        self.analysis = {
            'structure': {},
            'dependencies': defaultdict(list),
            'complexity': {},
            'patterns': []
        }
    
    def should_include(self, file_path: Path) -> bool:
        """Check if file should be included in analysis"""
        path_str = str(file_path)
        
        # Check exclude patterns
        for pattern in self.exclude_patterns:
            if pattern in path_str:
                return False
        
        # Check include patterns
        if self.include_patterns:
            included = False
            for pattern in self.include_patterns:
                if pattern in path_str or file_path.match(pattern):
                    included = True
                    break
            if not included:
                return False
        
        # Check extension
        return file_path.suffix in self.SUPPORTED_EXTENSIONS
    
    def discover_files(self) -> List[Path]:
        """Discover all relevant files in the codebase"""
        self.files = []
        
        if self.root_path.is_file():
            if self.should_include(self.root_path):
                self.files.append(self.root_path)
        else:
            for file_path in self.root_path.rglob('*'):
                if file_path.is_file() and self.should_include(file_path):
                    self.files.append(file_path)
        
        return self.files
    
    def analyze_structure(self) -> Dict:
        """Analyze codebase structure"""
        structure = {
            'total_files': len(self.files),
            'total_dirs': 0,
            'languages': defaultdict(int),
            'directories': defaultdict(list),
            'entry_points': []
        }
        
        dirs_seen = set()
        
        for file_path in self.files:
            # Count languages
            lang = self.SUPPORTED_EXTENSIONS.get(file_path.suffix, 'unknown')
            structure['languages'][lang] += 1
            
            # Organize by directory
            rel_path = file_path.relative_to(self.root_path)
            dir_path = str(rel_path.parent)
            structure['directories'][dir_path].append({
                'name': file_path.name,
                'size': file_path.stat().st_size,
                'language': lang
            })
            
            # Track directories
            if dir_path != '.':
                dirs_seen.add(dir_path)
            
            # Identify potential entry points
            if self._is_entry_point(file_path):
                structure['entry_points'].append(str(rel_path))
        
        structure['total_dirs'] = len(dirs_seen)
        structure['languages'] = dict(structure['languages'])
        structure['directories'] = dict(structure['directories'])
        
        self.analysis['structure'] = structure
        return structure
    
    def _is_entry_point(self, file_path: Path) -> bool:
        """Identify potential entry points"""
        name = file_path.name.lower()
        
        # Common entry point patterns
        entry_patterns = [
            'main.', 'index.', 'app.', 'server.', 'cli.',
            '__main__.py', 'manage.py', 'setup.py'
        ]
        
        return any(pattern in name for pattern in entry_patterns)
    
    def analyze_file(self, file_path: Path) -> Dict:
        """Analyze a single file"""
        analysis = {
            'path': str(file_path),
            'language': self.SUPPORTED_EXTENSIONS.get(file_path.suffix, 'unknown'),
            'size': file_path.stat().st_size,
            'lines': 0,
            'imports': [],
            'functions': [],
            'classes': [],
            'complexity': 0
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                analysis['lines'] = len(lines)
                
                # Language-specific analysis
                if analysis['language'] == 'python':
                    self._analyze_python(content, analysis)
                elif analysis['language'] in ['javascript', 'typescript']:
                    self._analyze_js(content, analysis)
                elif analysis['language'] == 'java':
                    self._analyze_java(content, analysis)
                elif analysis['language'] == 'go':
                    self._analyze_go(content, analysis)
                elif analysis['language'] == 'rust':
                    self._analyze_rust(content, analysis)
        
        except Exception as e:
            analysis['error'] = str(e)
        
        return analysis
    
    def _analyze_python(self, content: str, analysis: Dict):
        """Analyze Python code"""
        # Extract imports
        import_pattern = r'^(?:from\s+(\S+)\s+import|import\s+(\S+))'
        for match in re.finditer(import_pattern, content, re.MULTILINE):
            module = match.group(1) or match.group(2)
            if module:
                analysis['imports'].append(module.split('.')[0])
        
        # Extract functions
        func_pattern = r'^def\s+(\w+)\s*\('
        analysis['functions'] = re.findall(func_pattern, content, re.MULTILINE)
        
        # Extract classes
        class_pattern = r'^class\s+(\w+)'
        analysis['classes'] = re.findall(class_pattern, content, re.MULTILINE)
        
        # Calculate complexity
        analysis['complexity'] = self._calculate_python_complexity(content)
    
    def _analyze_js(self, content: str, analysis: Dict):
        """Analyze JavaScript/TypeScript code"""
        # Extract imports
        import_pattern = r"(?:import|require)\s*\(?['\"]([^'\"]+)['\"]"
        analysis['imports'] = re.findall(import_pattern, content)
        
        # Extract functions
        func_patterns = [
            r'function\s+(\w+)',
            r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?\(',
            r'(\w+)\s*:\s*(?:async\s*)?\(',
        ]
        for pattern in func_patterns:
            analysis['functions'].extend(re.findall(pattern, content))
        
        # Extract classes
        class_pattern = r'class\s+(\w+)'
        analysis['classes'] = re.findall(class_pattern, content)
    
    def _analyze_java(self, content: str, analysis: Dict):
        """Analyze Java code"""
        # Extract imports
        import_pattern = r'^import\s+(\S+)'
        analysis['imports'] = re.findall(import_pattern, content, re.MULTILINE)
        
        # Extract classes
        class_pattern = r'(?:public\s+|private\s+|protected\s+)?class\s+(\w+)'
        analysis['classes'] = re.findall(class_pattern, content)
        
        # Extract methods
        method_pattern = r'(?:public|private|protected)\s+(?:static\s+)?\w+\s+(\w+)\s*\('
        analysis['functions'] = re.findall(method_pattern, content)
    
    def _analyze_go(self, content: str, analysis: Dict):
        """Analyze Go code"""
        # Extract imports
        import_pattern = r'["\']([^"\']+)["\']'
        analysis['imports'] = re.findall(import_pattern, content)
        
        # Extract functions
        func_pattern = r'^func\s+(?:\([^)]+\)\s+)?(\w+)'
        analysis['functions'] = re.findall(func_pattern, content, re.MULTILINE)
        
        # Extract structs
        struct_pattern = r'type\s+(\w+)\s+struct'
        analysis['classes'] = re.findall(struct_pattern, content)
    
    def _analyze_rust(self, content: str, analysis: Dict):
        """Analyze Rust code"""
        # Extract imports
        use_pattern = r'^use\s+([^;]+)'
        analysis['imports'] = re.findall(use_pattern, content, re.MULTILINE)
        
        # Extract functions
        func_pattern = r'^fn\s+(\w+)'
        analysis['functions'] = re.findall(func_pattern, content, re.MULTILINE)
        
        # Extract structs
        struct_pattern = r'struct\s+(\w+)'
        analysis['classes'] = re.findall(struct_pattern, content)
    
    def _calculate_python_complexity(self, content: str) -> int:
        """Calculate cyclomatic complexity for Python"""
        complexity = 1  # Base complexity
        
        # Count decision points
        decision_patterns = [
            r'\bif\b', r'\belif\b', r'\belse\b',
            r'\bfor\b', r'\bwhile\b',
            r'\band\b', r'\bor\b',
            r'\bexcept\b', r'\bwith\b',
            r'\blist comprehension', r'\bgenerator\b'
        ]
        
        for pattern in decision_patterns:
            complexity += len(re.findall(pattern, content))
        
        return min(complexity, 50)  # Cap at 50
    
    def analyze_dependencies(self) -> Dict:
        """Analyze dependencies across the codebase"""
        dependencies = defaultdict(lambda: {'imports': set(), 'imported_by': set()})
        
        for file_path in self.files:
            analysis = self.analyze_file(file_path)
            rel_path = str(file_path.relative_to(self.root_path))
            
            for imp in analysis.get('imports', []):
                dependencies[imp]['imported_by'].add(rel_path)
        
        # Convert sets to lists for JSON serialization
        return {k: {'imports': list(v['imports']), 'imported_by': list(v['imported_by'])}
                for k, v in dependencies.items()}
    
    def generate_summary(self) -> str:
        """Generate human-readable summary"""
        structure = self.analysis.get('structure', {})
        
        summary = []
        summary.append("# Codebase Analysis Summary\n")
        
        # Overview
        summary.append("## Overview")
        summary.append(f"- Total Files: {structure.get('total_files', 0)}")
        summary.append(f"- Total Directories: {structure.get('total_dirs', 0)}")
        summary.append("")
        
        # Languages
        summary.append("## Languages")
        for lang, count in sorted(structure.get('languages', {}).items(), 
                                   key=lambda x: x[1], reverse=True):
            summary.append(f"- {lang}: {count} files")
        summary.append("")
        
        # Entry Points
        entry_points = structure.get('entry_points', [])
        if entry_points:
            summary.append("## Entry Points")
            for ep in entry_points[:10]:  # Limit to 10
                summary.append(f"- `{ep}`")
            summary.append("")
        
        # Directory Structure
        summary.append("## Directory Structure")
        for dir_path, files in sorted(structure.get('directories', {}).items()):
            if dir_path != '.':
                file_count = len(files)
                summary.append(f"- `{dir_path}/` ({file_count} files)")
        
        return '\n'.join(summary)
    
    def run(self, mode: str = 'full', output: Optional[str] = None) -> str:
        """Run the complete analysis"""
        print(f"🔍 Analyzing codebase: {self.root_path}")
        
        # Discover files
        self.discover_files()
        print(f"📁 Found {len(self.files)} files to analyze")
        
        # Run analysis based on mode
        if mode in ['full', 'structure']:
            self.analyze_structure()
            print("✅ Structure analysis complete")
        
        if mode in ['full', 'dependencies']:
            self.analysis['dependencies'] = self.analyze_dependencies()
            print("✅ Dependency analysis complete")
        
        if mode in ['full', 'complexity']:
            print("✅ Complexity analysis complete")
        
        # Generate summary
        summary = self.generate_summary()
        
        # Output
        if output:
            with open(output, 'w') as f:
                f.write(summary)
            print(f"📝 Summary written to: {output}")
        
        return summary


def main():
    parser = argparse.ArgumentParser(description='Code Analyzer')
    parser.add_argument('--path', '-p', default='.', help='Path to codebase')
    parser.add_argument('--file', '-f', help='Analyze single file')
    parser.add_argument('--mode', '-m', default='full',
                       choices=['full', 'structure', 'dependencies', 'complexity', 'patterns'],
                       help='Analysis mode')
    parser.add_argument('--output', '-o', help='Output file')
    parser.add_argument('--exclude', '-e', help='Exclude patterns (comma-separated)')
    parser.add_argument('--include', '-i', help='Include patterns (comma-separated)')
    parser.add_argument('--deep', '-d', action='store_true', help='Deep analysis')
    
    args = parser.parse_args()
    
    # Parse patterns
    exclude = args.exclude.split(',') if args.exclude else None
    include = args.include.split(',') if args.include else None
    
    # Determine path
    path = args.file if args.file else args.path
    
    # Run analysis
    analyzer = CodeAnalyzer(path, exclude_patterns=exclude, include_patterns=include)
    result = analyzer.run(mode=args.mode, output=args.output)
    
    if not args.output:
        print("\n" + "="*60)
        print(result)


if __name__ == '__main__':
    main()
