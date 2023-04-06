<svelte:head>
    <title>Data Visualizations</title> 
</svelte:head>

<script context="module" lang="ts">
	import Switch from '../../Components/switch.svelte';
	import Tabs from './Components/tabs.svelte';
	import { sharedTab } from './store';

	//The value of switched represents which tab we are on, but techincally in this case we only care about when it is updated, not its value
	let switched: boolean;

	//update switched value whenever the store is updated
	sharedTab.subscribe((data) => {
		switched = data;
	});
</script>

<main>
	<!-- Switch Component that allows us to switch between two tabs defined in tabs.svelte -->
	<Switch store={sharedTab} options={['Random Post', 'All Posts']} />

	<!-- Refresh current tab when a change is detected on the above switch -->
	{#key switched}
		<Tabs />
	{/key}
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
