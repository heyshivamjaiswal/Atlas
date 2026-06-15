import { create } from 'zustand';

type User = {
  id?: number;
  email: string;
};

type AuthState = {
  token: string | null;
  user: User | null;

  setToken: (token: string) => void;

  setUser: (user: User) => void;

  logout: () => void;
};

export const useAuthStore = create<AuthState>((set) => ({
  token: null,

  user: null,

  setToken: (token) => {
    localStorage.setItem('atlas_token', token);

    set({ token });
  },

  setUser: (user) => {
    set({ user });
  },

  logout: () => {
    localStorage.removeItem('atlas_token');

    set({
      token: null,
      user: null,
    });
  },
}));
