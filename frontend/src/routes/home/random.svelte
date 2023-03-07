<script lang="ts">
	import { onMount } from 'svelte';
	import { getRandomPost, getSentimentPlot, cur_post, cur_plot } from './+page.svelte';

	//set post_text for when page loads
	let post_text: string = cur_post.post_text;

	//plot_div is where our plot exists in the DOM
	let plot_div: object;
	let plot_data: object;
	let plot_layout: object;

	//Disables the intrusive plotly toolbar
	const config = {
		displayModeBar: false
	};

	//Set the text on the page to match the post when the page loads.
	onMount(async function () {
		//Get a random post from the backend and set the text
		await getRandomPost();
		post_text = cur_post.post_text;

		//Get sentiment analysis plot from backend and get plot data and layout
		await getSentimentPlot();
		plot_data = cur_plot.data;
		plot_layout = cur_plot.layout;

		//make sure plot div exists
		if (plot_div != undefined || plot_div != null) {
			//THIS LINE HAS TO STAY LIKE THIS, EVEN IF THERE IS A RED SQUIGGLED LINE
			/* eslint-disable */
			Plotly.react(plot_div, plot_data, plot_layout, config);
			/* eslint-enable */
		}
	});

	//Get a new random tweet and set the text on the page to match the tweet.
	//The post is saved in ./+page.svelte as 'cur_post' which can be imported into different files.
	async function ButtonUpdateComponent() {
		//Update Post Text
		await getRandomPost();
		post_text = cur_post.post_text;

		//Update Sentiment Plot
		await getSentimentPlot();
		plot_data = cur_plot.data;
		plot_layout = cur_plot.layout;

		//Make sure plot div exists
		if (plot_div != undefined || plot_div != null) {
			//remove previous plot and then add new plot
			/* eslint-disable */
			Plotly.purge(plot_div);
			//THIS LINE HAS TO STAY LIKE THIS, EVEN IF THERE IS A RED SQUIGGLED LINE
			Plotly.react(plot_div, plot_data, plot_layout, config);
			/* eslint-enable */
		}
	}
</script>

<svelte:head>
	<script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head>

<main>
	<div>
		<button
			class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
			on:click={ButtonUpdateComponent}
		>
			Get Random Post
		</button>

		<p>{post_text}</p>
	</div>

	<div id="plotly">
		<!-- This is where we draw our plot, anything interactive that has an effect on the plot should probably exist within this div -->
		<div id="plot_div" bind:this={plot_div}>
			<!-- Plotly chart will be drawn inside this DIV -->
		</div>
	</div>
</main>
