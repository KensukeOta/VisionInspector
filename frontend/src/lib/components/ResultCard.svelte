<script lang="ts">
	import type { PredictionResponse } from '$lib/types/prediction';

	type Props = {
		result: PredictionResponse;
	};

	let { result }: Props = $props();

	const scorePercent = $derived((result.score * 100).toFixed(1));
</script>

<div class="rounded-xl border bg-white p-6 shadow-sm">
	<h2 class="mb-6 text-xl font-semibold">推論結果</h2>

	<div class="grid gap-4 sm:grid-cols-2">
		<div>
			<p class="text-sm text-slate-500">異常スコア</p>

			<p class="text-3xl font-bold">
				{scorePercent}%
			</p>
		</div>

		<div>
			<p class="text-sm text-slate-500">判定</p>

			<p class={`text-2xl font-bold ${result.label ? 'text-red-600' : 'text-green-600'}`}>
				{result.message}
			</p>
		</div>

		<div class="sm:col-span-2">
			<p class="text-sm text-slate-500">判定内容</p>

			<p class="mt-1 text-slate-700 leading-relaxed">
				{result.description}
			</p>
		</div>

		<div>
			<p class="text-sm text-slate-500">使用モデル</p>

			<p class="font-semibold uppercase">
				{result.model}
			</p>
		</div>

		<div class="sm:col-span-2">
			<p class="text-sm text-slate-500">処理時間</p>

			<p class="font-semibold">
				{result.processing_time_ms.toFixed(1)} ms
			</p>
		</div>
	</div>
</div>
