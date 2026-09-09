"""Recreate local, absolute-path route receipts from portable requests."""
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]

if __name__=='__main__':
    output=ROOT/'routing'
    output.mkdir(exist_ok=True)
    python=REPO/'.venv/bin/python'
    interpreter=str(python) if python.exists() else sys.executable
    for packet in sorted((ROOT/'requests').glob('*.json')):
        result=subprocess.run([interpreter,str(REPO/'engine/scripts/specialist_route.py'),'route',str(packet),'--workspace',str(ROOT.parent)],text=True,capture_output=True)
        if result.returncode:
            raise SystemExit(result.stderr or result.stdout)
        (output/packet.name).write_text(result.stdout)
        print('Validated '+packet.name)
