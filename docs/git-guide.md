# Git 협업 가이드 🚀

## 브랜치 전략
- `main`: 최종 안정 버전
- `develop`: 기능 통합 테스트용
- `feature/*`: 기능별 브랜치 (ex. `feature/login`)

## 브랜치 생성 및 병합
```bash
# 브랜치 생성
git checkout -b develop

# 기능 브랜치 생성
git checkout -b feature/login develop

# 커밋
git add .
git commit -m "feat: 로그인 기능 추가"

# 원격 저장소에 푸시
git push origin feature/login

# PR: feature → develop → main

# 현재 develop 브랜치에서 문서 작업 완료
git status
git add .
git commit -m "docs: 프로젝트 문서 추가"
git push origin develop

# main으로 이동해서 병합
git checkout main
git merge develop
git push origin main

# develop 브랜치로 다시 돌아오기
git checkout develop
