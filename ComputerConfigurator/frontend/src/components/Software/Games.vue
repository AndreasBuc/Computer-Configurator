<template>
  <div class="Games">
    <div class="d-flex justify-content-between">
      <h3>Games</h3>

    </div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Price [€]</th>
          <th scope="col"><i class="fa fa-plus-square-o ml-2 fa-lg" data-toggle="modal" data-target="#gamesModel"></i></th>
        </tr>
      </thead>
      <tbody>
        <Game
            v-for="(game, index) in games"
            :key="game.id"
            :index="CounterGames - index"
            :id="game.id"
        ></Game>
      </tbody>
    </table>

    <!-- Modal -->
    <div class="modal fade" id="gamesModel" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">New Game</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="gameName">Name of the Game</label>
                <input v-model="name" type="email" class="form-control" id="gameName" aria-describedby="gameHelp" placeholder="Enter a Name">
              </div>
              <div class="form-group">
                <label for="Price">What does it cost</label>
                <input v-model="price" type="Number" class="form-control" id="Price" placeholder="Enter a Price">
              </div>
                <input type="file" @change="onFileSelected" class="btn btn-outline-dark" id="validatedCustomFile" required>
              <!-- Geht leider nicht mit Model -.- -->
              <!-- <input @change="onFileSelected" type="file" style="display:none" ref="fileInput">
              <button @click="$refs.fileInput.click()" class="btn btn-outline-dark">Choose File</button> -->
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" @click="addnewGame" class="btn btn-primary" data-dismiss="modal">Save</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Game from "@/components/Software/Game.vue";
import axios from "axios";
export default {
  name: 'Games',
  props: {

  },
  components: {
    Game
  },
  data() {
    return {
      games: [],
      name: null,
      price: null,
      image: null,
    }
  },
  methods: {
    async getGames() {
      try {
        const response = await axios.get('games-ids/');
        this.games=response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addnewGame() {
      if(this.name != null && this.name != "") {
        try {
          const response = await axios.post('games/', {"name":this.name, "price":this.price});
          console.log(response);
          if(this.image != null) {
            this.uploadPicture(response.data.id);
          }
          this.games.unshift(response.data)
        } catch (error) {
          console.error(error);
        }
      }
    },
    async uploadPicture(id) {

        const fd = new FormData();
        fd.append('image', this.image, this.image.name)
        try {
          const response = await axios.post(`games/${id}/upload-image/`, fd, {
            onUploadProgress: uploadEvent => {
              console.log('Upload Progress: ' + Math.round(uploadEvent.loaded / uploadEvent.total * 100) + '%')
            }
          });
          console.log(response);
          this.games.forEach(game => {
            if(game.id == response.data.id) {
              game.image = response.data.image;
            }
          });
        } catch (error) {
          console.error(error);
        }
        this.image=null;
    },
    onFileSelected(event) {
      console.log(event);
      this.image = event.target.files[0];
    },
  },
  created() {
    this.getGames()
  },
  computed: {
    CounterGames() {
      return this.games.length;
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
.orange:hover {
  color: rgb(182, 114, 56)
}
</style>
