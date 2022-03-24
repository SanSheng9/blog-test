export const state = () => ({
  user: {},
  loggedIn: "",
  posts: {},
});

export const mutations = {
  setUser(state, payload) {
    state.user = payload;
  },
  setPost(state, payload) {
    state.posts = payload;
  },
};

export const actions = {
  // USER
  async fetchUsers({ commit }) {
    try {
      const response = await fetch("http://localhost:8000/api/user", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });
      const content = await response.json();
      commit("setUser", content);
    } catch (e) {
      console.log("Auth is bad.., error: ", e);
    }
  },
  // POSTS
  async axiosPost() {
    let response = await $axios.get("/api/posts");
    commit("setPosts", response.data);
  },
};

export const getters = {
  getUser: (state) => state.users,
  getPosts: (state) => state.posts,
};
