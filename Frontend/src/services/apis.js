const API_URL = `${import.meta.env.VITE_SERVER_URL}/api/v1`;

export const songEndpoints = {
    GENERATE_LYRICS: `${API_URL}/random-lyric`,
    CHECK_GUESS: `${API_URL}/check-guess`,
};