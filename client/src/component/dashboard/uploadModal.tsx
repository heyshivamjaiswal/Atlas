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
import PdfUploadForm from './forms/PdfUploadForms';
import WebsiteForm from './forms/WebsiteForm';
import YoutubeForm from './forms/YouTubeForm';

export default function UploadModal() {
  const [websiteUrl, setWebsiteUrl] = useState('');
  const [youtubeUrl, setYoutubeUrl] = useState('');
  const [file, setFile] = useState<File | null>(null);

  function handleSubit() {
    console.log({ source: selectedSource, websiteUrl, youtubeUrl, file });
  }

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
          <PdfUploadForm file={file} setFile={setFile} />
        )}

        {selectedSource === 'website' && (
          <WebsiteForm url={websiteUrl} setUrl={setWebsiteUrl} />
        )}

        {selectedSource === 'youtube' && (
          <YoutubeForm videoUrl={youtubeUrl} setVideoUrl={setYoutubeUrl} />
        )}

        {selectedSource && (
          <Button
            className="mt-6 w-full bg-white text-black "
            onClick={handleSubit}
          >
            Submit Source
          </Button>
        )}
      </DialogContent>
    </Dialog>
  );
}
