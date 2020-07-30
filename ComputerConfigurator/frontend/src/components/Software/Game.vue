<template>


    <tr v-if="game" class="Game">
      <th>{{index}}</th>
      <td>{{game.name}}</td>
      <td>{{game.price}}</td>
    </tr>


</template>

<script>
// import  from "@/components/"
import axios from "axios";
export default {
  name: 'Game',
  props: {
    index: Number,
    id: Number
  },
  components: {

  },
  data() {
    return {
      game: null,
    }
  },
  methods: {
    async getGame() {
      try {
        const response = await axios.get(`games/${this.id}/`);
        this.game=response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.getGame();
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
