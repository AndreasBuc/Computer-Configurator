<template>
<div class="Configurator">
  <div class="row">
    <!-- SIDEBAR -->
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="sidebar-sticky pt-3">
        <ul class="nav flex-column">

          <!-- START SOFTWARE -->
          <li class="nav-item">
            <div class="nav-link active">
              <h3> Software</h3>
            </div>
          </li>
        </ul>

        <!-- START GAMES -->
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active collapse Software" data-toggle="collapse" data-target=".Games" aria-expanded="true" aria-controls="Games" style="cursor:pointer">
              <div class="orange"><i class="fa fa-gamepad mr-1" aria-hidden="true"></i> Games</div>
            </a>
          </li>
        </ul>

        <div class="Games">
          <ul class="nav flex-column">
            <!-- START DRAG SIDEBAR -->
            <draggable class="dragArea list-group" :list="games" :group="{ name: 'games', pull: 'clone', put: false }" @change="log">
              <div class=" " v-for="(game, index) in gamesRemaining" :key="index">
                <a class="nav-link active">
                  <small class="anotherorange">{{game.name}}</small>
                </a>
              </div>
            </draggable>
            <!-- END DRAG SIDEBAR -->

          </ul>
        </div>
        <!-- END GAMES -->

        <!-- START OFFICEWARE -->
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active collapse Software" data-toggle="collapse" data-target=".OfficeWare" aria-expanded="true" aria-controls="OfficeWare" style="cursor:pointer">
              <div class="orange"><i class="fa fa-file mr-1" aria-hidden="true"></i> OfficeWare</div>
            </a>
          </li>
        </ul>

        <div class="OfficeWare">
          <ul class="nav flex-column">
            <!-- START DRAG SIDEBAR -->
            <draggable class="dragArea list-group" :list="officewares" :group="{ name: 'officewares', pull: 'clone', put: false }" @change="log">
              <div class=" " v-for="(officeware, index) in officewaresRemaining" :key="index">
                <a class="nav-link active">
                  <small class="anotherorange">{{officeware.name}}</small>
                </a>
              </div>
            </draggable>
            <!-- END DRAG SIDEBAR -->

          </ul>
        </div>
        <!-- END OFFICEWARE -->
        <!-- END SOFTWARE -->
        <!-- END SIDEBAR -->

      </div>
    </nav>
    <!-- CONFIGURATOR -->
    <div class="col-md-9 ml-sm-auto col-lg-10 px-md-4 center-text">
      <h1>Configurator</h1>
      <h5 class="lead">Total Cost: {{cost}} €</h5>
      <hr>
      <!-- START DRAG CONFIGURATOR -->
      <h3 class="mt-2">Games</h3>
      <div class="Games">
        <draggable v-if="gamesIn" class="dragArea list-group" v-model="gamesIn" @change="onGameDrop" group="games">
          <div class="list-group-item" v-for="(element, idx) in gamesIn" :key="element.id">
            {{ element.name }} ({{element.price}} €)
            <i class="fa fa-times close" @click="removeClonedAt(idx)"></i>
          </div>
        </draggable>
      </div>
      <h3 class="mt-4">office Wares</h3>
      <div class="Office Ware">
        <draggable v-if="officewaresIn" class="dragArea list-group" v-model="officewaresIn" @change="onOfficeWareDrop" group="officewares">
          <div class="list-group-item" v-for="(element, idx) in officewaresIn" :key="element.id">
            {{ element.name }} ({{element.price}} €)
            <i class="fa fa-times close" @click="removeClonedOfficewaresInAt(idx)"></i>
          </div>
        </draggable>
      </div>
      <!-- END DRAG CONFIGURATOR -->
    </div>
  </div>
</div>
</template>

<script>
// import  from "@/components/"
import draggable from "vuedraggable";
import { gamesMixin } from "@/components/Software/Mixins/gamesMixins.js"
import { officewaresMixin } from "@/components/Software/Mixins/officewaresMixins.js"
export default {
  name: 'Configurator',
  props: {

  },
  components: {
    draggable,
  },
  mixins: [gamesMixin, officewaresMixin],
  data() {
    return {
      configurator_id: 1,
    }
  },
  methods: {

  },
  computed: {
    cost() {
      let sum = 0;
      for (let game of this.gamesIn) {
        sum += game.price;
      }
      return sum
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

.center-text {
  text-align: center;
}

.orange:hover {
  color: rgb(182, 114, 56)
}

.anotherorange:hover {
  color: rgb(241, 165, 100)
}

i {
  cursor: pointer;
}
</style>
