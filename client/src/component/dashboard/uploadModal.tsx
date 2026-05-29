'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';

import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';

import { FileText, Globe, Plus, Video } from 'lucide-react';

import SourceCard from './SourceCard';

export default function UploadModal() {
  const [selectedSource, setSelectedSource] = useState<string | null>(null);
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button className="gap-2 bg-white text-background font-semibold">
          <Plus size={15} />
          Add sources
        </Button>
      </DialogTrigger>

      <DialogContent className="bg-card text-white">
        <DialogHeader>
          <DialogTitle>Add knowledge source</DialogTitle>
        </DialogHeader>
        <div className="grid grid-cols-3 gap-4 mt-4 ">
          <SourceCard
            icon={<FileText size={20} />}
            title="PDF"
            onClick={() => setSelectedSource('pdf')}
          />

          <SourceCard
            icon={<Globe size={20} />}
            title="Website"
            onClick={() => setSelectedSource('website')}
          />

          <SourceCard
            icon={<Video size={20} />}
            title="YouTube"
            onClick={() => setSelectedSource('youtube')}
          />
        </div>
        {selectedSource === 'pdf' && (
          <div className="mt-6">PDF Upload Form</div>
        )}
        {selectedSource === 'website' && (
          <div className="mt-6">Website URL Form</div>
        )}
        {selectedSource === 'youtube' && (
          <div className="mt-6">YouTube URL Form</div>
        )}
      </DialogContent>
    </Dialog>
  );
}
