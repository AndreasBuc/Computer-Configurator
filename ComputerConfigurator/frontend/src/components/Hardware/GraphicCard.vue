<template>
  <tr v-if="gc">
    <th >{{index}}</th>
    <td>{{gc.name}}</td>
    <td>{{gc.memory_size}}</td>
    <td>{{gc.price}}</td>
    <td>
      <div class="d-flex flex-row">
        <i class="fa fa-edit mx-auto" data-toggle="modal" :data-target="GraphicCardModalID"></i>
        <i class="fa fa-times mx-auto" @click="deleteGraphicCard"></i>
        <!-- Modal -->
        <div class="modal fade" :id="'GC'+gc.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Edit Graphic Card</h5>
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
                <button type="button" @click="updateGraphicCard" data-dismiss="modal" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </td>
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
        this.gc = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async updateGraphicCard() {
      if((this.gc.manufacturer != undefined && this.gc.manufacturer != "") && (this.gc.model != undefined && this.gc.model != "")) {
      try {
        const response = await axios.put(`graphic-cards/${this.id}/`, this.gc);
        this.gc=response.data;
      } catch (error) {
        console.error(error);
      }
    }
    },
    async deleteGraphicCard() {
      try {
        const response = await axios.delete(`graphic-cards/${this.id}/`);
        this.gc=response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getGC()
  },
  computed: {
    GraphicCardModalID() {
      return `#GC${this.id}`
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
