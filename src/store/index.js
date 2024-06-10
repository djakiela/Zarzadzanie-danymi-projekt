import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    currentUser: null,
  },
  mutations: {
    setUser(state, user) {
      state.currentUser = user;
    },
    clearUser(state) {
      state.currentUser = null;
    },
  },
  actions: {
    async fetchCurrentUser({ commit }) {
      try {
        const response = await axios.get(
          "http://127.0.0.1:5000/api/current_user",
          {
            withCredentials: true,
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
          }
        );
        commit("setUser", response.data.username);
      } catch (error) {
        if (error.response) {
          // Serwer odpowiedział kodem statusu, który jest poza zakresem 2xx
          console.error("Error response:", error.response.data);
          console.error("Error status:", error.response.status);
          console.error("Error headers:", error.response.headers);
        } else if (error.request) {
          // Żądanie zostało wysłane, ale brak odpowiedzi
          console.error("Error request:", error.request);
        } else {
          // Coś się stało przy ustawianiu żądania, wyzwolenie błędu
          console.error("Error message:", error.message);
        }
        console.error("Error config:", error.config);
      }
    },
  },
});
