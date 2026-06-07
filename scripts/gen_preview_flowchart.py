#!/usr/bin/env python3
"""Generate the new section③ flowchart HTML for naming-rules-preview.html"""
import sys, json, html
sys.stdout.reconfigure(encoding='utf-8')

# Section data: (id, kind, tier, short_title, changed, old_id)
SECTIONS = [
  ('S001','story','','평범한 밤의 방',False,None),
  ('S002','story','','멈춘 시계와 이상한 창밖',False,None),
  ('S003','story','','휴대폰 화면에 뜬 문장',False,None),
  ('S004','story','','방 안에 없던 문',False,None),
  ('S005','story','','문틈에서 나타난 이안',False,None),
  ('S006','story','','그림자가 방 안으로',False,None),
  ('S007','decision','major','첫 선택',False,None),
  ('S008A','story','','이안에게 사실을 묻는다',False,None),
  ('S008B','story','','문밖을 직접 살핀다',False,None),
  ('S008C','story','','작은 글씨를 다시 본다',False,None),
  ('S008D','story','','방이 접히기 시작한다',False,None),
  ('S010','story','','낮은 별 아래로 떨어지다',False,None),
  ('S011','story','','사라진 문',False,None),
  ('S012','story','','이안의 설명은 부족하다',False,None),
  ('S013','story','','사잇별의 땅 첫 규칙',False,None),
  ('S014','story','','낮은 별이 가리키는 길',False,None),
  ('S015','story','','세 갈래 표지판',False,None),
  ('S016','decision','major','첫 퍼즐',False,None),
  ('S017','story','','작은 문장을 다시 읽는다',False,None),
  ('S018A','story','','왼쪽 길의 결과',False,None),
  ('S018B','story','','오른쪽 길의 결과',False,None),
  ('S018C','story','','표지판 뒤쪽 좁은 길',False,None),
  ('S018D','story','','이안에게 맡긴 결과',False,None),
  ('S019','story','','초저녁 정거장의 불빛',False,None),
  ('S020','decision','major','말하는 시간표',False,None),
  ('S021','decision','major','이안의 짧은 경고',False,None),
  ('S022','decision','major','너무 안전하다는 말',False,None),
  ('S023','decision','major','누구에게 도움을',False,None),
  ('S024','decision','major','역무원을 따른다',False,None),
  ('S025','decision','minor','매표소 작은 목소리',False,None),
  ('S025B','story','','이안에게 글씨 이유를 묻는다',False,None),
  ('S026','decision','minor','시간표를 직접 살핀다',False,None),
  ('S027A','story','','역무원 함정에서 빠져나오다',False,None),
  ('S027B','story','','이름을 말한 뒤',False,None),
  ('S028','decision','major','시간표 해독',False,None),
  ('S028A','story','','안전 승강장으로 간다',False,None),
  ('S028B','story','','분실물 보관소로 간다',False,None),
  ('S028C','story','','세 개의 별조각',False,None),
  ('S029','story','','거울숲으로 가는 표',False,None),
  ('S030','story','','표지판 수선공',False,None),
  ('S031','story','','거울이 매달린 숲',False,None),
  ('S032','story','','나를 따라오는 다른 나',False,None),
  ('S033','story','','마음을 비추는 거울',False,None),
  ('S034','decision','major','세 개의 거울',False,None),
  ('S035A','story','','웃는 거울을 따라간다',False,None),
  ('S035B','story','','아무것도 비추지 않는 거울',False,None),
  ('S035C','story','','보기 싫은 거울 앞에',False,None),
  ('S035D','story','','이안 뒤에 숨는다',False,None),
  ('S037','story','','이안의 그림자가 늦게 움직이다',False,None),
  ('S038','story','','첫 번째 별조각',False,None),
  ('S039','story','','거울 속 경고',False,None),
  ('S040','decision','minor','이름 없는 간판들',False,None),
  ('S040A','story','','가까운 노점부터 살핀다',False,None),
  ('S040B','story','','이안에게 이곳을 묻는다',False,None),
  ('S041','story','','기억을 파는 노점',False,None),
  ('S042','decision','major','기억 상인',False,None),
  ('S042A','story','','가격표를 요청한다',False,None),
  ('S042B','story','','거절한다',False,None),
  ('S042C','story','','어떻게 알았냐고 묻는다',False,None),
  ('S043','story','','이름 수집가 아이',False,None),
  ('S044','decision','major','거래 연쇄 추적',False,None),
  ('S044B','story','','잿빛 손 상인을 찾아서',False,None),
  ('S044C','story','','기록을 다시 살핀다',False,None),
  ('S045','decision','major','상인 셋',False,None),
  ('S046A','decision','minor','거짓말쟁이의 덫',False,None),
  ('S046B','story','','가짜 안내자의 함정',False,None),
  ('S047A','decision','minor','남은 두 명',False,None),
  ('S047B','decision','minor','여자와 상인만 남아',False,None),
  ('S048A','story','','가짜 안내자 함정 ②',False,None),
  ('S048B','decision','minor','거짓말쟁이의 덫 ②',False,None),
  ('S049','story','','이름을 빼앗기다',False,None),
  ('S050','story','','여자만 남아 있다',False,None),
  ('S051','story','','팔면 안 되는 것',False,None),
  ('S052','story','','두 번째 별조각',False,None),
  ('S053','story','','이안은 자기 이름을 모른다',False,None),
  ('S054','story','','검은 탑 앞에서',False,None),
  ('S055','story','','이안이 남는다',False,None),
  ('S056','story','','올라갈수록 내려가는 곳',False,None),
  ('S057','decision','major','세 개의 목소리',False,None),
  ('S057A','story','','부정의 방',False,None),
  ('S057B','story','','도피의 방',False,None),
  ('S058','story','','두려움의 심장',False,None),
  ('S059','story','','세 번째 별조각',False,None),
  ('S060','story','','탑을 나서다',False,None),
  ('S061','story','','녹슨 열쇠가 반응하다',False,None),
  ('S062','story','','세계의 균열',False,None),
  ('S063','story','','챕터5 마감',False,None),
  ('S064','story','','다시 나타난 현실의 문',False,None),
  ('S065','story','','문지기의 심사',False,None),
  ('S066','story','','말하지 않은 열쇠',False,None),
  ('S067','story','','이번에도 말하지 않은 아이',False,None),
  ('S068','decision','minor','열린 방과 남겨진 문턱',False,None),
  ('S069','story','','혼자 돌아온 방',True,'E001'),
  ('S070','story','','어스름의 심장으로',False,None),
  ('S071','decision','major','어스름의 심장',False,None),
  ('S071A','story','','피하지 않겠다는 약속',False,None),
  ('S071B','story','','얼음 속의 말 조각',False,None),
  ('S071C','story','','녹이 향하는 곳',False,None),
  ('S072','decision','major','기억①',True,'S071D'),
  ('S072A','story','','첫 번째 조각이 녹다',True,'S071E'),
  ('S072B','story','','너무 쉬운 원망',True,'S071F'),
  ('S072C','story','','잘못 읽은 외로움',True,'S071G'),
  ('S073','decision','major','기억②',True,'S071H'),
  ('S073A','story','','두 번째 조각이 떨리다',True,'S071I'),
  ('S073B','story','','차가운 질문',True,'S071J'),
  ('S073C','story','','잃어버린 글자',True,'S071K'),
  ('S074','decision','major','기억③',True,'S071L'),
  ('S074A','story','','세 번째 조각이 열린다',True,'S071M'),
  ('S074B','story','','보지 않게 해주고 싶은 마음',True,'S071N'),
  ('S074C','story','','곁에 서서 보게 하기',True,'S071O'),
  ('S075','decision','minor','찢어진 안내문',True,'S072'),
  ('S076A','story','','찢어진 문장을 건네다',True,'S073A'),
  ('S076','story','','이안이 말하다',True,'S073'),
  ('S077','decision','major','마지막 선택',True,'S074'),
  ('S079','story','','이름을 되찾은 소년',True,'E002'),
  ('S081','ending','','비밀 엔딩',True,'E004'),
  ('S078','story','','별빛 균열',True,'S075'),
  ('S080','ending','','진엔딩',True,'E003'),
]

