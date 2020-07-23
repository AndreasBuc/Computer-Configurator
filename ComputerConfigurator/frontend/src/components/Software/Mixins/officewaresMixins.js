import axios from "axios";
export const officewaresMixin = {

  data() {
    return {
      officewares: [],
      officewaresIn: [],
    }
  },
  methods: {
    async getOfficewares() {
      try {
        const response = await axios.get('officewares/');
        this.officewares = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getOfficewaresIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        this.officewaresIn = response.data.officeware;
      } catch (error) {
        console.error(error);
      }
    },
    removeClonedOfficewaresInAt(idx) {
      console.log(this.officewaresIn[idx].id);
      this.removeOfficeWare(this.officewaresIn[idx].id)
      this.officewares.unshift(this.officewaresIn[idx])

      this.officewaresIn.splice(idx, 1);
    },
    onOfficeWareDrop(evt) {
      window.console.log(evt.added.element.id);
      this.addOfficeware(evt.added.element.id)
    },
    async addOfficeware(ow_id) {
      try {
        const response = await axios.post(`add-or-remove-a-officeware/${ow_id}/${this.configurator_id}/`, {});
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    },
    async removeOfficeWare(ow_id) {
      try {
        const response = await axios.delete(`add-or-remove-a-officeware/${ow_id}/${this.configurator_id}/`);
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getOfficewaresIn();
    this.getOfficewares();

  },
  computed: {
    officewaresRemaining() {

      this.officewaresIn.forEach((officewareIn) => {
        this.officewares.forEach((officeware, index) => {
          if (officewareIn.id == officeware.id) {
            this.officewares.splice(index, 1);
          }
        });
      });
      return this.officewares
    },
  },
}
