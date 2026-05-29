import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

export default function SignupForm() {
  return (
    <div className="space-y-4">
      <Input placeholder="Name" />
      <Input placeholder="Email" />
      <Input type="password" placeholder="password" />

      <Button className="w-full cursor-pointer">Create Account</Button>
    </div>
  );
}
