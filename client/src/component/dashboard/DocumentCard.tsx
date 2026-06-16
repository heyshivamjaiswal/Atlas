import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';
import Link from 'next/link';
import { FileText } from 'lucide-react';
import PriorityDot from './PriorityDot';
import { DocumentType, PriorityType } from '@/types/document';

type Documentprops = {
  id: number;
  title: string;
  type: DocumentType;
  description: string;
};

export default function Document({
  id,
  title,
  type,
  description,
}: Documentprops) {
  return (
    <Link href={`/dashboard/source/${id}`}>
      <Card className="bg-red border-border p-5 hover:border-zinc-500 cursor-pointer">
        <div className="flex items-start justify-between">
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <FileText size={18} className="text-white" />

              <h3 className="font-medium text-white text-lg">{title}</h3>
            </div>
            <Badge variant="secondary">{type}</Badge>
          </div>
        </div>
        <p className="text-sm text-muted-foreground mt-3">{description}</p>
      </Card>
    </Link>
  );
}
