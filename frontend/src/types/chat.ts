export type AttachmentCategory = 'image' | 'document' | 'other';

export interface ChatAttachment {
  id: string;
  name: string;
  size: number;
  type: string;
  category: AttachmentCategory;
  previewUrl?: string; // Blob URL for images
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  attachments?: ChatAttachment[];
  timestamp: string; // ISO string for safe serialization
  isDemoNotice?: boolean;
  reaction?: 'like' | 'dislike' | null;
}

export interface ChatConversation {
  id: string;
  title: string;
  createdAt: string;
  updatedAt: string;
  messages: ChatMessage[];
}

export interface FileValidationError {
  fileName: string;
  reason: string;
}
