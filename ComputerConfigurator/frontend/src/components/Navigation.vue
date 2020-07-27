<template>
<div class="Navigation">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">

    <router-link class="navbar-brand" :to="{name: 'Homepage'}">
      Homepage
    </router-link>

    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse container" id="navbarSupportedContent">

      <ul class="navbar-nav mr-auto">

        <li class="nav-item dropdown active">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Configurations
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" v-for="config in configs" :key="config.id">
              <router-link class="nav-link active" :to="{name: 'Configurator', params: {configId: config.id, name: config.name}}">
                {{config.name}}
              </router-link>
            </a>
          </div>
        </li>

        <li class="nav-item active">
          <router-link class="nav-link active" :to="{name: 'Component'}">
            Component Shop
          </router-link>
        </li>
      </ul>
      <ul class="navbar-nav ml-auto">
        <li v-if="getUser" class="nav-item active">
          <a class="nav-link" href="/accounts/login/" @click="logout">
            Logout
          </a>
        </li>
      </ul>
    </div>
  </nav>
</div>
</template>

<script>
// import  from "@/components/"
import {
  mapActions
} from "vuex";
import {
  mapGetters
} from "vuex";
import axios from 'axios';
export default {
  name: 'Navigation',
  props: {

  },
  components: {

  },
  data() {
    return {
      configs: [],
    }
  },
  methods: {
    ...mapActions({
      unsetUser: 'unsetUser'
    }),
    logout() {
      axios.post('rest-auth/logout/', {});
      this.unsetUser();
    },
    async getConfigs() {
      try {
        const response = await axios.get('users-configurator-basics/');
        this.configs = response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.getConfigs();
  },
  computed: {
    ...mapGetters([
      'getUser',
    ])
  },
  // destroyed() {
  //
  // },
  // deactivated() {
  //
  // },
  // activated() {
  //
  // },
  // beforeRouteEnter(to, from, next) {
  //
  //   return next(vm => {
  //
  //     });
  //   next();
  // },
  // beforeRouteUpdate (to, from, next) {
  // next();
  // },
  // beforeRouteLeave (to, from, next) {
  // next();
  // }
}
</script>

<style scoped>

</style>
