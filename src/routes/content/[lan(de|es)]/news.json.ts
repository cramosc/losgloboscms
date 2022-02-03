import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { marked } from 'marked';

export function get(req, res, next) {
    const { lan } = req.params;
    const lanStr = { 'de': 'german', 'es': 'spanish' }[lan];

    const content = fs.readFileSync(path.join(process.cwd(), 'content', 'news.yml'), { encoding: 'utf-8' });
    const data = matter(`---\n${content}\n---`).data;
    const news = data.news.map(n => marked(n[lanStr]));

    res.writeHead(200, {
        'Content-Type': 'application/json'
    });

    res.end(JSON.stringify(news));
}