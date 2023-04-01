<script lang="ts">
	import type { Interaction } from '../../types';

	let interactions: Interaction[] = [];
	var question = '';

	async function askQuestion() {
		document.getElementById('textinput1').value = '';
		let response;

		try {
			response = await fetch('/api/ask?' + new URLSearchParams({ q: question }));
		} catch (error) {
			console.log('Failed API call.');
		}

		if (response?.ok) {
			let json = await response.json();
			let answer = json['choices'][0]['text'];
			interactions.push({ question, answer });
			interactions = interactions;
		} else {
			console.log(`HTTP response code: ${response?.status}`);
		}
	}
</script>

<main>
	<h1 style="font-size:150%;">Q & A (Powered By OpenAI)</h1>

	<input bind:value={question} placeholder="Your question here..." size="32" id="textinput1" />
	<button
		class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg"
		on:click={askQuestion}
		>Ask!
	</button>
	{#each interactions as interaction, i}
		<div
			class="rounded max-w-5xl max-y-2 overflow-hidden shadow-lg bg-slate-100 space-y-2 px-4 py-4"
		>
			<p style="color:Gray">{interaction.question}</p>
			<p>{interaction.answer}</p>
		</div>
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
