<script lang="ts">
	import Size from '../../../Components/size.svelte';
	import ShowPost from '../../../Components/show_post.svelte';
	import ShowPlot from '../../../Components/show_plot.svelte';
	import type { Comment, Plot, Post } from '../../../types';
	import type { Writable } from 'svelte/store';

	export let post_store: Writable<Post>;
	export let plot_store: Writable<Plot>;

	//Create and set current post for the page
	let cur_post: Post;
	//Create and set current plot for the page
	let cur_plot: Plot;

	//Subscribe to sharedPost store to update cur_post whenever a new post is stored in sharedPost
	post_store.subscribe((data) => {
		cur_post = data;
	});

	//Subscribe to sharedPlot store to update cur_plot whenever a new plot is stored in sharedPost
	plot_store.subscribe((data) => {
		cur_plot = data;
	});

	// Loads a random tweet into page memory to be accesed under the variable cur_tweet
	async function getRandomPost() {
		const response = await fetch('/api/posts/random');
		const responseJSON = await response.json();

		//List of comments
		let comments = getComments(responseJSON['comments']);

		//update our current post
		let post = {
			text: responseJSON['text'],
			id: responseJSON['id'],
			date: responseJSON['date'],
			comments: comments,
			type: responseJSON['type']
		};

		//Set data in sharedPost store so that the data can be shared between components and pages
		post_store.set(post);
	}

	//gets comments for the posts and returns list of comments if any exist
	function getComments(response: []) {
		let comments: Comment[] = [];
		if (response == null) {
			return comments;
		}

		//add every comment to the list of comments
		for (var comment of response) {
			comments.push({
				text: comment['content'],
				id: comment['_id'],
				post_id: comment['post_id'],
				date: comment['created_at']
			});
		}
		return comments;
	}

	//Set tweet plot data in store to the JSON data returned by the backend
	async function getTweetSentimentPlot() {
		//Don't create a plot if there is no post loaded into memory
		if (cur_post.text == 'N/A') return false;

		const response = await fetch('/api/plot/sentiment/tweets/' + cur_post.id);
		const responseJSON = await response.json();

		//update our current plot
		let plot = { data: responseJSON["data"], layout: responseJSON["layout"] }

		//Set data in sharedPlot store so that the data can be shared between components and pages
		plot_store.set(plot);
	}

	//Set tweet plot data in store to the JSON data returned by the backend
	async function getRedditSentimentPlot() {
		//Don't create a plot if there is no post loaded into memory
		if (cur_post.text == 'N/A') return false;

		const response = await fetch('/api/plot/sentiment/reddit/' + cur_post.id);
		const responseJSON = await response.json();

		let plot = { data: responseJSON["data"], layout: responseJSON["layout"] }

		//Set data in sharedPlot store so that the data can be shared between components and pages
		plot_store.set(plot);
	}

	//Handles updating data when button is pressed
	async function ButtonUpdateComponents() {
		//Update Post Text
		await getRandomPost();

		if (cur_post.type == 'tweet') {
			await getTweetSentimentPlot();
		} else if (cur_post.type == 'reddit') {
			await getRedditSentimentPlot();
		} else {
			return false;
		}
	}
</script>

<main>
	<h1 class="px-2 py-4 text-4xl text-slate-500">Random Universal Basic Income Post</h1>

	<!-- Page Content Goes In Here -->
	<div class="space-y-2">
		<!-- Update Post and Data Vis -->
		<button
			class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg transform active:scale-75 transition-transform"
			on:click={ButtonUpdateComponents}
		>
			Get Random Post
		</button>

		<!-- Display size of db -->
		<Size />

		<!-- Show Post Text, Date Posted, Post Source, and Post Comments, upon update -->
		{#key cur_post}
			<ShowPost post={cur_post} />
		{/key}

		<!-- Display Plot upon update -->
		{#key cur_plot}
			<ShowPlot plot={cur_plot} />
		{/key}
	</div>
</main>
