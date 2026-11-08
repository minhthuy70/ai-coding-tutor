import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface HealthStatusResponse {
  status: string;
  database: string;
  redis: string;
  environment?: string;
}

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getHealthStatus = async (): Promise<HealthStatusResponse> => {
  try {
    const response = await apiClient.get<HealthStatusResponse>('/api/health');
    return response.data;
  } catch (error: any) {
    if (error.response && error.response.data) {
      // Backend responded with non-2xx status (e.g. 503 degraded)
      return error.response.data;
    }
    return {
      status: 'error',
      database: 'disconnected (backend unreachable)',
      redis: 'disconnected (backend unreachable)',
      environment: 'unknown',
    };
  }
};

export interface MultimodalChatResponse {
  status: string;
  reply: string;
  sources: Array<{
    content: string;
    source: string;
    section: string;
    language: string;
    similarity_score: number;
  }>;
  suggestedFollowUps: string[];
  filesCount?: number;
  imagesCount?: number;
}

export const sendMultimodalChat = async (
  prompt: string,
  language?: string,
  codeFiles: File[] = [],
  imageFiles: File[] = []
): Promise<MultimodalChatResponse> => {
  const formData = new FormData();
  formData.append('prompt', prompt);
  if (language) {
    formData.append('language', language);
  }

  codeFiles.forEach((file) => {
    formData.append('code_files', file);
  });

  imageFiles.forEach((img) => {
    formData.append('image_files', img);
  });

  const response = await apiClient.post<MultimodalChatResponse>(
    '/api/tutor/multimodal-chat',
    formData,
    {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      timeout: 30000, // 30s timeout for vision & LLM
    }
  );
  return response.data;
};
