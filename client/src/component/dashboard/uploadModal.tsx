'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { uploadPdf, uploadWebsite, uploadYoutube } from '@/lib/source';

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
  const [loading, setLoading] = useState(false);

  async function handleSubit() {
    try {
      setLoading(true);

      if (selectedSource === 'pdf' && file) {
        await uploadPdf(file);
      }

      if (selectedSource === 'website') {
        await uploadWebsite(websiteUrl);
      }

      if (selectedSource === 'youtube') {
        await uploadYoutube(youtubeUrl);
      }

      alert('Source uploaded');

      window.location.reload();
    } catch (error) {
      console.error(error);

      alert('Upload failed');
    } finally {
      setLoading(false);
    }
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
            disabled={loading}
          >
            {loading ? 'Uploading...' : 'Submit Source'}
          </Button>
        )}
      </DialogContent>
    </Dialog>
  );
}
