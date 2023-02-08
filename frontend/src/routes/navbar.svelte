<script>
    export let menu = 1;
</script>

<ul id="menu">
	<li><a href="/" on:click|preventDefault={() => (menu = 1)}>Home</a></li>|
	<li><a href="/" on:click|preventDefault={() => (menu = 2)}>About</a></li>
</ul>

{#if menu==1}
	<p>This is tester home page</p>
{:else if menu==2}
	<p>This is tester about page</p>
{:else}
    <p>Page not found</p>

{/if}

<style>
	ul#menu li{
		display : inline;
	}
</style>