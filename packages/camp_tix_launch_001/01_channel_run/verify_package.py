"""Check the actual campaign files, source routes and review bindings.

--write-manifest records current files after review. The default mode checks
that snapshot without rewriting it. This never grants human approval.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
SEGMENTS=['lead_smb','lead_agency','lead_reseller_affiliate','customer_smb','customer_agency']


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PACKAGE-MANIFEST.json' and not (p.parent.name=='routing' and p.suffix=='.json'))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-manifest',action='store_true')
    args=parser.parse_args()
    checks=[]
    def check(name,value):
        if not value: raise AssertionError(name)
        checks.append(name)
    data=json.loads((ROOT/'review-data.json').read_text())
    check('review has eleven named items',len(data['assets'])==11 and len({a['id'] for a in data['assets']})==11)
    check('only prior media carries approval',{a['id'] for a in data['assets'] if a['approved']}=={'social-video','animation'})
    check('no new approvals or publishing',data['new_artifact_approvals']==[] and data['publishing_authorized'] is False)
    interpreter=REPO/'.venv/bin/python'
    article_check=subprocess.run([str(interpreter) if interpreter.exists() else sys.executable, str(ROOT/'blog/evidence/verify.py')],text=True,capture_output=True)
    check('portable article provenance',article_check.returncode==0)
    routes={}
    for packet in sorted((ROOT/'requests').glob('*.json')):
        result=subprocess.run([str(interpreter) if interpreter.exists() else sys.executable,str(REPO/'engine/scripts/specialist_route.py'),'route',str(packet),'--workspace',str(ROOT.parent)],text=True,capture_output=True)
        check('source route '+packet.stem,result.returncode==0)
        routes[packet.stem]=json.loads(result.stdout)
    for binding_file in sorted((ROOT/'bindings').glob('*.json')):
        binding=json.loads(binding_file.read_text());expected=binding.pop('sha256')
        actual=sha256(json.dumps(binding,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
        check('binding digest '+binding['asset_id'],expected==actual)
        for record in binding['files']:
            path=(ROOT/record['path']).resolve()
            check('bound file '+record['path'],ROOT in path.parents and path.is_file() and digest(path)==record['sha256'])
        row=next(a for a in data['assets'] if a['id']==binding['asset_id'])
        check('review matches binding '+binding['asset_id'],row['sha256']==expected and row['version']==binding['version'] and row['context_digest']==binding['context_digest'])
        lane='email_segments' if row['id'].startswith('email-') else {'popup':'in_app_popup','campaign':'campaign_plan'}.get(row['id'],row['id'])
        check('review context '+row['id'],row['context_digest']==routes[lane]['context_digest'])
    email=json.loads((ROOT/'email/emails.json').read_text())
    check('five exact segments',[v['id'] for v in email['variants']]==SEGMENTS)
    bodies=['\n'.join(p['text'] for p in v['paragraphs']) for v in email['variants']]
    check('five different email bodies',len(set(bodies))==5)
    valid_claims={c['id'] for c in json.loads((ROOT.parent/'00_baseline/claim-ledger.json').read_text())['claims']}
    for v in email['variants']:
        check('subject and preheader '+v['id'],bool(v['subject'] and v['preheader'] and v['subject']!=v['preheader']))
        check('email CTA '+v['id'],v['cta']=={'label':'Join the waitlist','url':'https://tixmancer.xyz'})
        check('email claim IDs '+v['id'],all(set(p['claim_ids'])<=valid_claims for p in v['paragraphs']))
        check('no new email approval '+v['id'],email['review_notes']['human_approved'] is False and email['review_notes']['sent'] is False)
    calendar=json.loads((ROOT/'campaign/calendar.json').read_text())
    all_ids={a['id'] for a in data['assets']}|{s['id'] for s in calendar['social_drafts']}
    check('calendar uses known assets',all(set(s['asset_ids'])<=all_ids for s in calendar['slots']))
    check('calendar is unscheduled',calendar['permissions']['scheduled'] is False)
    check('X copy fits 280 characters',all(len(s['text'])<=280 for s in calendar['social_drafts'] if s['channel']=='X'))
    manifest_path=ROOT/'PACKAGE-MANIFEST.json'
    current=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files()]
    if args.write_manifest:
        manifest_path.write_text(json.dumps({'schema_version':'campaign-file-manifest/v1','campaign_id':data['campaign_id'],'scope':'01_channel_run; source baseline checked through portable request routes','excluded':['PACKAGE-MANIFEST.json (self)','routing/*.json (host-local regenerated receipts)','__pycache__/'],'files':current},indent=2)+'\n')
    saved=json.loads(manifest_path.read_text())
    check('complete current file manifest',saved['files']==current)
    print(json.dumps({'status':'pass','checks_passed':len(checks),'manifest_files':len(current),'human_approval':False,'external_execution_tested':False},indent=2))


if __name__=='__main__':
    main()
