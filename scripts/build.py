import json
import sys
import os
import markdown2

from os.path import dirname, abspath, join

ROOT_DIR = dirname(dirname(abspath(__file__)))

SECTIONS_DIR = join(ROOT_DIR, '_sections')
JSON_FILE = join(ROOT_DIR, 'dist', 'l10n.json')


def main():
    l10n = {'es': {'job_sections': {}}, 'de': {'job_sections': {}}}
    for file in os.listdir(SECTIONS_DIR):
        if file.endswith('.json'):
            with open(os.path.join(SECTIONS_DIR, file), 'r') as f:
                section=json.load(f)
                key = section['title']

                for lan in 'de', 'es':
                    menu = section[f'menu_{lan}']
                    title = section.get(f'title_{lan}', '')
                    body = section.get(f'body_{lan}', '')
                    body = markdown2.markdown(body.strip())

                    if key.startswith('job_'):
                        l10n[lan]['job_sections'][key[len('job_'):]] = {
                            'menu': menu,
                            'title': title,
                            'body': body
                        }
                    else:
                        l10n[lan][key] = menu
                        l10n[lan][f'{key}_title'] = title
                        l10n[lan][f'{key}_body'] = body

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        f.write(json.dumps(l10n, ensure_ascii=False))


if __name__ == '__main__':
    sys.exit(main())
