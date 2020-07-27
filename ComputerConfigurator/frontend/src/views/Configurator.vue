<template>
<div class="Configurator">
  <div class="row">
    <!-- SIDEBAR -->
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="sidebar-sticky pt-3">
        <ul class="nav flex-column">
          <!-- START HARDWARE -->
          <!-- START CPU -->
          <ul class="nav flex-column">
            <li class="nav-item">
              <a class="nav-link active collapse Software" data-toggle="collapse" data-target=".Cpu" aria-expanded="true" aria-controls="Cpu" style="cursor:pointer">
                <div class="orange">CPU</div>
              </a>
            </li>
          </ul>

          <div class="Cpu">
            <ul class="nav flex-column">
              <!-- START DRAG SIDEBAR -->
              <draggable
                  :list="cpus"
                  class="dragArea list-group"
                  :group="{ name: 'CpusGroup', pull: 'clone', put: false }"
                  @change="log">
                <div v-for="(cpu, index) in remainingCpus" :key="index">
                  <a class="nav-link active">
                    <small class="anotherorange">{{cpu.name}}</small>
                  </a>
                </div>
              </draggable>
              <!-- END DRAG SIDEBAR -->
            </ul>
          </div>
          <!-- END CPU -->
          <!-- START GraphicCard -->
          <ul class="nav flex-column">
            <li class="nav-item">
              <a class="nav-link active collapse Software" data-toggle="collapse" data-target=".graphicCards" aria-expanded="true" aria-controls="graphicCards" style="cursor:pointer">
                <div class="orange">Graphic Card</div>
              </a>
            </li>
          </ul>

          <div class="graphicCards">
            <ul class="nav flex-column">
              <!-- START DRAG SIDEBAR -->
              <draggable
                  :list="graphicCards"
                  class="dragArea list-group"
                  :group="{ name: 'graphicCardsGroup', pull: 'clone', put: false }"
                  @change="log">
                <div v-for="(graphicCard, index) in remaininggraphicCards" :key="index">
                  <a class="nav-link active">
                    <small class="anotherorange">{{graphicCard.name}}</small>
                  </a>
                </div>
              </draggable>
              <!-- END DRAG SIDEBAR -->
            </ul>
          </div>
          <!-- END GraphicCard -->

          <!-- END HARDWARE -->
          <!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  -->
          <!-- START SOFTWARE -->

        </ul>

        <!-- START GAMES -->
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active collapse Software" data-toggle="collapse" data-target=".Games" aria-expanded="true" aria-controls="Games" style="cursor:pointer">
              <div class="orange">Games</div>
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
              <div class="orange">OfficeWare</div>
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
              <div class="orange">OperatingSystem</div>
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
      <h1>{{name}}</h1>
      <h3 class="lead">Total Cost: {{cost}} €</h3>

      <div class="container">
        <ul class="d-flex justify-content-between ">
          <p class="nav-item active">Software: </p>
          <p class="nav-item active">Games: {{costGames}} €</p>
          <p class="nav-item active">Office Ware: {{costOfficeWare}} €</p>
          <p class="nav-item active">Operating System: {{costoperationSystems}} €</p>
        </ul>
        <ul class="d-flex justify-content-between ">
          <p class="nav-item active">Hardware: </p>
          <p class="nav-item active">CPU: {{costCPU}} €</p>
          <p class="nav-item active">Graphic Card: {{costgraphicCard}} €</p>

        </ul>
      </div>

      <hr>

      <!-- START CONFIG GAME -->

      <div class="row d-flex align-items-baseline">
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
          <div class="col-lg-4 col-12">
            <div class="row">
              <div class="col-lg-12 col-sm-12">
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
              <!-- START CONFIG CPU -->
              <div class="col-lg-12 col-sm-12">
                  <div class="orange" data-toggle="collapse" data-target=".Cpu" aria-expanded="true" aria-controls="Games" style="cursor:pointer">
                    <h3 class="mt-2">CPU</h3>
                  </div>
                  <div class="Cpu">
                    <draggable
                          v-if="cpusIn"
                          class="dragArea list-group"
                          v-model="cpusIn"
                          @change="onCpuDrop"
                          group="CpusGroup">
                      <div class="list-group-item" v-for="(element, idx) in cpusIn" :key="element.id">
                        {{ element.name }} ({{element.price}} €)
                        <i class="fa fa-times close" @click="removeClonedCpusInAt(idx)"></i>
                      </div>
                    </draggable>
                </div>
              </div>
              <!-- END CONFIG CPU -->

              <!-- START CONFIG GRAPHIC CARDS -->
              <div class="col-lg-12 col-sm-12">
                <div class="orange" data-toggle="collapse" data-target=".Cpu" aria-expanded="true" aria-controls="Games" style="cursor:pointer">
                  <h3 class="mt-2">Graphic Cards</h3>
                </div>
                <div class="Cpu">
                  <draggable
                        v-if="graphicCardsIn"
                        class="dragArea list-group"
                        v-model="graphicCardsIn"
                        @change="ongraphicCardDrop"
                        group="graphicCardsGroup">
                    <div class="list-group-item" v-for="(element, idx) in graphicCardsIn" :key="element.id">
                      {{ element.name }} ({{element.price}} €)
                      <i class="fa fa-times close" @click="removeClonedgraphicCardsInAt(idx)"></i>
                    </div>
                  </draggable>
              </div>
              </div>
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
import { cpusMixin } from "@/components/Software/Mixins/cpusMixins.js"
import { graphicCardsMixin } from "@/components/Software/Mixins/graphicCardsMixins.js"

export default {
  name: 'Configurator',
  props: ['configId', 'name'],
  components: {
    draggable,
  },
  mixins: [gamesMixin, officewaresMixin, operationSystemsMixin, cpusMixin, graphicCardsMixin],
  data() {
    return {
      configurator_id: this.configId,
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
    costCPU() {
      let sum = 0;
      for (let cpu of this.cpusIn) {
        sum += cpu.price;
      }
      return sum
    },
    costgraphicCard() {
      let sum = 0;
      for (let graphicCard of this.graphicCardsIn) {
        sum += graphicCard.price;
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
      for (let cpu of this.cpusIn) {
        sum += cpu.price;
      }
      for (let graphicCard of this.graphicCardsIn) {
        sum += graphicCard.price;
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
  beforeRouteUpdate (to, from, next) {
    this.configurator_id = to.params.configId

    this.resetGamesData();
    this.resetOfficeWareData();
    this.resetOperatingSystemsData();
    this.resetCpusData()()
    //
  next();
  },
//   beforeRouteLeave (to, from, next) {
//
//   next();
// },
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
