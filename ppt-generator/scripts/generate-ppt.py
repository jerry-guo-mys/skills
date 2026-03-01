#!/usr/bin/env python3
"""
PPT Generator v2.0 - Generate beautiful HTML presentations
基于专业前端设计的幻灯片生成工具

新增功能:
- image: 图片展示页
- code: 代码展示页（Prism.js 语法高亮）
- two-column: 双列布局
- timeline: 时间线页
- fragments: 分步显示
- speaker notes: 演讲者笔记
- themes: 主题系统
"""

import argparse
import json
import html
from pathlib import Path
from datetime import datetime


def load_template(template_path: str) -> str:
    """加载 HTML 模板"""
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def escape_html(text: str) -> str:
    """转义 HTML 特殊字符，但保留已有的 HTML 标签"""
    if '<' in text and '>' in text:
        return text
    return html.escape(text)


def generate_slides(content: list) -> tuple[str, list]:
    """生成幻灯片 HTML，返回 (slides_html, notes_list)"""
    slides_html = []
    notes_list = []
    
    for i, slide in enumerate(content, 1):
        slide_type = slide.get('type', 'default')
        notes = slide.get('notes', '')
        notes_list.append(notes)
        
        fragments = slide.get('fragments', False)
        fragment_class = ' fragment' if fragments else ''
        
        if slide_type == 'title':
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
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
            items_data = slide.get('items', [])
            if fragments:
                items = ''.join([f'<li class="fragment">{item}</li>' for item in items_data])
            else:
                items = ''.join([f'<li>{item}</li>' for item in items_data])
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
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
                card_type = card.get('type', 'default')
                if card_type == 'negative':
                    card_class = 'error'
                    border_color = 'var(--accent-danger)'
                elif card_type == 'positive':
                    card_class = 'success'
                    border_color = 'var(--accent-green)'
                elif card_type == 'warning':
                    card_class = 'warning'
                    border_color = 'var(--accent-warning)'
                else:
                    card_class = ''
                    border_color = 'var(--accent-cyan)'
                    
                cards_html += f"""
                <div class="glass-card" style="border-top: 4px solid {border_color};">
                    <h3 class="{card_class}">{card.get('title', '')}</h3>
                    <ul>{card_items}</ul>
                </div>
                """
            
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <p style="text-align: center; font-size: 1.4rem; color: var(--text-muted); margin-bottom: 30px;">
                    {slide.get('description', '')}
                </p>
                <div class="grid-layout" style="max-width: 1000px;">{cards_html}</div>
            </div>
            """
        
        elif slide_type == 'quote':
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
                <div class="glass-card quote">
                    <span style="display:block; margin-bottom: 20px; color: var(--text-main);">{slide.get('text', '')}</span>
                    <span class="gradient-text" style="font-weight: 600; font-size: 1.2em;">{slide.get('highlight', '')}</span>
                </div>
            </div>
            """
        
        elif slide_type == 'tasks':
            tasks_data = slide.get('tasks', [])
            if fragments:
                tasks_html = ''.join([
                    f'<li class="fragment" style="margin-bottom: 30px;"><span class="highlight">{task.get("title", "")}</span><br><span style="font-size: 0.85em; color: var(--text-muted);">{task.get("desc", "")}</span></li>' 
                    for task in tasks_data
                ])
            else:
                tasks_html = ''.join([
                    f'<li style="margin-bottom: 30px;"><span class="highlight">{task.get("title", "")}</span><br><span style="font-size: 0.85em; color: var(--text-muted);">{task.get("desc", "")}</span></li>' 
                    for task in tasks_data
                ])
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <div class="glass-card" style="width: 100%; max-width: 900px;">
                    <ol style="padding-left: 20px;">{tasks_html}</ol>
                </div>
            </div>
            """
        
        elif slide_type == 'end':
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
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
        
        elif slide_type == 'mermaid':
            code = slide.get('code', '')
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <p style="text-align: center; font-size: 1.2rem; color: var(--text-muted); margin-bottom: 20px;">
                    {slide.get('description', '')}
                </p>
                <div class="mermaid-wrapper">
                    <pre class="mermaid" style="display:none;">
{code}
                    </pre>
                </div>
            </div>
            """
        
        elif slide_type == 'image':
            img_src = slide.get('src', '')
            img_alt = slide.get('alt', '')
            caption = slide.get('caption', '')
            fit = slide.get('fit', 'contain')
            
            caption_html = f'<p class="image-caption">{caption}</p>' if caption else ''
            
            html_content = f"""
            <div class="slide slide-image" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <div class="image-container" style="--fit: {fit};">
                    <img src="{img_src}" alt="{img_alt}" loading="lazy">
                </div>
                {caption_html}
            </div>
            """
        
        elif slide_type == 'code':
            code = slide.get('code', '')
            language = slide.get('language', 'javascript')
            filename = slide.get('filename', '')
            
            escaped_code = html.escape(code)
            
            filename_html = f'<div class="code-filename"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span><span class="filename-text">{filename}</span></div>' if filename else '<div class="code-filename"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>'
            
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <p style="text-align: center; font-size: 1.2rem; color: var(--text-muted); margin-bottom: 20px;">
                    {slide.get('description', '')}
                </p>
                <div class="code-wrapper">
                    {filename_html}
                    <pre class="code-block"><code class="language-{language}">{escaped_code}</code></pre>
                </div>
            </div>
            """
        
        elif slide_type == 'two-column':
            left = slide.get('left', {})
            right = slide.get('right', {})
            
            def render_column(col):
                col_type = col.get('type', 'text')
                if col_type == 'image':
                    return f'<img src="{col.get("src", "")}" alt="{col.get("alt", "")}" class="column-image">'
                elif col_type == 'list':
                    items = ''.join([f'<li>{item}</li>' for item in col.get('items', [])])
                    return f'<ul class="column-list">{items}</ul>'
                elif col_type == 'code':
                    escaped = html.escape(col.get('code', ''))
                    lang = col.get('language', 'javascript')
                    return f'<pre class="column-code"><code class="language-{lang}">{escaped}</code></pre>'
                else:
                    return f'<div class="column-text">{col.get("content", "")}</div>'
            
            left_title = f'<h3>{left.get("title", "")}</h3>' if left.get('title') else ''
            right_title = f'<h3>{right.get("title", "")}</h3>' if right.get('title') else ''
            
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <div class="two-column-layout">
                    <div class="column left-column glass-card">
                        {left_title}
                        {render_column(left)}
                    </div>
                    <div class="column right-column glass-card">
                        {right_title}
                        {render_column(right)}
                    </div>
                </div>
            </div>
            """
        
        elif slide_type == 'timeline':
            events = slide.get('events', [])
            events_html = ''
            for idx, event in enumerate(events):
                position = 'left' if idx % 2 == 0 else 'right'
                fragment_attr = ' class="fragment"' if fragments else ''
                events_html += f"""
                <div class="timeline-item {position}"{fragment_attr}>
                    <div class="timeline-content glass-card">
                        <span class="timeline-date">{event.get('date', '')}</span>
                        <h3>{event.get('title', '')}</h3>
                        <p>{event.get('description', '')}</p>
                    </div>
                </div>
                """
            
            html_content = f"""
            <div class="slide slide-timeline" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <div class="timeline-container">
                    <div class="timeline-line"></div>
                    {events_html}
                </div>
            </div>
            """
        
        elif slide_type == 'video':
            video_src = slide.get('src', '')
            video_type = slide.get('video_type', 'local')
            autoplay = slide.get('autoplay', False)
            
            if video_type == 'youtube':
                video_id = video_src.split('/')[-1].split('?')[0].replace('watch?v=', '')
                autoplay_param = '&autoplay=1' if autoplay else ''
                video_html = f'<iframe src="https://www.youtube.com/embed/{video_id}?rel=0{autoplay_param}" frameborder="0" allowfullscreen></iframe>'
            elif video_type == 'bilibili':
                video_html = f'<iframe src="//player.bilibili.com/player.html?bvid={video_src}&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>'
            else:
                autoplay_attr = 'autoplay' if autoplay else ''
                video_html = f'<video controls {autoplay_attr}><source src="{video_src}" type="video/mp4"></video>'
            
            html_content = f"""
            <div class="slide slide-video" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <div class="video-container">
                    {video_html}
                </div>
            </div>
            """
        
        elif slide_type == 'stats':
            stats = slide.get('stats', [])
            stats_html = ''
            for stat in stats:
                icon = stat.get('icon', '📊')
                stats_html += f"""
                <div class="stat-card glass-card">
                    <div class="stat-icon">{icon}</div>
                    <div class="stat-value gradient-text">{stat.get('value', '0')}</div>
                    <div class="stat-label">{stat.get('label', '')}</div>
                </div>
                """
            
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <p style="text-align: center; font-size: 1.2rem; color: var(--text-muted); margin-bottom: 30px;">
                    {slide.get('description', '')}
                </p>
                <div class="stats-grid">{stats_html}</div>
            </div>
            """
        
        else:
            html_content = f"""
            <div class="slide" data-notes="{escape_html(notes)}">
                <h2>{slide.get('title', '')}</h2>
                <div class="glass-card">{slide.get('content', '')}</div>
            </div>
            """
        
        slides_html.append(html_content)
    
    return '\n'.join(slides_html), notes_list


def get_theme_css(theme: dict) -> str:
    """生成主题 CSS 变量"""
    if not theme:
        return ''
    
    preset = theme.get('preset', 'dark')
    
    presets = {
        'dark': {
            'bg-color-1': '#0f172a',
            'bg-color-2': '#1e1b4b',
            'accent-cyan': '#06b6d4',
            'accent-green': '#10b981',
            'accent-warning': '#f59e0b',
            'accent-danger': '#f43f5e',
            'accent-purple': '#8b5cf6',
            'text-main': '#f8fafc',
            'text-muted': '#94a3b8',
        },
        'light': {
            'bg-color-1': '#f8fafc',
            'bg-color-2': '#e2e8f0',
            'accent-cyan': '#0891b2',
            'accent-green': '#059669',
            'accent-warning': '#d97706',
            'accent-danger': '#dc2626',
            'accent-purple': '#7c3aed',
            'text-main': '#1e293b',
            'text-muted': '#64748b',
        },
        'ocean': {
            'bg-color-1': '#0c1929',
            'bg-color-2': '#0f2942',
            'accent-cyan': '#22d3ee',
            'accent-green': '#34d399',
            'accent-warning': '#fbbf24',
            'accent-danger': '#fb7185',
            'accent-purple': '#a78bfa',
            'text-main': '#f0f9ff',
            'text-muted': '#7dd3fc',
        },
        'forest': {
            'bg-color-1': '#14231a',
            'bg-color-2': '#1a3a2a',
            'accent-cyan': '#5eead4',
            'accent-green': '#4ade80',
            'accent-warning': '#facc15',
            'accent-danger': '#f87171',
            'accent-purple': '#c4b5fd',
            'text-main': '#f0fdf4',
            'text-muted': '#86efac',
        },
    }
    
    base_colors = presets.get(preset, presets['dark']).copy()
    
    custom = theme.get('custom', {})
    base_colors.update(custom)
    
    css_vars = '\n'.join([f'            --{k}: {v};' for k, v in base_colors.items()])
    return f"""
        :root {{
{css_vars}
        }}
    """


def generate_ppt(config_path: str, output_path: str):
    """生成 PPT"""
    print(f"🎨 正在生成 PPT...")
    print(f"📄 配置文件：{config_path}")
    print(f"📤 输出文件：{output_path}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    template_path = Path(__file__).parent.parent / 'templates' / 'ppt-template.html'
    template = load_template(str(template_path))
    
    slides_html, notes_list = generate_slides(config.get('slides', []))
    
    theme = config.get('theme', {})
    theme_css = get_theme_css(theme)
    
    notes_json = json.dumps(notes_list, ensure_ascii=False)
    
    html_output = template.replace('{{TITLE}}', config.get('title', 'Presentation'))
    html_output = html_output.replace('{{TOTAL_SLIDES}}', str(len(config.get('slides', []))))
    html_output = html_output.replace('<!-- SLIDES_PLACEHOLDER -->', slides_html)
    html_output = html_output.replace('/* THEME_CSS_PLACEHOLDER */', theme_css)
    html_output = html_output.replace('/* NOTES_JSON_PLACEHOLDER */', f'const speakerNotes = {notes_json};')
    
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output, 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"✅ PPT 生成成功！")
    print(f"📊 共 {len(config.get('slides', []))} 页")
    print(f"🌐 打开文件：{output.absolute()}")
    
    import subprocess
    import platform
    
    system = platform.system()
    if system == 'Darwin':
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
