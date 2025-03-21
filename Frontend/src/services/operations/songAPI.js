import { apiConnector } from "../apiConnector";
import { songEndpoints } from "../apis";

const { GENERATE_LYRICS, CHECK_GUESS } = songEndpoints;

export async function generateLyrics() {
    try {
        const response = await apiConnector('GET', GENERATE_LYRICS);
        return response.data;
    } catch (error) {
        return error;
    }
}

export async function checkGuess(data) {
    try {
        const response = await apiConnector('POST', CHECK_GUESS, data);
        return response.data;
    } catch (error) {
        return error;
    }
}