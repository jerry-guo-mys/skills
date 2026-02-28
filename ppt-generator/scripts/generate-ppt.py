#!/usr/bin/env python3
"""
PPT Generator - Generate beautiful HTML presentations
基于专业前端设计的幻灯片生成工具
"""

import argparse
import json
from pathlib import Path
from datetime import datetime


def load_template(template_path: str) -> str:
    """加载 HTML 模板"""
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def generate_slides(content: list) -> str:
    """生成幻灯片 HTML"""
    slides_html = []
    
    for i, slide in enumerate(content, 1):
        slide_type = slide.get('type', 'default')
        
        if slide_type == 'title':
            html = f"""
            <div class="slide">
                <div class="emoji">{slide.get('emoji', '🚀')}</div>
                <h1 class="gradient-text">{slide.get('title', '')}</h1>
                <h2>{slide.get('subtitle', '')}</h2>
                <div style="margin-top: 50px; text-align: center; color: var(--text-muted);">
                    <p style="font-size: 1.5rem; color: #fff; margin-bottom: 8px;">{slide.get('author', 'Author')}</p>
                    <p style="letter-spacing: 2px;">{slide.get('year', '2026')}</p>
                </div>
            </div>
            """
        
        elif slide_type == 'list':
            items = ''.join([f'<li>{item}</li>' for item in slide.get('items', [])])
            html = f"""
            <div class="slide">
                <h2>{slide.get('title', '')}</h2>
                <div class="glass-card" style="width: 100%; max-width: 800px;">
                    <ul style="list-style: none; padding: 0;">{items}</ul>
                </div>
            </div>
            """
        
        elif slide_type == 'grid':
            cards = slide.get('cards', [])
            cards_html = ''
            for card in cards:
                card_items = ''.join([f'<li>{item}</li>' for item in card.get('items', [])])
                card_class = 'error' if card.get('type') == 'negative' else 'success'
                cards_html += f"""
                <div class="glass-card" style="border-top: 4px solid var(--accent-{card_class});">
                    <h3 class="{card_class}">{card.get('title', '')}</h3>
                    <ul>{card_items}</ul>
                </div>
                """
            
            html = f"""
            <div class="slide">
                <h2>{slide.get('title', '')}</h2>
                <p style="text-align: center; font-size: 1.4rem; color: var(--text-muted); margin-bottom: 30px;">
                    {slide.get('description', '')}
                </p>
                <div class="grid-layout" style="max-width: 1000px;">{cards_html}</div>
            </div>
            """
        
        elif slide_type == 'quote':
            html = f"""
            <div class="slide">
                <div class="glass-card quote">
                    <span style="display:block; margin-bottom: 20px; color: var(--text-main);">{slide.get('text', '')}</span>
                    <span class="gradient-text" style="font-weight: 600; font-size: 1.2em;">{slide.get('highlight', '')}</span>
                </div>
            </div>
            """
        
        elif slide_type == 'tasks':
            html = f"""
            <div class="slide">
                <h2>{slide.get('title', '')}</h2>
                <div class="glass-card" style="width: 100%; max-width: 900px;">
                    <ol style="padding-left: 20px;">
                        {''.join([f'<li style="margin-bottom: 30px;"><span class="highlight">{task.get("title", "")}</span><br><span style="font-size: 0.85em; color: var(--text-muted);">{task.get("desc", "")}</span></li>' for task in slide.get('tasks', [])])}
                    </ol>
                </div>
            </div>
            """
        
        elif slide_type == 'end':
            html = f"""
            <div class="slide">
                <div class="emoji" style="font-size: 5rem;">🎉</div>
                <h1 class="gradient-text">{slide.get('title', 'Thank You!')}</h1>
                <h2 style="color: var(--text-muted); text-shadow: none;">{slide.get('subtitle', '')}</h2>
                <div class="glass-card" style="margin-top: 40px; padding: 30px 60px; text-align: center;">
                    <p style="font-size: 1.8rem; margin-bottom: 10px; font-weight: bold;">{slide.get('author', '')}</p>
                    <p style="color: var(--text-muted); margin-bottom: 10px;">📧 {slide.get('email', '')}</p>
                    <p style="color: var(--accent-cyan);">💬 {slide.get('contact', '')}</p>
                </div>
            </div>
            """
        
        else:
            # 默认类型
            html = f"""
            <div class="slide">
                <h2>{slide.get('title', '')}</h2>
                <div class="glass-card">{slide.get('content', '')}</div>
            </div>
            """
        
        slides_html.append(html)
    
    return '\n'.join(slides_html)


def generate_ppt(config_path: str, output_path: str):
    """生成 PPT"""
    print(f"🎨 正在生成 PPT...")
    print(f"📄 配置文件：{config_path}")
    print(f"📤 输出文件：{output_path}")
    
    # 加载配置
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # 加载模板
    template_path = Path(__file__).parent.parent / 'templates' / 'ppt-template.html'
    template = load_template(str(template_path))
    
    # 生成幻灯片
    slides_html = generate_slides(config.get('slides', []))
    
    # 替换模板变量
    html = template.replace('{{TITLE}}', config.get('title', 'Presentation'))
    html = html.replace('{{TOTAL_SLIDES}}', str(len(config.get('slides', []))))
    html = html.replace('<!-- SLIDES_PLACEHOLDER -->', slides_html)
    
    # 保存文件
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ PPT 生成成功！")
    print(f"📊 共 {len(config.get('slides', []))} 页")
    print(f"🌐 打开文件：{output.absolute()}")
    
    # 自动打开（可选）
    import subprocess
    import platform
    
    system = platform.system()
    if system == 'Darwin':  # macOS
        subprocess.run(['open', str(output.absolute())])
    elif system == 'Windows':
        subprocess.run(['start', str(output.absolute())], shell=True)
    elif system == 'Linux':
        subprocess.run(['xdg-open', str(output.absolute())])


def main():
    parser = argparse.ArgumentParser(description='生成炫酷的 HTML 演示文稿')
    parser.add_argument('--config', '-c', required=True, help='JSON 配置文件路径')
    parser.add_argument('--output', '-o', default='output/presentation.html', help='输出文件路径')
    
    args = parser.parse_args()
    
    generate_ppt(args.config, args.output)


if __name__ == '__main__':
    main()
