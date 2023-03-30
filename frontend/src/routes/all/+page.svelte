<script lang="ts">
	import { onMount } from 'svelte';

	let posts = [];

	onMount(async () => {
		const response = await fetch('/api/posts/tweets');
		const json = await response.json();
		posts = JSON.parse(json)['data'];
	});
</script>

<main>
	<div class="space-y-2 px-0">
		{#each posts as post, i}
			<div
				class="rounded max-w-5xl max-y-2 overflow-hidden shadow-lg bg-slate-100 space-y-2 px-4 py-4"
			>
				<br />
				<h1 class="text-left font-bold">Post #{i + 1}</h1>
				<p>"{post.content}"</p>
				<p class="text-left font-bold">Date: {post.created_at}</p>
				<p class="text-left font-bold">ID: {post._id}</p>
				<p class="text-left underline">
					<a href="//twitter.com/user/status/{post._id}" target="_blank" rel="noreferrer"
						>Link to post</a
					>
				</p>
			</div>
		{:else}
			<p>Loading...</p>
		{/each}
		<div />
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
