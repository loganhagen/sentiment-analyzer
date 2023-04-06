<svelte:head>
    <title>About</title> 
</svelte:head>

<main>
	<div>
		<img
			src="https://i.imgur.com/LjZ0Gg5.png"
			alt="Graphex Icon"
			style="width:250px;height:300px;"
		/>
		<h1 class="text-4xl px-4 py-4" style="position:relative;">We are team graphex!</h1>
	</div>
	<br /><br /><br />

	<h1 class="text-4xl px-4 py-4">What is UBI?</h1>
	<p class="px-8 py-4">
		Universal basic income is a form of social welfare, people receive supplementary income from the
		state.
	</p>
	<small class="px-16 py-4"> - Full basic income, if it provides above the poverty line. </small>
	<br />
	<small class="px-16 py-4"> - Partial basic income, any amount below the poverty line. </small>

	<p class="px-8 py-4">
		No country has implemented either for their full population, however there have been pilot
		projects all over, including in <a
			href="https://www.ontario.ca/page/ontario-basic-income-pilot"
			style="color:blue;">Ontario</a
		>

		Some countries have a child benefit that is similar to UBI as it is a buffer income for people
		taking care of children.
	</p>

	<h1 class="text-4xl px-4 py-4">Automation</h1>
	<p class="px-8 py-4">
		There is an ongoing automation revolution leading to menial jobs being eliminated. Like cashiers
		in virtually every big box store. People are losing their jobs and the minimum wage is not being
		increased in relation to increases in productivity, at least in North America. Should the state
		protect workers pushed out of their industry by offering a supplemental wage? For example, truck
		drivers in the future with self driving trucks.
	</p>

	<h1 class="text-4xl px-4 py-4">Living Wage</h1>
	<p class="px-8 py-4">
		A living wage is the hourly wage a worker needs to earn to cover their basic expenses and
		participate in their community. This is not the same as the minimum wage. How do organizations
		determine the living wage for an area?
	</p>
	<a
		href="https://www.ontariolivingwage.ca/living_wage_week_2022"
		style="color:blue;"
		class="px-8 py-4">Ontario's living wage</a
	>
	<p class="px-8 py-4">
		What we consider a living wage is having enough money to have your physiological needs met, as
		seen in Maslow's hierarchy of basic needs.
	</p>
	<img src="https://i.imgur.com/MBB3Gwk.jpg" alt="basic needs" />
	<p class="px-8 py-4">UBI could serve as the gap closer between minimum wage and living wage.</p>

	<h1 class="text-4xl px-4 py-4">Why talk about this?</h1>
	<p class="px-8 py-4">
		We need to understand our topic so that we know what kind of data we can pull from the internet
		about it. Our job isn't to solve this issue or to give our opinions on it. We need to focus on
		delivering objective data about the topic in a clear and concise manner.
	</p>

	<h1 class="text-4xl px-4 py-4">Visualization</h1>

	<h1 class="text-2xl px-6 py-4">Idea 1: Random Post</h1>
	<p class="px-8 py-4">
		Display a random post from our database, along with information about where and when it came
		from.
	</p>

	<h1 class="text-2xl px-6 py-4">Idea 2: Sentiment Analysis</h1>
	<p class="px-8 py-4">
		See if we can determine overall political sentiment towards the issue. We are analyzing the
		sentiment of the random post. We plan to implement overall database sentiment across all posts.
	</p>
	<img
		src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Black_cherry_tree_histogram.svg/800px-Black_cherry_tree_histogram.svg.png"
		alt="histogram"
	/>

	<h1 class="text-2xl px-6 py-4">Idea 3: Histogram -> TO:DO Interactive word cloud.</h1>
	<p class="px-8 py-4">
		A world cloud showcases which words are most related to the central topic. A histogram is just a
		different visualization of the same idea. Clicking on a word in the word cloud will take you to
		its definition in google. Could possibly integrate chat gpt definitions or answer to questionss
		somehow through their API.
	</p>
	<img src="https://i.imgur.com/iPIfVIQ.jpg" alt="word cloud" />

	<h1 class="text-4xl px-4 py-4">Demo Video</h1>
	<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" style="color:blue;" class="px-8 py-4"
		>Video Link</a
	>

	<h1 class="text-4xl px-4 py-4">Team Members</h1>
	<h2 class="text-2xl px-6 py-4">Stefan Zupancic</h2>
	<ul class="px-8 py-4">
		<li>Evolving Scalable Initiatives.</li>
		<li>Streamlining Innovative Relationships.</li>

		<li>Engaging in .com convergence.</li>
		<li>Incubating intuitive portals.</li>
		<li>Orchestrating B2B systems.</li>
		<li>Business.</li>
		<li>Value Stream.</li>
		<li>Doing other real stuff.</li>
	</ul>

	<h2 class="text-2xl px-6 py-4">Jonalton Jude Hamilton - Principle Reddit Engineer</h2>
	<h2 class="text-2xl px-6 py-4">Kyle Lukaszek - Level 9 DevOps Artisan</h2>
	<h2 class="text-2xl px-6 py-4">Logan Hagen - Lord of the Scrum</h2>
	<h2 class="text-2xl px-6 py-4">Tiffiny Haluschak - User Experience Connoisseur</h2>

	<h1 class="text-4xl px-4 py-4">Real Quotes by the team</h1>
	<p class="px-8 py-4">
		"When the USB antenna went down, our only choice was to disconnect and hack the neural array!" -
		Stefan
	</p>
	<p class="px-8 py-4">
		"Let me give you a preview of static npm; I think you'd appreciate the fact that it's flexible."
		- Kyle
	</p>
	<p class="px-8 py-4">
		"We're starting to notice a trend toward P2P natural language processing over Nginx." - Logan
	</p>
	<p class="px-8 py-4">"It's about time we crowdfund Node.js." - Tiffiny</p>
	<p class="px-8 py-4">
		"If you neglect to deploy Kubernetes, prepare to handle Agile machine learning." - Jonalton
	</p>

	<h1 class="text-4xl px-4 py-4">Tech used to make the website</h1>
	<h2 class="text-2xl px-6 py-4">Backend</h2>
	<ul class="px-8 py-4">
		<li>Python, Flask, pylint</li>
		<li>mongoDB, pymongo</li>
	</ul>
	<h2 class="text-2xl px-6 py-4">Frontend</h2>
	<ul class="px-8 py-4">
		<li>Sveltekit</li>
		<li>Typescript</li>
		<li>Tailwind CSS</li>
	</ul>
</main>
