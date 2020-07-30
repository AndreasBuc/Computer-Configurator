<template>
  <div id="app" class="maxHeight">
    <Navigation></Navigation>
    <router-view />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation"
import {mapActions} from 'vuex';
import {mapGetters} from 'vuex';
export default {
  name: 'App',
  props: {

  },
  components: {
    Navigation,
  },
  data() {
    return {

    }
  },
  methods: {
    ...mapActions({
      setUser: 'setUser',
      setConf: 'setConf',
    }),
  },
  created() {
    this.setUser();
    this.setConf();
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

<style>
a { cursor: pointer }
.maxHeight {
    height: 100%;
}
</style>
