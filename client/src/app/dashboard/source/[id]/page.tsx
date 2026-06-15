'use client';

import { useEffect, useState } from 'react';

import { getSource, getSourceChunks } from '@/lib/source';

import { SourceDetails, SourceChunk } from '@/types/source';

type Props = {
  params: Promise<{
    id: string;
  }>;
};

export default function SourcePage({ params }: Props) {
  const [source, setSource] = useState<SourceDetails | null>(null);

  const [chunks, setChunks] = useState<SourceChunk[]>([]);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const { id } = await params;

      try {
        const sourceData = await getSource(Number(id));

        const chunkData = await getSourceChunks(Number(id));

        setSource(sourceData);
        setChunks(chunkData);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [params]);

  if (loading) {
    return <div className="p-8">Loading...</div>;
  }

  if (!source) {
    return <div className="p-8">Source not found</div>;
  }

  return (
    <div className="p-8 space-y-8">
      <div>
        <h1 className="text-3xl font-semibold">{source.title}</h1>

        <p className="text-muted-foreground mt-2">
          {source.source_type.toUpperCase()}
        </p>

        <p className="text-sm text-muted-foreground mt-2">
          {source.chunk_count} chunks
        </p>
      </div>

      <div className="space-y-4">
        {chunks.map((chunk) => (
          <div
            key={chunk.chunk_index}
            className="border border-border rounded-lg p-4"
          >
            <div className="text-xs text-muted-foreground mb-2">
              Page {chunk.page} • Chunk {chunk.chunk_index}
            </div>

            <p className="text-sm whitespace-pre-wrap">{chunk.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
