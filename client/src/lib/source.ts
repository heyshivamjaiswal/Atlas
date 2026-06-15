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

export async function uploadPdf(file: File) {
  const formData = new FormData();

  formData.append('file', file);

  const response = await api.post('/source/pdf', formData);

  return response.data;
}

export async function uploadWebsite(url: string) {
  const response = await api.post('/source/web', {
    url,
  });

  return response.data;
}

export async function uploadYoutube(url: string) {
  const response = await api.post('/source/youtube', {
    url,
  });

  return response.data;
}

export async function getSource(id: number) {
  const response = await api.get(`/source/${id}`);

  return response.data;
}

export async function getSourceChunks(id: number) {
  const response = await api.get(`/source/${id}/chunks`);

  return response.data;
}
