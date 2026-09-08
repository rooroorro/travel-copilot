#!/usr/bin/env python3
import argparse, json, shutil, subprocess, sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('json_file');ap.add_argument('--out-dir',default='travel-pack');a=ap.parse_args()
    src=Path(a.json_file).resolve();root=Path(__file__).resolve().parent;out=Path(a.out_dir).resolve();out.mkdir(parents=True,exist_ok=True)
    v=subprocess.run([sys.executable,str(root/'validate_trip.py'),str(src)])
    if v.returncode: raise SystemExit(v.returncode)
    data=json.loads(src.read_text(encoding='utf-8'));title=(data.get('trip') or {}).get('title','trip').replace('/','-').replace('\\','-')
    j=out/'trip.json';shutil.copyfile(src,j)
    subprocess.run([sys.executable,str(root/'build_html.py'),str(src),'-o',str(out/(title+'.html'))],check=True)
    subprocess.run([sys.executable,str(root/'build_ics.py'),str(src),'-o',str(out/(title+'-reminders.ics'))],check=True)
    (out/'使用说明.txt').write_text('1. 打开 HTML 查看互动行程。\n2. 把同一个 HTML 发给同行人。\n3. 每个人在 HTML 中选择自己的身份并导出 ICS 导入手机日历。\n4. 行程更新后请重新导出提醒。\n5. 地图需要联网；文字行程和本地完成状态不依赖地图。\n',encoding='utf-8')
    print(out)
if __name__=='__main__': main()
