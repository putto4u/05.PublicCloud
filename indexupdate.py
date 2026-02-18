<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>강의 자료 목록</title>
    <!-- 아이콘 및 폰트 라이브러리 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        /* 기본 스타일 설정 */
        body { font-family: 'Noto Sans KR', sans-serif; background-color: #f7fafc; color: #2d3748; margin: 0; padding: 40px; display: flex; flex-direction: column; align-items: center; }
        .container { width: 100%; max-width: 800px; }
        header { margin-bottom: 40px; text-align: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; }
        h1 { color: #0078D4; margin: 0; margin-bottom: 10px; }
        .subtitle { font-size: 14px; color: #718096; }
        
        /* 파일 목록 스타일 */
        .file-list { list-style: none; padding: 0; }
        .file-item { background: white; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 15px; transition: transform 0.2s, box-shadow 0.2s; }
        .file-item:hover { transform: translateY(-3px); box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-color: #0078D4; }
        
        /* 링크 스타일 */
        .file-link { display: flex; align-items: center; padding: 20px; text-decoration: none; color: inherit; }
        .icon { font-size: 24px; color: #0078D4; margin-right: 20px; width: 40px; text-align: center; }
        .info { flex-grow: 1; }
        .title { font-weight: 700; font-size: 18px; display: block; }
        .meta { font-size: 14px; color: #718096; margin-top: 4px; }
        .arrow { color: #cbd5e0; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><i class="fa-solid fa-folder-open"></i> 강의 자료 아카이브</h1>
            <p class="subtitle">Last Updated: 2026-02-18 19:00</p>
        </header>
        <ul class="file-list">
    
            <!-- 1. 고정된 메인 파일 -->
            <li class="file-item">
                <a href="index01.html" class="file-link" target="_blank">
                    <div class="icon"><i class="fa-solid fa-star"></i></div>
                    <div class="info">
                        <span class="title">index01.html</span>
                        <span class="meta">수정일: 2026-02-18 18:51</span>
                    </div>
                    <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </a>
            </li>

            <!-- 2. 나머지 파일들 (이름순 정렬) -->
            <li class="file-item">
                <a href="0010. 아마존 핵심 개념.html" class="file-link" target="_blank">
                    <div class="icon"><i class="fa-brands fa-html5"></i></div>
                    <div class="info">
                        <span class="title">0010. 아마존 핵심 개념.html</span>
                        <span class="meta">수정일: 2026-02-18 18:51</span>
                    </div>
                    <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </a>
            </li>
        
            <li class="file-item">
                <a href="0011.구글GCP핵심개념.html" class="file-link" target="_blank">
                    <div class="icon"><i class="fa-brands fa-html5"></i></div>
                    <div class="info">
                        <span class="title">0011.구글GCP핵심개념.html</span>
                        <span class="meta">수정일: 2026-02-18 18:51</span>
                    </div>
                    <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </a>
            </li>
        
            <li class="file-item">
                <a href="0012. Azure 핵심 개념.html" class="file-link" target="_blank">
                    <div class="icon"><i class="fa-brands fa-html5"></i></div>
                    <div class="info">
                        <span class="title">0012. Azure 핵심 개념.html</span>
                        <span class="meta">수정일: 2026-02-18 18:51</span>
                    </div>
                    <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </a>
            </li>
        
            <li class="file-item">
                <!-- 폴더 경로 포함된 파일 예시 -->
                <a href="020. IAM 자격증명 엑세스관리/0020. 유저관리와 IAM.html" class="file-link" target="_blank">
                    <div class="icon"><i class="fa-brands fa-html5"></i></div>
                    <div class="info">
                        <span class="title">0020. 유저관리와 IAM.html</span>
                        <span class="meta">수정일: 2026-02-18 18:51</span>
                    </div>
                    <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </a>
            </li>
        
            <li class="file-item">
                <a href="130. AWS 자동화와 테라폼.html" class="file-link" target="_blank">
                    <div class="icon"><i class="fa-brands fa-html5"></i></div>
                    <div class="info">
                        <span class="title">130. AWS 자동화와 테라폼.html</span>
                        <span class="meta">수정일: 2026-02-18 18:51</span>
                    </div>
                    <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </a>
            </li>
        
            <li class="file-item">
                <a href="902.테라폼아키텍처.html" class="file-link" target="_blank">
                    <div class="icon"><i class="fa-brands fa-html5"></i></div>
                    <div class="info">
                        <span class="title">902.테라폼아키텍처.html</span>
                        <span class="meta">수정일: 2026-02-18 18:51</span>
                    </div>
                    <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </a>
            </li>
        
            <li class="file-item">
                <a href="903.초코레티로 테라폼 설치.html" class="file-link" target="_blank">
                    <div class="icon"><i class="fa-brands fa-html5"></i></div>
                    <div class="info">
                        <span class="title">903.초코레티로 테라폼 설치.html</span>
                        <span class="meta">수정일: 2026-02-18 18:51</span>
                    </div>
                    <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
                </a>
            </li>
        
        </ul>
    </div>
</body>
</html>
