import json
import os
import requests
import re

API_URL = "http://localhost:8080/api/products"
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

def clean_and_parse_price(price_str):
    if price_str is None:
        return None
    try:
        # 숫자만 추출해서 6자리 이하의 값만 허용 (ex: 119000)
        digits = re.sub(r"[^\d]", "", str(price_str))
        if digits and len(digits) <= 6:
            return int(digits)
    except:
        pass
    return None

for filename in os.listdir(DATA_DIR):
    if not filename.endswith(".json"):
        continue

    file_path = os.path.join(DATA_DIR, filename)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ JSON 파싱 오류: {filename} → {e}")
        continue

    current_price = clean_and_parse_price(data.get("current_price"))
    review_count = clean_and_parse_price(data.get("review_count"))

    if current_price is None or current_price == 0:
        print(f"⚠️ current_price 무시됨: {data.get('current_price')} (파일: {filename})")
        continue

    payload = {
        "name": data.get("name"),
        "modelNumber": data.get("model_number"),
        "currentPrice": current_price,
        "color": data.get("color"),
        "description": data.get("description"),
        "deliveryInfo": data.get("delivery_info"),
        "imageUrl": data.get("image_url"),
        "reviewCount": review_count or 0
    }

    try:
        res = requests.post(API_URL, json=payload)
        print(f"📦 {filename} → {res.status_code} | {res.text}")
    except Exception as e:
        print(f"❌ 업로드 실패: {filename} → {e}")
