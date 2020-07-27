<template>
<div class="Configurator">
  <div class="row">
    <!-- SIDEBAR -->
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="sidebar-sticky pt-3">
        <ul class="nav flex-column">
          <!-- START HARDWARE -->
          <ul class="nav flex-column">
            <li class="nav-item">
              <a class="nav-link active collapse Software" data-toggle="collapse" data-target=".CPU" aria-expanded="true" aria-controls="CPU" style="cursor:pointer">
                <div class="orange"><i class="fa fa-gamepad mr-1" aria-hidden="true"></i> CPU</div>
              </a>
            </li>
          </ul>

          <!-- END HARDWARE -->
          <!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  -->
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
            <draggable class="dragArea list-group"
                  :list="games"
                  :group="{ name: 'games', pull: 'clone', put: false }"
                  @change="log"
                  @start="gameDrag = true"
                  @end="gameDrag = false"
                  >
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
            <draggable
                class="dragArea list-group"
                :list="officewares"
                :group="{ name: 'officewares', pull: 'clone', put: false }"
                @change="log">
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

        <!-- START OPERATING SYSTEMS -->
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active collapse Software" data-toggle="collapse" data-target=".OperatingSystem" aria-expanded="true" aria-controls="OperatingSystem" style="cursor:pointer">
              <div class="orange"><i class="fa fa-file mr-1" aria-hidden="true"></i> OperatingSystem</div>
            </a>
          </li>
        </ul>

        <div class="OperatingSystem">
          <ul class="nav flex-column">
            <!-- START DRAG SIDEBAR -->
            <draggable
                :list="operationSystems"
                class="dragArea list-group"
                :group="{ name: 'operatingSystemsGroup', pull: 'clone', put: false }"
                @change="log">
              <div v-for="(operationSystem, index) in remainingOperationSystems" :key="index">
                <a class="nav-link active">
                  <small class="anotherorange">{{operationSystem.name}}</small>
                </a>
              </div>
            </draggable>
            <!-- END DRAG SIDEBAR -->
          </ul>
        </div>
        <!-- END OPERATING SYSTEMS -->

        <!-- END SOFTWARE -->
        <!-- END SIDEBAR -->

      </div>
    </nav>
    <!-- CONFIGURATOR -->

    <div class="col-md-9 ml-sm-auto col-lg-10 px-md-4 center-text">
      <h1>Configurator</h1>
      <h3 class="lead">Total Cost: {{cost}} €</h3>

      <div class="container">
        <ul class="d-flex justify-content-between ">
          <p class="nav-item active">Software: </p>
          <p class="nav-item active">Games: {{costGames}} €</p>
          <p class="nav-item active">Office Ware: {{costOfficeWare}} €</p>
          <p class="nav-item active">Operating System: {{costoperationSystems}} €</p>
        </ul>
      </div>

      <hr>
      <!-- START CONFIG GAME -->
      <h1>Software</h1>

      <div class="row">

      <div class="col-lg-4 col-sm-12">
        <div class="orange" data-toggle="collapse" data-target=".Games" aria-expanded="true" aria-controls="Games" style="cursor:pointer">
          <h3 class="mt-2">Games</h3>
        </div>
        <div class="Games" :style="gameDrag ? drag_box : ''">
          <draggable v-if="gamesIn" class="dragArea list-group collapse" v-model="gamesIn" @change="onGameDrop" group="games" >
            <div class="list-group-item" v-for="(element, idx) in gamesIn" :key="element.id">
              {{ element.name }} ({{element.price}} €)
              <i class="fa fa-times close" @click="removeClonedAt(idx)"></i>
            </div>
          </draggable>
        </div>
      </div>
        <!-- END CONFIG OFFICEWARE -->

        <!-- START CONFIG OFFICEWARE -->
        <div class="col-lg-4 col-sm-12">
          <div class="orange" data-toggle="collapse" data-target=".OfficeWare" aria-expanded="true" aria-controls="Games" style="cursor:pointer">
            <h3 class="mt-2">Office Wares</h3>
            </div>
            <div class="OfficeWare">
              <draggable
                  v-if="officewaresIn"
                  class="dragArea list-group"
                  v-model="officewaresIn"
                  @change="onOfficeWareDrop"
                  group="officewares">
                <div class="list-group-item" v-for="(element, idx) in officewaresIn" :key="element.id">
                  {{ element.name }} ({{element.price}} €)
                  <i class="fa fa-times close" @click="removeClonedOfficewaresInAt(idx)"></i>
                </div>
              </draggable>
          </div>
        </div>
        <!-- END CONFIG OFFICEWARE -->

        <!-- START CONFIG OPERATINGSYSTEM -->
        <div class="col-lg-4 col-sm-12">
          <div class="orange" data-toggle="collapse" data-target=".OperatingSystem" aria-expanded="true" aria-controls="Games" style="cursor:pointer">
            <h3 class="mt-2">Operationsystem</h3>
          </div>


          <div class="OperatingSystem">
            <draggable
                  v-if="operationSystemsIn"
                  class="dragArea list-group"
                  v-model="operationSystemsIn"
                  @change="onOperatingSystemDrop"
                  group="operatingSystemsGroup">
              <div class="list-group-item" v-for="(element, idx) in operationSystemsIn" :key="element.id">
                {{ element.name }} ({{element.price}} €)
                <i class="fa fa-times close" @click="removeClonedOperationSystemsInAt(idx)"></i>
              </div>
            </draggable>
        </div>
      </div>
      </div>
      <!-- END CONFIG OPERATINGSYSTEM -->

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
import { operationSystemsMixin } from "@/components/Software/Mixins/operationSystemsMixins.js"

export default {
  name: 'Configurator',
  props: {
    
  },
  components: {
    draggable,
  },
  mixins: [gamesMixin, officewaresMixin, operationSystemsMixin],
  data() {
    return {
      configurator_id: 1,
      drag_box: "border: solid 1px rgb(182, 114, 56); opacity: 0.5",
    }
  },
  methods: {
    log: function(evt) {
      window.console.log(evt);
    }
  },
  computed: {
    costGames() {
      let sum = 0;
      for (let game of this.gamesIn) {
        sum += game.price;
      }
      return sum
    },
    costOfficeWare() {
      let sum = 0;
      for (let officeWare of this.officewaresIn) {
        sum += officeWare.price;
      }
      return sum
    },
    costoperationSystems() {
      let sum = 0;
      for (let operationSystem of this.operationSystemsIn) {
        sum += operationSystem.price;
      }
      return sum
    },
    cost() {
      let sum = 0;
      for (let game of this.gamesIn) {
        sum += game.price;
      }
      for (let officeWare of this.officewaresIn) {
        sum += officeWare.price;
      }
      for (let operationSystem of this.operationSystemsIn) {
        sum += operationSystem.price;
      }
      return sum
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
