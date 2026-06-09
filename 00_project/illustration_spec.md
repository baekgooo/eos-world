# 삽화 제작 스펙

## 확정된 전체 방향

| 항목 | 결정 |
|------|------|
| 이미지 비율 | 1:1 정방형. PDF 조판 때 크롭/여백 조정 |
| 기본 화풍 | watercolor and ink illustration. S002/S005처럼 수채 번짐, 잉크 선, 종이 질감, 빛의 번짐 유지 |
| 전체 톤 | 어둡기만 한 그림 금지. 챕터별 메인 컬러를 달리하고, 빛·유리·얼음·거울은 충분히 환하게 처리 |
| 인물 실루엣 | 실제 삽화 본문에서는 주인공 얼굴·표정은 실루엣/흐림 처리. 단, 이미지 생성 시에는 주인공 캐릭터시트 레퍼런스로 10대 후반 남자의 헤어스타일·체격·옷을 맞춘다. 이안은 S005/캐릭터 시트 기준 |
| 공통 키라이트 | 낮은 별빛·별조각·문빛은 따뜻한 금백색 또는 부드러운 흰빛 |
| 금지 | cute, chibi, anime/manga exaggeration, bright cheerful cartoon, photorealistic, 3D render, gore, watermark, signature |

---

## 챕터별 팔레트/무드 기준

- 프롤로그/방: deep navy, ink black, cold window blue, warm small star. S002/S005 기준의 어둡고 조용한 경이.
- 1장 낮은 별길: twilight teal, muted grass green, dusky violet, warm low stars. 낯설지만 숨 쉴 수 있는 초저녁 야외.
- 2장 초저녁 정거장: smoky amber, tarnished brass, old paper beige, railway green, blue shadows. 친절하지만 수상한 빈 정거장.
- 3장 거울숲: luminous misty silver, pale aqua, wet green-gray, glass highlights. 어둡게 죽이지 말고 비 젖은 유리와 거울빛을 환하게.
- 4장 숨은이름 시장: muted burgundy, old gold, dusty violet, bottle green, indigo shadow. 어둡지만 색이 많은 야시장.
- 5장 밤끝탑: moonlit stone gray, violet-black, desaturated blue, cold white floor light. 차갑고 높지만 완전한 암흑은 아님.
- 6장 열리지 않는 문: warm threshold cream, bureaucratic parchment, brass stamp, teal shadow. 문빛과 사무적인 판타지의 대비.
- 7장 어스름의 심장/엔딩: translucent ice blue, pearl white, pale lavender, crystal cyan, warm human light. 얼음·보석·거울처럼 밝고 투명하게.

---

## 캐릭터시트 레퍼런스 적용 규칙

- 주인공이 등장하는 삽화: 생성 시 주인공 캐릭터시트 레퍼런스 이미지를 함께 첨부하고, 헤어스타일·마른 체격·옷차림을 캐릭터시트에 맞춘다. 실제 삽화에서는 얼굴과 표정이 독자를 특정하지 않도록 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다.
- 이안이 등장하는 삽화: 생성 시 이안 캐릭터시트 레퍼런스 이미지를 함께 첨부하고, 헤어스타일·가는 체격·옷차림·녹슨 열쇠를 캐릭터시트에 맞춘다.

---

## 공통 네거티브 프롬프트

```
bright cheerful cartoon, cute, childlike, chibi, anime style, manga, photorealistic,
3D render, plastic skin, horror gore, violent, over-saturated neon, white empty background,
text, readable letters, watermark, signature, logo, extra fingers, distorted hands
```

---

## S002 — 멈춘 시계와 이상한 창밖

**파일**: `05_image/S002.png`  
**구도 핵심**: 방 안 + 창문 + 창가에 가까이 떠 있는 별 + 멈춘 시계 + 주인공 실루엣.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, atmospheric literary fantasy, matching the established watercolor-and-ink reference style.

A quiet bedroom at night in deep navy and ink-black washes. Center: an old wooden window with dark ink crossbars. Outside the glass, a single small star floats impossibly close at eye level, glowing warm gold-white. The light from the star and the strange outside world rises softly upward, making the window area cold blue and luminous while the room remains dark.

Foreground bottom: the protagonist seen only from behind as an ambiguous teen silhouette, one hand lifted toward the cold glass. Right background: a round wall clock barely visible in shadow, its hands stopped. Keep the composition still and intimate, with heavy watercolor granulation, wet-on-wet edges, and fine ink lines around the window and hand.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration.

Mood: quiet wonder, uneasy beauty, the first impossible thing. Palette: deep navy, cold blue, ink black, one warm star. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 멈춘 시계와 이상한 창밖 장면을 그린다. 핵심 구도는 다음과 같다: 창문 앞의 방, 낮게 떠 있는 별, 멈춘 시계. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 짙은 남색, 잉크 블랙, 차가운 창문빛, 작은 금백색 별빛을 중심으로 한 조용하고 불가사의한 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다.
```

---

## S004 — 방 안에 없던 문

**파일**: `05_image/S004.png`  
**구도 핵심**: 평범한 방 안에 원래 없던 문, 문틈의 별빛.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, atmospheric literary fantasy.

A familiar bedroom at night, painted with deep navy watercolor shadows and loose ink linework. The ordinary bedroom door is visible off to one side, unchanged and closed, while the impossible event happens on the wall beside the bookcase. On that blank wall, a thin vertical seam has opened, as if the wallpaper first tore and then slowly widened from the inside. The seam has become the outline of a narrow door that should not exist.

Through the crack spills an ambiguous dusk-colored light — not yellow, not pure white, somewhere between the sky just before nightfall and the first shadow of night. Tiny star-dust motes drift out of the gap and settle on the bedroom floor. The door itself should feel real but wrong: plain and old rather than ornate, with a worn metal handle and a few tiny scratched marks below the handle, too small and blurred to read.

Foreground or midground: the protagonist's ambiguous teen silhouette has taken one cautious step toward the door, shoulders tense, face turned away or obscured. Keep ordinary room details visible in the darkness — the bookcase beside the impossible door, bed corner, desk edge, scattered books — so the new door feels like a quiet violation of a real room.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration.

Mood: the moment just before someone speaks from behind the crack; hesitation, uncanny wonder, and a small held breath. Palette follows the prologue bedroom mood: deep room navy, ink black, dusk-blue doorlight, tiny warm star-dust sparks. No readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 익숙한 밤의 방 안에서, 원래 방문은 한쪽에 그대로 닫혀 있고, 책장 옆의 빈 벽에 있어서는 안 될 문이 생겨나는 장면을 그린다. 처음에는 벽지가 찢어진 것처럼 보이는 가느다란 세로선이 벽에 생겼고, 그 선이 안쪽에서 밀리는 것처럼 조금 벌어지며 좁은 문의 윤곽이 된다. 문은 화려한 판타지 문이 아니라, 현실 방과 조용히 어긋난 낡고 평범한 문처럼 보여야 한다.

문틈 사이로는 노란빛도 순백색도 아닌 애매한 어스름빛이 새어 나온다. 해가 완전히 지기 전의 하늘빛과 밤이 막 시작되기 전의 그림자가 섞인 듯한 차가운 푸른빛에, 아주 작은 별가루 같은 금백색 입자들이 흘러나와 방바닥에 내려앉는다. 문에는 낡은 금속 손잡이가 있고, 손잡이 아래에는 작게 긁힌 자국들이 있지만 실제로 읽을 수 있는 글자는 넣지 않는다.

주인공은 화면 앞쪽이나 중간 거리에서 그 문 쪽으로 조심스럽게 한 걸음 다가간 실루엣으로 표현한다. 얼굴과 표정은 특정되지 않게 뒷모습, 옆모습, 흐린 그림자 중심으로 처리하고, 어깨와 몸의 긴장만 보이게 한다. 책장, 침대 모서리, 책상 끝, 흩어진 책 같은 평범한 방의 물건들이 어둠 속에 보이게 해서, 갑자기 생긴 문이 현실 방을 조용히 어긋나게 만든 느낌을 살린다.

색감은 프롤로그 방 분위기 기준: 짙은 남색, 잉크 블랙, 어스름한 푸른 문틈빛, 작고 따뜻한 금백색 별가루. 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지한다. 분위기는 문턱을 넘기 전의 망설임, 문틈 뒤에서 누군가 숨을 삼키고 곧 말을 걸 것 같은 불가사의한 긴장으로 잡는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더, 치비, 애니 과장, 밝고 귀여운 카툰, 워터마크, 서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다.
```

