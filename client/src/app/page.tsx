import Document from '@/component/dashboard/DocumentCard';
import { Documents } from '@/types/document';

const docs: Documents[] = [
  {
    id: 1,
    title: 'Next.js Docs',
    type: 'Website',
    priority: 'high',
    description: 'Routing and server components',
  },

  {
    id: 2,
    title: 'Attention Paper',
    type: 'PDF',
    priority: 'medium',
    description: 'Transformer architecture',
  },

  {
    id: 3,
    title: 'LLM Lecture',
    type: 'Video',
    priority: 'low',
    description: 'Video transcript notes',
  },
];

export default function HomePage() {
  return (
    <div className="p-8">
      <div className="mb-8">
        <h1 className="text-3xl font-semibold">Library</h1>
        <p className="text-muted-foreground">Your knowledge sources</p>
      </div>
      <div className="grid grid-cols-3 gap-4">
        {docs.map((doc) => (
          <Document
            key={doc.id}
            id={doc.id}
            title={doc.title}
            type={doc.type}
            priority={doc.priority}
            description={doc.description}
          />
        ))}
      </div>
    </div>
  );
}
