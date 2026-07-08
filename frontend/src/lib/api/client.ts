import type { ModelName } from '$lib/types/model';
import type { PredictionResponse } from '$lib/types/prediction';
import { API_URL } from '$lib/config';

export type PredictRequest = {
	file: File;
	model: ModelName;
};

export async function predictImage({ file, model }: PredictRequest): Promise<PredictionResponse> {
	const formData = new FormData();

	formData.append('file', file);

	const response = await fetch(`${API_URL}/predict?model=${model}`, {
		method: 'POST',
		body: formData
	});

	if (!response.ok) {
		throw new Error('推論に失敗しました。');
	}

	return response.json();
}
