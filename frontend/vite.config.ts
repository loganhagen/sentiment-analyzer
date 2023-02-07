import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const config: UserConfig = {
	plugins: [sveltekit()],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	},
	server: {
		port: 3000,
		strictPort: true,
		host: true, // needed for docker container
		fs: {
			allow: ['../node_modules'] // Added to fix this issue: https://github.com/sveltejs/kit/issues/2701
		},
		watch: {
			usePolling: true
		}
	}
};

export default config;
