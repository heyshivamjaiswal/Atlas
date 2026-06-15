'use client';

import { useState } from 'react';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

import { signup } from '@/lib/auth';

type Props = {
  onSuccess?: () => void;
};

export default function SignupForm({ onSuccess }: Props) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [loading, setLoading] = useState(false);

  async function handleSignup() {
    try {
      setLoading(true);

      await signup(email, password);

      alert('Account created. Please login.');

      onSuccess?.();
    } catch (error) {
      console.error(error);

      alert('Signup failed');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-4">
      <Input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <Input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <Button className="w-full" disabled={loading} onClick={handleSignup}>
        {loading ? 'Creating...' : 'Create Account'}
      </Button>
    </div>
  );
}
