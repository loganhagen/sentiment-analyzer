<script context="module" lang='ts'>

	import Size from './size.svelte';
	import Random from './random.svelte';

	//Tweet data structure containing tweet text and tweet id. id is used in fetch requests so it is important the frontend has access to it.
	interface Tweet {
		tweet_text:string;
		tweet_id:number;
	}

	//Create and set 
	export let cur_tweet:Tweet;
	cur_tweet = {tweet_text: "N/A", tweet_id: NaN}

	// Loads a random tweet into page memory to be accesed under the variable cur_tweet
	export async function getRandomTweet() {
		const response = await fetch('http://localhost:8080/api/tweets/random');
		const responseJSON = await response.json();

		//get tweet string and id from responseJSON
		let text:string = responseJSON['tweet'];
		let id:number = responseJSON['id'];
		
		//update our current tweet
		cur_tweet = {tweet_text: text, tweet_id: id};
		console.log(cur_tweet.tweet_id);

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
