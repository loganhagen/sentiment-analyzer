<script lang="ts">
	import { onMount } from 'svelte';
	import { PUBLIC_API_URL } from '$env/static/public';
	let totalPosts = 0;

	const sizeEndpoint = PUBLIC_API_URL + 'tweets/size';
	onMount(async function () {
		const sizeResponse = await fetch(sizeEndpoint);
		const sizeJSON = await sizeResponse.json();
		totalPosts = sizeJSON['size'];
	});
</script>

<main>
	<p class="px-2">Total Posts: {totalPosts}</p>
</main>
