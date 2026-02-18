import os

def generate_index():
    # 제외할 폴더 및 파일 설정
    exclude_dirs = {'.git', '.github', '.pytest_cache'}
    exclude_files = {'index.html', 'generate_index.py'}
    
    html_content = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Public Cloud 강의 목록</title>
        <style>
            body { font-family: sans-serif; line-height: 1.6; padding: 20px; }
            ul { list-style-type: none; }
            .folder { font-weight: bold; color: #2c3e50; margin-top: 15px; }
            .file { margin-left: 20px; }
            a { text-decoration: none; color: #3498db; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>저장소 HTML 콘텐츠 목록</h1>
        <hr>
    """

    # 폴더 순, 파일명 순으로 정렬하여 탐색
    for root, dirs, files in os.walk('.'):
        # 제외 폴더 필터링 및 정렬
        dirs[:] = sorted([d for d in dirs if d not in exclude_dirs])
        files = sorted([f for f in files if f.endswith('.html') and f not in exclude_files])

        if files:
            rel_path = os.path.relpath(root, '.')
            if rel_path != '.':
                html_content += f'<div class="folder">📂 {rel_path}</div>'
            
            html_content += '<ul>'
            for file in files:
                file_path = os.path.join(rel_path, file) if rel_path != '.' else file
                # 새 창에서 열기 위해 target="_blank" 추가
                html_content += f'<li class="file">📄 <a href="{file_path}" target="_blank">{file}</a></li>'
            html_content += '</ul>'

    html_content += """
    </body>
    </html>
    """

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_index()
