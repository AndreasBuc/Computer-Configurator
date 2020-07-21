<template>
  <div class="OperatingSystems">
    <h3>OperatingSystem</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Price [€]</th>
        </tr>
      </thead>
      <tbody>
        <OperatingSystem
            v-for="(operatingSystem, index) in operatingSystems"
            :key="operatingSystem.id"
            :index="counterOperatingSystem - index"
            :id="operatingSystem.id"
        ></OperatingSystem>
      </tbody>
    </table>
  </div>
</template>

<script>
import OperatingSystem from "@/components/Software/OperationSystem";
import axios from "axios";
export default {
  name: 'OperatingSystems',
  props: {

  },
  components: {
    OperatingSystem,
  },
  data() {
    return {
      operatingSystems: []
    }
  },
  methods: {
    async getOperatingSystems() {
      try {
        const response = await axios.get('operating-systems-ids/');
        console.log(response);
        this.operatingSystems=response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.getOperatingSystems();
  },
  computed: {
    counterOperatingSystem() {
      return this.operatingSystems.length
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
