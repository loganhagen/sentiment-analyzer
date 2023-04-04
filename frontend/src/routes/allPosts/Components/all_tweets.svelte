<script lang="ts">
	import type { Post } from '../../../types';
	import ShowPost from '../../../Components/show_post.svelte';
	import Size from '../../../Components/size.svelte';

	let posts: Array<Post> = [];
	let i = 20;

	async function lazyLoad()
	{
		const response = await fetch('/api/posts/tweets');
		const responseJSON = await response.json();
		const data = responseJSON['data'];
		let objects = JSON.parse(responseJSON)['data'];

		objects.forEach((element: any) => {

			//create post struct to add to our post array
			let post: Post = {
				text: element.content,
				id: element._id,
				date: element.created_at,
				comments: [],
				type: "tweet"
			};

			posts.push(post);

		});
	}

</script>

<main>
	<div class="space-y-2 px-0">
		<Size collection="twitter"/>

		<!-- We wait for lazy load to complete before displaying anything to the user  -->
		{#await lazyLoad()}
			Loading...
		{:then}
			<!-- Load posts up to i -->
			{#each posts.slice(0, i) as post}
				<ShowPost post={post}/>
			{/each}

			<!-- Display load more button if i < # posts -->
			{#if i < posts.length}
				<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded shadow-lg" on:click={() => i += 20}>
					Load More...
				</button>
			{/if}
		{/await}
		
	</div>
</main>