import { writable } from 'svelte/store';
import type { Post, Plot } from '../../types';

const post: Post = { text: 'N/A', id: NaN, date: 'N/A', type: 'N/A' };
const plot: Plot = { data: {}, layout: {} };

export const sharedPost = writable(post);
export const sharedPlot = writable(plot);
