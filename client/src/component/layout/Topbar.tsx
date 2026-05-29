import { Input } from '@/components/ui/input';
import { Search } from 'lucide-react';
import UploadModal from '../dashboard/uploadModal';

export default function Topbar() {
  return (
    <header className="flex items-center justify-between border-b border-border px-6 py-4">
      <div className="relative w-[520px]">
        <Search
          size={15}
          className="absolute left-3  translate-y-1/2 text-muted-foreground"
        />

        <Input
          placeholder="search,  sources,  transcripts,  pages..."
          className="pl-25  bg-card"
        />
      </div>
      <UploadModal />
    </header>
  );
}
