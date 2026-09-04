#!/usr/bin/env python3
"""Run a builder. Usage:  python run.py build_tax.py

The builders were written to run with model, build and output files flat in one directory.
This assembles that directory in a temp space, runs the builder there, and copies anything
new or changed back into ../out/ . Nothing in ../model/ is ever written to.
"""
import os, sys, shutil, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MODEL, OUT = os.path.join(ROOT, 'model'), os.path.join(ROOT, 'out')

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print('available:', ', '.join(sorted(f for f in os.listdir(HERE)
              if f.endswith('.py') and f not in ('run.py', 'recalc.py'))))
        return 1
    target = sys.argv[1]
    if not os.path.exists(os.path.join(HERE, target)):
        print('no such builder:', target); return 1
    os.makedirs(OUT, exist_ok=True)
    work = tempfile.mkdtemp(prefix='eacm-')
    try:
        for src in (MODEL, HERE, OUT):
            for f in os.listdir(src):
                p = os.path.join(src, f)
                if os.path.isfile(p):
                    shutil.copy2(p, os.path.join(work, f))
        before = {f: os.path.getmtime(os.path.join(work, f)) for f in os.listdir(work)}
        r = subprocess.run([sys.executable, target], cwd=work)
        if r.returncode:
            print('builder failed with exit code', r.returncode); return r.returncode
        model_files = set(os.listdir(MODEL)) | set(os.listdir(HERE))
        moved = []
        for f in sorted(os.listdir(work)):
            p = os.path.join(work, f)
            if not os.path.isfile(p) or f in model_files:
                continue
            if f not in before or os.path.getmtime(p) > before[f]:
                shutil.copy2(p, os.path.join(OUT, f)); moved.append(f)
        print('\nwrote to out/:', ', '.join(moved) if moved else '(nothing changed)')
        if any(f.endswith('.xlsx') for f in moved):
            print('now run:  python recalc.py ../out/<file>.xlsx   — ship only at zero errors')
        return 0
    finally:
        shutil.rmtree(work, ignore_errors=True)

sys.exit(main())
