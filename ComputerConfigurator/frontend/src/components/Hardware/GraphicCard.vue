<template>
  <tr v-if="gc">
    <th >{{index}}</th>
    <td>{{gc.name}}</td>
    <td>{{gc.memory_size}}</td>
    <td>{{gc.price}}</td>
    <td>
      <div class="d-flex flex-row">
        <i class="fa fa-edit close mx-auto" data-toggle="modal" :data-target="GraphicCardModalID"></i>
        <i class="fa fa-times close mx-auto" @click="deleteGraphicCard"></i>
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
                <input v-model="gc.manufacturer" class="form-control my-1" type="text" id="Manufacturer" placeholder="Manufacturer">
                <label for="Manufacturer">Edit Manufacturer</label>

                <input v-model="gc.model" class="form-control my-1" type="text" id="model" placeholder="Model">
                <label for="model">Edit Model</label>

                <input v-model="gc.memory_size" class="form-control my-1" type="Number" id="Kernel" placeholder="Kernel">
                <label for="Kernel">Edit Kernel</label>

                <input v-model="gc.price" class="form-control my-1" type="Number" id="Price" placeholder="Price">
                <label for="Price">Edit Price</label>
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
      try {
        const response = await axios.put(`graphic-cards//${this.id}/`, this.gc);
        this.gc=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async deleteGraphicCard() {
      try {
        const response = await axios.delete(`graphic-cards//${this.id}/`);
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
