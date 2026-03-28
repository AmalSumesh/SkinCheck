import axios from 'axios';

const api = axios.create({
    // baseURL: 'https://skin-cancer-classification-gpqz.onrender.com',
    baseURL: 'http://localhost:5000',
});

export default api;