from pathlib import Path
import re,html,json,hashlib
from course import LESSONS
from illustrations import EXTRAS, SCANNER_VALIDATION
ROOT=Path(__file__).resolve().parents[1]
E=lambda x:html.escape(str(x),quote=True)
style=(ROOT/'tools/base-styles.css').read_text()
style+='''
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}html,body{max-width:100%;overflow-x:hidden}.lesson-copy p,.walkthrough li,.visual-note,.compare-item,.tree-branch{overflow-wrap:anywhere}.visual-card{margin:24px 0}.hero h1{overflow-wrap:break-word}
:root{--accent:#c44932} [hidden]{display:none!important} a,button{touch-action:manipulation} button{cursor:pointer} :focus-visible{outline:3px solid #d04a32;outline-offset:4px} .skip{position:fixed;left:16px;top:-90px;z-index:100;background:#fff;padding:12px}.skip:focus{top:12px}
.topbar{gap:12px}.top-actions button{border:1px solid #6e7e80;background:transparent;color:#f4f0e6;border-radius:3px;padding:5px 12px;font-size:.8rem}.top-actions button[aria-pressed=true]{background:#f1d57a;color:#122127}.brand span{font-size:.66rem}.search-wrap{position:relative}.search-wrap input{background:#24343a;border:1px solid #69797b;color:white;border-radius:3px;padding:7px 10px;width:200px;font-size:.8rem}.search-wrap input::placeholder{color:#c0cccb}.search-results{position:absolute;right:0;top:43px;width:430px;max-height:65vh;overflow:auto;background:var(--paper);color:var(--ink);box-shadow:var(--shadow);border:1px solid var(--line);padding:12px}.search-results a{display:block;color:var(--ink);padding:10px;text-decoration:none;border-bottom:1px solid var(--line)}.search-results small{display:block;color:var(--muted)}.search-results p{margin:8px;color:var(--muted)}
.course-home{max-width:1240px;margin:auto;padding:55px 30px 90px}.course-home h2{font:500 2.6rem Baskerville,Georgia,serif;margin:5px 0 28px}.course-home .topic-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}.topic-card{text-decoration:none;display:flex;flex-direction:column;min-height:260px;transition:transform .2s}.topic-card:hover{transform:translateY(-4px)}.topic-card h3{font:600 1.7rem/1.15 Baskerville,Georgia,serif;margin:20px 0 15px}.topic-card .section-label{font-size:.75rem}.topic-card p{flex:1}.card-tail{font-size:.75rem;color:var(--accent);font-family:Menlo,monospace;margin-top:25px}.home-note{border-top:1px solid var(--line);margin-top:40px;padding-top:24px;color:var(--muted);max-width:850px}.hero h1{font-size:clamp(3rem,6.5vw,6.6rem);line-height:.98}.hero{min-height:380px;padding-top:75px;padding-bottom:65px}.hero::after{pointer-events:none}.hero-meta .chip{font-size:.72rem}.chapter-shell{display:grid;grid-template-columns:235px minmax(0,1fr);gap:48px;max-width:1360px;margin:auto;padding:52px 34px 90px}.course-nav{position:sticky;top:86px;align-self:start;max-height:calc(100vh - 110px);overflow:auto;border-right:1px solid var(--line);padding-right:18px}.course-nav>a{display:flex;gap:12px;text-decoration:none;color:var(--muted);padding:10px 8px;font-size:.83rem;line-height:1.4;border-left:3px solid transparent}.course-nav>a.active{background:#e8e0d0;border-color:var(--accent);color:var(--ink)}.course-nav a b{font:700 .8rem Menlo,monospace;color:var(--accent)}.course-nav .nav-label{font:700 .7rem Menlo,monospace;letter-spacing:.1em;text-transform:uppercase;margin:0 0 12px}.lecture-content{min-width:0;max-width:920px}.section{margin-bottom:44px}.section h2{font-size:2.5rem}.lesson-block{grid-template-columns:42px minmax(0,1fr);gap:18px;padding:32px 0;scroll-margin-top:95px}.lesson-copy>p{font-size:1.02rem}.lesson-copy h3{font-size:1.85rem}.lesson-copy code,p code,li code{font-family:Menlo,monospace;font-size:.88em}.local-toc{background:#eee7da;border:1px solid var(--line);padding:14px 22px;margin:25px 0}.local-toc summary{font-weight:600;cursor:pointer}.local-toc ol{columns:2;padding-left:20px;font-size:.85rem}.local-toc a{text-decoration:none;color:var(--muted)}.local-toc li{padding:3px 0;break-inside:avoid}.goal-grid{margin:24px 0 34px}.goal{padding:16px;font-size:.9rem}.inline-visual{margin:28px 0 40px}.visual-card{box-shadow:5px 5px 0 var(--paper-deep)}.visual-card h3{font-size:1.6rem}.visual-card header{padding:20px}.visual-table th,.visual-table td{vertical-align:top}.visual-process{display:flex;flex-wrap:wrap;padding:20px;gap:12px;background:transparent}.visual-process-item{flex:1 1 140px;position:relative;padding:17px;background:#e6ebe4;border:1px solid #b9c5ba;min-height:112px}.visual-process-item:after{content:'→';position:absolute;right:-13px;top:42%;z-index:1;color:var(--accent);font-weight:bold}.visual-process-item:last-child:after{display:none}.visual-process-item strong,.visual-process-item small{display:block}.visual-process-item small{color:var(--muted);font-size:.8rem;line-height:1.5;margin-top:8px}.visual-index{display:block;color:var(--accent);font:700 .65rem Menlo,monospace;margin-bottom:9px}.visual-tree{padding:22px}.tree-root{text-align:center;background:#122127;color:#f4f0e6;padding:18px;font-weight:700}.tree-branches{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:18px;margin-top:28px;border-top:1px solid #9aab9d;padding-top:18px}.tree-branch{background:#e6ebe4;padding:16px;border:1px solid #b9c5ba}.tree-branch h4{margin:0 0 8px}.tree-branch p,.tree-branch li{font-size:.83rem}.tree-branch ul{padding-left:18px}.visual-compare{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1px;background:var(--line)}.compare-item{background:#f7f3ea;padding:22px}.compare-item h4{margin:10px 0;font:600 1.5rem Baskerville,serif}.compare-item>span{color:var(--accent);font:700 .7rem Menlo,monospace}.compare-item p,.compare-item li{font-size:.9rem}.visual-note{padding:12px 20px;background:#eee4d1;margin:0;font-size:.85rem}.visual-note strong{margin-right:10px}.visual-description{color:var(--muted);font-size:.9rem}.demo-block{border-top:3px solid var(--accent);margin:44px 0;padding-top:20px;scroll-margin-top:90px}.demo-block>h3{font:600 1.9rem/1.15 Baskerville,Georgia,serif;margin:12px 0 20px}.demo-tag{color:var(--accent);font:700 .7rem Menlo,monospace;letter-spacing:.08em;text-transform:uppercase}.code-example{max-width:100%;box-shadow:none;margin-top:14px}.code-example figcaption{display:flex;gap:10px;align-items:center;justify-content:space-between;flex-wrap:wrap}.code-example pre{tab-size:4}.code-example code{font-size:.8rem;line-height:1.75;white-space:pre}.code-actions{display:flex;gap:12px;align-items:center}.code-actions button{background:#24343a;border:1px solid #52686a;color:#e7eee9;border-radius:3px;font-size:.75rem;padding:3px 9px}.code-actions a{color:#bde0d2;font-size:.74rem;text-underline-offset:3px}.tok-key{color:#ffbb8e}.tok-str{color:#c9dc9a}.tok-comment{color:#9caeb3;font-style:italic}.tok-num{color:#96d4d5}.trace-grid{display:grid;grid-template-columns:minmax(150px,.7fr) minmax(0,1.3fr);border:1px solid #c9c0ae;margin-bottom:20px;background:#f8f4eb}.expected{background:#e4ebe3;padding:20px;min-width:0}.expected b,.walkthrough b{font:700 .7rem Menlo,monospace;color:#315e48;text-transform:uppercase;letter-spacing:.07em}.expected pre{white-space:pre-wrap;overflow-wrap:anywhere;font:.85rem/1.6 Menlo,monospace;margin-bottom:0}.walkthrough{padding:20px}.walkthrough ol{padding-left:20px;margin:12px 0 0}.walkthrough li{margin-bottom:10px;font-size:.9rem}.demo-input{padding:12px 18px;background:#eee7da;border:1px solid var(--line);font-size:.85rem}.demo-input pre{margin:8px 0;white-space:pre-wrap}.demo-run{font-size:.8rem;color:var(--muted);overflow-wrap:anywhere}.end-nav{display:flex;justify-content:space-between;gap:20px;border-top:1px solid var(--line);padding:30px 0}.end-nav a{text-decoration:none;color:var(--accent);max-width:48%}.end-nav small{display:block;font:700 .65rem Menlo,monospace;color:var(--muted);text-transform:uppercase}.page-footer{padding:24px 30px;background:var(--dark);color:#bdc9c6;display:flex;justify-content:space-between;font-size:.8rem}.mobile-select{display:none}.projector .lesson-copy>p,.projector .walkthrough li{font-size:1.2rem}.projector .code-example code{font-size:1rem}.projector .course-nav{display:none}.projector .chapter-shell{grid-template-columns:minmax(0,1fr);max-width:1120px}.projector .lecture-content{max-width:none}.projector .hero h1{font-size:4rem}.no-results{padding:20px}.status{position:fixed;bottom:20px;right:20px;z-index:100;background:#122127;color:#f4f0e6;padding:12px 20px;box-shadow:var(--shadow)}
@media(max-width:1000px){.chapter-shell{grid-template-columns:190px minmax(0,1fr);gap:25px;padding-left:22px;padding-right:22px}.course-home .topic-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.brand span{display:none}.search-wrap input{width:150px}}
@media(max-width:760px){.top-actions{display:flex;width:100%}.search-wrap{flex:1}.search-wrap input{width:100%!important}.topbar{position:relative;flex-wrap:wrap;padding:12px 18px}.top-actions{gap:8px;flex-wrap:wrap}.search-wrap input{width:140px}.search-results{position:fixed;top:110px;left:12px;right:12px;width:auto}.hero{min-height:0;padding:45px 22px}.hero h1{font-size:3.3rem}.chapter-shell{display:block;padding:24px 18px 50px}.course-nav{display:none}.mobile-select{display:block;padding:12px 18px;background:#e8e0d0}.mobile-select select{width:100%;padding:9px;background:#f4f0e6;border:1px solid #a99d86;font:inherit}.lesson-block{grid-template-columns:1fr;gap:8px}.lesson-copy h3{margin-top:0}.trace-grid{grid-template-columns:1fr}.local-toc ol{columns:1}.goal-grid{grid-template-columns:1fr}.course-home{padding:32px 20px 60px}.course-home .topic-grid{grid-template-columns:1fr}.visual-table{font-size:.8rem;min-width:520px}.visual-table-wrap{overflow:auto}.code-example pre{padding:15px}.code-example code{font-size:.74rem}.visual-card header{padding:16px}.visual-process{padding:14px}.projector .hero h1{font-size:3rem}.page-footer{gap:14px;flex-wrap:wrap}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
@media print{body{background:white;font-size:10pt}.topbar,.course-nav,.mobile-select,.local-toc,.end-nav,.code-actions,.skip,.status,.search-results,#home,.progress{display:none!important}.lecture[hidden]{display:block!important}.lecture{break-before:page}.hero{background:#fff!important;color:#182228!important;min-height:0;padding:10px 0!important;border-bottom:2px solid #c44932}.hero h1{font-size:28pt!important;color:#182228!important}.hero p,.eyebrow,.chip{color:#344249!important}.hero::before,.hero::after{display:none}.hero-meta{margin-top:10px}.chapter-shell{display:block;padding:20px 0}.lecture-content{max-width:none}.lesson-block{display:block;padding:16px 0}.lesson-number{margin-bottom:8px}.lesson-copy>p{font-size:10pt}.code-example{box-shadow:none;break-inside:auto}.code-example pre{white-space:pre-wrap}.code-example code{white-space:pre-wrap;overflow-wrap:anywhere;font-size:8pt}.demo-block,.visual-card,.trace-grid{break-inside:avoid}.visual-card{box-shadow:none}.lesson-copy h3,.demo-block h3{break-after:avoid}.page-footer{background:white;color:#344249}.goal-grid{grid-template-columns:repeat(2,1fr)}body.print-current .lecture[hidden]{display:none!important}}
#home .home-cover{min-height:0;padding:5.1vw 8.3vw 0 6.1vw;background:#122127;color:#f4f0e6;overflow:hidden}
#home .home-cover::before,#home .home-cover::after{display:none}
.cover-mark{width:3.4vw;min-width:44px;height:2px;background:#be9072}
#home .home-cover h1{max-width:none;margin:3.1vw 0 2.4vw;font:500 clamp(3rem,6.8vw,11rem)/1 Baskerville,Georgia,serif;letter-spacing:-.055em;overflow-wrap:normal}
#home .home-cover>p{max-width:none;color:#bcc7c7;font-size:clamp(1rem,1.48vw,2rem);letter-spacing:.025em;line-height:1.4}
.cover-signature{display:flex;justify-content:flex-end;align-items:center;gap:22px;margin-top:5vw;border-top:1px solid #37464a;padding:1.45vw 0 .45vw;color:#bbc6c6;font-size:clamp(.85rem,1.05vw,1.5rem);letter-spacing:.035em}
.cover-dot{color:#be9072}
@media(max-width:760px){#home .home-cover{padding:42px 24px 12px}#home .home-cover h1{font-size:clamp(2.8rem,10.8vw,5rem);margin:36px 0 24px;line-height:1.04}.cover-signature{margin-top:54px;padding-top:18px;gap:14px}}

.teaching-illustration svg{display:block;width:100%;height:auto;min-width:620px;font-family:"Avenir Next",Avenir,sans-serif}.illustration-scroll{overflow-x:auto;padding:16px 8px}.illustration-caption{padding:18px 22px;border-top:1px solid var(--line);color:var(--muted);font-size:.9rem}.platform-heading>strong{font-size:2.6rem}.platform-heading>span{font-size:1rem}.platform-heading small{font-size:.88rem}.platform-diagram{margin:32px 0}.platform-equation{font-size:1.7rem}.visual-table thead th{background:#122127;color:#f4f0e6;font:700 .82rem Menlo,monospace;padding:18px}.visual-table tbody th{color:#91482f;background:#f3eeea}.visual-table tbody td,.visual-table tbody th{padding:17px 18px;line-height:1.65}.visual-table tbody tr:nth-child(even) td{background:#f1ecdf}.visual-card>header{padding:26px}.visual-card>header h3{margin:10px 0 4px;font-size:1.9rem}@media print{.teaching-illustration svg{min-width:0}.illustration-scroll{overflow:visible}.platform-diagram{break-inside:avoid}}@media(max-width:760px){.platform-heading{flex-wrap:wrap;gap:10px}.platform-heading>strong{font-size:2rem}.platform-layer{padding:14px}.visual-card>header{padding:20px}.visual-card>header h3{font-size:1.65rem}}

.compile-scroll{overflow-x:auto;padding:28px 22px 20px}.compile-flow{display:grid;grid-template-columns:minmax(168px,1fr) 76px minmax(168px,1fr) 76px minmax(168px,1fr);align-items:stretch;min-width:700px;gap:8px}.compile-stage{padding:22px 16px;background:#f1e9dc;border:1px solid #c5b298;border-top:3px solid #9b4d2b;border-radius:4px}.compile-number{display:block;font:700 .64rem Menlo,monospace;letter-spacing:.06em;color:#9b4d2b;margin-bottom:22px}.compile-stage strong{display:block;white-space:nowrap;font:700 .85rem Menlo,monospace;letter-spacing:-.03em;color:#182228}.compile-stage p{font-size:.9rem;line-height:1.6;margin:18px 0;color:#59656a}.compile-stage small{font-size:.75rem;color:#59656a}.compile-link{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#9b4d2b}.compile-link>span{font:700 .65rem Menlo,monospace;margin-bottom:10px}.compile-link code{font:700 .8rem Menlo,monospace;background:#e8e0d0;padding:4px 7px;border-radius:3px}.compile-link b{font:400 2.4rem/1.3 Georgia,serif}.compile-link small{font-size:.68rem;line-height:1.5;color:#59656a}.compile-running{background:#122127;border-color:#122127}.compile-running strong{color:#f4f0e6}.compile-running .compile-number{color:#ddb294}.compile-running p,.compile-running small{color:#bccbc7}.compile-summary{display:flex;flex-wrap:wrap;gap:18px 36px;padding:16px 22px;margin:0;border-top:1px solid var(--line);font-size:.8rem;color:var(--muted)}.compile-summary b{color:#9b4d2b;margin-right:10px}@media(max-width:760px){.compile-scroll{padding:18px 14px}.compile-flow{min-width:720px}}@media print{.compile-flow{min-width:0;grid-template-columns:minmax(0,1fr) 50px minmax(0,1fr) 50px minmax(0,1fr)}.compile-stage{padding:12px 8px}.compile-stage strong{font-size:8pt}.compile-scroll{overflow:visible;padding:16px 10px}}

'''

