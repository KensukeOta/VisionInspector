<script lang="ts">
	type Props = {
		onFileSelected: (file: File) => void;
	};

	let { onFileSelected }: Props = $props();

	let isDragging = $state(false);

	function handleDrop(event: DragEvent) {
		event.preventDefault();
		isDragging = false;

		const file = event.dataTransfer?.files[0];

		if (file) {
			onFileSelected(file);
		}
	}

	function handleDragOver(event: DragEvent) {
		event.preventDefault();
		isDragging = true;
	}

	function handleDragLeave() {
		isDragging = false;
	}

	function handleChange(event: Event) {
		const input = event.currentTarget as HTMLInputElement;
		const file = input.files?.[0];

		if (file) {
			onFileSelected(file);
		}
	}
</script>

<label
	class={`block cursor-pointer rounded-xl border-2 border-dashed p-12 text-center transition-colors ${
		isDragging ? 'border-blue-500 bg-blue-50' : 'border-slate-300 bg-white'
	}`}
	ondrop={handleDrop}
	ondragover={handleDragOver}
	ondragleave={handleDragLeave}
>
	<input
		type="file"
		accept="image/png,image/jpeg,image/webp"
		class="sr-only"
		onchange={handleChange}
	/>

	<p class="mb-4 text-lg font-semibold text-slate-900">画像をドラッグ＆ドロップ</p>

	<p class="mb-6 text-sm text-slate-500">またはクリックして選択</p>

	<span
		class="inline-flex rounded-lg bg-blue-600 px-6 py-3 text-white transition hover:bg-blue-700"
	>
		画像を選択
	</span>
</label>
