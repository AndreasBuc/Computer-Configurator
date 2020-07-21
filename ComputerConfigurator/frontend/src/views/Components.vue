<template>
  <div class="Components">
    <h1
      class="mb-3"
      data-toggle="collapse"
      data-target="#Hardware"
      aria-expanded="true"
      aria-controls="Hardware"
      style="cursor:pointer"
    >Hardware</h1>
    <div class="collapse show" id="Hardware">
    <CPUs></CPUs>
    <GraphicCards></GraphicCards>
    </div>
    <h1
    class="mb-3"
    data-toggle="collapse"
    data-target="#Software"
    aria-expanded="true"
    aria-controls="Software"
    style="cursor:pointer"
    >Software</h1>
    <div class="collapse show" id="Software">
    <Games></Games>
    <OperatingSystems></OperatingSystems>
    <OfficeWares></OfficeWares>
    </div>
  </div>
</template>

<script>
import CPUs from "@/components/Hardware/CPUs"
import GraphicCards from "@/components/Hardware/GraphicCards"
import Games from "@/components/Software/Games"
import OperatingSystems from "@/components/Software/OperatingSystems"
import OfficeWares from "@/components/Software/OfficeWares"

export default {
  name: 'Components',
  props: {

  },
  components: {
    CPUs,
    GraphicCards,
    Games,
    OperatingSystems,
    OfficeWares,
  },
  data() {
    return {

    }
  },
  methods: {

  },
  // created() {
  //
  // },
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
