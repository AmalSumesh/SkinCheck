import axios from 'axios';

const api = axios.create({
    baseURL: 'https://skin-cancer-classification-gpqz.onrender.com',
});

export default api;