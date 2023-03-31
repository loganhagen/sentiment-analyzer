<script lang="ts">
	import type { Post } from '../../types';
	import { sharedPost } from './store';

	let post: Post;
	let visible = false;

	//Access post from store whenever the data is changed
	sharedPost.subscribe((data) => {
		post = data;
	});

	function toggleVibility() {
		visible = !visible;
	}
</script>

<div class="rounded max-w-5xl max-y-2 overflow-hidden shadow-lg bg-slate-100 space-y-2 px-4 py-4">
	<p>{post.text}</p>
	<p class="text-left font-bold">Date: {post.date}</p>
	{#if post.type == 'tweet'}
		<p class="text-left font-bold">Source: Twitter</p>
		<p class="text-left underline">
			<a href="//twitter.com/user/status/{post.id}" target="_blank" rel="noreferrer">Link to post</a
			>
		</p>
	{:else if post.type == 'reddit'}
		<p class="text-left font-bold">Source: Reddit</p>
		<p class="text-left underline">
			<a
				href="//reddit.com/r/basicincome/comments/{post.id}/{post.text}"
				target="_blank"
				rel="noreferrer">Link to post</a
			>
		</p>
		<button
			on:click={toggleVibility}
			type="button"
			class="left: 0.25rem text-xs text-blue-700 hover:text-white border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center mr-2 mb-2 dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:hover:bg-blue-500 dark:focus:ring-blue-800"
		>
			Show/Hide Comments({post.comments.length})
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
	{:else}
		<p class="text-left font-bold">Source: N/A</p>
	{/if}
</div>