def hi(code):
 pattern=r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\b(?:public|private|protected|static|final|class|interface|abstract|extends|implements|void|int|double|boolean|return|new|if|else|for|while|try|catch|finally|throw|throws|import|package|synchronized|instanceof|this|super|true|false|null)\b|\b\d+\b'
 out=[];pos=0
 for m in re.finditer(pattern,code):
  out.append(E(code[pos:m.start()]));v=m.group()
  kind='comment' if v.startswith(('//','/*')) else 'str' if v.startswith('"') else 'num' if v.isdigit() else 'key'
  out.append(f'<span class="tok-{kind}">{E(v)}</span>');pos=m.end()
 return ''.join(out)+E(code[pos:])

def render_visual(v):
 if v['kind']=='scanner-validation':return SCANNER_VALIDATION
 s=f'<figure class="visual-card"><header><span class="visual-type">{E('Reference table' if v['kind']=='table' else 'Concept relationship')}</span><h3>{E(v["title"])}</h3>'
 if v.get('description'):s+=f'<p class="visual-description">{E(v["description"])}</p>'
 s+='</header>'
 if v['kind']=='flow' and v['title']=='From source file to running program':
  s+='''<div class="compile-scroll" tabindex="0" role="region" aria-label="Java compilation and execution flow"><div class="compile-flow"><div class="compile-stage"><span class="compile-number">01 / SOURCE</span><strong>First.java</strong><p>Human-readable Java source</p><small>Write the program</small></div><div class="compile-link"><span>02</span><code>javac</code><b aria-hidden="true">→</b><small>Checks types<br>and syntax</small></div><div class="compile-stage"><span class="compile-number">03 / BYTECODE</span><strong>First.class</strong><p>Portable JVM bytecode</p><small>Compilation result</small></div><div class="compile-link"><span>04</span><code>java</code><b aria-hidden="true">→</b><small>Starts a JVM</small></div><div class="compile-stage compile-running"><span class="compile-number">05 / EXECUTION</span><strong>Running program</strong><p>The JVM executes the bytecode</p><small>Local OS and hardware</small></div></div></div><p class="compile-summary"><span><b>Compile</b> Source → bytecode</span><span><b>Run</b> Bytecode → JVM → execution</span></p>'''
 elif v['kind']=='flow':
  s+='<div class="visual-process">'+''.join(f'<div class="visual-process-item"><span class="visual-index">{i+1:02d}</span><strong>{E(t["label"])}</strong><small>{E(t.get("detail",""))}</small></div>' for i,t in enumerate(v['items']))+'</div>'
 elif v['kind']=='table':
  s+='<div class="visual-table-wrap"><table class="visual-table"><thead><tr>'+''.join(f'<th scope="col">{E(c)}</th>' for c in v['columns'])+'</tr></thead><tbody>'
  for row in v['rows']:s+='<tr>'+''.join(f'<th scope="row">{E(c)}</th>' if i==0 else f'<td>{E(c)}</td>' for i,c in enumerate(row))+'</tr>'
  s+='</tbody></table></div>'
 elif v['kind']=='tree':
  s+=f'<div class="visual-tree"><div class="tree-root">{E(v["root"])}</div><div class="tree-branches">'
  for b in v['branches']:s+=f'<div class="tree-branch"><h4>{E(b["label"])}</h4><p>{E(b.get("detail",""))}</p><ul>'+''.join(f'<li>{E(c)}</li>' for c in b.get('children',[]))+'</ul></div>'
  s+='</div></div>'
 elif v['kind']=='compare':
  s+='<div class="visual-compare">'
  for t in v['items']:s+=f'<div class="compare-item"><span>{E(t.get("kicker",""))}</span><h4>{E(t["title"])}</h4><p>{E(t["body"])}</p><ul>'+''.join(f'<li>{E(p)}</li>' for p in t.get('points',[]))+'</ul></div>'
  s+='</div>'
 if v.get('note'):s+='<p class="visual-note"><strong>Remember</strong>'+E(v['note'])+'</p>'
 return s+'</figure>'

