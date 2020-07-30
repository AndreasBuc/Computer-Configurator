<template>
  <tr v-if="cpu">
    <td>{{count}}</td>
    <td>{{cpu.name}}</td>
    <td>{{cpu.kernel}}</td>
    <td>{{cpu.speed}}</td>
    <td>{{cpu.price}}</td>
    <td>
      <div class="d-flex flex-row">
        <i class="fa fa-edit mx-auto" data-toggle="modal" :data-target="CpuModalID"></i>
        <i class="fa fa-times mx-auto" @click="deleteCPU"></i>
        <!-- Modal -->
        <div class="modal fade" :id="'CPU'+cpu.id" tabindex="-1" role="dialog" aria-labelledby="CPUModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="CPUModalLabel">Edit Processor</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">

                <div class="row mb-3">
                  <div class="col-12">
                  </div>
                  <div class="col">
                    <input v-model="cpu.manufacturer" class="form-control my-1" type="text" placeholder="Manufacturer*">
                  </div>
                  <div class="col">
                    <input v-model="cpu.model" class="form-control my-1" type="text" placeholder="Model*">
                  </div>
                  <div class="col-12">
                    <small class="form-text text-muted">Manufacturer and Model form the Name.</small>
                  </div>
                </div>
                <small class="form-text text-muted">Kernel:</small>
                <input v-model="cpu.kernel" class="form-control my-1" type="Number" placeholder="Kernel">
                <small class="form-text text-muted">Speed:</small>
                <input v-model="cpu.speed" class="form-control my-1" step="0.1" type="Number" placeholder="Speed">
                <small class="form-text text-muted">Price:</small>
                <input v-model="cpu.price" class="form-control my-1" type="Number" placeholder="Price">
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
