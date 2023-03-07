<script context="module" lang='ts'>

	import Size from './size.svelte';
	import Random from './random.svelte';
	import type { Post } from '../../types.svelte';

	//Create and set current post for the page
	export let cur_post:Post = {post_text: "N/A", post_id: NaN, post_date: "N/A", post_type: "N/A"};

	// Loads a random tweet into page memory to be accesed under the variable cur_tweet
	export async function getRandomTweet() {
		const response = await fetch('http://localhost:8080/api/tweets/random');
		const responseJSON = await response.json();

		//get tweet string and id from responseJSON
		let text:string = responseJSON['text'];
		let id:number = responseJSON['id'];
		let date:string = responseJSON['date'];
		let type:string = responseJSON['type'];
		
		//update our current post
		cur_post = {post_text: text, post_id: id, post_date: date, post_type: type};

		console.log(cur_post.post_text, cur_post.post_id, cur_post.post_date, cur_post.post_type)

		//solves promise error in dev console
		return true;
	}

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
