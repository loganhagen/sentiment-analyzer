<svelte:head>
    <title>Q&A</title> 
</svelte:head>

<script lang="ts">
	import type { Interaction } from '../../types';

	// Array to hold all interactions between the user and AI.
	let interactions: Interaction[] = [];

	async function askQuestion(question: string) {
		const response = await fetch('/api/ask?' + new URLSearchParams({ q: question }));
		const json = await response.json();

		if (response.ok) {
			let answer: string = json['choices'][0]['text'];
			interactions.push({ question, answer });
			interactions = interactions;
		}
	}

	async function handleClick() {
		(<HTMLInputElement>document.getElementById('response')).innerHTML = "Generating...";
		let question: string = (<HTMLInputElement>document.getElementById('textarea1')).value;
		await askQuestion(question);
		(<HTMLInputElement>document.getElementById('response')).innerHTML = "";
	}
</script>

<main>
	<h1 style="font-size:150%;">FAQ Chatbot</h1>
	<h2>Powered by OpenAI</h2>
	<hr />
	<div class="textarea1">
		<!-- <input placeholder="Your question here..." size="32" id="textinput1"/> -->
		<textarea
			name="textarea1"
			rows="5"
			cols="50"
			placeholder="Your question here..."
			id="textarea1"
		/>
	</div>
	<!-- {#await promise}
		<p>Generating...</p>
	{/await} -->
	<button
		class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg transform active:scale-75 transition-transform" on:click={handleClick}>
		Ask!
	</button>
	<p id="response"></p>

	<!-- Prints the array of interactions as it is updated. Since the array is empty on page load, nothing is printed.
	I would like some kind of loading action to appear on button click.  -->
	<div class="responseArea">
		{#each interactions as interaction, i}
			<div
				class="rounded max-w-5xl max-y-2 overflow-hidden shadow-lg bg-slate-100 space-y-2 px-4 py-4"
			>
				<p style="color:Gray">{interaction.question}</p>
				<hr />
				<p>{interaction.answer}</p>
			</div>
		{/each}
		<div />
	</div>
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
	h1 {
		margin: 10px;
	}
	.textarea1 {
		margin: 10px;
	}
	textarea {
		outline: 1px solid black;
	}
	.responseArea {
		margin: 10px;
	}
</style>
