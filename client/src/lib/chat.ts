import { api } from './api';

export async function createChat(title: string, sourceIds: number[]) {
  const response = await api.post('/chat', {
    title,
    source_ids: sourceIds,
  });

  return response.data;
}

export async function getChat(sessionId: number) {
  const response = await api.get(`/chat/${sessionId}`);

  return response.data;
}

export async function sendMessage(sessionId: number, message: string) {
  const response = await api.post(`/chat/${sessionId}/message`, {
    message,
  });

  return response.data;
}

export async function getChats() {
  const response = await api.get('/chat');

  return response.data;
}
