'use client';

import { useEffect, useState } from 'react';

import Document from '@/component/dashboard/DocumentCard';

import { getSources } from '@/lib/source';

import { Source } from '@/types/source';

export default function HomePage() {
  const [sources, setSources] = useState<Source[]>([]);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadSources() {
      try {
        const data = await getSources();

        setSources(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadSources();
  }, []);

  if (loading) {
    return <div className="p-8">Loading...</div>;
  }

  return (
    <div className="p-8">
      <div className="mb-8">
        <h1 className="text-3xl font-semibold">Library</h1>

        <p className="text-muted-foreground">Your knowledge sources</p>
      </div>

      <div className="grid grid-cols-3 gap-4">
        {sources.map((source) => (
          <Document
            key={source.id}
            id={source.id}
            title={source.title}
            type="PDF"
            priority="medium"
            description={`${source.chunk_count} chunks`}
          />
        ))}
      </div>
    </div>
  );
}
