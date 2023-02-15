<script>
	import { onMount } from 'svelte';
	let totalPosts = -1;

	const sizeEndpoint = 'http://127.0.0.1:8080/api/tweets/size';
	onMount(async function () {
		const sizeResponse = await fetch(sizeEndpoint);
		const sizeJSON = await sizeResponse.json();
		totalPosts = sizeJSON['size'];
	});
</script>

<main>
	<p class="px-2">Total Posts: {totalPosts}</p>
</main>
