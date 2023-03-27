<script lang="ts">
	import { onMount } from 'svelte';
	let totalPosts = 0;

	const sizeEndpoint = '/api/tweets/size';
	onMount(async function () {
		const sizeResponse = await fetch(sizeEndpoint);
		const sizeJSON = await sizeResponse.json();
		totalPosts = sizeJSON['size'];
	});
</script>

<main>
	<p class="px-2">Total Posts: {totalPosts}</p>
</main>
