//Tweet data structure containing tweet text and tweet id. id is used in fetch requests so it is important the frontend has access to it.
export type Post = {
	text: string;
	id: number;
	date: string;
	comments: Array<Comment>;
	type: string;
};

//Plot data structure containing plotly data and plotly layout as objects from JSON.
export type Plot = {
	data: object;
	layout: object;
};

//Comment data structure containing comment text, date, comment id, and post id
export type Comment = {
	text: string;
	id: number;
	post_id: number;
	date: string;
};
