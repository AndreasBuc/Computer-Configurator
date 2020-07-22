<template>
  <div class="Configurator">
    <div class="row">
      <!-- SIDEBAR -->
      <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
        <div class="sidebar-sticky pt-3">
          <ul class="nav flex-column">
            <li class="nav-item">
              <a
                class="nav-link active"
                data-toggle="collapse"
                data-target="#Games"
                aria-expanded="true"
                aria-controls="Games"
                style="cursor:pointer"
              >
                 <div class="orange"><i class="fa fa-gamepad" aria-hidden="true"></i> Games</div>
              </a>
            </li>
          </ul>

          <div id="Games">
            <ul class="nav flex-column" >
              <!-- START DRAG SIDEBAR -->
              <draggable
                class="dragArea list-group"
                :list="games"
                :group="{ name: 'people', pull: 'clone', put: false }"
                @change="log"
              >
              <div
                  class=" "
                  v-for="(game, index) in gamesRemaining"
                  :key="index"
                  >
                <a class="nav-link active">
                   <small class="anotherorange">{{game.name}}</small>
                </a>
              </div>
              </draggable>
              <!-- END DRAG SIDEBAR -->

            </ul>
          </div>
        </div>
      </nav>
      <!-- CONFIGURATOR -->
      <div class="col-md-9 ml-sm-auto col-lg-10 px-md-4 center-text">
        <h1>Configurator</h1>
        <h5 class="lead">Total Cost: {{cost}} €</h5>
        <hr>
        <!-- START DRAG CONFIGURATOR -->
        <draggable
          v-if="gamesIn"
          class="dragArea list-group"
          v-model="gamesIn"
          @change="log"
          group="people"
        >
          <div class="list-group-item" v-for="(element, idx) in gamesIn" :key="element.id">
            {{ element.name }} ({{element.price}} €)
            <i class="fa fa-times close" @click="removeClonedAt(idx)"></i>
          </div>
        </draggable>
        <!-- END DRAG CONFIGURATOR -->
      </div>
    </div>
  </div>
</template>

<script>
// import  from "@/components/"
import draggable from "vuedraggable";
import axios from "axios";
export default {
  name: 'Configurator',
  props: {

  },
  components: {
    draggable,
  },
  data() {
    return {
      games: [],
      gamesIn: [],
      configurator_id: 1,
    }
  },
  methods: {
    async getGames() {
      try {
        const response = await axios.get('games/');
        this.games=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getGamesIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        this.gamesIn =response.data.games;
      } catch (error) {
        console.error(error);
      }
    },
    log(evt) {
      window.console.log(evt.added.element.id);
      this.addGame(evt.added.element.id)
    },
    removeClonedAt(idx) {
      console.log(this.gamesIn[idx].id);
      this.removeGame(this.gamesIn[idx].id)
      this.games.unshift(this.gamesIn[idx])

      this.gamesIn.splice(idx, 1);
    },
    async addGame(game_id) {
      try {
        const response = await axios.post(`add-or-remove-a-game/${game_id}/${this.configurator_id}/`, {});
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    },
    async removeGame(game_id) {
      try {
        const response = await axios.delete(`add-or-remove-a-game/${game_id}/${this.configurator_id}/`);
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getGamesIn();
    this.getGames();

  },
  computed: {
    cost() {
      let sum = 0;
      for (let game of this.gamesIn) {
        sum += game.price;
      }
      return sum
    },
    gamesRemaining() {

      this.gamesIn.forEach( ( gameIn ) => {
        this.games.forEach( (game, index) => {
            if(gameIn.id == game.id) {
              this.games.splice(index,1);
            }
        });
      });
      return this.games
    },
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
.Configurator {
  height: 100%
}
nav {
  height: 100%
}
.row {
  height: 100%
}
.center-text{
  text-align: center;
}
.orange:hover{
  color: rgb(182, 114, 56)
}
.anotherorange:hover{
  color: rgb(241, 165, 100)
}
i {
  cursor:pointer;
}

</style>
