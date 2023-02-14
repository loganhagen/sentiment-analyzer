<script>
	import { onMount } from 'svelte';
	let totalPosts = -1;
	let random = 'N/A';

	const sizeEndpoint = 'http://127.0.0.1:8080/api/tweets/size';
	onMount(async function () {
		const sizeResponse = await fetch(sizeEndpoint);
		const sizeJSON = await sizeResponse.json();
		totalPosts = sizeJSON['size'];
	});

	async function getRandomTweet() {
		const response = await fetch('http://127.0.0.1:8080/api/tweets/random');
		const responseJSON = await response.json();
		console.log(responseJSON);
		random = responseJSON['tweet'];
	}
</script>

<main>
	<h1 class="px-2 py-4 text-4xl text-slate-500">Universal Basic Income</h1>
	<p class="px-2">Total Posts: {totalPosts}</p>
	<button
		class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
		on:click={getRandomTweet}>Get Random Tweet</button
	>
	<p>{random}</p>
</main>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.white);
	}
	main {
		text-align: center;
		padding: 1em;
		max-width: 1000px;
		margin: 0 auto;
	}
</style>
