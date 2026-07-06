<script lang="ts">
	import type { PredictionResponse } from '$lib/types/prediction';

	type Props = {
		result: PredictionResponse;
	};

	let { result }: Props = $props();
</script>

<div class="rounded-xl border bg-white p-6 shadow-sm">
	<h2 class="mb-6 text-xl font-semibold">異常マップ</h2>

	{#if result.overlay_url}
		<img
			src={`http://localhost:8000${result.overlay_url}`}
			alt="Overlay"
			class="mx-auto rounded-lg"
		/>
	{:else}
		<div class="rounded-lg border border-dashed p-12 text-center text-slate-400">
			推論を実行するとオーバーレイ画像が表示されます
		</div>
	{/if}
</div>
