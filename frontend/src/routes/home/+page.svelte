<script context="module" lang="ts">
	//import "plotly.js"
	import Size from './size.svelte';
	import Random from './random.svelte';
	import type { Plot, Post } from '../../types.svelte';

	//Create and set current post for the page
	export let cur_post: Post = {
		post_text: 'N/A',
		post_id: NaN,
		post_date: 'N/A',
		post_type: 'N/A'
	};

	//Create and set current plot for the page
	export let cur_plot: Plot = { data: {}, layout: {} };

	// Loads a random tweet into page memory to be accesed under the variable cur_tweet
	export async function getRandomPost() {
		const response = await fetch('http://localhost:8080/api/tweets/random');
		const responseJSON = await response.json();

		//update our current post
		cur_post = {
			post_text: responseJSON['text'],
			post_id: responseJSON['id'],
			post_date: responseJSON['date'],
			post_type: responseJSON['type']
		};

		//solves promise error in dev console
		return true;
	}

	export async function getSentimentPlot() {
		//Don't create a plot if there is no post loaded into memory
		if (cur_post.post_text == 'N/A') return false;

		const response = await fetch(
			'http://localhost:8080/api/plot/sentiment/tweet/' + cur_post.post_id
		);
		const responseJSON = await response.json();

		//Get plot as object
		let plot = JSON.parse(responseJSON);

		//update our current plot
		cur_plot = { data: plot.data, layout: plot.layout };

		return true;
	}
</script>

<main>
	<h1 class="px-2 py-4 text-4xl text-slate-500">Universal Basic Income</h1>
	<Size />
	<Random />
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
