Hardware/<template>
  <div class="GraphicCards">
    <h3>Graphic Cards</h3>
    <table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Memory Size [GB]</th>
        <th scope="col">Price [€]</th>
        <th scope="col"></th>
      </tr>
    </thead>
    <tbody>
      <GraphicCard
          v-for="(gc, index) in graphic_cards"
          :key="gc.id"
          :id="gc.id"
          :index="CounterCPU - index"
      ></GraphicCard>
    </tbody>
</table>

  </div>
</template>

<script>
import GraphicCard from "@/components/Hardware/GraphicCard"
import axios from "axios";
export default {
  name: 'GraphicCards',
  props: {

  },
  components: {
    GraphicCard,
  },
  data() {
    return {
      graphic_cards: [],
    }
  },
  methods: {
    async getGC() {
      try {
        const response = await axios.get('graphic-cards-ids/');
        this.graphic_cards=response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.getGC()
  },
  computed: {
    CounterCPU() {
      return this.graphic_cards.length
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
