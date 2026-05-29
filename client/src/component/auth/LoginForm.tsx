import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

export default function LoginForm() {
  return (
    <div className="space-y-4">
      <Input placeholder="Email" />

      <Input type="password" placeholder="password" />

      <Button className="w-full">Login</Button>
      <Button variant="outline" className="w-full cursor-pointer">
        Try Demo Workspace
      </Button>
    </div>
  );
}
