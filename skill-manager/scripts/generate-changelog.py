#!/usr/bin/env python3
"""
Changelog Generator - Generate CHANGELOG from improvement records
"""

import argparse
from datetime import datetime
from pathlib import Path


def generate_changelog(improvement_records: list, version: str, output: str):
    """Generate CHANGELOG from improvement records"""
    
    print(f"📝 生成变更日志：{version}")
    
    changelog = f"""## [{version}] - {datetime.now().strftime('%Y-%m-%d')}

### ✨ 新增
"""
    
    # Parse improvement records (simplified)
    new_features = []
    bug_fixes = []
    optimizations = []
    docs = []
    
    for record_file in improvement_records:
        try:
            with open(record_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple parsing
            if '新增' in content or '新功能' in content:
                new_features.append('功能改进')
            if '修复' in content or 'Bug' in content:
                bug_fixes.append('问题修复')
            if '优化' in content or '性能' in content:
                optimizations.append('性能优化')
            if '文档' in content:
                docs.append('文档更新')
                
        except Exception as e:
            print(f"  ⚠️ 读取失败 {record_file}: {e}")
    
    # Add sections
    if new_features:
        for item in set(new_features):
            changelog += f"- {item}\n"
    else:
        changelog += "- 暂无\n"
    
    changelog += "\n### 🐛 修复\n"
    if bug_fixes:
        for item in set(bug_fixes):
            changelog += f"- {item}\n"
    else:
        changelog += "- 暂无\n"
    
    changelog += "\n### ⚡ 优化\n"
    if optimizations:
        for item in set(optimizations):
            changelog += f"- {item}\n"
    else:
        changelog += "- 暂无\n"
    
    changelog += "\n### 📝 文档\n"
    if docs:
        for item in set(docs):
            changelog += f"- {item}\n"
    else:
        changelog += "- 暂无\n"
    
    output_path = Path(output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(changelog)
    
    print(f"✅ 变更日志已生成：{output_path}")
    print(f"\n📋 内容概览:")
    print(f"  新增：{len(new_features)} 项")
    print(f"  修复：{len(bug_fixes)} 项")
    print(f"  优化：{len(optimizations)} 项")
    print(f"  文档：{len(docs)} 项")


def main():
    parser = argparse.ArgumentParser(description='Generate CHANGELOG')
    parser.add_argument('--records', '-r', nargs='+', help='Improvement record files')
    parser.add_argument('--version', '-v', required=True, help='Version number')
    parser.add_argument('--output', '-o', default='CHANGELOG.md', help='Output file')
    
    args = parser.parse_args()
    
    generate_changelog(args.records or [], args.version, args.output)


if __name__ == '__main__':
    main()
