from datetime import datetime, timedelta
import json
import requests # python3 -m pip install requests
import yaml # python3 -m pip install pyyaml

repo='https://<some-helm-chart-repo>/index.yaml'
teams_webhook_url='https://somecompany.webhook.office.com/...'
response=requests.get(repo,auth=('<username>','<pass>'))
now = datetime.utcnow()
index=response.text
idxdict=yaml.safe_load(index)
apps=list(idxdict['entries'].keys())
for app in apps:
    created = idxdict['entries'][app][0]['created']
    created_iso = datetime.fromisoformat(created[:created.find('.')+7])
    if now - created_iso < timedelta(minutes=10):
    #if True:
        print('New release!!')
        version = idxdict['entries'][app][0]['version']
        jsondata = {'@type': 'MessageCard', '@context': 'http://schema.org/extensions', 'themeColor': '0076D7', 'summary': 'New release!', 'sections': [{'activityTitle': 'New release available! ' + app, 'activitySubtitle': version, 'activityImage': 'https://helm.sh/img/helm.svg', 'facts': [{'name': 'Software', 'value': app}, {'name': 'Version', 'value': version}, {'name': 'Released', 'value': created_iso.isoformat()+'Z'}], 'markdown': True}]}
        # send webhook with json payload
        requests.post(teams_webhook_url, json=jsondata)
        #print(json.dumps(jsondata))