checks=[]
def render_demo(l,d,index):
 n=l['number'];stem=f'lesson-{n:02d}/{d["name"]}';directory=ROOT/'demos'/stem;directory.mkdir(parents=True,exist_ok=True)
 package=re.search(r'^package ([\w.]+);',d['code'],re.M)
 mainfile=(package.group(1).replace('.','/')+'/' if package else '')+d['name']+'.java'
 files={mainfile:d['code'],**d['files']}
 if d['stdin']:files['input.txt']=d['stdin']
 for name,content in files.items():
  p=directory/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
 classname=(package.group(1)+'.' if package else '')+d['name']
 cmd=('javac -d out '+ ' '.join(name for name in files if name.endswith('.java'))+'\njava -cp out '+classname) if package else ('javac '+d['name']+'.java\njava '+d['name'])
 if d['stdin']:cmd+=' < input.txt'
 (directory/'README.txt').write_text('Open a terminal in this demo folder. Use JDK 21 or later.\n\n'+cmd+'\n\nExpected output:\n'+d['output']+'\n')
 checks.append(dict(directory=directory.relative_to(ROOT).as_posix(),classname=classname,stdin=d['stdin'],expected=d['output'],name=d['name']))
 s=f'<article class="demo-block" id="l{n}-demo-{index}"><span class="demo-tag">Code example · Complete Java program</span><h3>{E(d["title"])}</h3>'
 for fi,(name,code) in enumerate(files.items()):
  if name=='input.txt':continue
  cid=f'code-{n}-{index}-{fi}'
  if name.endswith('.java'):
   s+=f'<figure class="code-example"><figcaption><span>{E(name)}</span><span class="code-actions"><a href="demos/{E(stem)}/{E(name)}" download>Download</a><button type="button" data-copy="{cid}">Copy code</button></span></figcaption><pre><code id="{cid}">{hi(code)}</code></pre></figure>'
  else:s+=f'<div class="demo-input"><strong>Supporting file · {E(name)}</strong><pre>{E(code)}</pre></div>'
 if d['stdin']:s+=f'<div class="demo-input"><strong>Sample input · type these lines when running interactively</strong><pre>{E(d["stdin"])}</pre></div>'
 s+='<p class="demo-run">Run from the demo folder with JDK 21: <code>'+E(cmd).replace('\n','</code><br><code>')+'</code></p>'
 s+='<div class="trace-grid"><div class="expected"><b>Expected output</b><pre>'+E(d['output'])+'</pre></div><div class="walkthrough"><b>Read the execution</b><ol>'+''.join(f'<li>{E(t)}</li>' for t in d['explain'])+'</ol></div></div></article>'
 return s

