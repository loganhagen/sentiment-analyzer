<script context="module" lang="ts">
	import Size from './size.svelte';
	import ShowPost from './show_post.svelte';
	import ShowPlot from './show_plot.svelte';
	import type { Plot, Post } from '../../types';
	import { sharedPost, sharedPlot } from './store';

	// //Create and set current post for the page
	export let cur_post: Post;
	//Create and set current plot for the page
	export let cur_plot: Plot;

	//Subscribe to sharedPost store to update cur_post whenever a new post is stored in sharedPost
	sharedPost.subscribe((post) => {
		cur_post = post;
	});

	//Subscribe to sharedPlot store to update cur_plot whenever a new plot is stored in sharedPost
	sharedPlot.subscribe((plot) => {
		cur_plot = plot;
	});

	// Loads a random tweet into page memory to be accesed under the variable cur_tweet
	export async function getRandomPost() {
		const response = await fetch('/api/tweets/random');
		const responseJSON = await response.json();

		//update our current post
		let post = {
			text: responseJSON['text'],
			id: responseJSON['id'],
			date: responseJSON['date'],
			type: responseJSON['type']
		};

		//Set data in sharedPost store so that the data can be shared between components and pages
		sharedPost.set(post);
	}

	//Loads a plot into page memory to be accesed under the variable cur_plot from cur_post
	export async function getSentimentPlot() {
		//Don't create a plot if there is no post loaded into memory
		if (cur_post.text == 'N/A') return false;

		const response = await fetch('/api/plot/sentiment/tweet/' + cur_post.id);
		const responseJSON = await response.json();

		//Get plot as object
		let plot = JSON.parse(responseJSON);

		//update our current plot
		plot = { data: plot.data, layout: plot.layout };

		//Set data in sharedPlot store so that the data can be shared between components and pages
		sharedPlot.set(plot);
	}

	//Handles updating data when button is pressed
	async function ButtonUpdateComponents() {
		//Update Post Text
		await getRandomPost();

		//Update Sentiment Plot
		await getSentimentPlot();
	}
</script>

<main>
	<h1 class="px-2 py-4 text-4xl text-slate-500">Random Universal Basic Income Post</h1>

	<!-- Page Content Goes In Here -->
	<div class="space-y-2">
		<!-- Update Post and Data Vis -->
		<button
			class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg"
			on:click={ButtonUpdateComponents}
		>
			Get Random Post
		</button>

		<!-- Display size of db -->
		<Size />

		<!-- Show Post Text, Date Posted, and Post Source -->
		<ShowPost />

		<!-- Display Plot from store sharedData -->
		<ShowPlot />
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
</style>
