'use client';

import { useEffect, useState } from 'react';

import { getChat, sendMessage } from '@/lib/chat';

import { Chat } from '@/types/chat';

import ChatSidebar from '@/component/chat/ChatSidebar';

import { Input } from '@/components/ui/input';

import { Button } from '@/components/ui/button';

type Props = {
  params: Promise<{
    id: string;
  }>;
};

export default function ChatPage({ params }: Props) {
  const [chat, setChat] = useState<Chat | null>(null);

  const [loading, setLoading] = useState(true);

  const [message, setMessage] = useState('');

  const [sending, setSending] = useState(false);

  useEffect(() => {
    async function load() {
      const { id } = await params;

      try {
        const data = await getChat(Number(id));

        console.log('CHAT DATA', data);

        setChat(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [params]);

  async function handleSend() {
    if (!chat || !message.trim()) return;

    try {
      setSending(true);

      await sendMessage(chat.id, message);

      const updatedChat = await getChat(chat.id);

      setChat(updatedChat);

      setMessage('');
    } catch (error) {
      console.error(error);
    } finally {
      setSending(false);
    }
  }

  if (loading) {
    return <div className="p-8">Loading...</div>;
  }

  if (!chat) {
    return <div className="p-8">Chat not found</div>;
  }

  return (
    <div className="h-full flex">
      <ChatSidebar />

      <div className="flex-1 flex flex-col p-8">
        {/* Header */}
        <div>
          <h1 className="text-3xl font-semibold">{chat.title}</h1>

          <p className="text-sm text-muted-foreground mt-2">
            Chat with your knowledge source
          </p>
        </div>

        {/* Messages */}
        <div className="mt-8 flex-1 min-h-0 overflow-y-auto rounded-xl border border-border bg-card/30 p-6">
          <div className="space-y-6">
            {chat.messages.length === 0 && (
              <div className="text-center text-muted-foreground py-12">
                Ask your first question about this document.
              </div>
            )}

            {chat.messages.map((message, index) => (
              <div
                key={index}
                className={`max-w-4xl rounded-xl p-4 shadow-sm  ${
                  message.role === 'user'
                    ? 'ml-auto border border-border bg-zinc-900'
                    : 'mr-auto bg-gray-800 text-white'
                }`}
              >
                <div className="text-xs uppercase tracking-wide opacity-70 mb-2">
                  {message.role}
                </div>

                <div className="whitespace-pre-wrap">{message.content}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Input */}
        <div className="mt-4 flex gap-3 border-t border-border pt-4">
          <Input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask about this document..."
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !sending) {
                handleSend();
              }
            }}
          />

          <Button
            onClick={handleSend}
            disabled={sending}
            className="bg-white text-black"
          >
            {sending ? 'Sending...' : 'Send'}
          </Button>
        </div>
      </div>
    </div>
  );
}
