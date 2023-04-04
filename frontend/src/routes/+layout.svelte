<script>
	import '../app.css';
</script>

<nav class="bg-black border-gray-200 px-4 sm:px-4 py-2.5 dark:bg-gray-900">
	<div class="container flex flex-wrap items-center justify-start mx-auto">
		<img src="src/images/Favicon.png" alt="Logo" class="h-8 mx-4" />
		<div class="hidden w-full md:block md:w-auto" id="navbar-default">
			<ul
				class="flex flex-col p-4 mt-4 md:border-l-2 md:border-r-2 md:border-white bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-black dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"
			>
				<li>
					<a
						href="/home"
						class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent mod:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						Home
					</a>
				</li>
				<li>
					<a
						href="/about"
						class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						About
					</a>
				</li>
				<li>
					<a
						href="/allPosts"
						class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						All Posts
					</a>
				</li>
				<li>
					<a
						href="/ask"
						class="block py-2 pl-3 pr-4 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						Q&A
					</a>
				</li>
				<li class="relative pr-8">
					<button
						class="block px-4 py-2 pl-3 pr-8 text-white rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						Accessibility
					</button>
					<ul class="absolute z-10 hidden bg-white shadow-lg rounded-md">
						<li><button class="text-left">Contrast</button></li>
						<li><button class="text-left">Keyboard</button></li>
						<li><button class="text-left">Screen Readers</button></li>
					</ul>
				</li>
			</ul>
		</div>
	</div>
</nav>

<slot />

<style>
	.relative:hover .absolute {
		display: block;
	}
</style>
