export default function PdfUploadForm() {
  return (
    <div className="mt-6 space-y-3">
      <label className="text-sm font-medium mb-3">Upload PDF</label>

      <label
        className="flex items-center justify-center w-full h-28 rounded-lg border border-dashed border-border bg-background cursor-pointer hover:bg-muted/40 transition
        "
      >
        <div className="text-center">
          <p className="font-medium">Click to upload</p>

          <p className="text-sm text-muted-foreground mt-1">PDF up to 5MB</p>
        </div>

        <input type="file" accept=".pdf" className="hidden" />
      </label>
    </div>
  );
}
