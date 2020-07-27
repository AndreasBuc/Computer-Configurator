import Vue from "vue";
import VueRouter from "vue-router";
import Configurator from "@/views/Configurator";
import Component from "@/views/Components";
import Homepage from "@/views/Homepage";
Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Homepage',
    component: Homepage
  },
  {
    path: '/Configurator/',
    name: 'Configurator',
    component: Configurator,
    props: true
  },
  {
    path: '/Components',
    name: 'Component',
    component: Component
  },

];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
