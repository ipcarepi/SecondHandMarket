import os
import re
from collections import defaultdict

# 현재 py 파일 위치 기준
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
parsed_file = os.path.join(BASE_DIR, "parsed_tags.txt")

# 변수명 추출 규칙 (class 이름 → 변수 이름 매핑)
custom_mapping = {
    "product_title": "product_name",
    "product_info_brand": "brand_name",
    "product_img": "image_url",
    "num": "release_price",
    "description": "description",
    "size_box": "size_options"
}

# 기본 테이블
table_fields = defaultdict(list)

try:
    with open(parsed_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("❌ parsed_tags.txt 파일을 찾을 수 없습니다.")
    exit()

for line in lines:
    # 태그 파싱
    match = re.match(r"🔹 <(\w+)>.*?class=\"([^\"]+)\".*?→ 내용: \"(.*?)\"", line)
    if not match:
        continue

    tag, class_name, text = match.groups()
    field_name = custom_mapping.get(class_name, class_name)
    
    # 데이터 타입 유추
    if text.replace(",", "").isdigit():
        dtype = "INT"
    elif re.match(r"https?://", text):
        dtype = "TEXT"
    elif len(text) > 50:
        dtype = "TEXT"
    else:
        dtype = "VARCHAR"

    table_fields["Product"].append((field_name, dtype, text))

# 출력 결과 정리
print("\n📐 자동 ERD 추출 결과:\n")
for table, fields in table_fields.items():
    print(f"[{table}]")
    for field, dtype, sample in fields:
        print(f"- {field} ({dtype}) ← 예시: \"{sample}\"")
