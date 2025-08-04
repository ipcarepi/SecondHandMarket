import json
import re
from pathlib import Path

# --- 경로를 "이 .py 파일이 있는 위치" 기준으로 설정 ---
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = (BASE_DIR / "../data").resolve()       # 입력 폴더
OUT_DIR  = (BASE_DIR / "../data_int").resolve()   # 출력 폴더 (없으면 생성)

PRICE_KEYS = ["release_price", "current_price", "last_trade_price"]

def to_int_or_none(value):
    if value is None:
        return None
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, str):
        cleaned = re.sub(r"[^\d-]", "", value).strip()
        if cleaned in ("", "-"):
            return None
        return int(cleaned)
    cleaned = re.sub(r"[^\d-]", "", str(value)).strip()
    if cleaned in ("", "-"):
        return None
    return int(cleaned)

def process_file(src_path: Path):
    try:
        rel_path = src_path.relative_to(DATA_DIR)  # DATA_DIR 기준 상대경로
    except ValueError:
        # 혹시 다른 경로가 섞였을 때 안전장치
        rel_path = src_path.name

    out_path = OUT_DIR / rel_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with src_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[SKIP-READ] {src_path}: {e}")
        return

    if not isinstance(data, dict):
        print(f"[SKIP-TYPE] 객체(JSON Object)가 아님: {src_path}")
        return

    changed = False
    changes = []

    for key in PRICE_KEYS:
        if key in data:
            old_val = data[key]
            new_val = to_int_or_none(old_val)
            if new_val != old_val:
                data[key] = new_val
                changed = True
                changes.append(f"{key}: {old_val} -> {new_val}")

    try:
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        if changed:
            print(f"[WROTE-CHANGED] {out_path} | " + ", ".join(changes))
        else:
            print(f"[WROTE] {out_path} | 변경 없음")
    except Exception as e:
        print(f"[ERROR-WRITE] {out_path}: {e}")

def main():
    if not DATA_DIR.exists():
        print(f"[ERROR] 입력 경로 없음: {DATA_DIR}")
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    files = list(DATA_DIR.rglob("*.json"))
    if not files:
        print(f"[INFO] JSON 파일이 없습니다: {DATA_DIR}")
        return

    print(f"[INFO] 대상 파일 수: {len(files)}")
    for p in files:
        process_file(p)

if __name__ == "__main__":
    main()