search=[]
nav=''.join(f'<a href="#lesson-{x["number"]:02d}" data-lesson-link="{x["number"]}"><b>{x["number"]:02d}</b><span>{E(x["title"])}</span></a>' for x in LESSONS)
totald=sum(len(x['demos']) for x in LESSONS)
parts=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Java Programming · Twelve Lessons</title><meta name="description" content="Twelve Java lessons with concept explanations, relationship diagrams and runnable code demonstrations."><style>'+style+'</style></head><body><a class="skip" href="#main">Skip to teaching content</a><header class="topbar"><a class="brand" href="#home"><strong>Java Programming</strong><span>Candice Wang · Teaching Edition</span></a><div class="top-actions"><div class="search-wrap"><label class="sr-only" for="search">Search all lessons</label><input id="search" type="search" placeholder="Search all lessons…" autocomplete="off" aria-controls="search-results"><div class="search-results" id="search-results" hidden></div></div><button id="projector" type="button" aria-pressed="false">Large text</button><button id="print" type="button">Print lesson</button></div></header><main id="main"><section id="home"><div class="hero home-cover"><div class="cover-mark" aria-hidden="true"></div><h1>Java Programming</h1><p>Write Once, Run Anywhere</p><div class="cover-signature"><span>Candice Wang</span><span class="cover-dot" aria-hidden="true">·</span><span>2026</span></div></div><div class="course-home"><span class="section-label">The learning sequence</span><h2>Choose your next lesson</h2><div class="topic-grid">']
for l in LESSONS:
 n=l['number'];parts.append(f'<a class="topic-card" href="#lesson-{n:02d}"><span class="section-label">Lesson {n:02d}</span><h3>{E(l["title"])}</h3><p>{E(l["subtitle"])}</p><span class="card-tail">{len(l["sections"])} concepts · {len(l["demos"])} code demos →</span></a>')
