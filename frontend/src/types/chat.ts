export type AttachmentCategory = 'image' | 'document' | 'other';

export interface ChatAttachment {
  id: string;
  name: string;
  size: number;
  type: string;
  category: AttachmentCategory;
  previewUrl?: string; // Blob URL for images
  fileContent?: string; // Text content for code/document preview
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  attachments?: ChatAttachment[];
  timestamp: string; // ISO string
  isDemoNotice?: boolean;
  reaction?: 'like' | 'dislike' | null;
  modelUsed?: string;
  suggestedFollowUps?: string[];
  isStreaming?: boolean;
}

export interface ChatConversation {
  id: string;
  title: string;
  createdAt: string;
  updatedAt: string;
  isPinned?: boolean;
  messages: ChatMessage[];
}

export interface FileValidationError {
  fileName: string;
  reason: string;
}

export interface ModelSettings {
  temperature: number; // 0.0 - 1.0
  maxTokens: number;   // 512 - 4096
  persona: 'socratic' | 'strict_reviewer' | 'algorithm_expert' | 'casual';
}
