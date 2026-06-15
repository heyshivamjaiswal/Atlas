import { api } from './api';

export async function getSources(search?: string) {
  const response = await api.get('/source', {
    params: {
      search,
    },
  });

  return response.data;
}

export async function getSourceStats() {
  const response = await api.get('/source/stats');

  return response.data;
}
