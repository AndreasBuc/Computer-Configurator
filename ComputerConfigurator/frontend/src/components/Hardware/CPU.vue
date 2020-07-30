<template>
  <tr v-if="cpu">
    <td>{{count}}</td>
    <td>{{cpu.name}}</td>
    <td>{{cpu.kernel}}</td>
    <td>{{cpu.speed}}</td>
    <td>{{cpu.price}}</td>
    <td>
      <div class="d-flex flex-row">
        <i class="fa fa-edit close mx-auto" data-toggle="modal" :data-target="CpuModalID"></i>
        <i class="fa fa-times close mx-auto" @click="deleteCPU"></i>
        <!-- Modal -->
        <div class="modal fade" :id="'CPU'+cpu.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Edit Processor</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <input v-model="cpu.manufacturer" class="form-control my-1" type="text" id="Manufacturer" placeholder="Manufacturer">
                <label for="Manufacturer">Edit Manufacturer</label>
                <input v-model="cpu.model" class="form-control my-1" type="text" id="model" placeholder="Model">
                <label for="model">Edit Model</label>
                <input v-model="cpu.kernel" class="form-control my-1" type="Number" id="Kernel" placeholder="Kernel">
                <label for="Kernel">Edit Kernel</label>
                <input v-model="cpu.speed" class="form-control my-1" step="0.1" type="Number" id="Speed" placeholder="Speed">
                <label for="Speed">Edit Speed</label>
                <input v-model="cpu.price" class="form-control my-1" type="Number" id="Price" placeholder="Price">
                <label for="Price">Edit Price</label>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" @click="updateCPU" data-dismiss="modal" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </td>
  </tr>
</template>

<script>
// import  from "@/components/"
import axios from "axios"
export default {
  name: 'CPU',
  props: {
    id: Number,
    count: Number,
  },
  components: {

  },
  data() {
    return {
      cpu: null,
    }
  },
  methods: {
    async getCPU() {
      try {
        const response = await axios.get(`cpu/${this.id}/`);
        this.cpu=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async updateCPU() {
      try {
        const response = await axios.put(`cpu/${this.id}/`, this.cpu);
        this.cpu=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async deleteCPU() {
      try {
        const response = await axios.delete(`cpu/${this.id}/`);
        this.cpu=response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getCPU()
  },
  computed: {
    CpuModalID() {
      return `#CPU${this.id}`
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
