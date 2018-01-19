import json
import re
import sys
import os

SECTIONS_DIR = '../_sections'
JSON_FILE = '../dist/l10n.json'

def main():

    # data.feed.entry.forEach(function (row) {
    #     var key = row.gsx$key.$t;
    #
    # ['de', 'es'].forEach(function (lan) {
    #     l10n[lan][key] = row['gsx$'+lan].$t.trim();
    #
    # if (key.endsWith('body')) {
    # l10n[lan][key] = ('<p>' + l10n[lan][key].replace(/\n *\n/g, '</p><p>') + '</p>')
    # .replace(/\n/g, '<br>');
    # }
    # });
    # });
    l10n = {'es': {}, 'de': {}}
    for file in os.listdir(SECTIONS_DIR):
        if file.endswith('.json'):
            with open(os.path.join(SECTIONS_DIR, file), 'r') as f:
                section=json.load(f)
                key = section['title']

                for lan in 'de', 'es':
                    l10n[lan][key] = section[f'menu_{lan}']
                    if f'title_{lan}' in section:
                        l10n[lan][f'{key}_title'] = section[f'title_{lan}']
                    if f'body_{lan}' in section:
                        body = section[f'body_{lan}']
                        body = re.sub(r'\n *\n', '</p><p>', body)
                        body = re.sub(r'\n', '<br>', body)
                        l10n[lan][f'{key}_body'] = f'<p>{body}</p>'

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        f.write(json.dumps(l10n, ensure_ascii=False))

if __name__ == '__main__':
    sys.exit(main())
