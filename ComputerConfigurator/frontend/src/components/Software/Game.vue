<template>

    <tr v-if="game" class="Game">
      <th>{{index}}</th>
      <td>{{game.name}}</td>
      <td>{{game.price}}</td>
      <td>
        <div class="d-flex flex-row">
          <i class="fa fa-edit mx-auto" data-toggle="modal" :data-target="GameModalID"></i>
          <i class="fa fa-times mx-auto" @click="deleteGame"></i>
        </div>
      </td>

      <!-- Modal -->
      <div class="modal fade" :id="'Game'+id" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLongTitle">Edit Game</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-group">
                  <label >Name of the Game</label>
                  <input v-model="game.name" type="email" class="form-control" aria-describedby="gameHelp" placeholder="Enter a Name">
                </div>
                <div class="form-group">
                  <label >What does it cost</label>
                  <input v-model="game.price" type="Number" class="form-control" placeholder="Enter a Price">
                </div>
                  <input type="file" @change="onFileSelected" class="btn btn-outline-dark" id="validatedCustomFile" required>
                <!-- Geht leider nicht mit Model -.- -->
                <!-- <input @change="onFileSelected" type="file" style="display:none" ref="fileInput">
                <button @click="$refs.fileInput.click()" class="btn btn-outline-dark">Choose File</button> -->
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              <button type="button" @click="updateGame" class="btn btn-primary" data-dismiss="modal">Save</button>
            </div>
          </div>
        </div>
      </div>



    </tr>


</template>

<script>
// import  from "@/components/"
import axios from "axios";
export default {
  name: 'Game',
  props: {
    index: Number,
    id: Number
  },
  components: {

  },
  data() {
    return {
      game: null,
    }
  },
  methods: {
    async getGame() {
      try {
        const response = await axios.get(`games/${this.id}/`);
        this.game=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async updateGame() {
      if(this.game.name != undefined && this.game.name != "") {
        try {
          const response = await axios.put(`games/${this.id}/`, this.game);
          this.game=response.data;
        } catch (error) {
          console.error(error);
        }
      }
    },
    async deleteGame() {
      try {
        const response = await axios.delete(`games/${this.id}/`);
        this.game=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    onFileSelected() {
      // TODO: Hier weiterarbeiten!!
    },
  },
  created() {
    this.getGame();
  },
  computed: {
    GameModalID() {
      return `#Game${this.id}`
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
