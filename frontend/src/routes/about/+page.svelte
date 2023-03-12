<script>
	import { onMount } from 'svelte';
	let about = "Generating...";

	onMount (async function () {
		const response = await fetch('http://localhost:8080/api/about');
		const responseJSON = await response.json();

		about = responseJSON["choices"][0]["text"]
	});
</script>

<main>
	<h1 class="px-2 py-4 text-4xl text-slate-500">About Universal Basic Income</h1>
	<p>{about}</p>
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
