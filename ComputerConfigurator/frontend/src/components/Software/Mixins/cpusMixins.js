import axios from "axios";
export const cpusMixin = {

  data() {
    return {
      cpus: [],
      cpusIn: [],
    }
  },
  methods: {
    async getCpus() {
      try {
        const response = await axios.get('cpu/');
        this.checkCpuIn();
        this.cpus = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async checkCpuIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        if (response.data.cpu != null) {
          this.getCpuIn()
        }
        } catch (error) {
        console.error(error);
      }
    },
    async getCpuIn() {
      try {
        const response = await axios.get(`users-configurator/${this.configurator_id}/`);
        this.cpusIn.unshift(response.data.cpu_detail);
        } catch (error) {
        console.error(error);
      }
    },
    async onCpuDrop(evt) {
      this.cpusIn.forEach((cpuIn, index) => {
        if(cpuIn.id != evt.added.element.id) {
          this.cpus.unshift(cpuIn);
          this.cpusIn.splice(index, 1);
        }
      });
      try {
        await axios.patch(`users-configurator/${this.configurator_id}/`,{"cpu": evt.added.element.id});
      } catch (error) {
        console.error(error);
      }
    },
    async removeClonedCpusInAt(idx) {
      this.cpus.unshift(this.cpusIn[idx])
      this.cpusIn.splice(idx, 1);
      try {
        await axios.patch(`users-configurator/${this.configurator_id}/`,{"cpu": null});
      } catch (error) {
        console.error(error);
      }
    },
    resetCpusData() {
      this.cpus= [];
      this.cpusIn= [];
      this.getCpus();
    }
  },
  created() {
    this.getCpus()
  },
  computed: {
    remainingCpus() {
      this.cpusIn.forEach((item) => {
        this.cpus.forEach((element, i) => {
          if(item.id == element.id) {
            this.cpus.splice(i,1)
          }
        });

      });
      return this.cpus;
    },
  },
}
