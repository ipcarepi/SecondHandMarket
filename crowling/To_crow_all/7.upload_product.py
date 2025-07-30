import json
import os
import requests

API_URL = "http://localhost:8080/api/products"  # 서버 실행 중이어야 함

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

for filename in os.listdir(DATA_DIR):
    if filename.endswith(".json"):
        file_path = os.path.join(DATA_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"❌ JSON 파싱 오류: {filename} → {e}")
                continue

        # 데이터 검증 및 필터링
        try:
            payload = {
                "name": data.get("name"),
                "modelNumber": data.get("model_number"),
                "currentPrice": int(data.get("current_price", 0)),
                "color": data.get("color"),
                "description": data.get("description"),
                "deliveryInfo": data.get("delivery_info"),
                "imageUrl": data.get("image_url"),
                "reviewCount": int(data.get("review_count", 0))
            }

            res = requests.post(API_URL, json=payload)
            print(f"📦 {filename} → {res.status_code} | {res.text}")
        except Exception as e:
            print(f"❌ 업로드 실패: {filename} → {e}")
