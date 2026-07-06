<script lang="ts">
	import type { Snippet } from 'svelte';

	type Variant = 'primary' | 'secondary';

	type Props = {
		children: Snippet;
		variant?: Variant;
		disabled?: boolean;
		type?: 'button' | 'submit';
		onclick?: () => void;
	};

	let {
		children,
		variant = 'primary',
		disabled = false,
		type = 'button',
		onclick
	}: Props = $props();

	const classes = $derived(
		variant === 'primary'
			? 'bg-blue-600 hover:bg-blue-700 text-white'
			: 'bg-slate-200 hover:bg-slate-300 text-slate-900'
	);
</script>

<button
	{type}
	{disabled}
	{onclick}
	class={`rounded-lg px-6 py-3 font-semibold transition disabled:cursor-not-allowed disabled:opacity-50 ${classes}`}
>
	{@render children()}
</button>
