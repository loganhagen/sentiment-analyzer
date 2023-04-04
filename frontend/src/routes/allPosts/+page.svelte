<script lang='ts'>
	import Switch from "../../Components/switch.svelte";
	import { sharedTab } from "./store";
	import Tabs from "./Components/tabs.svelte";

	//The value of switched represents which tab we are on, but techincally in this case we only care about when it is updated, not its value
	let switched: boolean;

	//update switched value whenever the store is updated
	sharedTab.subscribe((data) => {
		switched = data;
	});
</script>


<main>
	<div class="space-y-2 px-0">
		<Switch store={sharedTab} options={["Twitter", "Reddit"]}/>
		<!-- Update page if switched bool is changed at any point -->
		{#key switched}
			<Tabs />
		{/key}
	</div>
</main>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.white);
	}
	div {
		text-align: center;
		padding: 1em;
		max-width: 1000px;
		margin: 0 auto;
	}
</style>
