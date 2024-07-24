import axios from "axios";

const api = await axios.create({
    baseUrl: 'http://localhost:8001/memes',
})

export default api;