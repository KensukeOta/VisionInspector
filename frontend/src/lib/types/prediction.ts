export interface PredictionResponse {
	model: string;
	score: number;
	label: boolean;
	message: string;
	description: string;
	overlay_url: string;
	processing_time_ms: number;
}
