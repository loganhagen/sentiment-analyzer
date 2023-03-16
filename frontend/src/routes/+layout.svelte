<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import Dropdown from 'svelte';

	let dropdown = null;
	onMount(() => {
		dropdown = new Dropdown({
			target: document.querySelector('.relative'),
			props: {
				onShow: () => {
					dropdown.$refs.trigger.setAttribute('aria-expanded', true);
					dropdown.$refs.menu.classList.remove('hidden');
				},
				onHide: () => {
					dropdown.$refs.trigger.setAttribute('aria-expanded', false);
					dropdown.$refs.menu.classList.add('hidden');
				},
				placement: 'bottom-start'
			}
		});
	});
</script>

<nav class="bg-white border-gray-200 px-2 sm:px-4 py-2.5 dark:bg-gray-900">
	<div class="container flex flex-wrap items-center justify-between mx-auto">
		<div class="hidden w-full md:block md:w-auto" id="navbar-default">
			<ul
				class="flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"
			>
				<li>
					<a
						href="/home"
						class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent mod:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						Home
					</a>
				</li>
				<li>
					<a
						href="/about"
						class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						About
					</a>
				</li>
				<li>
					<a
						href="/question"
						class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						Q&A
					</a>
				</li>
				<li class="relative">
					<a
						href="/accessibility"
						class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
					>
						Accessibility
					</a>
					<ul class="absolute z-10 hidden bg-white shadow-lg rounded-md">
						<li><a href="/accessibility/contrast">Contrast</a></li>
						<li><a href="/accessibility/keyboard">Keyboard</a></li>
						<li><a href="/accessibility/screenreaders">Screen Readers</a></li>
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
