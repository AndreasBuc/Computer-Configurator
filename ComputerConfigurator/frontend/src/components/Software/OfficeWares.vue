<template>
  <div class="OfficeWares">
    <h3>Office Ware</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Price [€]</th>
        </tr>
      </thead>
      <tbody>
        <OfficeWare
            v-for="(officeware, index) in officewares"
            :key="officeware.id"
            :index="counterOfficeware - index"
            :id="officeware.id"
        ></OfficeWare>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import OfficeWare from "@/components/Software/OfficeWare"
export default {
  name: 'OfficeWares',
  props: {

  },
  components: {
    OfficeWare,
  },
  data() {
    return {
      officewares: [],
    }
  },
  methods: {
    async getOfficeWares() {
      try {
        const response = await axios.get('officewares-ids/');
        console.log(response);
        this.officewares=response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
  this.getOfficeWares()
  },
  computed: {
    counterOfficeware() {
      return this.officewares.length
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
