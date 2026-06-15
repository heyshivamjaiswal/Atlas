'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

import { login } from '@/lib/auth';

export default function LoginForm() {
  const router = useRouter();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [loading, setLoading] = useState(false);

  async function handleLogin() {
    try {
      setLoading(true);

      const data = await login(email, password);

      localStorage.setItem('atlas_token', data.access_token);

      router.push('/dashboard');
    } catch (error) {
      console.error(error);

      alert('Login failed');
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

      <Button className="w-full" disabled={loading} onClick={handleLogin}>
        {loading ? 'Logging in...' : 'Login'}
      </Button>

      <Button variant="outline" className="w-full">
        Try Demo Workspace
      </Button>
    </div>
  );
}
