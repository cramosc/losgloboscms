import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

export function get(req, res, next) {
    const { lan } = req.params;
    const lanStr = { 'de': 'german', 'es': 'spanish' }[lan];

    const content = fs.readFileSync(path.join(process.cwd(), 'content', 'layout.yml'), { encoding: 'utf-8' });
    const data = matter(`---\n${content}\n---`).data;
    const layout = Object.entries(data)
        .map(([k, v]) => [k, v[lanStr]])
        .reduce((o, [k, v]) => ({ ...o, [k]: v }), {});

    res.writeHead(200, {
        'Content-Type': 'application/json'
    });

    res.end(JSON.stringify(layout));
}