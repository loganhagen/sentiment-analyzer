<script lang="ts">
	import { onMount } from 'svelte';
	import type { Plot, Post } from '../../types';
	import { sharedPlot, sharedPost } from './store';
	import Plotly, { type Root } from 'plotly.js-dist-min';

	//initialize variables
	let plot: Plot;
	let plot_div: Root;
	let post: Post;

	//Disables the intrusive plotly toolbar
	const config = {
		displayModeBar: false
	};

	//Access plot from store whenever the data is changed
	sharedPlot.subscribe((data) => {
		plot = data;
		if (plot_div != undefined || plot_div != null) {
			/* eslint-disable */
			Plotly.purge(plot_div);
			//THIS LINE HAS TO STAY LIKE THIS, EVEN IF THERE IS A RED SQUIGGLED LINE
			Plotly.react(plot_div, plot.data, plot.layout, config);
			/* eslint-enable */
		}
	});

	//Get post data from store whenever the data is changed
	sharedPost.subscribe((data) => {
		post = data;
	});

	//Load plot on component mount in slot
	onMount(() => {
		//If page is being loaded for the first time or nothing exists in store memory, don't draw a plot
		if (post.text != 'N/A' && post.date != 'N/A') {
			if (plot_div != undefined && plot_div != null) {
				/* eslint-disable */
				Plotly.react(plot_div, plot.data, plot.layout, config);
				Plotly.redraw(plot_div);
				/* eslint-enable */
			}
		}
	});
</script>

<div class="shadow-lg px-4" id="plot_div" bind:this={plot_div}>
	<!-- Plotly chart will be drawn inside this DIV -->
</div>
