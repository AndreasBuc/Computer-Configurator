import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    configs: null,
  },
  getters: {
    getUser: (state) => {
      return state.user;
    },
    getConf: (state) => {
      console.log(state.configs)
      return state.configs;
    },
  },
  mutations: {
    setConf: (state, conf) => {
      state.configs = conf;
    },
    setUser: (state, user) => {
      state.user = user;
    },
    unsetUser: (state) => {
      state.user = null;
    }
  },
  actions: {
    setConf: async ({commit}) => {
      try {
        const response = await axios.get('users-configurator-basics/');
        commit('setConf', response.data)
      } catch (error) {
        console.error(error);
      }
    },
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
    },
  },
  modules: {}
});
