<script>
    import { onMount } from 'svelte';

    let tweets = new Array();

    onMount(async function () {
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
        });

</script>

{#each tweets as tweet, i}
    <br>
    <p>{i + 1}</p>
    <p>{tweet["_id"]}</p>
    <p>{tweet["content"]}</p>
    <p ><a href="//twitter.com/user/status/{tweet["_id"]}" target="_blank" rel="noreferrer">Link to post</a></p>
{/each} 