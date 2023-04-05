<script lang="ts">
	import type { Post } from '../types';
	import ShowComments from './show_comments.svelte';

	export let post: Post;
</script>

<head>
	<title>All Posts</title>
	<meta name="description" content="Put your description here.">
</head>
<body>
	<div class="rounded max-w-5xl max-y-2 overflow-hidden shadow-lg bg-slate-100 space-y-2 px-4 py-4">
		{#if post.type == 'tweet'}
			<img src="src/images/twitter_icon.png" alt="Logo" class="h-8" width="35" height="30"/>
			<p>{post.text}</p>
			<p class="text-left font-bold">Date: {post.date}</p>
			<p class="text-left font-bold">Source: Twitter</p>
			<p class="text-left underline">
				<a href="//twitter.com/user/status/{post.id}" target="_blank" rel="noreferrer">Link to post</a
				>
			</p>
		{:else if post.type == 'reddit'}
			<img src="src/images/reddit_icon.png" alt="Logo" class="h-8" width="35" height="30"/>
			<p>{post.text}</p>
			<p class="text-left font-bold">Date: {post.date}</p>
			<p class="text-left font-bold">Source: Reddit</p>
			<p class="text-left underline">
				<a
					href="//reddit.com/r/basicincome/comments/{post.id}/{post.text}"
					target="_blank"
					rel="noreferrer">Link to post</a
				>
			</p>
	
			<!-- Displays button for showing/hiding comments -->
			<ShowComments {post} />
		{:else}
			<p class="text-left font-bold">No Post Loaded</p>
		{/if}
	</div>
</body>
