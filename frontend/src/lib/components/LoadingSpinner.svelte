<script lang="ts">
	type Props = {
		message?: string;
	};

	let { message = 'AIが画像を解析しています...' }: Props = $props();
</script>

<div
	class="flex flex-col items-center justify-center gap-4 rounded-xl border bg-white py-10 shadow-sm"
>
	<div
		class="h-12 w-12 animate-spin rounded-full border-4 border-slate-200 border-t-blue-600"
	></div>

	<p class="text-slate-600">
		{message}
	</p>
</div>
