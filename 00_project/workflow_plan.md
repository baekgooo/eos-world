# 《어스름 너머의 세계》 제작 작업계획서

## 1. 목표

최종 목표는 선택지, 퍼즐, 실패 페이지, 삽화, 링크가 포함된 **PDF 전자책 게임북**을 완성하는 것이다.

단, 제작 중간 단계부터 PDF를 반복 생성하면 수정과 검수가 무거워지므로, 초중반에는 **마크다운 원고와 HTML 미리보기**를 중심으로 작업하고, 원고·게임 구조·삽화 방향이 안정된 뒤 테스트 PDF와 최종 PDF를 만든다.

## 2. 핵심 원칙

1. 채팅은 회의실로 사용한다.
2. 실제 원고, 설정, 분기, 퍼즐, 삽화 지시는 파일로 저장한다.
3. 작품 기준서와 게임 규칙을 먼저 고정한다.
4. 장면은 섹션 단위로 쪼개어 관리한다.
5. 각 선택지는 다음 섹션 ID로 연결한다.
6. 중간 빌드는 PDF가 아니라 마크다운/HTML 미리보기로 검수한다.
7. 최종 PDF는 원고, 삽화, 링크 구조가 안정된 뒤 제작한다.

## 3. 폴더 구조

```text
projects/eos-world/
  00_project/
  01_outline/
  02_chapters/
  03_sections/
  04_puzzles/
  05_endings/
  06_illustrations/
  07_build/
  08_exports/
```

## 4. 폴더별 역할

### 00_project/
작품의 기준을 보관한다.

예상 파일:

```text
concept.md
world_rules.md
character_bible.md
style_guide.md
game_rules.md
glossary.md
workflow_plan.md
```

역할:
- 작품 소개
- 대상 독자
- 문체와 분위기
- 사잇별의 땅 규칙
- 이안과 주요 인물 설정
- 선택지와 퍼즐 규칙
- 금지할 표현과 방향

### 01_outline/
전체 구조와 분기 흐름을 관리한다.

예상 파일:

```text
table_of_contents.md
chapter_summary.md
section_index.md
route_map.md
ending_map.md
```

역할:
- 목차
- 장별 목표
- 섹션 목록
- 전체 루트맵
- 엔딩 구조

### 02_chapters/
장 단위 읽기용 원고를 관리한다.

예상 파일:

```text
00_prologue.md
01_land_of_between_stars.md
02_dusk_station.md
03_mirror_forest.md
04_hidden_name_market.md
05_nightend_tower.md
06_unopening_door.md
07_heart_of_dusk.md
```

역할:
- 장별 통합 초안
- 문체와 감정선 확인용 원고

### 03_sections/
실제 게임북 섹션을 관리한다.

예상 파일 예시:

```text
S001_prologue_room.md
S002_clock_stops.md
S003_ian_appears.md
S004_follow_ian.md
```

각 섹션 기본 양식:

```md
# S000. 섹션 제목

## 위치

## 목적

## 본문

## 선택지
- A. 선택 내용 → S000

## 게임 기능

## 삽화 필요

## 메모
```

### 04_puzzles/
퍼즐을 별도로 관리한다.

예상 파일:

```text
puzzle_index.md
P001_signpost_rule.md
P002_station_timetable.md
P003_mirror_forest.md
P004_liar_merchant.md
P005_three_doors.md
```

각 퍼즐 기본 양식:

```md
# P000. 퍼즐 제목

## 등장 위치

## 문제

## 정답

## 단서

## 오답 결과

## 공정성 체크
```

### 05_endings/
엔딩과 실패 페이지를 관리한다.

예상 파일:

```text
ending_01_alone_return.md
ending_02_ian_name.md
ending_03_true_ending.md
ending_04_stay_in_dusk.md
bad_end_index.md
bad_end_01_stationmaster.md
```

역할:
- 주요 엔딩
- 배드엔딩
- 실패 페이지
- 재도전 안내 문구

### 06_illustrations/
삽화 기획과 제작물을 관리한다.

예상 구조:

```text
illustration_index.md
style_guide.md
prompts/
drafts/
final/
```

역할:
- 표지
- 장 시작 삽화
- 핵심 장면 삽화
- 퍼즐용 이미지
- 삽화 프롬프트와 최종 파일 관리

### 07_build/
중간 미리보기와 빌드 파일을 관리한다.

예상 파일:

```text
preview.html
route_test.html
build_notes.md
```

역할:
- 선택지 링크 테스트
- HTML 미리보기
- PDF 전 단계 검수

### 08_exports/
최종 산출물을 관리한다.

예상 파일:

```text
eos_world_draft_01.pdf
eos_world_draft_02.pdf
eos_world_final.pdf
```

## 5. 전체 제작 단계

### 1단계. 작품 기준서 작성

먼저 다음 문서를 만든다.

```text
00_project/concept.md
00_project/world_rules.md
00_project/character_bible.md
00_project/game_rules.md
00_project/style_guide.md
```

