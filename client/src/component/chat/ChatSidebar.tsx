'use client';

import { useEffect, useState } from 'react';

import Link from 'next/link';

import { getChats } from '@/lib/chat';

import { ChatListItme } from '@/types/chat';

export default function ChatSidebar() {
  const [chats, setChats] = useState<ChatListItme[]>([]);

  useEffect(() => {
    async function loadChats() {
      try {
        const data = await getChats();

        setChats(data);
      } catch (error) {
        console.error(error);
      }
    }
    loadChats();
  }, []);

  return (
    <div className="w-72 border-r border-border p-4">
      <h2 className="font-semibold mb-4">Chats</h2>

      <div className="space-y-">
        {chats.map((chat) => (
          <Link
            key={chat.id}
            href={`/dashboard/chat/${chat.id}`}
            className="block rounded-lg border border-border p-3 hover:bg-card"
          >
            <p className="text-sm truncate"></p>
          </Link>
        ))}
      </div>
    </div>
  );
}
