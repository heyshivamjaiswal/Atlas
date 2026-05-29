import { Input } from '@/components/ui/input';

export default function YoutubeForm() {
  return (
    <div className="mt-6">
      <label className="block mb-3">YouTube URL</label>
      <Input placeholder="http://youtube.com/watch?v=..." />
    </div>
  );
}
