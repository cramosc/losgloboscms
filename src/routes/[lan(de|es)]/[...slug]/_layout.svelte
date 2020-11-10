<script context="module" lang="ts">
    export async function preload({ params }) {
        const { lan, slug } = params;
        const contentUrl = `/content/${lan}`;
        const path = slug.join('/');

        const layout = await this.fetch(`${contentUrl}/layout.json`).then((r) => r.json());
        const news = await this.fetch(`${contentUrl}/news.json`).then((r) => r.json());
        const sitemap = await this.fetch(`${contentUrl}/sitemap.json`).then((r) => r.json());
        const links = (sitemap[path] || []).map(([link, menu]) => ({
            link: `${path}/${link}`,
            menu,
        }));
        const homeLinks = sitemap[''].map(([link, menu]) => ({ link, menu }));

        return { lan, links, path, homeLinks, layout, news };
    }
</script>

<script lang="ts">
    export let lan: string;
    export let links: any[];
    export let homeLinks: any[];
    export let path: string;
    export let layout: { [key: string]: string };
    export let news: string[];

    import News from '../../../components/News.svelte';
    import Nav from '../../../components/Nav.svelte';

    let menuOpen = false;
</script>

<Nav {lan} {homeLinks} {path} bind:menuOpen />

<News {lan} {news} />

<div class="content-wrapper" class:hide-content={menuOpen}>
    <div class="content-container">
        <img src="http://losglobos.de/img/homepage.jpg" alt="Los Globos" />
        <div class="quote">{layout.quote}</div>
        <main class="content">
            <slot />
            <nav>
                {#each links as { link, menu }}
                    <a class:selected={link === path} href={`${lan}/${link}`}>{menu}</a>
                {/each}
            </nav>
        </main>
    </div>
</div>

<style>
    .quote {
        font-family: 'Amatica SC', cursive;
        font-size: 20px;
        text-align: center;
        font-weight: 700;
        color: #8a78aa;
        padding: 0 8px 20px;
        background-color: #fff9d7;
    }
    .content-container {
        max-width: 1000px;
        margin: auto;
    }
    img {
        width: 100%;
    }
    .content {
        padding: 32px;
        background-color: white;
    }

    .content-wrapper {
        margin-left: 160px;
        background-color: #ebf47d;
        min-height: 100vh;
    }
    nav a {
        display: block;
        margin: 0 0 8px;
        padding: 16px 8px;
        background-color: #c2da78;
        color: #49474a;
        border-radius: 4px;
        text-decoration: none;
        cursor: pointer;
        font-size: 16px;
        font-weight: 700;
    }
    nav a:hover {
        background-color: #ff8200;
        color: #49474a;
    }

    @media (max-width: 800px) {
        .content-wrapper {
            margin-left: 0;
            min-height: calc(100vh - 80px);
        }
        .content {
            padding: 16px;
        }
        .hide-content {
            max-height: calc(100vh - 80px);
            overflow-y: hidden;
        }
    }
</style>
