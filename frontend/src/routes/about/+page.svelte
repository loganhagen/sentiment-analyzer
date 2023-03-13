<script>
    let tweets = new Array();

    async function getTweets () {
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

<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg" 
	on:click={getTweets}>Get Tweets!
</button>

{#each tweets as tweet}
    <br>
    <p>{tweet["_id"]}</p>
    <p>{tweet["content"]}</p>
    <p ><a href="//twitter.com/user/status/{tweet["_id"]}" target="_blank" rel="noreferrer">Link to post</a></p>
{/each} 