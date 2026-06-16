'use client';

import { useEffect, useState } from 'react';

import { getSource } from '@/lib/source';

import { SourceDetails } from '@/types/source';

import { Button } from '@/components/ui/button';

import { createChat } from '@/lib/chat';
import { useRouter } from 'next/navigation';

type Props = {
  params: Promise<{
    id: string;
  }>;
};

export default function SourcePage({ params }: Props) {
  const router = useRouter();

  const [source, setSource] = useState<SourceDetails | null>(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const { id } = await params;

      try {
        const sourceData = await getSource(Number(id));

        setSource(sourceData);
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

  async function handleStartChat() {
    if (!source) return;

    try {
      const chat = await createChat(source.title, [source.id]);

      router.push(`/dashboard/chat/${chat.id}`);
    } catch (error) {
      console.error(error);
    }
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

      <Button className="bg-white text-black" onClick={handleStartChat}>
        Start Chat
      </Button>

      <div className="rounded-lg border border-border p-6">
        <h2 className="text-lg font-medium">Source Information</h2>

        <div className="mt-4 space-y-2 text-sm">
          <p>
            <span className="text-muted-foreground">Type:</span>{' '}
            {source.source_type.toUpperCase()}
          </p>

          <p>
            <span className="text-muted-foreground">Chunks:</span>{' '}
            {source.chunk_count}
          </p>

          <p>
            <span className="text-muted-foreground">File:</span>{' '}
            {source.file_name}
          </p>
        </div>
      </div>
    </div>
  );
}
