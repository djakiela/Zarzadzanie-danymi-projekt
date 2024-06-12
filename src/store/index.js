import { createStore } from "vuex";

const store = createStore({
  state: {
    user: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    login({ commit }, user) {
      commit("setUser", user);
    },
  },
  getters: {
    user: (state) => state.user,
  },
});

export default store;
