<script>
	import { onMount } from 'svelte';
	let about = "Generating...";
	let input = "";
	let result = "";
	let answer = "";

	async function askQuestion () {
		const res = await fetch('http://localhost:8080/api/question', {
			method: 'POST',
			body: JSON.stringify({
				input,
			}),
			headers: {
				"Content-type" : "application/json"
			}
		})
		.then((response) => response.json())
  		.then((json) => answer = json["choices"][0]["text"]);
	}

</script>

<main>
	<p>Q & A (Powered By OpenAI)</p>
	<input bind:value={input} placeholder="Your question here...">
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
