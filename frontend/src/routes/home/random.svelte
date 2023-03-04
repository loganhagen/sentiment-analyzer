<script lang="ts">

	import { getRandomTweet, cur_tweet } from "./+page.svelte"

	//set tweet_text for when page loads
	let tweet_text:string = cur_tweet.tweet_text;

	//Get a new random tweet and set the text on the page to match the tweet.
	//The tweet is saved in ./+page.svelte as 'cur_tweet' which can be imported into different files.
	async function ButtonUpdateComponent() {
		await getRandomTweet();
		tweet_text = cur_tweet.tweet_text;
	}

</script>

<main>
	<button
		class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
		on:click={ButtonUpdateComponent}>Get Random Tweet</button
	>
	<p>{tweet_text}</p>
</main>
