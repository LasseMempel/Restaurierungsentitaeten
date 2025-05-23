// Entity types
export interface Entity {
  id: string;
  text: string;
  label: string;
  start: number;
  end: number;
  confidence: number;
  isManualEdit?: boolean;
}

// Document types
export interface Document {
  id: string;
  title: string;
  content: string;
  createdAt: string;
  updatedAt: string;
  userId: string;
}

// Annotation types
export interface AnnotationResult {
  documentId: string;
  entities: Entity[];
  threshold: number;
  modelVersion: string;
}

// API response types
export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

// Export types
export interface NIFExport {
  format: 'turtle' | 'json-ld';
  includeOriginal: boolean;
  includeEdits: boolean;
}