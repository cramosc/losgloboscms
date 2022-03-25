<script context="module" lang="ts">
    export async function load({ params, fetch }) {
        const { lan, slug } = params;
        const contentUrl = `/content/${lan}`;
        const path = slug.replace(/\/$/, '');
        const props = await fetch(`${contentUrl}/${path}.json`).then((r) => r.json());
        return { props };
    }
</script>

<script lang="ts">
    import { afterUpdate } from 'svelte';

    export let content: string;
    export let data: { title: string };

    let contentNode: HTMLElement;

    afterUpdate(() => {
        Array.from(contentNode.getElementsByTagName('img'))
            .map((n) => n.parentNode)
            .filter((n: Element) => n.tagName === 'P')
            .forEach((n: HTMLElement) => (n.style.display = 'flex'));
    });
</script>

{#if data.title}
    <h1>{data.title}</h1>
{/if}

<div bind:this={contentNode}>
    {@html content}
</div>

<style>
    div :global(table),
    div :global(th),
    div :global(td) {
        border: 1px solid black;
    }
    div :global(table) {
        border-collapse: collapse;
    }
    div :global(th),
    div :global(td) {
        padding: 4px;
    }
    h1,
    div :global(h1),
    div :global(h2),
    div :global(h3),
    div :global(h4) {
        color: #ff8200;
        font-weight: bold;
        margin: 32px 0;
    }
    h1,
    div :global(h1),
    div :global(h2) {
        font-size: 1.2em;
    }
    div :global(img) {
        margin: auto;
        max-width: 100%;
    }
</style>
