Hardware/<template>
  <div class="GraphicCards">
    <div class="d-flex justify-content-between">
      <h3>Graphic Cards</h3>

    </div>
    <!-- Modal -->
    <div class="modal fade" id="gcModal" tabindex="-1" role="dialog" aria-labelledby="GCsModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="GCsModalLabel">Add Graphic Card</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">

            <div class="row mb-3">
              <div class="col-12">
              </div>
              <div class="col">
                <input v-model="gc.manufacturer" class="form-control my-1" type="text" placeholder="Manufacturer*">
              </div>
              <div class="col">
                <input v-model="gc.model" class="form-control my-1" type="text" placeholder="Model*">
              </div>
              <div class="col-12">
                <small class="form-text text-muted">Manufacturer and Model form the Name.</small>
              </div>
            </div>
            <small class="form-text text-muted">Memory Size:</small>
            <input v-model="gc.memory_size" class="form-control my-1" type="Number" placeholder="Memory Size">

            <small class="form-text text-muted">Price:</small>
            <input v-model="gc.price" class="form-control my-1" type="Number" placeholder="Price">

          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button v-if="sendOK" type="button" @click="addGC" data-dismiss="modal" class="btn btn-primary">Save</button>
            <button v-if="!sendOK" type="button" data-dismiss="modal" class="btn btn-primary" disabled>Save</button>
          </div>
        </div>
      </div>
    </div>
    <table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Memory Size [GB]</th>
        <th scope="col">Price [€]</th>
        <th scope="col"><i class="fa fa-plus-square-o fa-lg orange ml-2" data-toggle="modal" data-target="#gcModal"></i></th>
      </tr>
    </thead>
    <tbody>
      <GraphicCard
          v-for="(gc, index) in graphic_cards"
          :key="gc.id"
          :id="gc.id"
          :index="CounterCPU - index"
      ></GraphicCard>
    </tbody>
</table>

  </div>
</template>

<script>
import GraphicCard from "@/components/Hardware/GraphicCard"
import axios from "axios";
export default {
  name: 'GraphicCards',
  props: {

  },
  components: {
    GraphicCard,
  },
  data() {
    return {
      graphic_cards: [],
      gc: {},
    }
  },
  methods: {
    async getGC() {
      try {
        const response = await axios.get('graphic-cards-ids/');
        this.graphic_cards=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addGC() {
      if((this.gc.manufacturer != undefined && this.gc.manufacturer != "") && (this.gc.model != undefined && this.gc.model != "")) {
        try {
          const response = await axios.post('graphic-cards/', this.gc);
          console.log(response);
          this.gc = {};
          this.graphic_cards.unshift(response.data)
        } catch (error) {
          console.error(error);
        }
      }
    },
  },
  created() {
    this.getGC()
  },
  computed: {
    CounterCPU() {
      return this.graphic_cards.length
    },
    sendOK() {
      if((this.gc.manufacturer != undefined && this.gc.manufacturer != "") && (this.gc.model != undefined && this.gc.model != "")) {
        return true;
      } else {
        return false;
      }
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
