from pathlib import Path
import json,subprocess,tempfile,concurrent.futures
root=Path(__file__).resolve().parents[1]
checks=json.loads((root/'tools/checks.json').read_text())
def check(c):
 p=root / c['directory']
 with tempfile.TemporaryDirectory(prefix='java-teaching-') as out:
  compile=subprocess.run(['javac','--release','21','-Xlint:all','-d',out,*[str(f) for f in p.rglob('*.java')]],capture_output=True,text=True,timeout=40)
  if compile.returncode:return dict(name=c['name'],ok=False,error=compile.stderr)
  run=subprocess.run(['java','-cp',out,c['classname']],input=c['stdin'],cwd=p,capture_output=True,text=True,timeout=15)
  return dict(name=c['name'],ok=run.returncode==0 and run.stdout.strip()==c['expected'].strip(),warnings=compile.stderr,output=run.stdout,error=run.stderr)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(check,checks))
(root/'tools/code-validation.json').write_text(json.dumps(results,indent=2))
print(json.dumps({'passed':sum(r['ok'] for r in results),'total':len(results),'failures':[r for r in results if not r['ok']],'warnings':[r for r in results if r.get('warnings')]},indent=2))
