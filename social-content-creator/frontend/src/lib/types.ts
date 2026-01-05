export type Platform = 'instagram' | 'tiktok' | 'youtube' | 'linkedin' | 'twitter';
export type ContentType = 'post' | 'reels' | 'stories' | 'carousel' | 'video' | 'short';
export type ToneOfVoice = 'professional' | 'casual' | 'motivational' | 'educational' | 'humorous' | 'inspirational';

export interface ContentRequest {
  description: string;
  platform: Platform;
  content_type: ContentType;
  tone: ToneOfVoice;
  reference_profile?: string;
  reference_text?: string;
  user_copy?: string;
  generate_image: boolean;
  generate_video: boolean;
  generate_audio: boolean;
  additional_instructions?: string;
}

export interface ContentResponse {
  success: boolean;
  content: string;
  session_id?: string;
  error?: string;
}

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}
