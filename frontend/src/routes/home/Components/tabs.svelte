<script lang="ts">
	import RandomPost from './RandomPost.svelte';
	import DataSentiment from './DataSentiment.svelte';
	import { sharedPost, sharedPlot, sharedTab } from '../store';

	//represents the current state of the switch tab
	let switched: boolean;

	//update switched value whenever the store is updated
	sharedTab.subscribe((data) => {
		switched = data;
	});
</script>

<main>
	<!-- If switched == true, load random post tab -->
	{#if switched}
		<RandomPost post_store={sharedPost} plot_store={sharedPlot} />
		<!-- else, load DataSentiment tab -->
	{:else}
		<DataSentiment />
	{/if}
</main>
