<script lang="ts">
    export let menuOpen: boolean;
    export let lan: string;
    export let homeLinks: { link: string; menu: string }[];
    export let path: string;

    const switchLanguageString = {
        de: 'Español',
        es: 'Deutsch',
    };
    const swithLanguage = { de: 'es', es: 'de' };
</script>

<div class="header" on:click={() => (menuOpen = false)}>
    <a class="logo" href={`/${lan}/home`}><img src="/img/logo.jpg" alt="Los Globos e.V." /></a>
    <nav class:open={menuOpen}>
        {#each homeLinks as { link, menu }}
            <a class:selected={path.startsWith(link)} href={`/${lan}/${link}`}>{menu}</a>
        {/each}
        <a href={`/${swithLanguage[lan]}/${path}`}>{switchLanguageString[lan]}</a>
    </nav>
    <button type="button" class="navbar-toggle-mobile" on:click|stopPropagation={() => (menuOpen = !menuOpen)}>
        <span class="icon-bar" />
        <span class="icon-bar" />
        <span class="icon-bar" />
    </button>
</div>

<style>
    nav {
        background-color: white;
    }
    nav a {
        display: block;
        padding: 20px 10px;
        color: #ff8200;
        text-decoration: none;
        cursor: pointer;
        font-size: 16px;
        font-weight: 700;
    }
    nav a:hover,
    .selected {
        background-color: #ff8200;
        color: #49474a;
    }
    .header {
        box-sizing: border-box;
        width: 160px;
        padding: 10px;
        background-color: white;
        position: fixed;
        top: 0;
        bottom: 0;
        box-shadow: #dddddd 1px 0px 6px 0;
        overflow-y: auto;
    }
    img {
        height: 60px;
    }
    .icon-bar {
        display: block;
        width: 30px;
        height: 3px;
        border-radius: 2px;
        background-color: #888;
        margin-top: 5px;
    }

    .icon-bar:first-child {
        margin-top: 0;
    }
    .navbar-toggle-mobile {
        display: none;

        background-color: transparent;
        border: 1px solid #ddd;
        border-radius: 4px;
        height: 40px;
        position: absolute;
        top: 20px;
        right: 20px;
    }

    @media (max-width: 800px) {
        .header {
            position: relative;
            top: 0;
            width: 100%;
            bottom: auto;
            height: 80px;
            overflow-y: visible;
        }
        nav {
            position: absolute;
            right: 0;
            top: 80px;
            width: 0;
            overflow-x: hidden;
            transition: width 0.2s ease-in-out;
            min-height: calc(100vh - 80px);
        }
        nav a {
            text-align: center;
        }
        .navbar-toggle-mobile {
            display: block;
        }
        .open {
            width: 100%;
        }
    }
</style>
