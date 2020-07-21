<template>
  <tr v-if="cpu">
    <td>{{count}}</td>
    <td>{{cpu.name}}</td>
    <td>{{cpu.kernel}}</td>
    <td>{{cpu.speed}}</td>
    <td>{{cpu.price}}</td>
  </tr>
</template>

<script>
// import  from "@/components/"
import axios from "axios"
export default {
  name: 'CPU',
  props: {
    id: Number,
    count: Number,
  },
  components: {

  },
  data() {
    return {
      cpu: null,
    }
  },
  methods: {
    async getCPU() {
      try {
        const response = await axios.get(`cpu/${this.id}/`);
        console.log(response);
        this.cpu=response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getCPU()
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
