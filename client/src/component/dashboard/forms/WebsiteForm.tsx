'use client';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

type props = {
  url: string;
  setUrl: React.Dispatch<React.SetStateAction<string>>;
};

export default function WebsiteForm({ url, setUrl }: props) {
  function handleSubmit() {
    console.log(url);
  }
  return (
    <div className="mt-6 flex flex-col items-center gap-3">
      <label className="block mb-3">Website URl</label>
      <Input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="http://nextjs.org/docs"
      />
      <Button className="bg-white text-black" onClick={handleSubmit}>
        Add Website
      </Button>
    </div>
  );
}
