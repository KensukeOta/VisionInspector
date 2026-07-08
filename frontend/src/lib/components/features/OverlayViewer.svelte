<script lang="ts">
	import type { SelectedImage } from '$lib/types/image';
	import type { PredictionResponse } from '$lib/types/prediction';
	import { API_URL } from '$lib/config';
	import Card from '$lib/components/ui/Card.svelte';
	import EmptyState from '$lib/components/ui/EmptyState.svelte';

	type Props = {
		image: SelectedImage;
		result: PredictionResponse | null;
	};

	let { image, result }: Props = $props();

	const overlayUrl = $derived(result ? `${API_URL}${result.overlay_url}` : '');
</script>

<Card>
	<h2 class="mb-6 text-xl font-semibold">異常マップ</h2>

	<div class="grid gap-6 md:grid-cols-2">
		<div>
			<p class="mb-2 text-sm font-medium text-slate-700">元画像</p>

			<img
				src={image.url}
				alt={image.file.name}
				class="mx-auto max-h-96 rounded-lg border object-contain"
			/>
		</div>

		<div>
			<p class="mb-2 text-sm font-medium text-slate-700">Overlay画像</p>

			{#if result}
				<img
					src={overlayUrl}
					alt="異常マップの重ね合わせ"
					class="mx-auto max-h-96 rounded-lg border object-contain"
				/>
			{:else}
				<EmptyState
					title="まだ推論していません"
					description="推論を実行するとAIが異常箇所をヒートマップで表示します。"
				/>
			{/if}
		</div>
	</div>

	<p class="mt-4 text-sm leading-6 text-slate-600">
		左は入力画像、右はAIが異常と判断した領域をヒートマップとして重ね合わせた画像です。
	</p>
</Card>
