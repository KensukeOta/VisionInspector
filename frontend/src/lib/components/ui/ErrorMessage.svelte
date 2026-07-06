<script lang="ts">
	type Props = {
		message: string;
	};

	let { message }: Props = $props();
</script>

<div class="rounded-xl border border-red-200 bg-red-50 p-4 text-red-700" role="alert">
	{message}
</div>
