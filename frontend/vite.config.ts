import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const { PUBLIC_SERVER_PORT, PUBLIC_SERVER_HOST } = process.env;
const proxyTarget = `${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}`;

const config: UserConfig = {
	plugins: [sveltekit()],
	test: {
		globals: true,
		include: ['src/**/*.{test,spec}.{js,ts}'],
		environment: 'jsdom',
		setupFiles: ['src/test/setupTest.ts']
	},
	server: {
		proxy: {
			'/api': {
				target: proxyTarget,
				changeOrigin: true
			}
		},
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
