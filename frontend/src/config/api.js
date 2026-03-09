const apiHost = import.meta.env.VITE_API_HOST || "127.0.0.1";
const apiPort = import.meta.env.VITE_API_PORT || "8080";

export const API_BASE_URL = `http://${apiHost}:${apiPort}`;
