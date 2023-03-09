<script lang="ts">

	import { getRandomTweet, cur_post } from "./+page.svelte"

	//set tweet_text for when page loads
	let post_text:string = cur_post.post_text;

	//Get a new random tweet and set the text on the page to match the tweet.
	//The tweet is saved in ./+page.svelte as 'cur_tweet' which can be imported into different files.
	async function ButtonUpdateComponent() {
		await getRandomTweet();
		post_text = cur_post.post_text;
	}

</script>

<main>
	<button
		class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
		on:click={ButtonUpdateComponent}>Get Random Post</button
	>
	<p>{post_text}</p>
</main>
