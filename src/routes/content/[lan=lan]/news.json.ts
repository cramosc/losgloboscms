import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { marked } from 'marked';

export function get({ params }) {
    const { lan } = params;
    const lanStr = { 'de': 'german', 'es': 'spanish' }[lan];

    const content = fs.readFileSync(path.join(process.cwd(), 'content', 'news.yml'), { encoding: 'utf-8' });
    const data = matter(`---\n${content}\n---`).data;
    const news = data.news.map(n => marked(n[lanStr]));

    return {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(news)
    }
}