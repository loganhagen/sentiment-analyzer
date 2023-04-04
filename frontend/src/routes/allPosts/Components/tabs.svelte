<script lang="ts">
	import { sharedTab } from '../store';
	import AllReddit from './all_reddit.svelte';
	import AllTweets from './all_tweets.svelte';

	//represents the current state of the switch tab
	let switched: boolean;

	//update switched value whenever the store is updated
	sharedTab.subscribe((data) => {
		switched = data;
	});
</script>

<main>
	<!-- If switched == true, load tweet post tab -->
	{#if switched}
		<AllTweets />
		<!-- else, load reddit post tab -->
	{:else}
		<AllReddit />
	{/if}
</main>
