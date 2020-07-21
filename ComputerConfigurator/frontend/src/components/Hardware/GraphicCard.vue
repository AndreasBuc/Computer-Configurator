<template>
  <tr v-if="gc">
    <th >{{index}}</th>
    <td>{{gc.name}}</td>
    <td>{{gc.memory_size}}</td>
    <td>{{gc.price}}</td>
  </tr>
</template>

<script>
import axios from "axios";
export default {
  name: 'GraphicCard',
  props: {
    id: Number,
    index: Number,
  },
  components: {

  },
  data() {
    return {
      gc: null,
    }
  },
  methods: {
    async getGC() {
      try {
        const response = await axios.get(`graphic-cards/${this.id}/`);
        console.log(response);
        this.gc = response.data;
      } catch (error) {
        console.error(error);
      }
}
  },
  created() {
    this.getGC()
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
