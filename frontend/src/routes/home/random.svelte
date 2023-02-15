<script>
	import { onMount } from 'svelte';
	let random = 'N/A';

	async function getRandomTweet() {
		const response = await fetch('http://localhost:8080/api/tweets/random');
		const responseJSON = await response.json();
		console.log(responseJSON);
		random = responseJSON['tweet'];
	}
</script>

<main>
	<button
		class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
		on:click={getRandomTweet}>Get Random Tweet</button
	>
	<p>{random}</p>
</main>
