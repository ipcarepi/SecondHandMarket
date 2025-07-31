import json
import os
import requests

API_URL = "http://localhost:8080/api/products"

# 이 .py 파일이 있는 경로 기준으로 ../data_int
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR_INT = os.path.abspath(os.path.join(BASE_DIR, "../data_int"))

def iter_json_files(root):
    """root 아래 모든 .json 파일 경로를 yield (서브디렉토리 포함)"""
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith(".json"):
                yield os.path.join(dirpath, fn)

def main():
    if not os.path.isdir(DATA_DIR_INT):
        print(f"❌ 입력 경로가 없습니다: {DATA_DIR_INT}")
        return

    count_total = 0
    count_success = 0
    count_fail = 0

    for file_path in iter_json_files(DATA_DIR_INT):
        filename = os.path.basename(file_path)
        count_total += 1

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ JSON 파싱 오류: {filename} → {e}")
            count_fail += 1
            continue

        # data_int에는 숫자 필드가 이미 int라고 가정
        payload = {
            "name": data.get("name"),
            "modelNumber": data.get("model_number"),
            "currentPrice": data.get("current_price"),
            "color": data.get("color"),
            "description": data.get("description"),
            "deliveryInfo": data.get("delivery_info"),
            "imageUrl": data.get("image_url"),
            "reviewCount": data.get("review_count") if data.get("review_count") is not None else 0
        }

        try:
            res = requests.post(API_URL, json=payload, timeout=10)
            print(f"📦 {filename} → {res.status_code} | {res.text}")
            if 200 <= res.status_code < 300:
                count_success += 1
            else:
                count_fail += 1
        except Exception as e:
            print(f"업로드 실패: {filename} → {e}")
            count_fail += 1

    print(f"\n=== 업로드 요약 ===")
    print(f"총 파일: {count_total}")
    print(f"성공: {count_success}")
    print(f"실패: {count_fail}")

if __name__ == "__main__":
    main()
