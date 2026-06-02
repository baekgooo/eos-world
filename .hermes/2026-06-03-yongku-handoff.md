# 작업 메모 - 2026-06-03 - Claude Code → 용쿠

## 작업 범위
- 원고 수정 없음 (이번 세션은 전부 삽화·웹 작업)
- 관련 파일: `00_project/illustration_spec.md`, `scripts/build_preview.py`, `05_image/`, `docs/`

## 완료한 것

**삽화 화풍 전체 확정**
- 비율: 1:1 정방형 (PDF 레이아웃 확정 후 크롭으로 2:3 조정 가능)
- 화풍: 어두운 수채화 + 먹선 (dark watercolor + ink line)
- 주인공 실루엣: 청년 체형 (young adult, 성별 미지정)
- 모든 프롬프트 → `00_project/illustration_spec.md`에 저장

**S002 프롬프트 확정**
- Before: child silhouette → After: `a slender young adult's dark silhouette`
- 핵심: `light rises upward from the ground` + 별이 창문 높이에 + 손끝이 유리에

**S005 프롬프트 확정**
- 이안 첫 등장. 문틈 반쪽 얼굴, 녹슨 열쇠, 흐릿한 윤곽, 바닥 그림자(주인공)

**이안 캐릭터 시트 프롬프트 작성 (GPT/DALL·E용)**
- 얼굴 4각도 / 전신 2컷 / 상반신 / 표정 5종 / 소품(열쇠) / 컬러팔레트
- `05_image/Character_sheet_ian.png` 이미 존재 — 새 스펙과 맞는지 검토 필요

**큰작업실 웹 [캐릭터] 메뉴 추가**
- 주인공 카드: S002.png + 핵심믿음/별빛/성장/갈등 태그
- 이안 카드: 캐릭터시트 이미지 + 전체 설정 + 빌린 이름 시크릿 태그

**큰작업실 웹 [이미지] 메뉴 추가**
- 북커버 + 이안 캐릭터 시트 + 씬별 삽화 20개 현황 한 화면에
- 이미지 있음 배지(초록) / 프롬프트 있음 배지(갈색) / 이미지 생성 필요(회색)
- S002·S005 프롬프트 펼쳐보기 가능
- 이미지 클릭 → 모달로 확대 (ESC 또는 배경 클릭 닫기)
- 캐릭터/이미지 메뉴 선택 시 스토리줄기 프레임 자동 숨김

## 아직 안 한 것
- S002, S005 외 나머지 씬 이미지 프롬프트 미작성 → 이미지 패널에서 "이미지 생성 필요"로 표시됨
- 4장(숨은이름 시장 S040~) 원고 미작성

## 주의할 점
- 정본은 `03_sections/`
- 빌드/프리뷰 생성 여부: 이번 세션 빌드 완료, GitHub 배포됨
- 다음 작업자가 먼저 봐야 할 파일: `00_project/illustration_spec.md`
- `05_image/`에 새 이미지 추가하면 빌드(`python scripts/build_preview.py`) 한 번 돌려야 웹에 반영됨
- `Character_sheet_ian.png`가 새 스펙(크림 배경, 표정 5종 등)과 맞는지 확인 필요

## 결정된 설정/방향
- **삽화 화풍**: 어두운 수채화 + 먹선, 전 챕터 동일 적용
- **이미지 비율**: 1:1 우선
- **주인공 실루엣**: 항상 청년 체형 (young adult), 성별 미지정
- **이안 일관성**: 씬 이미지 생성 시 Character_sheet_ian.png를 GPT에 참조로 첨부
- **05_image/ 구조**: 씬별 삽화(`S###.png`) + `Character_sheet_ian.png` + `cover.png`

## 다음 추천 작업
1. `Character_sheet_ian.png` 검토 — 새 스펙 기준과 맞으면 유지, 아니면 재생성
2. 나머지 씬 이미지 생성 (illustration_spec.md 참고, 생성 후 `05_image/`에 저장 → 빌드)
3. 4장 숨은이름 시장(S040~) 원고 작업 재개
