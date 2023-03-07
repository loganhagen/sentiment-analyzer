<script context="module" lang="ts">
	//Tweet data structure containing tweet text and tweet id. id is used in fetch requests so it is important the frontend has access to it.
	export type Post = {
		post_text: string;
		post_id: number;
		post_date: string;
		post_type: string;
	};

	//Plot data structure containing plotly data and plotly layout as objects from JSON.
	export type Plot = {
		data: object;
		layout: object;
	};
</script>
