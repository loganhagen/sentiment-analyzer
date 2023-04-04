<script lang="ts">
	//This component is a toggle between two different states (in our case we are using this to tab between pages within the same route)

	import type { Writable } from 'svelte/store';

	export let store: Writable<boolean>;
	export let options: Array<string> = ['On', 'Off'];
	export let switched = true;

	//update switched value whenever the store is updated
	store.subscribe((data) => {
		switched = data;
	});

	export function handleClick() {
		store.set(!switched);
	}
</script>

<main>
	<button class="py-4" on:click={handleClick}>
		{#if switched}
			<span
				class="text-white font-bold py-2 px-4 rounded-l-md dark:bg-blue-500 peer-checked:dark:bg-gray-300"
				>{options[0]}</span
			>
			<span
				class="text-gray-700 font-bold py-2 px-4 shadow-lg rounded-r-md dark:bg-gray-300 peer-checked:dark:bg-blue-500"
				>{options[1]}</span
			>
		{:else}
			<span
				class="text-gray-700 font-bold py-2 px-4 rounded-l-md dark:bg-gray-300 peer-checked:dark:bg-blue-500"
				>{options[0]}</span
			>
			<span
				class="text-white font-bold py-2 px-4 shadow-lg rounded-r-md dark:bg-blue-500 peer-checked:dark:bg-gray-300"
				>{options[1]}</span
			>
		{/if}
	</button>
</main>
