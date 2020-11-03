import json
import sys
import os
import markdown2
import frontmatter
import yaml
from collections import defaultdict

from os.path import dirname, abspath, join

ROOT_DIR = dirname(dirname(abspath(__file__)))

SECTIONS_DIR = join(ROOT_DIR, '_sections')
JSON_FILE = join(ROOT_DIR, 'dist', 'l10n.json')
JS_FILE = join(ROOT_DIR, 'dist', 'l10n.js')

CONTENT_DIR = join(ROOT_DIR, 'content')
CONTENT_DEST_DIR = join(ROOT_DIR, 'dist', 'content')

def create_new_pages():
    for lan in ['de', 'es']:
        directory = join(CONTENT_DIR, 'pages', lan)
        sitemap = defaultdict(list)

        for file in os.listdir(directory):
            path = os.path.splitext(file)[0].split('_')
            page = frontmatter.load(join(directory, file))
            sitemap['/'.join(path[:-1])].append((page.metadata['order'], path[-1], page.metadata['menu']))
            json_str = json.dumps({'data': page.metadata, 'content': markdown2.markdown(page.content, extras=["tables"])}, ensure_ascii=False)
            file_dir = join(CONTENT_DEST_DIR, lan, *path[:-1])
            os.makedirs(file_dir, exist_ok=True)
            with open(join(file_dir, path[-1] + '.json'), 'w') as f:
                f.write(json_str)

        sitemap = {k: [a[1:] for a in sorted(v, key=lambda a: a[0])] for k, v in sitemap.items()}
        with open(join(CONTENT_DEST_DIR, lan, 'sitemap.json'), 'w') as f:
                f.write(json.dumps(sitemap, ensure_ascii=False))

        lang = {'de': 'german', 'es': 'spanish'}[lan]
        with open(join(CONTENT_DIR, 'layout.yml'), 'r') as f:
            data = {k: v[lang] for k, v in yaml.safe_load(f).items()}
        with open(join(CONTENT_DEST_DIR, lan, 'layout.json'), 'w') as f:
            f.write(json.dumps(data, ensure_ascii=False))
        with open(join(CONTENT_DIR, 'news.yml'), 'r') as f:
            data = [markdown2.markdown(n[lang], extras=["tables"]) for n in yaml.safe_load(f)['news']]
        with open(join(CONTENT_DEST_DIR, lan, 'news.json'), 'w') as f:
            f.write(json.dumps(data, ensure_ascii=False))

def main():
    create_new_pages()
    
    l10n = {'es': {'job_sections': {}}, 'de': {'job_sections': {}}}
    for file in os.listdir(SECTIONS_DIR):
        if file.endswith('.json'):
            with open(os.path.join(SECTIONS_DIR, file), 'r') as f:
                section=json.load(f)
                key = section['title']

                for lan in 'de', 'es':
                    menu = section[f'menu_{lan}']
                    title = section.get(f'title_{lan}', '')
                    body = section.get(f'body_{lan}', '').strip()
                    body = body and markdown2.markdown(body, extras=["tables"])

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
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write(f'var l10n = {json.dumps(l10n, ensure_ascii=False)}')


if __name__ == '__main__':
    sys.exit(main())
