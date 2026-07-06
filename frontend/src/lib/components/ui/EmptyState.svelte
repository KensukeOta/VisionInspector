<script lang="ts">
	type Props = {
		title: string;
		description: string;
	};

	let { title, description }: Props = $props();
</script>

<div
	class="flex min-h-96 flex-col items-center justify-center rounded-lg border-2 border-dashed border-slate-300 px-6 text-center"
>
	<h3 class="text-lg font-semibold text-slate-700">
		{title}
	</h3>

	<p class="mt-3 max-w-sm text-sm leading-6 text-slate-500">
		{description}
	</p>
</div>
