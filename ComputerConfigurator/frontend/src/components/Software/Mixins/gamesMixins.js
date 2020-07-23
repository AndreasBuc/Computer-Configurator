import axios from "axios";
export const gamesMixin = {

  data() {
    return {
      games: [],
      gamesIn: [],
    }
  },
  methods: {
    async getGames() {
      try {
        const response = await axios.get('games/');
        this.games = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getGamesIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        this.gamesIn = response.data.games;
      } catch (error) {
        console.error(error);
      }
    },
    removeClonedAt(idx) {
      console.log(this.gamesIn[idx].id);
      this.removeGame(this.gamesIn[idx].id)
      this.games.unshift(this.gamesIn[idx])

      this.gamesIn.splice(idx, 1);
    },
    onGameDrop(evt) {
      window.console.log(evt.added.element.id);
      this.addGame(evt.added.element.id)
    },
    async addGame(game_id) {
      try {
        const response = await axios.post(`add-or-remove-a-game/${game_id}/${this.configurator_id}/`, {});
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    },
    async removeGame(game_id) {
      try {
        const response = await axios.delete(`add-or-remove-a-game/${game_id}/${this.configurator_id}/`);
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getGamesIn();
    this.getGames();

  },
  computed: {
    gamesRemaining() {

      this.gamesIn.forEach((gameIn) => {
        this.games.forEach((game, index) => {
          if (gameIn.id == game.id) {
            this.games.splice(index, 1);
          }
        });
      });
      return this.games
    },
  },
}
