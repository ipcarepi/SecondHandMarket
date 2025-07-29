import json
import os
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ 디렉토리 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LINKS_PATH = os.path.join(BASE_DIR, "product_links.json")

# ✅ WebDriver 설정
options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

# ✅ 셀레니움 감지 우회
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

# ✅ product_links.json 불러오기
with open(LINKS_PATH, "r", encoding="utf-8") as f:
    product_links = json.load(f)

# ✅ 각 URL 크롤링
for idx, url in enumerate(product_links):
    print(f"\n[{idx+1}/{len(product_links)}] 🔗 접속할 URL: {url}")
    try:
        driver.get(url)
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_title"))
        )
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        result = {"url": url}

        # ✅ name & brand from <title>
        title_tag = soup.find("title")
        if title_tag:
            parts = title_tag.text.strip().split("|")
            if len(parts) >= 2:
                result["name"] = parts[0].strip()
                result["brand"] = parts[1].strip()

        # ✅ model_number
        model_tag = soup.select_one("div.model_number span")
        result["model_number"] = model_tag.text.strip() if model_tag else None

        # ✅ release_price
        release_tag = soup.find(text=re.compile("발매가"))
        if release_tag:
            price_text = release_tag.find_parent().find_next("div")
            if price_text:
                result["release_price"] = re.sub(r"[^\d]", "", price_text.text)

        # ✅ current_price
        curr_tag = soup.select_one(".price .amount")
        result["current_price"] = re.sub(r"[^\d]", "", curr_tag.text) if curr_tag else None

        # ✅ last_trade_price
        last_tag = soup.find(text=re.compile("최근 거래가"))
        if last_tag:
            value = last_tag.find_parent().find_next("div")
            if value:
                result["last_trade_price"] = re.sub(r"[^\d]", "", value.text)

        # ✅ color
        color_tag = soup.find(text=re.compile("대표 색상"))
        if color_tag:
            value = color_tag.find_parent().find_next("div")
            if value:
                result["color"] = value.text.strip()

        # ✅ description
        desc_tag = soup.select_one("div.detail_section .description")
        result["description"] = desc_tag.text.strip() if desc_tag else result.get("name")

        # ✅ delivery_info
        delivery_tag = soup.find(text=re.compile("배송 정보"))
        if delivery_tag:
            section = delivery_tag.find_parent("div")
            result["delivery_info"] = section.get_text(strip=True) if section else None

        # ✅ image_url
        image_tag = soup.select_one("picture img")
        result["image_url"] = image_tag["src"] if image_tag else None

        # ✅ review_score
        score_tag = soup.find("div", class_=re.compile("score_area"))
        if score_tag:
            match = re.search(r"\d\.\d", score_tag.get_text())
            if match:
                result["review_score"] = float(match.group())

        # ✅ review_count
        review_tag = soup.find(text=re.compile("리뷰"))
        if review_tag:
            match = re.search(r"\d[\d,]*", review_tag)
            if match:
                result["review_count"] = int(match.group().replace(",", ""))

        # ✅ 수집 확인
        collected = [k for k, v in result.items() if v]
        missing = [k for k, v in result.items() if not v]
        print(f"🟢 수집된 필드: {collected}")
        print(f"🔴 누락된 필드: {missing}")

        # ✅ JSON 저장
        safe_name = result.get("name", f"product_{idx+1}").replace(" ", "_").replace("/", "_")
        json_path = os.path.join(BASE_DIR, f"{safe_name}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"✅ 저장 완료: {json_path}")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

# ✅ 종료
driver.quit()
