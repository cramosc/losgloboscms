import path from 'path';
import matter from 'gray-matter';
import marked from 'marked';

export function get(req, res, next) {
    const { lan, slug } = req.params;

    const parsed = matter.read(path.join(process.cwd(), 'content', 'pages', lan, slug.filter(x => x).join('_')) + '.md');

    res.writeHead(200, {
        'Content-Type': 'application/json'
    });

    res.end(JSON.stringify({ data: parsed.data, content: marked(parsed.content) }));
}