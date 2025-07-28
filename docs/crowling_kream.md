# 예: KREAM 상품 상세 페이지
https://kream.co.kr/products/82991
```bash
# 크롤링 대상:

상품명 (예: Nike Dunk Low Retro White Black)

브랜드 (예: Nike)

카테고리 (예: 신발, 의류 등)

사이즈 옵션 (예: 230, 240, 250, ...)

발매가

썸네일 이미지 URL

# https://kream.co.kr/robots.txt (정책 살펴보기)
User-agent: *
Allow: /
Disallow: /my*
Disallow: /history*
Sitemap: https://kream.co.kr/sitemap.xml

my,랑 history 같이 개인정보 부분만 놔두면 물품 정보나 이런건 크롤링 가능한듯!

