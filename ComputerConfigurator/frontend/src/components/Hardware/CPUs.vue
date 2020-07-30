<template>
  <div class="CPUs">
    <div class="d-flex justify-content-between">
      <h3>Processors</h3>

    </div>
    <!-- Modal -->
    <div class="modal fade" id="cpuModal" tabindex="-1" role="dialog" aria-labelledby="CPUsModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="CPUsModalLabel">Add Processor</h5>
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
            <button v-if="sendOK" type="button" @click="addCPU" data-dismiss="modal" class="btn btn-primary">Save</button>
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
      <th scope="col">Kernel</th>
      <th scope="col">Speed [GHz]</th>
      <th scope="col">Price [€]</th>
      <th scope="col"><i class="fa fa-plus-square-o fa-lg ml-3 orange" data-toggle="modal" data-target="#cpuModal"></i></th>
    </tr>
    <CPU
      v-for="(cpu, index) in cpus"
        :key="cpu.id"
        :id="cpu.id"
        :count="CounterCPU-index"
    ></CPU>
  </thead>
  <tbody>

  </tbody>
</table>




  </div>
</template>

<script>
import CPU from "@/components/Hardware/CPU";
import axios from "axios";
export default {
  name: 'CPUs',
  props: {

  },
  components: {
    CPU,
  },
  data() {
    return {
      cpus: [],
      cpu: {},
    }
  },
  methods: {
    async getCPUs() {
      try {
        const response = await axios.get('cpu-ids/');
        this.cpus=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addCPU() {
      if((this.cpu.manufacturer != undefined && this.cpu.manufacturer != "") && (this.cpu.model != undefined && this.cpu.model != "")) {
        try {
          const response = await axios.post('cpu/', this.cpu);
          console.log(response);
          this.cpu = {};
          this.cpus.unshift(response.data)
        } catch (error) {
          console.error(error);
        }
      }
    },
  },
  created() {
    this.getCPUs()
  },
  computed: {
    CounterCPU() {
      return this.cpus.length
    },
    sendOK() {
      if((this.cpu.manufacturer != undefined && this.cpu.manufacturer != "") && (this.cpu.model != undefined && this.cpu.model != "")) {
        return true;
      } else {
        return false;
      }
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

</style>
