<template>
  <tr v-if="operatingSystem" class="OperatingSystem">
      <th scope="row">{{index}}</th>
      <td>{{operatingSystem.name}}</td>
      <td>{{operatingSystem.price}}</td>
    </tr>
</template>

<script>
// import  from "@/components/"
import axios from "axios";
export default {
  name: 'OperatingSystem',
  props: {
    index: Number,
    id: Number,
  },
  components: {

  },
  data() {
    return {
      operatingSystem: null,
    }
  },
  methods: {
    async getOperatingSystem() {
      try {
        const response = await axios.get(`operating-systems/${this.id}/`);
        console.log(response);
        this.operatingSystem=response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.getOperatingSystem();
  },
  // computed: {
  //
  // },
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
