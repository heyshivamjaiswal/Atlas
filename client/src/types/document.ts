export type DocumentType = 'PDF' | 'Website' | 'Video';

export type PriorityType = 'high' | 'medium' | 'low';

export type Documents = {
  id: number;

  title: string;

  type: DocumentType;

  priority: PriorityType;

  description: string;
};
