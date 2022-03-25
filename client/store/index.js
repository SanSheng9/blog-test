export const state = () => ({
  user: {},
  loggedIn: false,
});

export const mutations = {
  setUser(state, payload) {
    state.user = payload;
  },
  setLoggedIn(state, payload) {
    state.loggedIn = payload;
  },
};

export const actions = {
  // USER
  fetchUser(content, { commit }) {
    commit("setUser", content);
  },
  fetchLoggedIn(content, { commit }) {
    commit("setLoggedIn", content);
  },
};

export const getters = {
  getUser: (state) => state.user,
  getLoggedIn: (state) => state.loggedIn,
};
