<script lang="ts">
	import type { Interaction } from '../../types';

	// Array to hold all interactions between the user and AI.
	let interactions: Interaction[] = [];

	async function askQuestion(question: string) {
		const response = await fetch('/api/ask?' + new URLSearchParams({ q: question }));
		const json = await response.json();

		if (response.ok) {
			let answer: string = json['choices'][0]['text'];
			interactions.push({question, answer});
			interactions = interactions;
		}
	}

	async function handleClick() {
		let question: string = (<HTMLInputElement>document.getElementById('textinput1')).value;
		await askQuestion(question);
	}

</script>

<main>
	<h1 style="font-size:150%;">Q & A (Powered By OpenAI)</h1>
	<input placeholder="Your question here..." size="32" id="textinput1"/>
	<button
		class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg"
		on:click={handleClick}
		>Ask!
	</button>
	<!-- Prints the array of interactions as it is updated. Since the array is empty on page load, nothing is printed.
	I would like some kind of loading action to appear on button click.  -->
	{#each interactions as interaction, i}
		<div class="rounded max-w-5xl max-y-2 overflow-hidden shadow-lg bg-slate-100 space-y-2 px-4 py-4">
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