parts.append('</div><p class="home-note">Each lesson connects definitions with diagrams and complete code examples. Read the sample input and expected output before running a demo. Use Large text for classroom viewing, or print the current lesson for a paper copy. Start with basic Java expressions, conditionals, loops and arrays in mind; the opening lesson refreshes the program structure.</p><button type="button" id="print-all">Print all lessons</button></div></section>')
parts.append('<div class="mobile-select" id="mobile-nav" hidden><label for="lesson-select">Go to lesson</label><select id="lesson-select"><option value="home">Course overview</option>'+''.join(f'<option value="lesson-{l["number"]:02d}">{l["number"]:02d} · {E(l["title"])}</option>' for l in LESSONS)+'</select></div>')
for l in LESSONS:
 n=l['number'];lid=f'lesson-{n:02d}'
 parts.append(f'<section class="lecture" id="{lid}"><div class="hero"><div class="eyebrow">Lesson {n:02d} / 12</div><h1>{E(l["title"])}</h1><p>{E(l["subtitle"])}</p><div class="hero-meta"><span class="chip">Concepts &amp; definitions</span><span class="chip">Relationship diagrams</span><span class="chip">{len(l["demos"])} runnable demos</span></div></div><div class="chapter-shell"><nav class="course-nav" aria-label="Course lessons"><div class="nav-label">Course contents</div><a href="#home">← Course overview</a>{nav}</nav><div class="lecture-content"><section class="section"><span class="section-label">What you will understand</span><div class="goal-grid">'+''.join(f'<div class="goal">{E(g)}</div>' for g in l['goals'])+'</div></section>')
 parts.append('<details class="local-toc"><summary>In this lesson</summary><ol>'+''.join(f'<li><a href="#{lid}-s{i+1}">{E(s["title"])}</a></li>' for i,s in enumerate(l['sections']))+'</ol></details>')
 vi=di=0
 for i,s in enumerate(l['sections']):
  sid=f'{lid}-s{i+1}'
  parts.append(f'<article class="lesson-block" id="{sid}"><div class="lesson-number">{i+1:02d}</div><div class="lesson-copy"><h3>{E(s["title"])}</h3>'+''.join(f'<p>{E(p)}</p>' for p in s['paragraphs']))
  if s.get('html'):parts.append(s['html'])
  if s.get('note'):parts.append('<aside class="teaching-note"><strong>Remember</strong>'+E(s['note'])+'</aside>')
  parts.append('</div></article>')
  parts.extend(EXTRAS.get((n,i+1),[]))
  search.append(dict(id=sid,lesson=n,title=s['title'],text=' '.join(s['paragraphs'])))
  for subindex,sub in enumerate(s.get('subsections',[]),1):
   subid=f'{sid}-topic-{subindex}'
   parts.append(f'<article class="lesson-block" id="{subid}" style="display:block"><div class="lesson-copy"><h3>{E(sub["title"])}</h3>'+''.join(f'<p>{E(p)}</p>' for p in sub['paragraphs']))
   if sub.get('html'):parts.append(sub['html'])
   if sub.get('note'):parts.append('<aside class="teaching-note"><strong>Remember</strong>'+E(sub['note'])+'</aside>')
   parts.append('</div></article>')
   search.append(dict(id=subid,lesson=n,title=sub['title'],text=' '.join(sub['paragraphs'])))
   for v in sub.get('visuals',[]):parts.append('<div class="inline-visual">'+render_visual(v)+'</div>')
   while di<len(l['demos']) and l['demos'][di]['after']==i+1 and l['demos'][di].get('subpart')==subindex:
    parts.append(render_demo(l,l['demos'][di],di+1));di+=1
  if l['visuals'] and all('after' in v for v in l['visuals']):
   for v in l['visuals']:
    if v['after']==i+1:parts.append('<div class="inline-visual">'+render_visual(v)+'</div>')
   vi=len(l['visuals'])
  elif (i+1)%3==0 and vi<len(l['visuals']):parts.append('<div class="inline-visual">'+render_visual(l['visuals'][vi])+'</div>');vi+=1
  while di<len(l['demos']) and l['demos'][di]['after']==i+1:
   parts.append(render_demo(l,l['demos'][di],di+1));di+=1
 for v in l['visuals'][vi:]:parts.append('<div class="inline-visual">'+render_visual(v)+'</div>')
 for j,d in enumerate(l['demos'][di:],di+1):parts.append(render_demo(l,d,j))
 for j,d in enumerate(l['demos'],1):search.append(dict(id=f'l{n}-demo-{j}',lesson=n,title=d['title'],text=d['code']+' '+' '.join(d['explain'])))
 parts.append('<nav class="end-nav" aria-label="Adjacent lessons">'+(f'<a href="#lesson-{n-1:02d}"><small>Previous lesson</small>← {E(LESSONS[n-2]["title"])}</a>' if n>1 else '<a href="#home">← Course overview</a>')+(f'<a href="#lesson-{n+1:02d}"><small>Next lesson</small>{E(LESSONS[n]["title"])} →</a>' if n<12 else '<a href="#home"><small>Course complete</small>Return to overview →</a>')+'</nav></div></div></section>')
