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
git status
git add .
git commit -m "기능 설명 또는 메모"
git push origin develop # 내 github develop 에 push
git push upstream develop # 형 github에 push


# 원격 저장소에 푸시
git push origin 브랜치 이름/거기 디렉토리

# 내 main에 추가하기 develop이랑 합치기
git checkout main
git merge develop
git push origin main
git push upstream main # 형 main에 push

# develop 브랜치로 다시 돌아오기
git checkout develop

# 최신 정보 가져오기
git fetch upstream

# 1. 원격 저장소 최신 상태 가져오기
git fetch upstream
# 2. git merge upstream/main --no-edit
팀의 main을 내 main에 병합 형이 작업한거 가져오기.
git checkout main
git merge upstream/main
git push origin main  # 내 GitHub 저장소에도 반영
