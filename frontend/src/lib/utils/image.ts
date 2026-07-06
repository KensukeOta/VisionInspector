import type { SelectedImage } from '$lib/types/image';

export async function createSelectedImage(file: File): Promise<SelectedImage> {
	const url = URL.createObjectURL(file);

	const image = new Image();

	await new Promise<void>((resolve, reject) => {
		image.onload = () => resolve();
		image.onerror = () => reject(new Error('画像の読み込みに失敗しました。'));
		image.src = url;
	});

	return {
		file,
		url,
		width: image.width,
		height: image.height
	};
}

export function formatFileSize(size: number): string {
	return `${(size / 1024).toFixed(1)} KB`;
}