---

## S005 — 문틈에서 나타난 이안

**파일**: `05_image/S005.png`  
**구도 핵심**: 문틈에서 나타난 이안, 녹슨 열쇠, 반쪽 얼굴의 빛.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, atmospheric literary fantasy, matching the established Ian character reference style.

A mysterious adolescent boy stands in a half-open doorway, caught in a vertical blade of cold silver light. He is slender, slightly androgynous, with dark tousled hair whose tips carry a faint gold-indigo twilight glow. One side of his face is lit, the other dissolves into blue-black shadow. His edges blur subtly in watercolor at the shoulders and sleeves, as if he is not fully present.

In his hand he grips an old rust-covered key, held so tightly the knuckles look pale. The doorway and room around him are painted in deep navy, gray, and ink stains, with expressive fine ink marks in the hair, eyes, key, and doorframe.

Character reference: If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: ancient, quiet, unsettling but not threatening; someone who has searched for a long time. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 문틈에서 나타난 이안 장면을 그린다. 핵심 구도는 다음과 같다: 문틈에서 나타난 이안, 녹슨 열쇠, 어스름빛. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 짙은 남색, 잉크 블랙, 차가운 창문빛, 작은 금백색 별빛을 중심으로 한 조용하고 불가사의한 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S008B — 문밖을 직접 살핀다

**파일**: `05_image/S008B.png`  
**구도 핵심**: 문틈 너머 낮은 별과 어스름 풀밭.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, literary fantasy.

View from inside the dark bedroom through the opened impossible door. Beyond the threshold is not a hallway but a twilight meadow under low-hanging stars. The grass is muted teal-green and violet-gray, brushed loosely with watercolor. Several small warm stars hover close to the ground like quiet lanterns, lighting the grass from below.

Foreground: the dark edge of the doorframe and the protagonist's partial silhouette, one hand on the frame, leaning forward to look. The interior behind them remains deep navy, while the outside meadow is brighter, misty, and breathable.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration.

