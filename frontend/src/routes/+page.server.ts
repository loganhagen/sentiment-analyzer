import { redirect } from '@sveltejs/kit';

// If anyone tries to access the frontend from the URL with no route, they are redirected to
export const load = () => {
	throw redirect(302, '/home');
};
