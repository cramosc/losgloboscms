import path from 'path';
import matter from 'gray-matter';
import fs from 'fs';

export function get(req, res, next) {
    const { lan } = req.params;

    const dirPath = path.join(process.cwd(), 'content', 'pages', lan);

    const sitemap = fs.readdirSync(dirPath, 'utf-8')
        .filter(f => path.extname(f) === '.md')
        .map(f => [path.parse(f).name.split('_'), matter.read(path.join(dirPath, f)).data] as [string[], any])
        .sort(([_, d1], [__, d2]) => d1.order - d2.order)
        .map(([p, { menu }]) => [p, menu] as [string[], string])
        .map(([p, menu]) => [p.pop(), p.join('/'), menu])
        .reduce((o, [s, k, menu]) => ({
            ...o,
            [k]: [...(o[k] || []), [s, menu]]
        }), {});

    res.writeHead(200, {
        'Content-Type': 'application/json'
    });

    res.end(JSON.stringify(sitemap));
}