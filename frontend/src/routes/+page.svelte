<script lang="ts">
	import type { PredictionResponse } from '$lib/types/prediction';
	import type { ModelName } from '$lib/types/model';
	import { predictImage } from '$lib/api/client';
	import ModelSelector from '$lib/components/ModelSelector.svelte';
	import UploadArea from '$lib/components/UploadArea.svelte';
	import ResultCard from '$lib/components/ResultCard.svelte';
	import OverlayViewer from '$lib/components/OverlayViewer.svelte';

	let selectedModel = $state<ModelName>('padim');

	let selectedFile = $state<File | null>(null);

	let prediction = $state<PredictionResponse | null>(null);

	let isLoading = $state(false);

	let errorMessage = $state('');

	function handleFileSelected(file: File) {
		selectedFile = file;
	}

	async function handlePredict() {
		if (!selectedFile) {
			return;
		}

		errorMessage = '';
		isLoading = true;

		try {
			prediction = await predictImage({
				file: selectedFile,
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

	{#if selectedFile}
		<div class="rounded-lg border bg-white p-4 shadow-sm">
			<p class="font-medium">選択中のファイル</p>
			<p class="mt-2 text-slate-600">
				{selectedFile.name}
			</p>
		</div>

		<button
			type="button"
			class="rounded-lg bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-slate-400"
			onclick={handlePredict}
			disabled={!selectedFile || isLoading}
		>
			{#if isLoading}
				推論中...
			{:else}
				推論する
			{/if}
		</button>
	{/if}

	{#if prediction}
		<ResultCard result={prediction} />
	{/if}

	{#if prediction}
		<OverlayViewer result={prediction} />
	{/if}
</div>