Mood: first glimpse of another world, fear mixed with invitation. Palette: twilight teal, muted grass green, dusky violet, warm low star gold. Keep the established watercolor-and-ink texture but make the outside air softer and less dark. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 문밖을 직접 살피는 장면을 그린다. 핵심 구도는 다음과 같다: 어두운 방 안의 문틀 너머로 보이는 어스름 풀밭, 낮게 떠 있는 별, 종이처럼 접힌 먼 산맥, 하늘 쪽으로 거꾸로 올라가는 강. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 방 안쪽은 짙은 남색과 잉크 블랙으로 어둡게 두고, 문밖 세계는 어스름한 청록, 부드러운 풀빛, 흐린 보라, 따뜻한 낮은 별빛으로 더 숨 쉴 수 있게 밝힌다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 처음 보는 세계의 조용한 초대와 불안을 함께 느끼게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다.
```

---

## S010 — 낮은 별 아래로 떨어지다

**파일**: `05_image/S010.png`  
**구도 핵심**: 낮은 별 아래 풀밭에 떨어진 주인공과 이안.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, atmospheric fantasy.

A twilight field in the land between reality and dream. The protagonist has just fallen into damp grass under low stars; show an ambiguous teen silhouette crouched or half-sitting in the foreground, one hand pressed into the grass. Ian stands a short distance away, slim and quiet, his outline faintly blurred, holding the rusty key.

The sky is not overhead-only; small stars float low among the grass and near the horizon, casting warm gold-white dots across cool teal, blue, and violet washes. The field should feel strange but open, a relief after the dark room.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: disorientation, wonder, the first breath in a new world. Palette: dusky teal, soft violet, wet grass green, warm low stars. Loose watercolor blooms and fine ink accents. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 낮은 별 아래 풀밭에 떨어진 직후의 장면을 그린다. 핵심 구도는 다음과 같다: 축축한 풀밭에 무릎이나 손을 짚은 주인공 실루엣, 조금 떨어져 조용히 서 있는 이안, 풀잎 사이와 낮은 하늘에 떠 있는 작은 별들. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 색감은 어스름한 청록, 검푸른 풀빛, 부드러운 보라, 젖은 흙의 어두운 녹색, 따뜻한 금백색 낮은 별빛으로 잡는다. 방 장면보다 공기가 열려 있고, 낯선 세계에 처음 숨을 들이마시는 느낌이 나야 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S014 — 낮은 별이 가리키는 길

**파일**: `05_image/S014.png`  
**구도 핵심**: 세 갈래 길 앞의 주인공과 이안, 낮은 별, 표지판.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, atmospheric literary fantasy.

A wide traveling scene in a twilight meadow in the land between reality and dream, before the characters fully arrive at the puzzle. The protagonist and Ian are small figures walking after a low floating star through grass that opens only a few steps ahead of them. Behind them, the grass has already closed cleanly, leaving no trace of the protagonist's footprints. Near Ian's feet, show only a few faint marks like pale water stains drying on old paper, almost disappearing.

The low star is the main focus: it hovers just above the grass at walking height, not a perfect round orb but a small gold-white shape like a star drawn on trembling water, its edges softly wavering as it leads the way. The path should feel temporary and alive, sliding open through the grass.

Make the strange world larger than the puzzle: far above the dusky hills, a river flows upward into the sky. Somewhere near the protagonist's next step, a thin black thread-like crack hides between grass blades, barely visible. The three-way fork and the old signboards should appear only in the far distance as small silhouettes or a vague destination, not as the central subject; do not include the small stone clue in this image.

Palette: twilight teal, muted grass green, dusky violet, blue-gray shadows, warm gold-white low-star light. Use wet watercolor blooms, paper texture, and fine ink lines for grass, the wavering star, the temporary path, and the two quiet silhouettes.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: uncanny wonder during the first walk through the new world, a quiet moving journey rather than a puzzle close-up. This must be an outdoor meadow scene only: no bedroom, no interior wall, no door, no doorway, no doorframe, no portal, no glowing crack in a wall. No readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 주인공과 이안이 낮은 별을 따라 풀밭 사이를 걸어가는 넓은 이동 장면을 그린다. 아직 퍼즐의 단서에 가까이 도착한 장면이 아니라, 사잇별의 땅을 처음 걸으며 이 세계의 규칙을 몸으로 느끼는 장면이다. 시점은 두 인물의 뒤쪽 또는 옆뒤쪽에서 바라보는 구도. 두 인물은 화면 아래쪽이나 중간 거리의 작은 실루엣으로 두고, 낮은 별과 이상한 풀길, 하늘로 흐르는 강이 장면의 중심이 되게 한다.

장면의 핵심은 사잇별의 땅의 이상한 규칙이다. 풀밭은 두 사람 앞에서만 길처럼 갈라지고, 지나온 뒤쪽은 다시 닫혀 주인공의 발자국이 전혀 남지 않는다. 반면 이안의 발밑에는 오래전 물에 젖었던 종이가 마르며 남긴 얼룩 같은 희미한 자국이 몇 개만 거의 사라지듯 남아 있다. 풀잎 사이에는 발밑의 위험을 암시하는 가느다란 검은 실 같은 틈이 숨어 있고, 먼 산등성이 위로는 강물이 하늘 쪽으로 거꾸로 흘러 올라간다.

화면의 중심에는 손바닥보다 조금 큰 낮은 별이 풀 위에 낮게 떠서 길을 이끈다. 별은 완전한 둥근 빛덩어리가 아니라, 물 위에 그린 별 모양이 천천히 흔들리는 듯한 금백색 빛으로 표현한다. 길은 살아 있는 풀밭이 앞쪽에서만 조용히 열리는 느낌이어야 한다. 세 갈래 길과 낡은 표지판은 멀리 있는 작은 실루엣이나 희미한 목적지 정도로만 보이게 하고, 이 이미지에서는 작은 돌 단서를 넣지 않는다.

색감은 어스름한 청록, 부드러운 풀빛, 흐린 보라, 푸른 회색 그림자, 낮게 뜬 따뜻한 금백색 별빛. 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 방 장면보다 숨 쉴 수 있는 야외의 밝기를 남긴다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 낯설고 아름다운 문학적 판타지와 첫 이동의 조용한 경이로 잡는다.

표지판이 멀리 보이더라도 실제로 읽을 수 있는 글자는 넣지 말고, 글씨가 있을 듯한 추상적인 잉크 자국만 표현한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더, 치비, 애니 과장, 밝고 귀여운 카툰, 워터마크, 서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S015 — 세 갈래 표지판

**파일**: `05_image/S015.png`  
**구도 핵심**: 세 갈래 표지판, 작은 돌, 뒤쪽의 희미한 반짝임.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, close-up fantasy puzzle scene.

A low, close view at the base of two old weathered signboards standing between the paths. The signboards point in opposite directions, but their words are not readable; suggest writing only as blurred abstract ink strokes on cracked wood. The main focus is a small half-buried stone between the two posts, almost hidden by grass blades. The stone is ordinary and easy to miss, but a tiny warm gold-white glimmer catches its edge.

Compose the image like a clue being discovered: foreground grass large and detailed, the small stone near the lower center, two leaning wooden signboards rising above it, and a faint low-star sparkle peeking from behind the signboards. The three path choices should be implied by dark and light gaps in the background, not shown as a wide landscape. The protagonist may appear only as a partial blurred hand or knee at the edge, as if bending down to look; Ian may be a soft shadow behind the signboards. Do not make the characters the focus.

Keep the scene luminous but intimate: damp grass in muted green-teal, dusky lavender shadows, soft gold-white glints, ink cracks in wood, delicate texture on the stone. This image is about noticing the small hidden clue, not the journey across the meadow.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: quiet concentration, a puzzle clue waiting to be seen. Watercolor washes, ink details. This must be an outdoor ground-level scene at the base of signboards: no bedroom, no interior wall, no door, no doorway, no doorframe, no portal, no glowing crack in a wall. No readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 세 갈래 길 전체를 멀리 보여주는 장면이 아니라, 표지판 아래에 숨은 작은 단서를 가까이 들여다보는 클로즈업 장면을 그린다. 화면의 중심은 서로 반대 방향을 가리키는 낡은 표지판 두 개와, 그 사이 풀잎에 반쯤 묻힌 작은 돌 하나다. 표지판의 나무결과 갈라진 잉크 자국은 보이지만, 실제로 읽을 수 있는 글자는 절대 넣지 않는다.

구도는 낮고 가까운 시점이다. 앞쪽 풀잎은 크게 보이고, 작은 돌은 화면 아래쪽 중앙 근처에서 거의 놓치기 쉬운 크기로 놓인다. 돌 가장자리에는 아주 약한 금백색 빛이 닿아 있어, 평범하지만 중요한 단서처럼 느껴지게 한다. 두 표지판은 화면 위쪽으로 비스듬히 솟아 있고, 표지판 뒤쪽에는 낮은 별빛 하나가 아주 작게 숨어 반짝인다. 세 갈래 길은 배경의 어둡고 밝은 틈으로만 암시하고, 넓은 풍경이나 이동 장면처럼 보이지 않게 한다.

주인공과 이안은 이 이미지의 중심이 아니다. 주인공은 화면 가장자리에 흐릿한 손끝이나 무릎 일부만 보여, 허리를 숙여 돌을 살피는 느낌이면 충분하다. 이안은 표지판 뒤쪽의 부드러운 그림자 정도로만 남겨도 된다. 이 장면은 두 사람이 걷는 장면이 아니라, 큰 표지판보다 작고 낮은 돌을 알아차리는 순간이다.

색감은 어스름한 청록, 젖은 풀빛, 흐린 보라 그림자, 부드러운 금백색 반짝임. 수채 번짐, 종이 질감, 섬세한 잉크 선으로 풀잎, 나무 표지판의 갈라짐, 작은 돌의 표면을 자세히 살린다. 분위기는 조용한 집중, 숨은 단서를 발견하기 직전의 문학적 판타지로 잡는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더, 치비, 애니 과장, 밝고 귀여운 카툰, 워터마크, 서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S019 — 초저녁 정거장의 불빛

**파일**: `05_image/S019.png`  
**구도 핵심**: 선로 없는 초저녁 정거장, 여러 시계, 역무원 실루엣.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, atmospheric fantasy station.

A strange dusk station with no railway tracks. Old platforms stretch into blue-gray mist, lit by smoky amber lamps. Several clocks hang at different angles from beams and pillars, each slightly different, their faces suggested but not readable. At mid-distance stands the stationmaster as a polite silhouette in uniform, welcoming but too still.

The protagonist and Ian are small in the foreground, entering the station. Ian's posture is guarded. Use tarnished brass, old paper beige, smoky amber, railway green, and cool blue shadows. Keep the watercolor texture loose and the ink architecture delicate.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: antique, polite, suspiciously safe. Not horror, not bright cartoon. No readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 초저녁 정거장의 불빛 장면을 그린다. 핵심 구도는 다음과 같다: 선로 없는 초저녁 정거장, 여러 개의 시계, 친절한 역무원 실루엣. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 스모키 앰버, 오래된 종이색, 낡은 황동, 철도 녹색, 푸른 그림자를 중심으로 한 수상한 정거장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S020 — 말하는 시간표

**파일**: `05_image/S020.png`  
**구도 핵심**: 말하는 시간표 앞의 주인공, 웃는 역무원, 경계하는 이안.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, literary fantasy.

Inside the dusk station, a large old timetable board stands like a living object. Its panels are filled with marks and rows, but no readable text. The board seems to lean forward as if speaking. A smiling stationmaster stands beside it, too courteous, one hand raised in explanation. The protagonist faces the board; Ian stands slightly behind, tense and wary.

Palette: old paper beige, tarnished brass, smoky amber lamps, muted railway green, blue-violet shadows. The board should feel charming at first glance and unsettling on a second look. Use ink lines for panels, clocks, and uniform details; watercolor blooms for lamplight.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: helpful information that may not be safe. No readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 말하는 시간표 장면을 그린다. 핵심 구도는 다음과 같다: 말하는 시간표 앞에 선 주인공, 웃는 역무원, 경계하는 이안. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 스모키 앰버, 오래된 종이색, 낡은 황동, 철도 녹색, 푸른 그림자를 중심으로 한 수상한 정거장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S022 — 너무 안전하다는 말

**파일**: `05_image/S022.png`  
**구도 핵심**: 웃는 역무원, 굳은 이안, 바닥 물에 비친 새장 그림자.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, moody fantasy station.

A station platform under warm amber lamps. The stationmaster smiles politely at the protagonist, his posture neat and reassuring. Ian stands nearby, rigid and silent, half in blue shadow. On the wet floor between them, a puddle reflects not the ceiling but the faint shape of a birdcage, its bars curved across the reflected light.

The scene should not be pitch-black. Use smoky amber, tarnished brass, wet blue-gray, muted green, and ink-black reflections. The birdcage reflection must be subtle but readable as a warning.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: the word "safe" beginning to feel like a trap. Watercolor and ink texture, no text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 너무 안전하다는 말 장면을 그린다. 핵심 구도는 다음과 같다: 웃는 역무원과 굳은 이안, 바닥 물에 비친 새장 그림자. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 스모키 앰버, 오래된 종이색, 낡은 황동, 철도 녹색, 푸른 그림자를 중심으로 한 수상한 정거장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S024 — 역무원을 따른다

**파일**: `05_image/S024.png`  
**구도 핵심**: 이름 빈칸이 입처럼 벌어지는 임시 보관표.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, symbolic fantasy close-up.

A temporary storage form or ticket slip lies on an old station counter under amber light. The blank name field is not normal: it opens like a small dark mouth in the paper, as if waiting to swallow a name. Around it are station objects — brass stamp, ink pad, old paper stacks — rendered with fine ink lines. Do not render readable words or labels.

In the background, blurred silhouettes of the stationmaster and protagonist lean over the counter; Ian's shadow is pulled back, alarmed. Palette: old paper beige, smoky amber, tarnished brass, deep blue shadows, a small dangerous black opening.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: bureaucratic politeness turning predatory. Watercolor washes, ink details, no text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 역무원을 따른다 장면을 그린다. 핵심 구도는 다음과 같다: 이름 빈칸이 입처럼 벌어지는 임시 보관표. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 스모키 앰버, 오래된 종이색, 낡은 황동, 철도 녹색, 푸른 그림자를 중심으로 한 수상한 정거장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S025 — 매표소 안쪽의 작은 목소리

**파일**: `05_image/S025.png`  
**구도 핵심**: 닫힌 매표소 틈으로 나온 작은 종이표.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, quiet fantasy station detail.

A closed ticket booth in the dusk station. From a narrow slot or crack in the shutter, a small paper ticket has slipped out, catching a soft warm glow. The booth is old wood and brass, with dark green paint worn away at the edges. Behind the slot, only darkness and a suggestion of a small hidden presence.

Foreground: the protagonist's hand hesitates near the paper; Ian's faint silhouette watches from behind. Keep any marks on the paper abstract and unreadable. Palette: tarnished brass, old green, warm paper beige, blue shadow.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: a tiny honest voice inside a place of traps. Watercolor and ink, delicate light, no text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 매표소 안쪽의 작은 목소리 장면을 그린다. 핵심 구도는 다음과 같다: 닫힌 매표소 틈으로 나온 작은 종이표. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 스모키 앰버, 오래된 종이색, 낡은 황동, 철도 녹색, 푸른 그림자를 중심으로 한 수상한 정거장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S028 — 시간표 해독

**파일**: `05_image/S028.png`  
**구도 핵심**: 세 승강장 안내가 적힌 말하는 시간표.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, fantasy puzzle board.

A large living timetable board dominates the composition, divided into three platform columns. The board has rows, arrows, clock icons, and abstract marks, but no readable letters or numbers. The surface is old paper and dark wood, lit by amber station lamps. The protagonist studies the board closely while Ian points or watches with tense attention.

Make the puzzle feel fair and visual: three distinct areas, subtle symbols, warm light on the clue surfaces, cool blue shadows around the edges. Use fine ink lines for the board grid and loose watercolor for lamplight and mist.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: concentration, decoding, a path through confusion. No readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 시간표 해독 장면을 그린다. 핵심 구도는 다음과 같다: 세 승강장 안내가 적힌 말하는 시간표. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 스모키 앰버, 오래된 종이색, 낡은 황동, 철도 녹색, 푸른 그림자를 중심으로 한 수상한 정거장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S029 — 거울숲으로 가는 표

**파일**: `05_image/S029.png`  
**구도 핵심**: 검은 물길 위에 떠내려온 거울 손잡이 문.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, transitional fantasy scene.

At the edge of the station, a black water channel runs where tracks should be. Floating on the dark water is a door-like frame with a mirror handle, drifting toward the platform as if it is a train. The water reflects amber station lamps and cold silver fragments of another forest beyond.

The protagonist and Ian stand on the platform, small and cautious. The mirror handle catches a bright pale glint, promising the next chapter. Palette bridges chapters: station amber and brass fading into luminous silver, pale aqua, and wet green-gray reflections.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: departure by an impossible vehicle, beautiful and uncanny. Watercolor and ink, no text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 거울숲으로 가는 표 장면을 그린다. 핵심 구도는 다음과 같다: 검은 물길 위에 떠내려온 거울 손잡이 문. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 스모키 앰버, 오래된 종이색, 낡은 황동, 철도 녹색, 푸른 그림자를 중심으로 한 수상한 정거장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S030 — 표지판 수선공

**파일**: `05_image/S030.png`  
**구도 핵심**: 승강장 기둥 아래에서 작은 글씨를 고치는 표지판 수선공.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, gentle fantasy station vignette.

Under a station pillar, a small sign mender crouches with tools, repairing a weathered signboard. The figure should feel quiet and helpful, not cute or comic. Tiny brushes, nails, paper scraps, and a dim lantern surround them. The sign surface may have abstract strokes but no readable text.

The protagonist and Ian are nearby, watching. Station colors remain warm but subdued: old paper beige, smoky amber, tarnished brass, muted green, blue shadows. Use delicate ink lines for tools and sign edges; watercolor for soft lantern glow.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: a small honest craft in a suspicious place. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 표지판 수선공 장면을 그린다. 핵심 구도는 다음과 같다: 승강장 기둥 아래에서 작은 글씨를 고치는 표지판 수선공. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 스모키 앰버, 오래된 종이색, 낡은 황동, 철도 녹색, 푸른 그림자를 중심으로 한 수상한 정거장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S031 — 거울이 매달린 숲

**파일**: `05_image/S031.png`  
**구도 핵심**: 비 젖은 숲, 나뭇가지의 거울들, 늦게 웃는 반사.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, luminous mirror-forest fantasy.

A rain-wet forest where many small mirrors hang from branches like leaves or fruit. Do not make the scene too dark; the mirrors and raindrops catch pale silver, aqua, and pearl light. The forest floor is damp green-gray, with misty air and soft reflections everywhere.

Foreground: the protagonist stands before the nearest mirror. In that mirror, instead of the forest, a delayed version of the protagonist's face or silhouette is smiling a little too late. Ian stands a step behind, partially reflected in other mirror shards.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: beautiful, cold, self-conscious, uncanny. Palette: luminous misty silver, pale aqua, wet green-gray, glass highlights, thin dark ink branches. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 거울이 매달린 숲 장면을 그린다. 핵심 구도는 다음과 같다: 비 젖은 숲속 나뭇가지마다 거울들이 매달려 있고, 가장 가까운 거울 속에는 숲 대신 늦게 웃는 주인공의 얼굴이 겹쳐 보이는 장면. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 환한 은빛, 옅은 아쿠아, 젖은 녹회색, 유리와 거울의 반사광을 중심으로 한 밝고 차가운 거울숲 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S032 — 나를 따라오는 다른 나

**파일**: `05_image/S032.png`  
**구도 핵심**: 숲길 양쪽 거울 속의 서로 다른 주인공 표정.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, reflective fantasy forest.

A narrow wet path through the mirror forest. On both sides, small hanging mirrors follow the protagonist like watching eyes. Each mirror contains a different reflection of the ambiguous protagonist silhouette — one trying to smile, one looking away, one frozen, one smaller and ashamed — without defining gender or exact facial features.

The actual protagonist walks in the center foreground, shoulders tight. Ian is visible farther back as a quiet dark-blue figure. Keep the scene bright with glass light: pale aqua mist, pearl silver reflections, wet green-gray bark, fine ink branches.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: being judged by versions of yourself. Elegant and eerie, not horror. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 나를 따라오는 다른 나 장면을 그린다. 핵심 구도는 다음과 같다: 젖은 숲길 양쪽의 작은 거울들 속에서 서로 다른 순간의 주인공이 다른 표정으로 따라오는 장면. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 환한 은빛, 옅은 아쿠아, 젖은 녹회색, 유리와 거울의 반사광을 중심으로 한 밝고 차가운 거울숲 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S034 — 세 개의 거울

**파일**: `05_image/S034.png`  
**구도 핵심**: 밝은 거울, 검은 빈 거울, 금 간 흐린 거울 앞의 선택.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, luminous fantasy choice scene.

In a clearing of the wet mirror forest stand three full-length mirrors. Left: a bright smooth mirror with flattering pale light. Center: a black empty mirror like dark water, absorbing reflections. Right: a cracked cloudy mirror with silver fractures and misted glass. The protagonist stands before them, small but central; Ian waits one step behind and to the side, not choosing for them.

The clearing is filled with pale aqua mist, pearl silver highlights, damp green-gray ground, and delicate ink branches. The glass surfaces should be bright and reflective, not muddy or black overall.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: choosing which truth to face. Beautiful, tense, quiet. No readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 세 개의 거울 장면을 그린다. 핵심 구도는 다음과 같다: 세 개의 거울 앞에 선 주인공과 한 걸음 물러선 이안. 왼쪽은 밝고 매끈한 거울, 가운데는 검은 빈 거울, 오른쪽은 금이 간 흐린 거울. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 환한 은빛, 옅은 아쿠아, 젖은 녹회색, 유리와 거울의 반사광을 중심으로 한 밝고 차가운 거울숲 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S038 — 첫 번째 별조각

**파일**: `05_image/S038.png`  
**구도 핵심**: 손바닥 위 별조각, 빛나는 숲의 거울들.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, luminous close-up fantasy.

Close-up of the protagonist's open palm holding the first star shard. The shard looks like a wet piece of glass or mirror, irregular and translucent, glowing warm gold-white from within. Around the hand, the mirror forest blurs into pale aqua and pearl silver; many hanging mirrors in the background catch the same light and answer faintly.

Do not define the protagonist's gender. The hand should be natural and carefully drawn. Use bright glass highlights, soft watercolor blooms, and fine ink lines on fingers, shard edges, and raindrops.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration.

Mood: a small truth accepted, fragile relief. Palette: silver, pale aqua, wet green-gray, warm star gold. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 첫 번째 별조각 장면을 그린다. 핵심 구도는 다음과 같다: 젖은 유리 조각 같은 별조각이 주인공 손바닥 위에 내려앉고, 숲의 거울들이 희미하게 빛나는 장면. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 환한 은빛, 옅은 아쿠아, 젖은 녹회색, 유리와 거울의 반사광을 중심으로 한 밝고 차가운 거울숲 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다.
```

