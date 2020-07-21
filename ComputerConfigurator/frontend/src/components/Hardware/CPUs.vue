<template>
  <div class="CPUs">
    <h3>Processors</h3>
    <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Name</th>
      <th scope="col">Kernel</th>
      <th scope="col">Speed [GHz]</th>
      <th scope="col">Price [€]</th>
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
    }
  },
  methods: {
    async getCPUs() {
      try {
        const response = await axios.get('cpu-ids/');
        console.log(response);
        this.cpus=response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getCPUs()
  },
  computed: {
    CounterCPU() {
      return this.cpus.length
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
