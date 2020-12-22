<script lang="ts">
    export let lan: string;
    export let news: string[];

    let closed = false;
</script>

{#if news && news.length > 0}
    <div class="container" class:closed>
        <div class="news">
            <button on:click={() => (closed = !closed)}>{closed ? '◀' : '▶'}</button>
            <h2>{lan === 'de' ? 'Aktuelles' : 'Novedades'}</h2>
            {#each news as newItem}
                <div class="item">
                    {@html newItem}
                </div>
            {/each}
        </div>
    </div>
{/if}

<style>
    .container {
        position: absolute;
        top: 90px;
        right: 0;
        width: 364px;
        overflow: hidden;
        box-shadow: #696969 -4px 6px 7px 3px;
        border-radius: 4px 0 0 4px;
        transition: width 0.2s ease-out;
    }
    .news {
        width: 364px;
        box-sizing: border-box;
        padding: 32px 16px 16px 32px;
        background-color: #ffa140;
    }
    h2 {
        font-weight: 700;
        font-size: 1em;
    }
    .container.closed {
        width: 32px;
    }
    button {
        position: absolute;
        top: 0;
        left: 0;
        background: transparent;
        border: none;
        cursor: pointer;
        width: 32px;
        height: 100%;
    }
    .item::before {
        content: '';
        display: block;
        width: 100%;
        border-bottom: gray 1px solid;
    }
</style>
