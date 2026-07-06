<script lang="ts">
	import type { ModelName } from '$lib/types/model';

	type Props = {
		selectedModel: ModelName;
		onModelChanged: (model: ModelName) => void;
	};

	let { selectedModel, onModelChanged }: Props = $props();

	function handleChange(event: Event) {
		const select = event.currentTarget as HTMLSelectElement;
		onModelChanged(select.value as ModelName);
	}
</script>

<div class="rounded-xl border bg-white p-4 shadow-sm">
	<label for="model" class="mb-2 block text-sm font-medium text-slate-700"> 使用モデル </label>

	<select
		id="model"
		value={selectedModel}
		onchange={handleChange}
		class="w-full rounded-lg border border-slate-300 px-3 py-2"
	>
		<option value="padim">PaDiM</option>
	</select>

	<p class="mt-2 text-sm text-slate-500">
		現在はPaDiMのみ対応しています。PatchCoreは今後追加予定です。
	</p>
</div>
