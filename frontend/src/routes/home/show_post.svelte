<script lang="ts">
	import type { Post } from '../../types';
	import { sharedPost } from './store';

	let post: Post;

	//Access post from store whenever the data is changed
	sharedPost.subscribe((data) => {
		post = data;
	});
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
	{:else}
		<p class="text-left font-bold">Source: N/A</p>
	{/if}
</div>
