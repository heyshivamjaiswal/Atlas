type Props = {
  params: Promise<{
    id: string;
  }>;
};

export default async function DocumentPage({ params }: Props) {
  const { id } = await params;

  return (
    <div className="p-8">
      <h1 className="text-3xl font-semibold">Document {id}</h1>
    </div>
  );
}
