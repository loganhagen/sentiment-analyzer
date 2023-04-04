import { writable } from 'svelte/store';

const tab = true;
export const sharedTab = writable(tab);
