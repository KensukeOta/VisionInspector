<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/favicon.png" />

	<meta property="og:type" content="website" />
	<meta property="og:site_name" content="VisionInspector" />
	<meta property="og:title" content="VisionInspector" />
	<meta property="og:description" content="AIによる画像異常検知Webアプリケーションです。" />
	<meta property="og:url" content="https://vision-inspector-kensuke.vercel.app" />
	<meta property="og:image" content="https://vision-inspector-kensuke.vercel.app/ogp.png" />

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content="VisionInspector" />
	<meta name="twitter:description" content="AIによる画像異常検知Webアプリケーションです。" />
	<meta name="twitter:image" content="https://vision-inspector-kensuke.vercel.app/ogp.png" />
</svelte:head>
{@render children()}
