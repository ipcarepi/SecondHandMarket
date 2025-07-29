import os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 📁 디렉토리 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_PATH = os.path.join(BASE_DIR, "product_links.json")

# 🌐 브라우저 설정
options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"
})

# 🎯 크림 홈 리치슈즈 탭 진입
url = "https://kream.co.kr/?tab=home_richshoes"
driver.get(url)

# ⏳ 요소 로딩 대기
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_card"))
    )
except:
    print("❌ 상품 카드가 로딩되지 않았습니다.")
    driver.quit()
    exit()

# 🧠 HTML 파싱
soup = BeautifulSoup(driver.page_source, "html.parser")

# 🔗 제품 링크 추출
product_links = []
for a_tag in soup.select("a.product_card"):
    href = a_tag.get("href")
    if href and href.startswith("/products/"):
        full_url = "https://kream.co.kr" + href
        if full_url not in product_links:
            product_links.append(full_url)

# 💾 JSON 저장
with open(SAVE_PATH, "w", encoding="utf-8") as f:
    json.dump(product_links, f, indent=2, ensure_ascii=False)

print(f"✅ 총 {len(product_links)}개의 링크 저장 완료: {SAVE_PATH}")
driver.quit()
