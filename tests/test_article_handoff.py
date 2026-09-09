"""Exercise recipient verification with relocated bytes and no builder receipt."""
import json
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

REPO = Path(__file__).resolve().parents[1]
REL = Path('packages/camp_tix_launch_001/01_channel_run/blog')


@pytest.fixture
def recipient(tmp_path):
    shutil.copytree(REPO / 'packages/camp_tix_launch_001', tmp_path / 'packages/camp_tix_launch_001',
                    ignore=shutil.ignore_patterns('__pycache__', 'routing'))
    # Canonical implementation stays shared; campaign files move to a new host path.
    (tmp_path / 'engine').symlink_to(REPO / 'engine', target_is_directory=True)
    return tmp_path / REL


def verify(root, *args):
    return subprocess.run([sys.executable, str(root / 'evidence/verify.py'), *args],
                          capture_output=True, text=True, timeout=30)


def test_relocated_article_passes_without_route_file_and_is_read_only(recipient):
    report = recipient / 'evidence/checks.json'
    before = report.read_bytes()
    assert not (recipient.parent / 'routing/blog.json').exists()
    for _ in range(2):
        result = verify(recipient)
        assert result.returncode == 0, result.stdout + result.stderr
    assert report.read_bytes() == before


@pytest.mark.parametrize('target', ['article', 'source'])
def test_changed_bytes_are_rejected(recipient, target):
    if target == 'article':
        path = recipient / 'article.md'
    else:
        request = json.loads((recipient.parent / 'requests/blog.json').read_text())
        source = next(s for s in request['sources'] if s['kind'] == 'fact')
        path = recipient.parents[1] / source['path']
    original = path.read_bytes()
    path.write_bytes(original + b'\nChanged during recipient audit.\n')
    assert verify(recipient).returncode != 0
    path.write_bytes(original)
    assert verify(recipient).returncode == 0


def test_changed_context_is_rejected_even_with_forged_route(recipient):
    provenance = recipient / 'provenance.json'
    receipt = json.loads(provenance.read_text())
    receipt['route']['context_digest'] = '0' * 64
    provenance.write_text(json.dumps(receipt))
    route = recipient.parent / 'routing/blog.json'
    route.parent.mkdir()
    route.write_text(json.dumps({'context_digest': '0' * 64, 'status': 'ready_for_protocol'}))
    result = verify(recipient)
    assert result.returncode == 1, result.stderr
    assert '"status": "fail"' in result.stdout


def test_report_write_requires_explicit_flag(recipient):
    report = recipient / 'evidence/checks.json'
    report.write_text('{}')
    result = verify(recipient, '--write-report')
    assert result.returncode == 0, result.stdout + result.stderr
    assert json.loads(report.read_text())['status'] == 'pass'