---

## S040 — 이름 없는 간판들

**파일**: `05_image/S040.png`  
**구도 핵심**: 이름이 긁힌 간판들이 늘어선 시장 골목.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, atmospheric fantasy market.

A narrow market alley in the land between worlds. Shop signs hang everywhere, but their names have been scratched away, leaving pale scars and blank spaces. Do not render readable words. Low star-glow pools on the ground like spilled gold. In the middle distance, blurred figures with indistinct outlines browse stalls.

The market should be dark but colorful, not flat black: muted burgundy awnings, dusty violet shadows, old gold lanterns, bottle green glass, indigo corners. The protagonist and Ian enter small in the foreground; Ian's outline is especially uneasy here.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: alluring bargains, missing identities, a beautiful trap. Watercolor and ink, no text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 이름 없는 간판들 장면을 그린다. 핵심 구도는 다음과 같다: 이름이 긁혀 나간 간판들이 늘어선 시장 골목. 별빛이 바닥에 낮게 고여 있음. 중경에 윤곽이 흐릿한 사람들이 서성거리는 모습. 어둡고 공기가 무거운 분위기. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 버건디 천막, 오래된 금빛, 먼지 낀 보라, 병유리 초록, 남색 그림자를 중심으로 한 어두우면서도 색이 살아 있는 시장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S043 — 이름 수집가 아이

