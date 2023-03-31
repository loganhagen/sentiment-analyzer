<script lang="ts">
	type Interaction = {
		question: string,
		answer: string,
	};

	let interactions: Interaction[] = [];
	let question = '';
	let answer = '';

	async function askQuestion() {
		document.getElementById('textinput1').value = "";
		let response;

		try {
			response = await fetch('/api/ask?' + new URLSearchParams({ q: question }));
		} catch (error) {
			console.log('Failed API call.');
		}

		if (response?.ok) {
			let json = await response.json();
			answer = json['choices'][0]['text'];
			interactions.push({question, answer});
			console.log(interactions);
		} else {
			console.log(`HTTP response code: ${response?.status}`);
		}
	}
</script>

<main>
	<h1 style="font-size:150%;">Q & A (Powered By OpenAI)</h1>
	
	<input bind:value={question} placeholder="Your question here..." size="32" id="textinput1"/>
	<button
		class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg"
		on:click={askQuestion}
		>Ask!
	</button>
	{#if answer}
		<div>
			<p class="rounded max-w-5xl max-y-2 overflow-hidden shadow-lg bg-slate-100 space-y-2 px-4 py-4">{answer}</p>
		</div>
	{/if}
	{#each interactions as interaction}
		<p>{interaction.question}</p>
		<p>{interaction.answer}</p>
	{/each}
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
