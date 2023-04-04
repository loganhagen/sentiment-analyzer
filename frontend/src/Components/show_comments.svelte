<script lang="ts">
	import type { Post } from '../types';

	export let post: Post;
	let visible = false;

	//toggle visibility to show the list of comments
	function toggleVibility() {
		visible = !visible;
	}
	1;
</script>

<button
	on:click={toggleVibility}
	type="button"
	class="text-left text-xs text-blue-700 hover:text-white border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 mr-2 mb-2 dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:hover:bg-blue-500 dark:focus:ring-blue-800"
>
	Show/Hide Comments ({post.comments.length})
</button>
{#if visible}
	<ul class="text-left space-y-5 text-gray-500 list-disc list-inside dark:text-gray-400">
		{#each post.comments as comment}
			<li>
				{comment.text}
			</li>
		{/each}
	</ul>
{/if}
