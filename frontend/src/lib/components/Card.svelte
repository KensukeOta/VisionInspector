<script lang="ts">
	import type { Snippet } from 'svelte';

	type Props = {
		children: Snippet;
	};

	let { children }: Props = $props();
</script>

<div class="rounded-xl border bg-white p-6 shadow-sm">
	{@render children()}
</div>
