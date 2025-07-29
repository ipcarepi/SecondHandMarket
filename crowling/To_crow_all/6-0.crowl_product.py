import json
import time
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# ✅ 현재 디렉토리 기준
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LINKS_PATH = os.path.join(BASE_DIR, "product_links.json")

# ✅ 셀레니움 옵션 설정 (우회 포함)
options = Options()
# options.add_argument("--headless")  # 필요시 주석 제거
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

# ✅ URL 불러오기
with open(LINKS_PATH, "r", encoding="utf-8") as f:
    product_links = json.load(f)

url = product_links[0]
print(f"🔗 접속할 URL: {url}")
driver.get(url)

try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_title"))
    )
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # ✅ 데이터 수집
    result = {}
    result["url"] = url

    # ERD 기반 항목들
    result["name"] = soup.find("p", class_="product_title").text.strip() if soup.find("p", class_="product_title") else None
    result["brand"] = soup.find("p", class_="product_brand").text.strip() if soup.find("p", class_="product_brand") else None
    result["model_number"] = soup.select_one("div.model_number span").text.strip() if soup.select_one("div.model_number span") else None
    result["current_price"] = soup.select_one(".price .amount").text.replace(",", "").replace("원", "").strip() if soup.select_one(".price .amount") else None
    result["image_url"] = soup.select_one("picture img")["src"] if soup.select_one("picture img") else None
    result["description"] = soup.select_one("div.detail_section .description").text.strip() if soup.select_one("div.detail_section .description") else None

    # ✅ 결과 확인
    collected = [k for k, v in result.items() if v]
    missing = [k for k, v in result.items() if not v]

    print("🟢 수집된 필드:", collected)
    print("🔴 누락된 필드:", missing)

    # ✅ 안전한 파일명 생성 및 저장
    safe_name = result["name"] if result["name"] else "unknown"
    safe_name = re.sub(r"[\\/:*?\"<>|]", "_", safe_name.replace(" ", "_"))
    save_path = os.path.join(BASE_DIR, f"{safe_name}.json")

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON 저장 완료: {save_path}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    driver.quit()
