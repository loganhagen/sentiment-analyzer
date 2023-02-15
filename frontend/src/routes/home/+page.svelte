<script>
	import { onMount } from 'svelte';
	import Size from './size.svelte';
	import Random from './random.svelte';
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
