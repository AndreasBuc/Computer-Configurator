import axios from "axios";
export const graphicCardsMixin = {

  data() {
    return {
      graphicCards: [],
      graphicCardsIn: [],
    }
  },
  methods: {
    async getgraphicCards() {
      try {
        const response = await axios.get('graphic-cards/');
        this.checkgraphicCardIn();
        this.graphicCards = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async checkgraphicCardIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        if (response.data.grafic_card != null) {
          this.getgraphicCardIn()
        }
        } catch (error) {
        console.error(error);
      }
    },
    async getgraphicCardIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        this.graphicCardsIn.unshift(response.data.graphic_cards_detail);
        } catch (error) {
        console.error(error);
      }
    },
    async ongraphicCardDrop(evt) {
      this.graphicCardsIn.forEach((graphicCardIn, index) => {
        if(graphicCardIn.id != evt.added.element.id) {
          this.graphicCards.unshift(graphicCardIn);
          this.graphicCardsIn.splice(index, 1);
        }
      });
      try {
        await axios.patch(`users-configurator/${this.configurator_id}/`,{"grafic_card": evt.added.element.id});
      } catch (error) {
        console.error(error);
      }
    },
    async removeClonedgraphicCardsInAt(idx) {
      this.graphicCards.unshift(this.graphicCardsIn[idx])
      this.graphicCardsIn.splice(idx, 1);
      try {
        await axios.patch(`users-configurator/${this.configurator_id}/`,{"grafic_card": null});
      } catch (error) {
        console.error(error);
      }
    },
    resetgraphicCardsData() {
      this.graphicCards= [];
      this.graphicCardsIn= [];
      this.getgraphicCards();
    }
  },
  created() {
    this.getgraphicCards()
  },
  computed: {
    remaininggraphicCards() {
      this.graphicCardsIn.forEach((item) => {
        this.graphicCards.forEach((element, i) => {
          if(item.id == element.id) {
            this.graphicCards.splice(i,1)
          }
        });

      });
      return this.graphicCards;
    },
  },
}