**파일**: `05_image/S043.png`  
**구도 핵심**: 이름 수집가 아이가 이안에게 별빛 조각을 보여주는 장면.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, intimate fantasy market scene.

In a dim but colorful market corner, a small cautious name-collector child holds out a tiny shard of star-light toward Ian. The child should feel wary and lonely, not cute. Ian is shown from the side or back, his hand near the rusty key, his posture guarded. The protagonist watches nearby.

Around them are shelves of small bottles and folded papers, all without readable labels. Palette: muted burgundy, old gold, dusty violet, bottle green glass, indigo shadow. The star shard gives a warm gold-white light on their hands.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: fragile trust inside a place of transactions. Watercolor blooms, expressive ink lines, no text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 이름 수집가 아이 장면을 그린다. 핵심 구도는 다음과 같다: 이름 수집가 아이가 이안에게 별빛 조각을 보여주는 장면. 이안의 측면 또는 뒷모습. 아이는 작고 조심스럽다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 버건디 천막, 오래된 금빛, 먼지 낀 보라, 병유리 초록, 남색 그림자를 중심으로 한 어두우면서도 색이 살아 있는 시장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S044 — 별조각 거래 연쇄 추적

**파일**: `05_image/S044.png`  
**구도 핵심**: 낡은 거래 기록판 앞의 주인공, 복잡한 기록 게시판.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, fantasy investigation scene.

A large worn transaction board fills the market wall, crowded with strings, tags, bottle shapes, torn slips, and scratched-out marks. It should look complex and trackable, but contain no readable letters or numbers. The protagonist stands close, following connections with one hand. Ian stands beside them, tense, his face half-lit by old gold market light.

Use a richer market palette: dusty violet shadows, muted burgundy cloth, old gold lamps, bottle green glass, faded parchment. Fine ink lines make the board feel detailed; watercolor keeps the background soft.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: piecing together a hidden chain, suspicion becoming understanding. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 별조각 거래 연쇄 추적 장면을 그린다. 핵심 구도는 다음과 같다: 낡은 거래 기록판 앞에 선 주인공. 복잡한 기록들이 담긴 게시판. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 버건디 천막, 오래된 금빛, 먼지 낀 보라, 병유리 초록, 남색 그림자를 중심으로 한 어두우면서도 색이 살아 있는 시장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S051 — 팔면 안 되는 것

**파일**: `05_image/S051.png`  
**구도 핵심**: 말없는 여자의 가판대, 이안이 쪽지에 손 뻗는 순간.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, emotional fantasy market climax.

At a quiet stall in the hidden-name market, a silent woman stands behind a simple counter. On the counter lies a small note or slip, blank to the viewer, glowing faintly with low gold light. Ian reaches toward it with hesitation, his rusty key visible in the other hand. Beside him, the protagonist is just about to speak, body leaning forward.

The market around them is dim but not black: muted burgundy, dusty violet, bottle green, old gold lantern light, indigo shadows. The woman's face may be calm and indistinct; she must not look like a villain. The emotional focus is Ian's reaching hand and the protagonist's almost-spoken intervention.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: the danger of selling what should not be sold. Watercolor and ink, no readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 팔면 안 되는 것 장면을 그린다. 핵심 구도는 다음과 같다: 말없는 여자의 가판대 앞, 이안이 쪽지 쪽으로 손을 뻗으려는 순간. 주인공이 이안의 옆에서 입을 열려는 찰나. 빛이 낮게 깔린 어두운 분위기. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 버건디 천막, 오래된 금빛, 먼지 낀 보라, 병유리 초록, 남색 그림자를 중심으로 한 어두우면서도 색이 살아 있는 시장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 표지판, 시간표, 종이, 간판에는 읽을 수 있는 글자를 넣지 않는다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S055 — 이안이 남는다

**파일**: `05_image/S055.png`  
**구도 핵심**: 밤끝탑 입구, 주인공과 이안 사이에 다르게 닿는 빛.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, moonlit tower fantasy.

Before the entrance of the Night-End Tower, the protagonist and Ian stand facing a high stone doorway. Cold white light from the tower falls clearly on the protagonist, sharpening their silhouette. The same light touches Ian but fails to hold him; his edges blur and dissolve softly, especially at shoulders and hands. Ian grips the rusty key.

The tower is tall, pale stone-gray and violet-black, with thin ink cracks and upward perspective. The scene is cold but not muddy: moonlit gray, desaturated blue, violet shadow, white threshold light.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: separation before ascent, unspoken worry. Watercolor and ink, quiet and solemn, no text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 이안이 남는다 장면을 그린다. 핵심 구도는 다음과 같다: 탑 입구 앞에 선 두 사람. 빛이 주인공의 윤곽을 또렷하게 밝히고 있고, 이안은 같은 빛 속에서 가장자리가 흐릿하게 번지고 있다. 이안의 손에 열쇠. 두 사람 사이의 빛의 차이가 핵심. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 달빛 석회색, 보랏빛 검정, 채도 낮은 파랑, 차가운 흰 바닥빛을 중심으로 한 밤끝탑 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S057 — 세 개의 목소리

**파일**: `05_image/S057.png`  
**구도 핵심**: 아무것도 쓰여 있지 않은 세 개의 문 앞의 주인공.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, symbolic tower interior.

Inside the Night-End Tower, three blank doors stand side by side in a cold stone chamber. The doors are the same height and size but subtly different in material: one pale and smooth, one heavy and dark, one cracked and weathered. No signs, no words, no symbols. The protagonist stands alone with their back to the viewer, centered before the three doors.

A faint cold light rises from the floor, illuminating stone dust and the lower edges of the doors. Palette: moonlit stone gray, violet-black, desaturated blue, cold white floor glow. Use ink linework for cracks and door edges, watercolor for mist and light.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration.

Mood: inner voices becoming architecture, lonely choice. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 세 개의 목소리 장면을 그린다. 핵심 구도는 다음과 같다: 아무것도 쓰여 있지 않은 세 개의 문. 앞에 홀로 서 있는 주인공의 뒷모습. 문들이 전부 같은 크기, 같은 높이지만 재질이 미묘하게 다르다. 바닥에서 희미한 빛이 올라오고 있다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 달빛 석회색, 보랏빛 검정, 채도 낮은 파랑, 차가운 흰 바닥빛을 중심으로 한 밤끝탑 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다.
```

---

## S057A — 또 다른 나, 부정의 방

**파일**: `05_image/S057A.png`  
**구도 핵심**: 표정 없는 또 다른 나와 마주 선 주인공.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, psychological fantasy scene.

A bare tower room washed in cold blue-white light. The protagonist faces another version of themselves across a shallow reflective floor. Both figures remain gender-ambiguous. One has a living, tense gaze and imperfect posture; the other has the same outline but a blank, expressionless face, eyes dim as if erased.

The room is simple: stone-gray walls, violet shadows, a faint circular pool of light between them. Avoid horror; make it emotionally unsettling rather than monstrous. Use ink lines sparingly on the two silhouettes and watercolor blooms in the empty space.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration.

Mood: denial made visible, confronting the self that gave up feeling. Palette: moonlit gray, desaturated blue, cold white, violet shadow. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 또 다른 나, 부정의 방 장면을 그린다. 핵심 구도는 다음과 같다: 표정 없는 또 다른 나. 서로를 마주보고 있는 두 사람. 같은 얼굴인데 한 쪽은 눈빛이 살아 있고 다른 한 쪽은 꺼져 있다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 달빛 석회색, 보랏빛 검정, 채도 낮은 파랑, 차가운 흰 바닥빛을 중심으로 한 밤끝탑 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다.
```

