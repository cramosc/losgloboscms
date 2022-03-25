import path from 'path';
import matter from 'gray-matter';
import { marked } from 'marked';

export function get({ params }) {
    const { lan, slug } = params;
    const filename = `${slug.replace(/\/$/, '').replace(/\//g, '_')}.md`

    const parsed = matter.read(path.join(process.cwd(), 'content', 'pages', lan, filename));

    return {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: parsed.data, content: marked(parsed.content) })
    }
}