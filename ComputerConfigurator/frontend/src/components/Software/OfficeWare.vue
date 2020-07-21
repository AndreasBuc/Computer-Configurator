<template>

    <tr v-if="officeware" class="OfficeWare">
      <th scope="row">{{index}}</th>
      <td>{{officeware.name}}</td>
      <td>{{officeware.price}}</td>
    </tr>

</template>

<script>
// import  from "@/components/"
import axios from "axios";
export default {
  name: 'OfficeWare',
  props: {
    index: Number,
    id: Number,
  },
  components: {

  },
  data() {
    return {
      officeware: null,
    }
  },
  methods: {
    async getOfficeWare() {
      try {
        const response = await axios.get(`officewares/${this.id}/`);
        console.log('Ich bin in OfficeWare');
        this.officeware=response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.getOfficeWare();
  },
  // computed: {
  //
  // },
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
