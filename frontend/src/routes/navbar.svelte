<script>
	export let menu = 1;
</script>

<nav class="bg-white border-gray-200 px-2 sm:px-4 py-2.5 dark:bg-gray-900">
	<div class="container flex flex-wrap items-center justify-between mx-auto">
		<div class="hidden w-full md:block md:w-auto" id="navbar-default">
			<ul
				class="flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"
			>
				<li>
					<a
						href="/"
						class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent mod:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
						on:click|preventDefault={() => (menu = 1)}>Home</a
					>
				</li>
				<li>
					<a
						href="/"
						class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
						on:click|preventDefault={() => (menu = 2)}>About</a
					>
				</li>
			</ul>
		</div>
	</div>
</nav>

{#if menu == 1}
	<p>This is tester home page</p>
{:else if menu == 2}
	<p>This is tester about page</p>
{:else}
	<p>Page not found</p>
{/if}

<style>
	ul#menu li {
		display: inline;
	}
</style>
