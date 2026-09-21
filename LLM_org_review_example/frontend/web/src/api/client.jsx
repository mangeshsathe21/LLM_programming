import axios from "axios"

const api_client_handle = axios.create({
    baseURL : "http://127.0.0.1:8000/",
    timeout : 0,
    headers:{
        "Content-Type" : "application/json",
    },
});

export default api_client_handle;