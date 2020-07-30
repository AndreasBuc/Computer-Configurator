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
            <div v-if="getConf" >
              <a class="dropdown-item" v-for="config in getConf" :key="config.id">
                <router-link class="nav-link active" :to="{name: 'Configurator', params: {configId: config.id, name: config.name}}">
                  {{config.name}}
                </router-link>
              </a>
            </div>
            <hr>
            <div class="d-flex flex-row">
              <input v-model="newConfig" class="form-control ml-2" style="width:80%" :placeholder="placeholder" type="text" name="" value="">
              <i class="fa fa-plus-square-o fa-lg my-auto mx-auto orange" style="cursor:pointer" @click="addnewConfig"></i>
            </div>
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
      newConfig: "",
      placeholder: 'new config'
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
    },
    async addnewConfig() {
      if (this.newConfig) {
        try {
          const response = await axios.post('users-configurator-basics/', {'name': this.newConfig});
          this.newConfig = "";
          this.getConfigs();
          this.$router.push({
            name: 'Configurator',
            params: {
              configId: response.data.id,
              name: response.data.name
            }})
        } catch (error) {
          console.error(error);
        }
      }
    }
  },
  created() {
    this.getConfigs();
  },
  computed: {
    ...mapGetters([
      'getUser',
      'getConf',
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
.orange:hover {
  color: rgb(182, 114, 56)
}
</style>
