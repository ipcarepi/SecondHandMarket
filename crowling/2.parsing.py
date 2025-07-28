import os
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ✅ 현재 스크립트 기준 디렉토리 (py파일 실행 위치)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ 셀레니움 브라우저 설정
options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

# ✅ 셀레니움 감지 우회
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

# ✅ 대상 상품 URL
url = "https://kream.co.kr/products/82991"
driver.get(url)
time.sleep(5)  # 충분한 로딩 대기

# ✅ HTML 가져오기
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# ✅ 상품명 추출
product_name_tag = soup.find("p", class_="product_title")
product_name = product_name_tag.text.strip() if product_name_tag else "unknown_product"

# ✅ 파일에 쓸 수 없는 문자 제거
safe_name = re.sub(r"[\\/:*?\"<>|]", "_", product_name)
filename = os.path.join(BASE_DIR, f"{safe_name}.html")

# ✅ HTML 저장
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 저장 완료: {filename}")

driver.quit()