---

## S059 — 세 번째 별조각

**파일**: `05_image/S059.png`  
**구도 핵심**: 손바닥 위 세 개의 서로 다른 별조각.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, symbolic close-up.

Close-up of the protagonist's open palms holding three star shards. Each shard has a different texture: one like wet mirror-glass, one like warm market amber or old gold, one like pale tower crystal. They are separate shapes, but their lights pulse together as if forming one heartbeat. The hands are natural, ambiguous, and carefully drawn.

Background is the Night-End Tower interior fading into soft violet-blue darkness, with a cold white floor glow. The shards provide warm gold-white highlights on the fingers.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration.

Mood: fear acknowledged, choices gathered, quiet power. Watercolor and ink, luminous but restrained. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 세 번째 별조각 장면을 그린다. 핵심 구도는 다음과 같다: 손바닥 위에 세 개의 별조각. 각자 다른 형태와 질감을 가지고 있지만 함께 있으면 하나처럼 박동하는 느낌이 있어야 한다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 달빛 석회색, 보랏빛 검정, 채도 낮은 파랑, 차가운 흰 바닥빛을 중심으로 한 밤끝탑 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다.
```

---

## S064 — 다시 나타난 현실의 문

**파일**: `05_image/S064.png`  
**구도 핵심**: 허공에 열린 문, 도장을 든 문지기, 주인공의 별조각, 굳은 이안.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, bureaucratic threshold fantasy.

A rectangular opening has been cut out of the air, like a door to reality. From the gap leans a fussy gatekeeper holding an old stamp, half official and half magical. The gatekeeper should feel sharp and inconvenient, not comic. The protagonist stands before the opening with three star shards glowing in their hands. Behind them, Ian is silent and stiff, his rusty key hidden or low at his side.

Palette shifts warmer than the tower: threshold cream light, parchment beige, brass stamp, teal-blue shadows, a little violet around the torn air. Use ink linework for the stamp, papers, and doorframe edge; watercolor for the glowing cut in space.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: almost home, but blocked by a rule. No readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 다시 나타난 현실의 문 장면을 그린다. 핵심 구도는 다음과 같다: 허공이 네모나게 도려내지듯 열리고, 그 틈에서 낡은 도장을 든 까칠한 문지기가 고개를 내미는 장면. 주인공의 손에는 세 별조각이 빛나고, 뒤쪽에는 말없이 굳어 있는 이안. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 따뜻한 문턱의 크림빛, 양피지색, 황동 도장, 청록 그림자를 중심으로 한 귀환문 심사 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S065 — 문지기의 심사

**파일**: `05_image/S065.png`  
**구도 핵심**: 문지기가 이안을 심사하고, 이안 발밑의 불꽃이 꺼지는 장면.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, fantasy inspection scene.

At the open return gate, the gatekeeper peers sharply at Ian as if checking a rule only they can see. Warm cream doorlight reaches the protagonist clearly, but when it touches Ian it thins and slides away. At Ian's feet, a small flame or light mark is going out, leaving a faint smoke-like shadow. Ian's outline becomes softer and less certain.

The protagonist stands between concern and confusion. Palette: warm threshold cream, parchment beige, tarnished brass, teal shadow, muted indigo around Ian. Use expressive ink for the gatekeeper's stamp and frown, soft watercolor for failing light.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: a door that opens for one but not the other. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 문지기의 심사 장면을 그린다. 핵심 구도는 다음과 같다: 문지기가 이안을 심사하듯 바라보고, 이안의 발밑에서 불꽃이 꺼지는 장면. 문빛은 주인공에게는 닿지만 이안에게는 스며들어 윤곽을 흐리게 한다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 따뜻한 문턱의 크림빛, 양피지색, 황동 도장, 청록 그림자를 중심으로 한 귀환문 심사 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S066 — 말하지 않은 열쇠

**파일**: `05_image/S066.png`  
**구도 핵심**: 세 별조각과 녹슨 열쇠가 반응하는 순간.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, emotional object-focused fantasy.

The protagonist's three star shards glow in one hand while Ian's rusty key reacts in his half-hidden hand. Thin threads of warm gold-white light stretch between shards and key. Ian is trying to hide the key or pull it back, shoulders tense. The gatekeeper stands nearby with a brass stamp, irritated and alert.

The setting is the return gate threshold: warm cream light, parchment beige, teal-blue shadow, brass details, violet edge of the torn doorway. Focus on the contrast between the living star-shard light and the corroded key.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: a secret object answering before its owner speaks. Watercolor and ink, no readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 말하지 않은 열쇠 장면을 그린다. 핵심 구도는 다음과 같다: 주인공의 세 별조각과 이안의 녹슨 열쇠가 서로 반응하는 장면. 이안은 손을 숨기려 하고, 문지기는 귀찮고 날카로운 표정으로 도장을 든다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 따뜻한 문턱의 크림빛, 양피지색, 황동 도장, 청록 그림자를 중심으로 한 귀환문 심사 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S067 — 이번에도 말하지 않은 아이

**파일**: `05_image/S067.png`  
**구도 핵심**: 귀환문 표면에 비치는 어린 이안과 얼굴 없는 옛 동행자.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, memory reflected on a gate.

The surface of the return gate becomes like a sheet of water. In that watery reflection appears a memory: young Ian, smaller and more transparent, hiding a key behind his back; beside him or ahead of him is a faceless old companion silhouette. The present Ian and protagonist stand outside the reflection, watching.

Use warm threshold cream around the gate but cool teal and pale blue inside the water-memory. The reflected figures should be soft, blurred, and emotionally clear without detailed faces. Fine ink ripples cross the gate surface.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: the past showing itself because it was never spoken. Not horror, not villainous. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 이번에도 말하지 않은 아이 장면을 그린다. 핵심 구도는 다음과 같다: 귀환문 표면에 어린 이안과 얼굴 없는 옛 동행자의 장면이 물막처럼 비치는 순간. 어린 이안은 열쇠를 등 뒤로 숨기고 있다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 따뜻한 문턱의 크림빛, 양피지색, 황동 도장, 청록 그림자를 중심으로 한 귀환문 심사 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S068 — 열린 방과 남겨진 문턱

**파일**: `05_image/S068.png`  
**구도 핵심**: 열린 귀환문 너머 방의 빛, 반대편 사잇별 깊은 곳의 가는 빛줄기.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, threshold choice scene.

An open return door shows the protagonist's real room beyond, filled with warm ordinary light. On the other side of the composition, a thin line of pale star-light leads deeper into the land between worlds. The protagonist stands on the threshold, caught between the warm room and the cool twilight path. Ian waits silently nearby, his key visible, not forcing the choice.

Palette: warm cream and soft room amber on one side; teal, indigo, and pale low-star light on the other. Use watercolor to blend the two atmospheres without making them muddy; ink lines for the doorway and silhouettes.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: home is open, but someone is still left behind. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 열린 방과 남겨진 문턱 장면을 그린다. 핵심 구도는 다음과 같다: 열린 귀환문 너머로 따뜻한 방의 빛이 보이고, 반대편 흐릿한 사잇별의 땅 깊은 곳으로 가는 가는 빛줄기가 나타나는 장면. 주인공은 문턱 앞에 서 있고, 이안은 말없이 기다린다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 따뜻한 문턱의 크림빛, 양피지색, 황동 도장, 청록 그림자를 중심으로 한 귀환문 심사 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S069 — 혼자 돌아온 방

**파일**: `05_image/S069.png`  
**구도 핵심**: 현실 방으로 돌아온 주인공이 문이 사라진 벽을 만지는 장면.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, quiet real-world aftermath.

The protagonist is back in the ordinary bedroom, touching the wall where the impossible door used to be. The room is now warmer and more realistic than the opening scenes, but still painted in watercolor and ink. The wall is plain, yet near the touched spot remains a faint low-star afterglow, almost invisible.

Use warm lamplight, soft beige, muted blue shadows, and a tiny pale gold residue. The protagonist's face remains unseen or ambiguous. The composition should feel empty because Ian is absent.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: relief mixed with the hollow shape of someone left behind. Gentle, not melodramatic. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 혼자 돌아온 방 장면을 그린다. 핵심 구도는 다음과 같다: 현실의 방으로 돌아온 주인공이 문이 사라진 벽을 만지는 장면. 방은 평범하고 조용하며, 벽 근처에 아주 희미한 낮은 별빛의 잔상만 남아 있다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 색감은 따뜻한 현실 조명, 부드러운 베이지, 나무색, muted blue shadow, 벽 가장자리의 아주 약한 금백색 별빛 잔상으로 잡는다. 귀환문 심사 장면처럼 보이지 않게 하고, 혼자 돌아온 뒤의 조용한 여운과 현실의 무게가 중심이 되게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S071 — 어스름의 심장

**파일**: `05_image/S071.png`  
**구도 핵심**: 얼어붙은 어스름의 심장 전경, 얼음 속 별빛과 기억조각.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, luminous crystal fantasy.

A wide view of the frozen Heart of Twilight. It is not a dark cave; it is a bright, translucent ice field filled with pale blue, pearl white, crystal cyan, and lavender light. Inside the ice are small trapped star-lights and gem-like memory fragments, glowing softly like things preserved under glass.

The protagonist and Ian stand small on the ice, surrounded by enormous reflective surfaces. Ian holds the rusty key, which trembles with a faint warm glimmer. Use delicate ink cracks, glassy watercolor gradients, and bright reflected light. Shadows should be blue and violet, never muddy black.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: awe, cold pressure, the beauty of a frozen wound. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 어스름의 심장 장면을 그린다. 핵심 구도는 다음과 같다: 얼어붙은 어스름의 심장 전경. 짙은 남색과 보랏빛의 얼음 벌판, 얼음 속에 갇힌 작은 별빛과 보석 같은 기억조각들. 주인공과 이안은 작게 서 있고, 이안의 손에는 녹슨 열쇠가 희미하게 떨린다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S072 — 기억 조각 ①. 같이 걷던 시절

**파일**: `05_image/S072.png`  
**구도 핵심**: 두 인물이 나란히 걷는 얼어붙은 기억.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, luminous frozen memory scene.

Inside a transparent ice or gemstone fragment, two figures walk side by side in a dim twilight path. The companion is a faceless, soft silhouette, looking forward and speaking or gesturing without noticing Ian. Young Ian walks half a step behind or beside them, lips slightly parted as if about to speak, but stopped. His key is not yet fully rusted.

The whole scene is suspended in bright ice-blue and pearl-white refractions, with pale lavender shadows and tiny warm star motes. Edges should blur like watercolor seen through glass. The companion must be indistinct and not villainous.

Character reference: If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: an ordinary small silence preserved forever. Watercolor and ink, no readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 기억 조각 ①. 같이 걷던 시절 장면을 그린다. 핵심 구도는 다음과 같다: 두 인물이 나란히 걷는 얼어붙은 기억. 동행자는 얼굴 없는 실루엣으로 앞을 보며 말하고, 어린 이안은 반걸음 뒤에서 입을 열려다 멈춘다. 열쇠는 아직 녹슬지 않았고, 장면 전체는 투명한 얼음/보석 안에 갇혀 있는 느낌. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S073 — 기억 조각 ②. 숨은이름 시장에서 물러난 발

**파일**: `05_image/S073.png`  
**구도 핵심**: 시장 기억, 유리병, 동행자의 분노 앞에서 물러나는 어린 이안.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, frozen memory inside crystal.

A memory of the hidden-name market trapped inside translucent ice. A merchant extends a small glass bottle toward the faceless companion, who is turning away angrily or defensively, trying to sell an unwanted feeling. Young Ian stands nearby with a not-yet-fully-rusted key in one hand, his other hand half-raised as if to stop them, but one foot has already stepped back.

The market colors are visible through the ice: muted burgundy cloth, bottle green glass, old gold lanterns, dusty violet shadows, all cooled by crystal blue and pearl-white refraction. Ian's whole body should show the tension of stopping himself.

Character reference: If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: wanting to speak, retreating before anger. No readable labels or text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 기억 조각 ②. 숨은이름 시장에서 물러난 발 장면을 그린다. 핵심 구도는 다음과 같다: 숨은이름 시장의 기억 조각. 상인은 유리병을 내밀고, 얼굴 흐릿한 동행자는 잊고 싶은 감정을 팔려 한다. 어린 이안은 한 손에 아직 덜 녹슨 열쇠를 쥔 채 막으려 하지만, 동행자의 분노 앞에서 한 걸음 물러나는 순간이다. 말풍선이나 실제 대사는 넣지 말고, 막으려다 멈춘 몸짓과 물러나는 발로 표현한다. 시장은 오래된 천막, 유리병, 낮은 금빛과 남색 그림자로 구성. 이안의 몸 전체에 멈춤의 긴장이 보여야 한다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S074 — 기억 조각 ③. 현실로 돌아간 동행자

**파일**: `05_image/S074.png`  
**구도 핵심**: 현실 문 앞, 떠나는 동행자, 말하지 못하는 어린 이안.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, brightest and most painful frozen memory.

A return door glows with warm white human light inside a translucent ice fragment. The faceless companion has one foot inside the doorway, body already leaning toward home, not cruel but already leaving. Young Ian stands outside the threshold holding a key that has begun to rust. His lips are parted, his posture says he wants to speak, but no words come out.

Keep the memory luminous: pearl white doorlight, crystal cyan ice, pale lavender shadows, warm cream spilling from the doorway. Around Ian, faint scratch-like marks in the ice may suggest unsaid sentences, but do not render readable words.

Character reference: If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: the last chance passing in silence. Watercolor and ink, no readable text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 기억 조각 ③. 현실로 돌아간 동행자 장면을 그린다. 핵심 구도는 다음과 같다: 현실로 돌아가는 문 앞의 얼어붙은 기억. 문 안쪽에서는 따뜻한 현실의 흰빛이 새어 나오고, 얼굴이 흐릿한 동행자는 한 발을 문 안에 들여놓은 채 뒤돌아 말하려는 자세다. 어린 이안은 문턱 바깥에 서서 녹슬기 시작한 열쇠를 쥐고 있고, 입술은 열렸지만 말은 나오지 않는다. 얼음 표면에는 말하지 못한 문장들이 실제 글자가 아니라 흠집 같은 흔적으로 희미하게 떠 있다. 동행자는 악역처럼 보이지 않되, 이미 자기 빛 쪽으로 기울어진 몸짓이어야 한다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 얼음 표면의 흔적들은 읽을 수 있는 글자가 아니라 흠집 같은 흔적으로만 표현한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S075 — 찢어진 안내문

**파일**: `05_image/S075.png`  
**구도 핵심**: 얼음 위의 찢어진 안내문 조각, 이안이 알아보는 문장.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, delicate object-focused fantasy.

On the bright ice of the Heart of Twilight floats a torn, weathered notice fragment. It is not a neat ticket, not a form, not a name tag. Its edges are worn away, and most of the surface is missing. The protagonist's hand hesitates near it. Ian stands close, gripping the rusty key, recognizing the fragment with a still, shaken posture.

The paper is warm off-white against luminous crystal blue and pearl ice. Add faint marks where a phrase once was, but avoid generated readable text; if the exact Korean phrase is needed, leave a clean space for manual lettering later. No labels, no fields, no form boxes.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: a borrowed name traced back to a torn remnant. Watercolor and ink, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 찢어진 안내문 장면을 그린다. 핵심 구도는 다음과 같다: 얼음 위에 떠오른 낡고 찢어진 안내문 조각. 온전한 티켓이나 양식 문서가 아니라 가장자리가 닳고 일부가 사라진 종이에 `...이 안에 있어...`만 겨우 남아 있다. 주인공은 손을 뻗을 듯 말 듯 멈춰 있고, 이안은 녹슨 열쇠를 쥔 채 그 문장을 알아본다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 종이에 실제 글자를 자동 생성하지 말고, 필요한 문구는 나중에 수동으로 넣을 수 있도록 비워 둔다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S076 — 이안이 말하다

**파일**: `05_image/S076.png`  
**구도 핵심**: 이안이 자기 안쪽으로 이름을 말하고, 열쇠의 녹이 떨어지는 순간.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, luminous emotional climax.

Ian holds the torn notice fragment close to his chest and speaks his true name inwardly. Do not show the name as letters. His outline becomes clear for the first time: shoulders, hands, face, and hair no longer dissolving. The rusty key in his hand sheds rust like dark red-brown dust, revealing a warmer metal beneath.

Around him, the ice of the Heart of Twilight glows from below with pearl white, crystal cyan, pale lavender, and many small low-star lights. The protagonist stands nearby, witnessing quietly rather than interrupting.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: a voice finally becoming real. Bright ice, warm human light, watercolor blooms, fine ink details on Ian and the key. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 이안이 말하다 장면을 그린다. 핵심 구도는 다음과 같다: 이안이 찢어진 안내문을 가슴 가까이에 들고 자기 안쪽으로 이름을 말하는 순간. 독자에게 이름 글자는 보이지 않는다. 녹슨 열쇠의 녹이 가루처럼 떨어지고, 이안의 윤곽이 처음으로 선명해진다. 주변 얼음 아래의 이름들은 낮은 별빛처럼 조용히 빛난다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S078 — 별빛 균열

**파일**: `05_image/S078.png`  
**구도 핵심**: 균열 앞의 주인공과 이안, 회복된 열쇠가 문을 여는 순간.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, radiant threshold fantasy.

A crack of starlight opens in the air before the protagonist and Ian. Ian, now fully clear, uses the restored key to open the way. The protagonist stands beside him, not behind him. From the crack pours a mixture of warm real-world light and low star-light from the land between worlds.

The surroundings are bright ice and crystal: pearl white, translucent blue, pale lavender, with warm gold-white light threading through the fracture. Use ink lines for the crack and key, watercolor for the glowing transition.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: not escape alone, but a door opened together. Luminous, hopeful, still mysterious. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 별빛 균열 장면을 그린다. 핵심 구도는 다음과 같다: 균열 앞에서 주인공과 이안이 나란히 서 있고, 이안의 회복된 열쇠가 문을 여는 순간. 현실의 따뜻한 빛과 사잇별의 낮은 별빛이 함께 섞여 있어야 한다. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S079 — 이름을 되찾은 소년

**파일**: `05_image/S079.png`  
**구도 핵심**: 현실 방에 돌아온 두 사람, 이안이 선명하게 존재함.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, warm quiet ending scene.

The protagonist and Ian have returned to the real bedroom. Ian is now fully solid and clear, no blurred shoulders, no fading edges, and the rusty key is gone from his hand. He stands in ordinary warm room light, looking quietly present. The protagonist is nearby, still ambiguous and mostly from behind or side.

The window shows a normal real-world night or early dawn, not a fantasy sky. The room palette is warmer than the earlier night-room scenes: soft cream, muted blue shadows, gentle brown wood, with only a faint memory of star-light. Keep watercolor and ink texture consistent with the earlier room illustrations.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: someone impossible is now really here. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 이름을 되찾은 소년 장면을 그린다. 핵심 구도는 다음과 같다: 현실의 방 안에 돌아온 두 사람. 이안은 완전히 선명하게 존재하고, 손에는 더 이상 열쇠가 없다. 창밖은 평범한 현실 풍경이며, 방 안의 따뜻한 빛과 두 사람 사이의 조용한 여운이 중심. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S080 — 별빛이 남은 세계 ★ 진엔딩

**파일**: `05_image/S080.png`  
**구도 핵심**: 창가에 나란히 선 주인공과 이안, 아주 작은 낮은 별빛.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, final true ending atmosphere.

The protagonist and Ian stand side by side at the bedroom window. They are not dramatically embracing; they simply share the same quiet space. On one small corner of the window glass remains a tiny low-star glimmer, almost hidden, showing that the land between worlds has not vanished completely.

The room is filled with warm real-world light, soft cream and pale gold, balanced by gentle blue shadows. Ian is fully clear and calm. The protagonist remains visually open enough for the reader to inhabit. Use fine ink lines on the window and soft watercolor washes across the room.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: the world is ordinary again, but now it has room for wonder. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 별빛이 남은 세계 ★ 진엔딩 장면을 그린다. 핵심 구도는 다음과 같다: 창가에 선 주인공과 이안. 창문 유리 한쪽에 아주 작고 희미한 낮은 별빛이 남아 있고, 방 안은 현실의 따뜻한 빛으로 채워져 있다. 두 사람은 손을 잡기보다 나란히 서 있으며, 사잇별의 땅이 사라지지 않고 조용히 남아 있다는 느낌이 중심. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## S081 — 어스름에 남은 나 ✦ 비밀 엔딩

**파일**: `05_image/S081.png`  
**구도 핵심**: 닫히는 현실 문, 빛으로 가는 이안, 어스름에 남는 주인공.

### 메인 프롬프트

```
Watercolor and ink illustration, square format, bittersweet secret ending.

