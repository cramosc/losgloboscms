import json
import requests
import sys


def main():
    spreadsheetID = '16kX9l1AO9-F1LeztEwwXjaMs163kfwlCxEY_GZ_QNZM'
    response = requests.request(
        'GET',
        'https://spreadsheets.google.com/feeds/list/' + spreadsheetID + '/od6/public/values?alt=json'
    )
    data = response.json()

    jsons = {}

    for row in data['feed']['entry']:
        key = row['gsx$key']['$t']
        es = row['gsx$es']['$t']
        de = row['gsx$de']['$t']

        if key.endswith('_body'):
            k = key[:-5]
            if k not in jsons:
                jsons[k] = {}
            jsons[k]['title'] = k
            jsons[k]['body_de'] = de
            jsons[k]['body_es'] = es

        elif key.endswith('_title'):
            k = key[:-6]
            if k not in jsons:
                jsons[k] = {}
            jsons[k]['title'] = k
            jsons[k]['title_de'] = de
            jsons[k]['title_es'] = es

        else:
            if key not in jsons:
                jsons[key] = {}
            jsons[key]['title'] = key
            jsons[key]['menu_de'] = de
            jsons[key]['menu_es'] = es

    for key, content in jsons.items():
        with open('../_sections/{}{}.json'.format(key, ''), 'w', encoding='utf-8') as file:
            j = json.dumps(content, ensure_ascii=False)
            file.write(j)

if __name__ == '__main__':
    sys.exit(main())
