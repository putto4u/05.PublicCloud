import os
from datetime import datetime

def generate_index():
    # 제외할 폴더 및 파일 설정
    exclude_dirs = {'.git', '.github', '.pytest_cache', '__pycache__', 'assets'}
    exclude_files = {'index.html', 'generate_index.py'}
    
    # 현대적인 디자인을 위한 CSS 및 HTML 구조 정의
    html_header = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Putto's Lectures - 학습 콘텐츠 목록</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
        body {{ font-family: 'Noto Sans KR', sans-serif; background-color: #f8fafc; }}
        .hero-gradient {{
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        }}
        .card-hover {{
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .card-hover:hover {{
            transform: translateY(-4px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        }}
    </style>
</head>
<body class="text-slate-800">
    <header class="hero-gradient text-white py-12 px-6 shadow-lg mb-10">
        <div class="max-w-5xl mx-auto">
            <div class="flex items-center space-x-4 mb-4">
                <i class="fas fa-graduation-cap text-4xl text-blue-400"></i>
                <h1 class="text-4xl font-bold tracking-tight">Putto's Lectures</h1>
            </div>
            <p class="text-slate-300 text-lg">공용 클라우드 및 IT 기술 교육 자료 저장소</p>
            <div class="mt-6 flex items-center text-sm text-slate-400">
                <i class="far fa-clock mr-2"></i>
                <span>마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}</span>
            </div>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-6 pb-20">
"""

    html_footer = """
    </main>
    <footer class="border-t border-slate-200 py-10 text-center text-slate-500 text-sm">
        <p>&copy; 2026 Putto's Lectures. 모든 권리 보유.</p>
    </footer>
</body>
</html>
"""

    content_body = ""
    
    # 저장소 탐색 및 데이터 구조화
    structure = {}
    for root, dirs, files in os.walk('.'):
        # 제외 폴더 필터링
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        rel_path = os.path.relpath(root, '.')
        html_files = sorted([f for f in files if f.endswith('.html') and f not in exclude_files])
        
        if html_files:
            structure[rel_path] = html_files

    # 정렬된 키(폴더명) 순으로 루프
    for folder in sorted(structure.keys()):
        files = structure[folder]
        display_folder = "루트 디렉터리" if folder == "." else folder
        folder_icon = "fa-folder-open" if folder != "." else "fa-house"
        
        content_body += f"""
        <section class="mb-12">
            <div class="flex items-center space-x-3 mb-6 border-b border-slate-200 pb-2">
                <i class="fas {folder_icon} text-blue-500"></i>
                <h2 class="text-2xl font-bold text-slate-700">{display_folder}</h2>
                <span class="bg-slate-200 text-slate-600 text-xs font-bold px-2 py-1 rounded-full">{len(files)}개 파일</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        """
        
        for file in files:
            file_path = os.path.join(folder, file) if folder != "." else file
            # 파일명에서 확장자 제거 및 가독성 개선
            display_name = file.replace('.html', '').replace('_', ' ').replace('-', ' ')
            
            content_body += f"""
                <a href="{file_path}" target="_blank" class="card-hover bg-white p-5 rounded-xl border border-slate-100 shadow-sm flex items-start space-x-4">
                    <div class="bg-blue-50 p-3 rounded-lg text-blue-600">
                        <i class="far fa-file-code text-xl"></i>
                    </div>
                    <div class="overflow-hidden">
                        <h3 class="font-semibold text-slate-800 truncate" title="{display_name}">{display_name}</h3>
                        <p class="text-xs text-slate-400 mt-1 truncate">{file}</p>
                    </div>
                </a>
            """
            
        content_body += """
            </div>
        </section>
        """

    # 최종 파일 작성
    full_html = html_header + content_body + html_footer
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"성공: {datetime.now().strftime('%H:%M:%S')} - index.html 파일이 생성되었습니다.")

if __name__ == "__main__":
    generate_index()
