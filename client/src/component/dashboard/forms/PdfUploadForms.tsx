'use client';

import { Button } from '@/components/ui/button';

type Props = {
  file: File | null;

  setFile: React.Dispatch<React.SetStateAction<File | null>>;
};

export default function PdfUploadForm({ file, setFile }: Props) {
  function handleSubmit() {
    console.log(file);
  }
  return (
    <div className="mt-6 space-y-3 flex flex-col items-center">
      <label className="text-sm font-medium d">Upload PDF</label>

      <label
        className="flex items-center justify-center w-full h-28 rounded-lg border border-dashed border-border bg-background cursor-pointer hover:bg-muted/40 transition
        "
      >
        <div className="text-center">
          <p className="text-sm text-muted-foreground mt-1">PDF up to 5MB</p>
          {file && <p className="text-xs mt-2">{file.name}</p>}
        </div>

        <input
          type="file"
          accept=".pdf"
          className="hidden"
          onChange={(e) => setFile(e.target.files?.[0] ?? null)}
        />
      </label>
      <Button className="bg-white text-black" onClick={handleSubmit}>
        Upload pdf
      </Button>
    </div>
  );
}
