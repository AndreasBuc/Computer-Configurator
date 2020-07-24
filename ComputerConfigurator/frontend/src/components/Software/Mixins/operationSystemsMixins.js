import axios from "axios";
export const operationSystemsMixin = {

  data() {
    return {
      operationSystems: [],
      operationSystemsIn: [],
    }
  },
  methods: {
    async getOperatinSystems() {
      try {
        const response = await axios.get('operating-systems/');
        this.checkOperatinSystemIn();
        this.operationSystems = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async checkOperatinSystemIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        if (response.data.operating_system != null) {
          this.getOperatinSystemIn()
        }
        } catch (error) {
        console.error(error);
      }
    },
    async getOperatinSystemIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        this.operationSystemsIn.unshift(response.data.operating_system_detail);
        } catch (error) {
        console.error(error);
      }
    },
    async onOperatingSystemDrop(evt) {
      this.operationSystemsIn.forEach((operationSystemIn, index) => {
        if(operationSystemIn.id != evt.added.element.id) {
          this.operationSystems.unshift(operationSystemIn);
          this.operationSystemsIn.splice(index, 1);
        }
      });
      try {
        await axios.patch(`users-configurator/${this.configurator_id}/`,{"operating_system": evt.added.element.id});
      } catch (error) {
        console.error(error);
      }
    },
    async removeClonedOperationSystemsInAt(idx) {
      this.operationSystems.unshift(this.operationSystemsIn[idx])
      this.operationSystemsIn.splice(idx, 1);
      try {
        await axios.patch(`users-configurator/${this.configurator_id}/`,{"operating_system": null});
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.getOperatinSystems()
  },
  computed: {
    remainingOperationSystems() {
      this.operationSystemsIn.forEach((item) => {
        this.operationSystems.forEach((element, i) => {
          if(item.id == element.id) {
            this.operationSystems.splice(i,1)
          }
        });

      });
      return this.operationSystems;
    },
  },
}
