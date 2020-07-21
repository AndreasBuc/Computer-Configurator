import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
  },
  getters: {
    getUser: (state) => {
      return state.user
    },
  },
  mutations: {
    setUser: (state, user) => {
      state.user = user;
    },
    unsetUser: (state) => {
      state.user = null;
    }
  },
  actions: {
    setUser: async ({commit}) => {
      try {
        const response = await axios.get('rest-auth/user/');
        commit('setUser', response.data)
      } catch (error) {
        console.error(error);
      }

    },
    unsetUser: ({commit}) => {
      commit('unsetUser')
    }
  },
  modules: {}
});
