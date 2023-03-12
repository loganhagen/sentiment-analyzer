<script>
	import { onMount } from 'svelte';
	let about = "Generating...";
	let input = "";
	let result = "";
	let answer = "";

	// onMount (async function () {
	// 	const response = await fetch('http://localhost:8080/api/about');
	// 	const responseJSON = await response.json();

	// 	about = responseJSON["choices"][0]["text"]
	// });

	async function askQuestion () {
		const res = await fetch('http://localhost:8080/api/about', {
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
	<!-- <h1 class="px-2 py-4 text-4xl text-slate-500">About Universal Basic Income</h1>
	<p>{about}</p> -->
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
