export type Message = {
  role: string;
  content: string;
};

export type Chat = {
  id: number;
  title: string;
  messages: Message[];
};

export type ChatListItme = {
  id: number;
  title: string;
  created_at: string;
};
