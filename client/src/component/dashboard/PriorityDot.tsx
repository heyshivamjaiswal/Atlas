type prop = {
  priority: 'high' | 'medium' | 'low';
};

export default function PriorityDot({ priority }: prop) {
  const colors = {
    high: 'bg-red-500',
    medium: 'bg-orange-500',
    low: 'bg-green-500',
  };

  return <div className={`h-3 w-3 rounded-full ${colors[priority]}`}></div>;
}
