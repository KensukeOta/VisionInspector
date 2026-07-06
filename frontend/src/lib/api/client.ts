import type { PredictionResponse } from '$lib/types/prediction';
import type { ModelName } from '$lib/types/model';

export type PredictRequest = {
	file: File;
	model: ModelName;
};

const API_URL = 'http://localhost:8000';

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
