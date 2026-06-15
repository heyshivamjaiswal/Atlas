export type Source = {
  id: number;

  source_type: string;

  title: string;

  chunk_count: number;
};

export type SourceDetails = {
  id: number;
  source_type: string;
  title: string;
  file_name: string;
  chunk_count: number;
};

export type SourceChunk = {
  chunk_index: number;
  page: number;
  content: string;
};
