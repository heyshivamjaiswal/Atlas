'use client';

import LoginForm from '@/component/auth/LoginForm';
import SignupForm from '@/component/auth/SignupForm';
import { useState } from 'react';

export default function AuthPage() {
  const [mode, setMode] = useState<'login' | 'signup'>('login');

  return (
    <div className="min-h-screen flex items-center justify-center bg-background">
      <div className="w-[420px] rounded-xl flex flex-col items-center border border-border bg-card p-8">
        <h1 className="text-2xl font-semibold">Atlas</h1>

        <p className="text-muted-foreground mt-2">
          Build your knowledge workspace
        </p>

        <div className="mt-6">
          {mode === 'login' ? (
            <LoginForm />
          ) : (
            <SignupForm onSuccess={() => setMode('login')} />
          )}
        </div>

        <button
          className="mt-6 text-sm text-muted-foreground cursor-pointer"
          onClick={() => setMode(mode === 'login' ? 'signup' : 'login')}
        >
          {mode == 'login'
            ? 'Need account? Signup'
            : 'Already have account ? Login'}
        </button>
      </div>
    </div>
  );
}
