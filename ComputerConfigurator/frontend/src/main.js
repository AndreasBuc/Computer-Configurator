import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from 'axios'
import { CSRF_TOKEN } from "@/common/csrf_token.js"

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
axios.defaults.headers.common['X-CSRFTOKEN'] = CSRF_TOKEN;


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