A warm reality door is closing. Ian, now fully clear, steps into the warm light beyond the door. On this side, the protagonist remains in the deep twilight world, standing on a pale ice path under low stars. The protagonist looks toward a small star-light ahead, not collapsed in despair.

Balance the composition between two lights: warm cream and human gold through the door, and cool crystal blue, lavender, and low-star white in the twilight world. The scene should feel like a quiet chosen beginning, not a tragic punishment.

Character reference: If the protagonist appears, use the attached protagonist character sheet as the reference for his late-teen male hairstyle, lean build, and clothing; keep his face and expression subdued, turned away, blurred, or silhouetted in the actual illustration. If Ian appears, use the attached Ian character sheet as the reference for Ian's hairstyle, slim build, clothing, and rusty key.

Mood: farewell, courage, a new path in the in-between world. Watercolor and ink, luminous rather than gloomy. No text, no watermark.
```

### 한글 프롬프트

```
정방형 수채화와 잉크 삽화. 어스름에 남은 나 ✦ 비밀 엔딩 장면을 그린다. 핵심 구도는 다음과 같다: 닫히는 현실의 문 앞에서 이안이 완전히 선명한 실루엣으로 빛 속에 들어가고, 주인공은 어스름의 깊은 남색 세계 쪽에 남아 작은 별빛을 바라보는 장면. 문 너머는 따뜻한 현실의 빛, 이쪽은 낮은 별빛과 얼음길. 비극만이 아니라 조용한 선택과 새로운 시작의 느낌. 화풍은 기존 수채·잉크 기준처럼 수채 번짐, 종이 질감, 섬세한 잉크 선을 유지하되, 이 장면의 색감은 투명한 얼음 파랑, 진주빛 흰색, 크리스털 시안, 옅은 라벤더, 따뜻한 사람의 빛을 중심으로 한 밝고 투명한 어스름의 심장 분위기로 잡는다. 분위기는 과장된 공포나 귀여운 만화풍이 아니라, 조용한 판타지와 문학적인 여운이 느껴지게 한다. 사진처럼 사실적으로 만들지 말고, 3D 렌더·치비·애니 과장·워터마크·서명은 피한다.

