<script lang="ts">
	import type { SelectedImage } from '$lib/types/image';
	import { formatFileSize } from '$lib/utils/image';
	import Card from './Card.svelte';

	type Props = {
		image: SelectedImage;
	};

	let { image }: Props = $props();
</script>

<Card>
	<h2 class="mb-4 text-xl font-semibold">選択画像</h2>

	<img src={image.url} alt={image.file.name} class="mx-auto max-h-80 rounded-lg object-contain" />

	<div class="mt-4 space-y-1 text-sm text-slate-600">
		<p class="font-medium text-slate-900">{image.file.name}</p>
		<p>{image.width} × {image.height}px</p>
		<p>{formatFileSize(image.file.size)}</p>
	</div>
</Card>
