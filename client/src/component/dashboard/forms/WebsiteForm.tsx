import { Input } from '@/components/ui/input';

export default function WebsiteForm() {
  return (
    <div className="mt-6">
      <label className="block mb-3">Website URl</label>
      <Input placeholder="http://nextjs.org/docs" />
    </div>
  );
}