캐릭터 레퍼런스: 주인공이 등장하면 첨부한 주인공 캐릭터시트 레퍼런스 이미지를 기준으로 10대 후반 남자의 헤어스타일, 마른 체격, 옷차림을 맞추되, 실제 삽화에서는 얼굴과 표정은 실루엣, 뒷모습, 옆모습, 흐린 그림자 중심으로 처리한다. 이안이 등장하면 첨부한 이안 캐릭터시트 레퍼런스 이미지를 기준으로 헤어스타일, 가는 체격, 옷차림, 녹슨 열쇠를 맞춘다.
```

---

## 이안 캐릭터 시트

**파일**: `05_image/Character_sheet_ian.png`  
**용도**: 전체 삽화 제작 시 이안의 외형·표정 일관성 기준.

### 메인 프롬프트

```
Character reference sheet for Ian, watercolor and ink illustration, clean grid layout.

Ian appears adolescent, slender, slightly androgynous, but carries an ancient weathered feeling. Dark tousled hair reaching around the ears or jawline, faint pale gold-indigo glow at the tips. Dark eyes with tiny unstable star-like points deep inside. Simple old-fashioned layered clothing in navy, gray, and muted blue. His shoulders and sleeves can blur subtly at the edges in some views. He often grips a rust-covered old key.

Show face close-ups, full-body views, expression variations, and a close-up of the rusty key. Keep the background pale parchment for reference clarity. Style should match the established Ian reference: expressive ink hair lines, watercolor shadows, delicate melancholy, not cute, not anime-chibi, not photorealistic. No text labels, no watermark.
```
