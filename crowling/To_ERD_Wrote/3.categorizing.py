import os
from bs4 import BeautifulSoup

# 현재 .py 파일이 있는 디렉토리
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 분석 대상 HTML 파일 경로
html_path = os.path.join(BASE_DIR, "unknown_product.html")

# 출력 파일 경로
output_path = os.path.join(BASE_DIR, "parsed_tags.txt")

# HTML 파일 열기
try:
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
except FileNotFoundError:
    print(f"❌ 파일을 찾을 수 없습니다: {html_path}")
    exit()

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html, "html.parser")

# 결과 저장 리스트
seen_tags = set()
output_lines = []
output_lines.append("📊 HTML 구조 분석 결과:\n")

# 태그 순회하며 구조 분석
for tag in soup.find_all():
    tag_name = tag.name
    tag_class = " ".join(tag.get("class", [])) if tag.get("class") else ""
    tag_id = tag.get("id", "")
    tag_text = tag.get_text(strip=True)[:30]

    identifier = (tag_name, tag_class, tag_id)
    if identifier in seen_tags:
        continue
    seen_tags.add(identifier)

    # 출력 형식
    line = f"🔹 <{tag_name}>"
    if tag_class:
        line += f' class="{tag_class}"'
    if tag_id:
        line += f' id="{tag_id}"'
    line += f' → 내용: "{tag_text}"'

    print(line)
    output_lines.append(line)

# 파일로 저장
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print(f"\n✅ 분석 결과 저장 완료: {output_path}")
