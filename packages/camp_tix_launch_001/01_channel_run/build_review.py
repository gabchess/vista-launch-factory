"""Bind the finished local campaign assets to one portable review.

Bindings include the visible rendition, copy and evidence metadata. Review
intent cannot survive a changed source/voice context or a changed rendition.
"""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parent


def load(path):
    return json.loads((ROOT/path).read_text())


def write(path, data):
    dest = ROOT/path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')


def bind(asset_id, paths, context, version):
    records = []
    for path in sorted(paths):
        file = ROOT/path
        if not file.is_file():
            raise FileNotFoundError(file)
        records.append({'path':path,'sha256':sha256(file.read_bytes()).hexdigest()})
    binding = {'schema_version':'asset-review-binding/v1','asset_id':asset_id,'version':version,'context_digest':context,'files':records}
    canonical = json.dumps(binding,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    binding['sha256'] = sha256(canonical).hexdigest()
    write('bindings/'+asset_id+'.json',binding)
    return binding['sha256']


def row(asset_id,label,title,description,kind,preview,source_file,paths,deliverable,claim_ids,job,style_note,review_note,voice, height=920, version=1):
    context=load('routing/'+deliverable+'.json')['context_digest']
    digest=bind(asset_id,paths,context,version)
    return {'id':asset_id,'label':label,'title':title,'description':description,'type':kind,'preview':preview,'source_file':source_file,'version':version,'sha256':digest,'context_digest':context,'claim_ids':claim_ids,'approved':False,'job':job,'style_note':style_note,'review_note':review_note,'voice_path':'voice/'+voice+'.md','preview_height':height,'group':'Ready for review'}


def main():
    assets=[]
    b=load('blog/metadata.json')
    assets.append(row('blog','Blog post',b['title'],'Feature article · '+str(b['estimated_reading_minutes'])+' minute read','iframe','blog/article.html','blog/article.md',['blog/article.md','blog/article.html','blog/metadata.json','blog/provenance.json','blog/assets/tix-hero.png','blog/assets/tix-camera-brief.png'],'blog',['TIX-C01','TIX-C02','TIX-C03','TIX-C04','TIX-C05','TIX-C06','TIX-C07','TIX-C08'],'Help a reader understand the conversation and form a useful buying brief.','Based on four actual Vista Insights articles. Tix remains the product and publisher.','Article, SEO fields and two images are included. Confirm copy and the waitlist destination before publishing.','blog',1200,version=b['version']))
    email=load('email/emails.json')
    for v in email['variants']:
        name=v['id'];ids=sorted(set(c for p in v['paragraphs'] for c in p['claim_ids']))
        a=row('email-'+name,v['label'],v['subject'],v['preheader'],'iframe','email/'+name+'.html','email/'+name+'.md',['email/'+name+'.md','email/'+name+'.html','email/'+name+'.json'],'email_segments',ids,v['reader_job'],'Vista public feature register adapted for email. No private newsletter corpus was supplied.','Audience labels are test contexts. Confirm the real list, waitlist collection and ESP footer before sending.','email',1000,version=v.get('version',email['version']))
        a['group']='Email variants';assets.append(a)
    c=load('changelog/entry.json')
    assets.append(row('changelog','Changelog',c['title'],'Concise product preview update','iframe','changelog/entry.html','changelog/entry.md',['changelog/entry.md','changelog/entry.html','changelog/entry.json','blog/assets/tix-camera-brief.png','popup/assets/Poppins-Regular.ttf','popup/assets/Poppins-SemiBold.ttf'],'changelog',['TIX-C01','TIX-C02','TIX-C03','TIX-C05','TIX-C06','TIX-C08'],'Give returning readers a short account of the preview and a first useful action.','Based on three rendered Vista changelog entries, including the current Vista Home update.','Availability stays qualified as a preview. A public launch date has not been assigned.','changelog',1020,version=c['version']))
    p=load('popup/copy.json')
    assets.append(row('popup','In-app popup',p['copy']['headline'],'Graphic + copy · Desktop and mobile preview','iframe','popup/popup.html','popup/copy.json',['popup/popup.html','popup/graphic.svg','popup/copy.json'],'in_app_popup',['TIX-C01','TIX-C02','TIX-C08'],p['purpose'],'Vista login typography and published palette informed the original popup layout.','The modal is an original design. Review the message and artwork together; production targeting still needs integration.','popup',700,version=p['version']))
    calendar=load('campaign/calendar.json')
    assets.append(row('campaign','Campaign calendar',calendar['title'],'Two proposed weeks · Includes LinkedIn, X and Threads drafts','calendar','campaign/calendar.json','campaign/calendar.csv',['campaign/calendar.json','campaign/calendar.csv'],'campaign_plan',['TIX-C01','TIX-C02','TIX-C03','TIX-C05','TIX-C06','TIX-C08'],'Move from the product story to practical buyer questions, then invite a real brief.','One source, different channel jobs. Dates and times are planning choices for review.','Nothing is scheduled. The social cut and login crop are named dependencies.','campaign',version=calendar['version']))
    assets.extend([
        {'id':'social-video','group':'Approved creative','label':'Product launch video','title':'Dinner with Tix','description':'Approved master · 1920 × 1080 · 55 seconds','type':'video','preview':'/media/film.mp4','source_file':None,'version':3,'sha256':'1e73f611ecaacaa9aabe1b3cfdc53f571888573ae876aebb65674ad2903604d2','context_digest':'accepted-dinner-with-tix-v3','approved':True,'approval_quote':"Love it. It's perfect now.",'note':'The accepted master is preserved. A ≤30-second cut and social crop still need a separate review for the strict Vista social slot.','job':'Show the human situation and the intended Tix buying conversation.','style_note':'Accepted creative from the prior video loop.','review_note':'Actual production used ChatCut, authored HyperFrames scenes and one Higgsfield enhancement. The handoff preserves that provider lineage.'},
        {'id':'animation','group':'Approved creative','label':'Short animation','title':'Tix motion','description':'Approved creative · 1080 × 1080 · 10 seconds','type':'video','preview':'/media/animation.mp4','source_file':None,'version':1,'sha256':'f16b7cfda2d6ef8671fc2add7a404cf77be321dffec56503a1326b387bb7b76a','context_digest':'accepted-tix-motion-v1','approved':True,'approval_quote':"Imho it's ready to ship.",'note':'The accepted animation is preserved. Its login-page placement needs a responsive crop and a separate HTML action.','job':'Introduce Tix in a short visual sequence.','style_note':'Original Tix creative, reviewed and accepted by Gabe.','review_note':'Vista login research is saved for the future surface integration; this accepted square render was not altered.'}
    ])
    data={'schema_version':'campaign-review/v1','campaign_id':'camp_tix_launch_001','product_id':'tixmancer','source_revision':b['source_revision'] if 'source_revision' in b else load('requests/blog.json')['source_revision'],'human_reviewer':'gabe','assets':assets,'calendar':calendar,'new_artifact_approvals':[],'publishing_authorized':False}
    write('review-data.json',data)
    print(f'Bound {len(assets)} review items: {sum(a["approved"] for a in assets)} approved creative, {sum(not a["approved"] for a in assets)} awaiting review.')


if __name__ == '__main__':
    main()