# Edge data with new IDs
EDGES = [
  ('S001','S002',''),('S002','S003',''),('S003','S004',''),('S004','S005',''),('S005','S006',''),('S006','S007',''),
  ('S007','S008A','A'),('S007','S008B','B'),('S007','S008C','C'),('S007','S008D','D'),
  ('S008A','S010',''),('S008B','S010',''),('S008C','S010',''),('S008D','S010',''),
  ('S010','S011',''),('S011','S012',''),('S012','S013',''),('S013','S014',''),('S014','S015',''),('S015','S016',''),
  ('S016','S018A','A'),('S016','S018B','B'),('S016','S018C','C'),('S016','S018D','D'),
  ('S017','S018C',''),('S018A','S017',''),('S018B','S017',''),('S018C','S019',''),('S018D','S017',''),
  ('S019','S020',''),
  ('S020','S024','A'),('S020','S021','B'),('S020','S025','C'),('S020','S026','D'),
  ('S021','S022','A'),('S021','S026','B'),('S021','S025','C'),
  ('S022','S024','A'),('S022','S023','B'),('S022','S026','C'),
  ('S023','S024','A'),('S023','S025','B'),('S023','S026','C'),
  ('S024','S027A','A'),('S024','S027B','B'),
  ('S025','S028','A'),('S025','S025B','B'),('S025B','S026',''),
  ('S026','S028','A'),('S026','S028C','B'),
  ('S027A','S026',''),('S027B','S026',''),
  ('S028','S028A','A'),('S028','S028B','B'),('S028','S028C','C'),
  ('S028A','S028C',''),('S028B','S028C',''),
  ('S028C','S029',''),('S029','S030',''),('S030','S031',''),
  ('S031','S032',''),('S032','S033',''),('S033','S034',''),
  ('S034','S035A','A'),('S034','S035B','B'),('S034','S035C','C'),('S034','S035D','D'),
  ('S035A','S034',''),('S035B','S034',''),('S035C','S037',''),('S035D','S034',''),
  ('S037','S038',''),('S038','S039',''),('S039','S040',''),
  ('S040','S040A','A'),('S040','S040B','B'),('S040A','S041',''),('S040B','S041',''),
  ('S041','S042',''),
  ('S042','S042A','A'),('S042','S042B','B'),('S042','S042C','C'),
  ('S042A','S043',''),('S042B','S043',''),('S042C','S043',''),
  ('S043','S044',''),
  ('S044','S045','A'),('S044','S044B','B'),('S044','S044C','C'),
  ('S044B','S044','A'),('S044C','S045','A'),
  ('S045','S051','A'),('S045','S046A','B'),('S045','S046B','C'),
  ('S046A','S049','A'),('S046A','S047A','B'),
  ('S046B','S047B','A'),
  ('S047A','S051','A'),('S047A','S048A','B'),
  ('S047B','S051','A'),('S047B','S048B','B'),
  ('S048A','S050','A'),
  ('S048B','S049','A'),('S048B','S050','B'),
  ('S049','S050','A'),('S050','S051','A'),
  ('S051','S052',''),('S052','S053',''),('S053','S054',''),
  ('S054','S055',''),('S055','S056',''),('S056','S057',''),
  ('S057','S057A','A'),('S057','S057B','B'),('S057','S058','C'),
  ('S057A','S058',''),('S057B','S058',''),
  ('S058','S059',''),('S059','S060',''),('S060','S061',''),('S061','S062',''),('S062','S063',''),
  ('S063','S064',''),('S064','S065',''),('S065','S066',''),('S066','S067',''),('S067','S068',''),
  # S068 branches: A→S069(new, was E001), B→S070
  ('S068','S069','A'),('S068','S070','B'),
  ('S070','S071',''),
  ('S071','S071A','A'),('S071','S071B','B'),('S071','S071C','C'),
  # S071A/B/C all go to S072 (was S071D)
  ('S071A','S072',''),('S071B','S072',''),('S071C','S072',''),
  # S072 (was S071D) branches to S072A/B/C (was S071E/F/G)
  ('S072','S072A','A'),('S072','S072B','B'),('S072','S072C','C'),
  # S072A→S073, S072B/C loop back to S072
  ('S072A','S073',''),('S072B','S072',''),('S072C','S072',''),
  # S073 (was S071H) branches to S073A/B/C (was S071I/J/K)
  ('S073','S073A','A'),('S073','S073B','B'),('S073','S073C','C'),
  # S073A→S074, S073B/C loop back to S073
  ('S073A','S074',''),('S073B','S073',''),('S073C','S073',''),
  # S074 (was S071L) branches to S074A/B/C (was S071M/N/O)
  ('S074','S074A','A'),('S074','S074B','B'),('S074','S074C','C'),
  # S074A/C→S075, S074B loops to S074
  ('S074A','S075',''),('S074B','S074',''),('S074C','S075',''),
  # S075 (was S072) branches to S076 (B) and S076A (C)
  ('S075','S076','B'),('S075','S076A','C'),
  # S076A (was S073A) → S076 (was S073)
  ('S076A','S076',''),
  # S076 (was S073) → S077 (was S074)
  ('S076','S077',''),
  # S077 (was S074) branches: A→S079(was E002), B→S078(was S075), C→S081(was E004)
  ('S077','S079','A'),('S077','S078','B'),('S077','S081','C'),
  # S078 (was S075) → S080 (was E003)
  ('S078','S080',''),
]

