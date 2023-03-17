<script>
    import { onMount } from 'svelte';
    import { PUBLIC_API_URL } from '$env/static/public';

    let posts = [];

    onMount(async () => {
        const response = await fetch(PUBLIC_API_URL + 'tweets');
        const json = await response.json();
        posts = JSON.parse(json)["data"]
    });

</script>

<main>
    <div>
        {#each posts as post, i}
            <br>
            <p>Post #{i + 1}</p>
            <p>ID: {post._id}</p>
            <p>"{post.content}"</p>
            <p>----</p>
            <p><a href="//twitter.com/user/status/{post._id}" style="color: blue" target="_blank" rel="noreferrer">Link</a></p>
        {:else}
            <p>Loading...</p>
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