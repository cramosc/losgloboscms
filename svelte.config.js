import adapter from '@sveltejs/adapter-static';
import preprocess from 'svelte-preprocess';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: preprocess(),

	kit: {
		adapter: adapter({ pages: 'out' }),
		prerender: {
			default: true
		},
		trailingSlash: 'always',
		browser: {
			router: false
		}
	}
};

export default config;