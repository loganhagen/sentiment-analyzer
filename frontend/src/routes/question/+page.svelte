<script>
	import { onMount } from 'svelte';
	let question = "";
	let answer = "";

	async function askQuestion () {
		let response;

		try {
			response = await fetch('http://localhost:8080/api/question?' + new URLSearchParams({"q" : question}));
		} catch (error) {
			console.log("Failed API call.");
		}

		if (response?.ok) {
			let json = await response.json();
			answer = json["choices"][0]["text"];
		} else {
			console.log(`HTTP response code: ${response?.status}`);
		}
	}
</script>

<main>
	<p>Q & A (Powered By OpenAI)</p>
	<input bind:value={question} placeholder="Your question here...">
	<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg" 
	on:click={askQuestion}>Ask!
	</button>
	<p>{answer}</p>
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
