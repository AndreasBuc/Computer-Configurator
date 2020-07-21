<template>
  <div class="Games">
    <h3>Games</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Price [€]</th>
        </tr>
      </thead>
      <tbody>
        <Game
            v-for="(game, index) in games"
            :key="game.id"
            :index="CounterGames - index"
            :id="game.id"
        ></Game>
      </tbody>
    </table>

  </div>
</template>

<script>
import Game from "@/components/Software/Game.vue";
import axios from "axios";
export default {
  name: 'Games',
  props: {

  },
  components: {
    Game
  },
  data() {
    return {
      games: [],
    }
  },
  methods: {
    async getGames() {
      try {
        const response = await axios.get('games-ids/');
        console.log(response);
        this.games=response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.getGames()
  },
  computed: {
    CounterGames() {
      return this.games.length;
    }
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