sec_map = {s[0]: s for s in SECTIONS}

def make_node(sec_id):
    sid, kind, tier, short_title, changed, old_id = sec_map[sec_id]
    classes = ['flow-node']
    if kind == 'story': classes.append('story')
    elif kind == 'decision': classes.append('decision'); classes.append(tier)
    elif kind == 'ending': classes.append('ending')
    if changed: classes.append('changed')
    cls = ' '.join(classes)
    label = html.escape(f'{sid}. {short_title}')
    if old_id:
        label += f' (← {html.escape(old_id)})'
    title_esc = html.escape(short_title)
    if kind == 'decision' and tier == 'major':
        inner = f'<div class="node-inner"><span class="nid">{sid}</span><span class="ntitle">{title_esc}</span></div>'
    else:
        inner = f'<span class="nid">{sid}</span><span class="ntitle">{title_esc}</span>'
    return f'<button class="{cls}" data-section="{sid}" aria-label="{label}">{inner}</button>'

def row(node_ids, row_type='single-row'):
    nodes = ' '.join(make_node(sid) for sid in node_ids)
    return f'<div class="flow-row {row_type}">{nodes}</div>'

# Build grid rows
GRID_ROWS = [
  ('band', '프롤로그 · 1장 · 사잇별의 땅'),
  ('single', ['S001']),('single', ['S002']),('single', ['S003']),('single', ['S004']),
  ('single', ['S005']),('single', ['S006']),
  ('single', ['S007']),
  ('branch', ['S008A','S008B','S008C','S008D']),
  ('single', ['S010']),
  ('single', ['S011']),('single', ['S012']),('single', ['S013']),('single', ['S014']),('single', ['S015']),
  ('single', ['S016']),
  ('single', ['S017']),
  ('branch', ['S018A','S018B','S018C','S018D']),
  ('band', '2장 · 초저녁 정거장'),
  ('single', ['S019']),
  ('single', ['S020']),('single', ['S021']),('single', ['S022']),('single', ['S023']),('single', ['S024']),
  ('single', ['S025']),('single', ['S025B']),('single', ['S026']),
  ('branch', ['S027A','S027B']),
  ('single', ['S028']),
  ('branch', ['S028A','S028B','S028C']),
  ('single', ['S029']),('single', ['S030']),
  ('band', '3장 · 거울숲'),
  ('single', ['S031']),('single', ['S032']),('single', ['S033']),
  ('single', ['S034']),
  ('branch', ['S035A','S035B','S035C','S035D']),
  ('single', ['S037']),('single', ['S038']),('single', ['S039']),
  ('band', '4장 · 숨은이름 시장'),
  ('single', ['S040']),
  ('branch', ['S040A','S040B']),
  ('single', ['S041']),
  ('single', ['S042']),
  ('branch', ['S042A','S042B','S042C']),
  ('single', ['S043']),('single', ['S044']),
  ('branch', ['S044B','S044C']),
  ('single', ['S045']),
  ('branch', ['S046A','S046B']),
  ('branch', ['S047A','S047B']),
  ('branch', ['S048A','S048B']),
  ('single', ['S049']),('single', ['S050']),
  ('single', ['S051']),('single', ['S052']),('single', ['S053']),
  ('band', '5장 · 밤끝탑'),
  ('single', ['S054']),('single', ['S055']),('single', ['S056']),
  ('single', ['S057']),
  ('branch', ['S057A','S057B']),
  ('single', ['S058']),('single', ['S059']),('single', ['S060']),
  ('single', ['S061']),('single', ['S062']),('single', ['S063']),
  ('band', '6장 · 열리지 않는 문'),
  ('single', ['S064']),('single', ['S065']),('single', ['S066']),('single', ['S067']),
  ('single', ['S068']),
  ('single', ['S069']),  # changed from E001
  ('band', '7장 · 어스름의 심장'),
  ('single', ['S070']),
  ('single', ['S071']),
  ('branch', ['S071A','S071B','S071C']),
  ('single', ['S072']),    # changed from S071D
  ('branch', ['S072A','S072B','S072C']),  # changed from S071E/F/G
  ('single', ['S073']),    # changed from S071H
  ('branch', ['S073A','S073B','S073C']),  # changed from S071I/J/K
  ('single', ['S074']),    # changed from S071L
  ('branch', ['S074A','S074B','S074C']),  # changed from S071M/N/O
  ('single', ['S075']),    # changed from S072
  ('branch', ['S076A','S076']),  # changed
  ('single', ['S077']),    # changed from S074
  ('branch', ['S079','S081']),   # changed from E002, E004
  ('single', ['S078']),    # changed from S075
  ('band', '엔딩'),
  ('single', ['S080']),    # changed from E003
]

