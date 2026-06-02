# 작업 메모 - 2026-06-03 - Claude Code

## 작업 범위
- 삽화 제작 방향 전체 확정 (비율·화풍·구도)
- 수정한 챕터: 없음 (원고 작업 아님)
- 관련 파일: `00_project/illustration_spec.md` (신규), `05_image/` (폴더 트래킹 시작)

## 완료한 것

**전체 삽화 화풍 확정**
- 비율: 1:1 정방형. PDF 레이아웃 확정 후 크롭/여백으로 2:3 조정 가능성 열어둠
- 화풍: 어두운 수채화 + 먹선 (dark watercolor + ink line)
- 배경 톤: 짙은 남색·인디고·다크 퍼플. 빛 포인트는 따뜻한 금백색
- 실루엣: 청년 체형 (young adult, 성별 미지정 유지). "child silhouette"은 청소년 독자 이질감 이유로 기각

**S002 삽화 프롬프트 확정** → `00_project/illustration_spec.md`
- Before: child silhouette
- After: `a slender young adult's dark silhouette from behind`
- 핵심 묘사: `light rises upward from the ground` (역광 아래→위), 별이 창문 높이에 있음, 손끝이 유리에 닿는 순간

**S005 삽화 프롬프트 확정** → `00_project/illustration_spec.md`
- 이안 첫 등장. 문틈 반쪽 얼굴, 녹슨 열쇠, 흐릿한 윤곽, 바닥 그림자(주인공 존재 암시)
- 핵심: `door gap pours cold light across exactly half his face`, `outlines blur softly at the edges`

**이안 캐릭터 시트 프롬프트 작성** → `00_project/illustration_spec.md`
- GPT(DALL·E)용. 얼굴 4각도, 전신 2컷, 상반신, 표정 5종, 소품(열쇠), 컬러팔레트
- 배경: 크림/양피지색 (어두운 의상이 묻히지 않도록 시트용만 예외)
- 이 시트를 만든 뒤 이후 이안 등장 씬 생성 시 GPT에 참조 이미지로 첨부

**05_image/ 폴더 구조 확정**
- `05_image/` = 씬별 삽화 이미지 + `ian_character_sheet.png` + `cover.png`
- 현재 `S002.png`, `S005.png`, `cover.png` 이미 존재 (이전 작업 산출물)
- 새 프롬프트로 S002, S005 이미지 재생성 필요

## 아직 안 한 것
- 실제 이미지 생성 (GPT에서 이안 캐릭터 시트 생성 → 이후 씬 이미지 순서로)
- S002, S005 이미지 재생성 (기존 파일은 이전 프롬프트 산출물, 새 스펙과 다를 수 있음)
- S003, S004, S006 이후 섹션들의 삽화 프롬프트 미작성
- 4장(숨은이름 시장) 이후 원고 미작성

## 주의할 점
- 정본은 `03_sections/`
- 빌드/프리뷰 생성 여부: 이번 세션 없음 (원고 수정 없었음)
- 다음 작업자가 먼저 봐야 할 파일: `00_project/illustration_spec.md`
- `.superpowers/` 는 `.gitignore`에 추가됨 (브레인스토밍 세션 임시파일)
- `05_image/`의 기존 PNG들은 이전 작업 산출물 — 새 스펙과 맞는지 확인 필요

## 결정된 설정/방향
- **삽화 화풍**: 어두운 수채화 + 먹선. 전 챕터 동일하게 적용
- **이미지 비율**: 1:1 우선, PDF 레이아웃 확정 후 조정
- **실루엣 방침**: 주인공은 항상 청년 체형 실루엣 (young adult, 성별 미지정)
- **이안 일관성**: 캐릭터 시트를 먼저 생성해두고 이후 이안 등장 씬마다 참조로 활용
- **05_image/ 용도**: 씬별 삽화 + 이안 캐릭터 시트 + 북커버 일괄 보관

## 다음 추천 작업
1. `05_image/Character_sheet_ian.png` 확인 — 이미 존재. 새 스펙 기준과 맞는지 검토 필요
2. S002, S005 이미지 재생성 (새 프롬프트 + 캐릭터 시트 참조)
4. 4장(숨은이름 시장 S040~) 원고 작업 재개 — `01_outline/` 플랜 확인 후 시작
