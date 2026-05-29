'use client';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

type Props = {
  videoUrl: string;
  setVideoUrl: React.Dispatch<React.SetStateAction<string>>;
};

export default function YoutubeForm({ videoUrl, setVideoUrl }: Props) {
  //   const [videoUrl, setVideoUrl] = useState('');

  function handleSubmit() {
    console.log(videoUrl);
  }
  return (
    <div className="mt-6 flex flex-col items-center gap-4">
      <label className="block mb-3">YouTube URL</label>
      <Input
        value={videoUrl}
        onChange={(e) => setVideoUrl(e.target.value)}
        placeholder="http://youtube.com/watch?v=..."
      />
    </div>
  );
}
