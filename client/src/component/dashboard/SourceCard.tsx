type SourceCardType = {
  icon: React.ReactNode;
  title: string;
  onClick: () => void;
};

export default function SourceCard({ icon, title, onClick }: SourceCardType) {
  return (
    <button
      className="border border-border rounded-lg p-6 hover:bg-zinc-800 transition"
      onClick={onClick}
    >
      <div className="flex flex-col items-center gap-3">
        {icon}
        <span>{title}</span>
      </div>
    </button>
  );
}