parts.append('</main><footer class="page-footer"><span>Java Programming · Candice Wang</span><span>Understand → Trace → Run → Explain</span></footer><div class="status" id="status" role="status" hidden></div>')
script='''
const searchData=SEARCH_DATA;
const $=id=>document.getElementById(id);
let current=0;
function route(){
 const target=decodeURIComponent(location.hash.slice(1)||'home');
 const node=$(target);const lecture=node?.closest('.lecture');
 const n=lecture ? Number(lecture.id.slice(-2)) : 0;current=n;
 document.querySelectorAll('.lecture').forEach(el=>el.hidden=el!==lecture);
 $('home').hidden=!!n;$('mobile-nav').hidden=!n;
 $('lesson-select').value=n?'lesson-'+String(n).padStart(2,'0'):'home';
 document.querySelectorAll('[data-lesson-link]').forEach(a=>{const active=Number(a.dataset.lessonLink)===n;a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
 document.title=n?`Lesson ${String(n).padStart(2,'0')} · ${lecture.querySelector('h1').textContent} · Java Programming`:'Java Programming · Twelve Lessons';
 $('search-results').hidden=true;
 requestAnimationFrame(()=>{if(node&&node!==lecture&&target!=='home')node.scrollIntoView({block:'start'});else window.scrollTo({top:0,behavior:'instant'});});
}
window.addEventListener('hashchange',route);route();
$('lesson-select').addEventListener('change',e=>location.hash=e.target.value);
$('projector').addEventListener('click',()=>{const on=document.body.classList.toggle('projector');$('projector').setAttribute('aria-pressed',String(on));});
$('print').addEventListener('click',()=>{document.body.classList.toggle('print-current',current>0);window.print();});
$('print-all').addEventListener('click',()=>{document.body.classList.remove('print-current');window.print();});
const esc=t=>String(t).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
$('search').addEventListener('input',e=>{const q=e.target.value.trim().toLowerCase();const box=$('search-results');if(q.length<2){box.hidden=true;return;}const hits=searchData.filter(s=>(s.title+' '+s.text).toLowerCase().includes(q));box.innerHTML=hits.length?'<p>'+hits.length+' matches · showing up to 20</p>'+hits.slice(0,20).map(s=>`<a href="#${s.id}"><small>Lesson ${String(s.lesson).padStart(2,'0')}</small>${esc(s.title)}</a>`).join(''):'<p>No matching concept. Try “Scanner”, “monitor” or “stream”.</p>';box.hidden=false;});
document.addEventListener('keydown',e=>{if(e.key==='Escape')$('search-results').hidden=true;});
document.addEventListener('click',e=>{if(!e.target.closest('.search-wrap'))$('search-results').hidden=true;});
function announce(t){$('status').textContent=t;$('status').hidden=false;setTimeout(()=>$('status').hidden=true,2200);}
document.addEventListener('click',async e=>{const b=e.target.closest('[data-copy]');if(!b)return;const value=$(b.dataset.copy).textContent;try{if(navigator.clipboard&&window.isSecureContext)await navigator.clipboard.writeText(value);else{const area=document.createElement('textarea');area.value=value;area.style.position='fixed';area.style.opacity='0';document.body.append(area);area.select();const ok=document.execCommand('copy');area.remove();if(!ok)throw new Error('clipboard');}announce('Code copied');}catch{const range=document.createRange();range.selectNodeContents($(b.dataset.copy));const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);announce('Code selected. Press Command+C or Ctrl+C.');}});
'''.replace('SEARCH_DATA',json.dumps(search,ensure_ascii=False).replace('</','<\\/'))
parts.append('<script>'+script+'</script></body></html>')
(ROOT/'index.html').write_text('\n'.join(parts))
(ROOT/'tools/checks.json').write_text(json.dumps(checks,indent=2))
(ROOT/'tools/course-data.json').write_text(json.dumps(LESSONS,indent=2,ensure_ascii=False))
(ROOT/'README.md').write_text('''# Java Programming — Twelve Lessons

Open `index.html` in a modern browser. All lesson text, styling, diagrams and navigation are included in that file and work offline. Keep the demos folder beside it for the Download links.

- Twelve lessons with concept explanations, relationship diagrams and complete Java demonstrations.
- Search across all lessons; use Large text for classroom viewing.
- Print the current lesson or print all lessons from the course overview.
- Each demo folder includes source files, supporting input when needed, and run instructions.
- Examples target JDK 21. Expected output is shown beside each demonstration.

## Rebuild and verify

Use Python 3.12 or later and JDK 21 or later. No Python packages are required.

```sh
python3 tools/build.py
python3 tools/verify.py
```

The build regenerates index.html, demo files and course data from tools/.
The verifier compiles every demonstration with Java 21 compatibility and checks its output.
All build inputs are included in this repository.
''')
print(json.dumps(dict(lessons=len(LESSONS),sections=sum(len(l['sections']) for l in LESSONS),demos=totald,visuals=sum(len(l['visuals']) for l in LESSONS),size=(ROOT/'index.html').stat().st_size)))