목표:
- 작품의 정체성 고정
- 독자 연령과 분위기 고정
- 이안의 캐릭터 방향 고정
- 사잇별의 땅 규칙 고정
- 선택지, 퍼즐, 실패 페이지 규칙 고정

### 2단계. 전체 루트맵 확정

다음 문서를 만든다.

```text
01_outline/table_of_contents.md
01_outline/section_index.md
01_outline/route_map.md
01_outline/ending_map.md
```

목표:
- 전체 장 구성 확정
- 섹션 50~60개 내외로 설계
- 퍼즐 12~16개 배치
- 실패 페이지 8~12개 배치
- 주요 엔딩 3~4개 설계

### 3단계. 샘플 제작

먼저 프롤로그와 1장을 완성한다.

목표:
- 1인칭 독자 주인공 방식 확인
- 이안 첫 등장 검수
- 첫 선택지 검수
- 첫 퍼즐 공정성 검수
- 첫 실패 페이지 톤 검수

### 4단계. 섹션 단위 본문 제작

한 번에 한 장 전체를 무리하게 쓰지 않고, 섹션 묶음 단위로 제작한다.

권장 작업 단위:

```text
S001~S005
S006~S010
S011~S015
```

각 섹션마다 확인할 항목:
- 본문
- 선택지
- 다음 섹션 연결
- 퍼즐 여부
- 실패 페이지 여부
- 삽화 필요 여부
- 복선과 후속 영향

### 5단계. 장별 검수

각 장이 끝날 때마다 검수한다.

검수 항목:
1. 이야기 흐름이 자연스러운가?
2. 선택지가 의미 있는가?
3. 퍼즐 단서가 미리 심어졌는가?
4. 실패가 억울하지 않은가?
5. 이안의 비밀이 너무 빨리 드러나지 않는가?
6. 분량이 너무 길거나 짧지 않은가?
7. 삽화 위치가 분명한가?

### 6단계. 전체 링크/게임 구조 테스트

전체 초고가 나오면 문장 다듬기보다 먼저 게임 구조를 테스트한다.

확인 항목:
- 끊긴 선택지가 없는가?
- 모든 선택지가 섹션으로 연결되는가?
- 너무 빠른 엔딩이 과도하지 않은가?
- 퍼즐 정답이 공정한가?
- 배드엔딩이 납득 가능한가?
- 진엔딩 조건이 충분히 설득력 있는가?

### 7단계. 문체 통일과 감정선 강화

게임 구조가 통과된 뒤 문장을 다듬는다.

작업 항목:
- 1인칭 몰입감 강화
- 이안 대사 통일
- 사잇별의 땅 묘사 통일
- 반복 표현 제거
- 유치한 표현 제거
- 긴장감 조절
- 복선 회수 강화

### 8단계. 삽화 제작

원고가 어느 정도 고정된 뒤 삽화를 제작한다.

추천 순서:
1. 표지
2. 스타일 샘플 2~3장
3. 장 시작 삽화
4. 핵심 장면 삽화
5. 퍼즐용 이미지
6. 작은 장식 이미지

삽화는 스타일 통일을 위해 한꺼번에 관리한다.

### 9단계. PDF 제작

최종 PDF에는 다음 요소를 포함한다.

- 표지
- 속표지
- 사용법
- 목차
- 본문 섹션
- 선택지 링크
- 실패 페이지
- 엔딩
- 삽화
- 판권 페이지

최종 검수 항목:
- 선택지 링크 작동
- 페이지 이동 정확성
- 삽화 배치
- 오탈자
- 문체 통일
- 전체 분량

## 6. 채팅에서의 협업 방식

### 대장이 결정할 것

- 방향성
- 분위기
- 장면의 강약
- 이안의 매력과 수상함 정도
- 퍼즐 난이도
- 실패 페이지 수위
- 삽화 취향
- 최종 채택 여부

### 용쿠가 할 것

- 파일 단위 정리
- 장면 초안 작성
- 선택지 설계
- 퍼즐 설계
- 실패 페이지 작성
- 삽화 프롬프트 작성
- 루트맵 정리
- 모순 체크
- 링크 구조 점검
- PDF용 원고 정리

## 7. 한 번의 작업 단위

매 작업은 다음 순서로 진행한다.

1. 오늘 만들 범위 정하기
2. 해당 섹션의 목적 확인
3. 본문 작성
4. 선택지 작성
5. 퍼즐/함정 설계
6. 실패 페이지 작성
7. 다음 섹션 연결
8. 삽화 필요 여부 기록
9. 대장 검토
10. 수정 후 확정

## 8. 중간 산출물 방식

### 초반
마크다운 문서 중심.

### 중반
HTML 미리보기 중심.

### 후반
테스트 PDF 생성.

### 최종
링크와 삽화가 포함된 최종 PDF 전자책 완성.

## 9. 당장 시작할 문서

우선 다음 세 문서를 만든다.

```text
00_project/concept.md
00_project/game_rules.md
01_outline/section_index.md
```

이 세 문서가 앞으로의 작업판이 된다.
