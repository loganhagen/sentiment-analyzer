<script>
    let tweets = new Array();

    async function getTweets() {
            let response;
            var as = "";

            try {
                response = await fetch('http://localhost:8080/api/tweets');
            } catch (error) {
                console.log("Failed API call.");
            }

            if (response?.ok) {
                let json = await response.json();
                let data = JSON.parse(json);
                tweets = data["data"];
            } else {
                console.log(`HTTP response code: ${response?.status}`);
            }
        }

</script>

<main>
    <div>
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg" 
        on:click={getTweets}>Get Tweets!
        </button>
        <br>
        {#each tweets as tweet, i}
            <br>
            <p>Post #{i + 1}</p>
            <p>ID: {tweet["_id"]}</p>
            <p>"{tweet["content"]}"</p>
            <p>----</p>
            <p><a href="//twitter.com/user/status/{tweet["_id"]}" style="color: blue" target="_blank" rel="noreferrer">Link</a></p>
        {/each} 
    <div>
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