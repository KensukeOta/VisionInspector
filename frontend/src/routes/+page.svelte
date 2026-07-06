<script lang="ts">
	import type { PredictionResponse } from '$lib/types/prediction';
	import type { ModelName } from '$lib/types/model';
	import type { SelectedImage } from '$lib/types/image';
	import { predictImage } from '$lib/api/client';
	import { createSelectedImage } from '$lib/utils/image';
	import ImagePreview from '$lib/components/features/ImagePreview.svelte';
	import ModelSelector from '$lib/components/features/ModelSelector.svelte';
	import OverlayViewer from '$lib/components/features/OverlayViewer.svelte';
	import ResultCard from '$lib/components/features/ResultCard.svelte';
	import UploadArea from '$lib/components/features/UploadArea.svelte';
	import LoadingSpinner from '$lib/components/ui/LoadingSpinner.svelte';
	import Button from '$lib/components/ui/Button.svelte';
	import ErrorMessage from '$lib/components/ui/ErrorMessage.svelte';

	let selectedModel = $state<ModelName>('padim');

	let selectedImage = $state<SelectedImage | null>(null);

	let prediction = $state<PredictionResponse | null>(null);

	let isLoading = $state(false);

	let errorMessage = $state('');

	async function handleFileSelected(file: File) {
		if (selectedImage) {
			URL.revokeObjectURL(selectedImage.url);
		}

		selectedImage = await createSelectedImage(file);
		prediction = null;
		errorMessage = '';
	}

	async function handlePredict() {
		if (!selectedImage) {
			return;
		}

		errorMessage = '';
		isLoading = true;

		try {
			prediction = await predictImage({
				file: selectedImage.file,
				model: selectedModel
			});
		} catch (error) {
			errorMessage = error instanceof Error ? error.message : '推論中にエラーが発生しました。';
		} finally {
			isLoading = false;
		}
	}
</script>

<svelte:head>
	<title>Vision Inspector</title>
	<meta name="description" content="AIによる画像異常検知アプリケーション" />
</svelte:head>

<div class="mx-auto flex min-h-screen max-w-5xl flex-col gap-8 px-6 py-10">
	<header class="text-center">
		<h1 class="text-4xl font-bold">Vision Inspector</h1>
		<p class="mt-2 text-slate-600">AIによる画像異常検知アプリケーション</p>
	</header>

	<ModelSelector {selectedModel} onModelChanged={(model) => (selectedModel = model)} />

	<UploadArea onFileSelected={handleFileSelected} />

	{#if errorMessage}
		<ErrorMessage message={errorMessage} />
	{/if}

	{#if selectedImage}
		<ImagePreview image={selectedImage} />

		<Button onclick={handlePredict} disabled={!selectedImage || isLoading}>推論する</Button>
		{#if isLoading}
			<LoadingSpinner />
		{/if}
	{/if}

	{#if prediction}
		<ResultCard result={prediction} />
	{/if}

	{#if selectedImage}
		<OverlayViewer image={selectedImage} result={prediction} />
	{/if}
</div>