lines = []
for item in GRID_ROWS:
    if item[0] == 'band':
        lines.append(f'<div class="chapter-band">{html.escape(item[1])}</div>')
    elif item[0] == 'single':
        lines.append(row(item[1], 'single-row'))
    elif item[0] == 'branch':
        lines.append(row(item[1], 'branch-row'))

grid_html = '\n'.join(lines)

# Build edge data JSON
edge_data = [{'from': f, 'to': t, 'label': lbl} for f, t, lbl in EDGES]

# Build section data JSON
sec_json = []
for sid, kind, tier, short_title, changed, old_id in SECTIONS:
    sec_json.append({'id': sid, 'kind': kind, 'tier': tier, 'title': f'{sid}. {short_title}', 'changed': changed, 'old': old_id})

# Generate the JS renderEdges (same as big-workshop)
JS = r"""
const flowCanvas=document.getElementById('flowCanvas');
const flowGrid=document.getElementById('flowGrid');
const edgeLayer=document.getElementById('edgeLayer');
const nodes=[...document.querySelectorAll('.flow-node[data-section]')];
const sections=JSON.parse(document.getElementById('sectionData').textContent);
const edges=JSON.parse(document.getElementById('edgeData').textContent);
function renderEdges(){
  const box=flowCanvas.getBoundingClientRect();
  edgeLayer.setAttribute('width',flowCanvas.scrollWidth);
  edgeLayer.setAttribute('height',flowCanvas.scrollHeight);
  [...edgeLayer.querySelectorAll('path.edge')].forEach(p=>p.remove());
  const sideRoutes=new Map();
  const point=(rect,node,where,side=0)=>{
    const centerX=rect.left+rect.width/2-box.left+flowCanvas.scrollLeft;
    const centerY=rect.top+rect.height/2-box.top+flowCanvas.scrollTop;
    const isDecision=node.classList.contains('decision');
    if(isDecision&&where==='side'&&side!==0){
      return {x:(side<0?rect.left:rect.right)-box.left+flowCanvas.scrollLeft,y:centerY};
    }
    return {x:centerX,y:(where==='bottom'?rect.bottom:where==='top'?rect.top:rect.top+rect.height/2)-box.top+flowCanvas.scrollTop};
  };
  for(const edge of edges){
    const a=document.querySelector(`[data-section="${edge.from}"]`);
    const b=document.querySelector(`[data-section="${edge.to}"]`);
    if(!a||!b)continue;
    const ar=a.getBoundingClientRect();
    const br=b.getBoundingClientRect();
    const downward=br.top>=ar.top;
    const ac=point(ar,a,'center');
    const bc=point(br,b,'center');
    const ax=ac.x,bx=bc.x;
    const sameColumn=Math.abs(ax-bx)<10;
    const longJump=Math.abs(bc.y-ac.y)>85;
    const path=document.createElementNS('http://www.w3.org/2000/svg','path');
    path.setAttribute('class','edge');
    path.dataset.from=edge.from;path.dataset.to=edge.to;
    const edgeTitle=document.createElementNS('http://www.w3.org/2000/svg','title');
    edgeTitle.textContent=edge.label?`${edge.from} → ${edge.to} · ${edge.label}`:`${edge.from} → ${edge.to}`;
    path.appendChild(edgeTitle);
    if(sameColumn&&longJump){
      const routeKey=`${Math.round(ax)}:${downward?'down':'up'}`;
      const count=sideRoutes.get(routeKey)||0;
      sideRoutes.set(routeKey,count+1);
      const dir=count%2===0?-1:1;
      const offset=dir*(46+Math.floor(count/2)*24);
      const start=point(ar,a,a.classList.contains('decision')?'side':downward?'bottom':'top',dir);
      const end=point(br,b,b.classList.contains('decision')?'side':downward?'top':'bottom',dir);
      path.setAttribute('d',`M ${start.x} ${start.y} C ${start.x+offset} ${start.y+18*(downward?1:-1)}, ${end.x+offset} ${end.y-18*(downward?1:-1)}, ${end.x} ${end.y}`);
    }else{
      const start=point(ar,a,downward?'bottom':'top');
      const end=point(br,b,downward?'top':'bottom');
      const midY=start.y+(end.y-start.y)*0.55;
      path.setAttribute('d',`M ${start.x} ${start.y} C ${start.x} ${midY}, ${end.x} ${midY}, ${end.x} ${end.y}`);
    }
    edgeLayer.appendChild(path);
  }
}
window.addEventListener('resize',renderEdges);
flowCanvas.addEventListener('scroll',()=>requestAnimationFrame(renderEdges));
requestAnimationFrame(renderEdges);
"""

section_html = f'''  <!-- ③ 전체 순서도 (신규 규칙 미리보기) -->
  <section>
    <h2>전체 스토리 순서도 — 신규 규칙 적용 미리보기</h2>
    <p style="color:var(--muted);font-size:13px;margin:0 0 16px;">기존 파일명은 그대로 유지. 이 화면에서만 신규 규칙을 적용한 ID로 표시합니다. <span class="changed-badge">노란 하이라이트</span> = 신규 규칙으로 ID가 변경되는 섹션.</p>

    <div class="flow-canvas" id="flowCanvas">
      <div class="flow-grid" id="flowGrid">
        <svg class="edge-layer" id="edgeLayer"></svg>
{chr(10).join("        "+l for l in grid_html.split(chr(10)))}
      </div>
    </div>

    <script type="application/json" id="sectionData">{json.dumps(sec_json, ensure_ascii=False)}</script>
    <script type="application/json" id="edgeData">{json.dumps(edge_data, ensure_ascii=False)}</script>
    <script>{JS}</script>
  </section>'''

# Write output
with open('scripts/_section3_output.html', 'w', encoding='utf-8') as f:
    f.write(section_html)
print(f"Written section3 HTML ({len(section_html)} chars)")
print("First 200 chars:", section_html[:200])
