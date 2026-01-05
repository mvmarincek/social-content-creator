const API_URL = import.meta.env.VITE_API_URL || '';
const API_BASE = `${API_URL}/api/content`;

export async function transcribeAudio(file: File): Promise<{ success: boolean; transcription: string }> {
  const formData = new FormData();
  formData.append('file', file);
  
  const response = await fetch(`${API_BASE}/transcribe`, {
    method: 'POST',
    body: formData,
  });
  
  if (!response.ok) {
    throw new Error('Failed to transcribe audio');
  }
  
  return response.json();
}

export async function createContent(data: {
  description: string;
  platform: string;
  content_type: string;
  tone: string;
  reference_profile?: string;
  reference_text?: string;
  user_copy?: string;
  generate_image: boolean;
  generate_video: boolean;
  generate_audio: boolean;
  additional_instructions?: string;
}) {
  const response = await fetch(`${API_BASE}/create`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  
  if (!response.ok) {
    throw new Error('Failed to create content');
  }
  
  return response.json();
}

export async function analyzeProfile(profile_url: string, platform: string) {
  const response = await fetch(`${API_BASE}/analyze-profile`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ profile_url, platform }),
  });
  
  if (!response.ok) {
    throw new Error('Failed to analyze profile');
  }
  
  return response.json();
}

export async function chatWithAgent(prompt: string, session_id?: string) {
  const response = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt, session_id }),
  });
  
  if (!response.ok) {
    throw new Error('Failed to send message');
  }
  
  return response.json();
}

export async function healthCheck() {
  const response = await fetch(`${API_BASE}/health`);
  return response.json();
}
