//Stores all data that is shared throughout components in this route

import { writable } from 'svelte/store';
import type { Post, Plot } from '../../types';

const post: Post = { text: 'N/A', id: NaN, date: 'N/A', type: 'N/A', comments: [] };
const plot: Plot = { data: {}, layout: {} };
const tab = true;
const dbSentiment: Plot = { data: {}, layout: {} };

export const sharedPost = writable(post);
export const sharedPlot = writable(plot);
export const sharedTab = writable(tab);
export const sharedDB = writable(dbSentiment);
