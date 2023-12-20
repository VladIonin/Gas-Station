<script>
import axios from "axios";

export default {
  data() {
    return {
      stationId: '',
      showStationInfo: false,
      isNewStation: false,
      invalidId: false,
      stationInfo: {
        station: {},
        data: []
      }
    };
  },
  methods: {
    getFuelCardHeaderClass(fuelType) {
      switch (fuelType) {
        case '92':
          return 'bg-danger text-white';
        case '95':
          return 'bg-success text-white';
        case '98':
          return 'bg-primary text-white';
        case 'DF':
          return 'bg-dark text-white';
        default:
          return 'bg-warning text-white';
      }
    },
    loadStationData() {
      this.baseForm()

      if (isNaN(this.stationId) || this.stationId < 1 || this.stationId > 99) {
        this.invalidId = true;
        return;
      }

      const apiUrl = `http://127.0.0.1:8080/getStationInfo/?id=${this.stationId}`;

      axios.get(apiUrl)
          .then(response => {
            this.stationInfo = response.data;
            this.showStationInfo = true;
          })
          .catch(error => {
            this.status = error.response.status
            if (error.response && error.response.status === 404) {
              this.stationInfo.station.station_id = this.stationId
              this.isNewStation = true;
              this.showStationInfo = true;
            } else {
              console.error('Error loading data:', error);
            }
          });
    },
    saveChanges() {
      const apiUrl = 'http://127.0.0.1:8080/setStation/';

      const postData = {
        id: this.stationInfo.station.station_id,
        address: this.stationInfo.station.address,
        data: this.stationInfo.data.map(item => ({
          fuel: item.fuel,
          price: parseFloat(item.price),
          amount: parseInt(item.amount),
        })),
      };

      axios.post(apiUrl, postData)
          .then(response => {
            console.log('Changes saved successfully:', response.data);
          })
          .catch(error => {
            console.error('Error saving changes:');
          });
    },
    baseForm() {
      this.showStationInfo = false;
      this.isNewStation = false;
      this.invalidId = false;
      this.stationInfo = {
        station: {},
        data: [
          {
            fuel: "92",
            price: null,
            amount: null
          },
          {
            fuel: "95",
            price: null,
            amount: null
          },
          {
            fuel: "98",
            price: null,
            amount: null
          },
          {
            fuel: "DF",
            price: null,
            amount: null
          },
        ]
      }
    }
  }
};
</script>

<template>
  <div class="container my-4">
    <form class="input-group mb-4" @submit.prevent="loadStationData">
      <input v-model="stationId" type="text" class="form-control bg-light" placeholder="Enter station ID">
      <button type="submit" class="btn btn-dark px-3">Load Data</button>
    </form>

    <div v-if="invalidId" class="alert alert-danger" role="alert">
      Invalid ID. Please enter a value between 1 and 99.
    </div>

    <form v-if="showStationInfo" @submit.prevent="saveChanges">
      <h3 v-if="!isNewStation"> Управление АЗС №{{ stationInfo.station.station_id }}</h3>
      <h3 v-else> Создание АЗС №{{ stationInfo.station.station_id }}</h3>
      <input id="address" type="text" class="form-control mb-2" placeholder="Адрес АЗС"
             v-model="stationInfo.station.address">
      <div class="row g-2 mb-4">
        <div v-for="fuelData in stationInfo.data" :key="fuelData.fuel" class="col-sm-6">
          <div class="card">
            <h5 class="card-header" :class="getFuelCardHeaderClass(fuelData.fuel)">{{ fuelData.fuel }}</h5>
            <div class="card-body bg-light">
              <label class="form-label">Price:</label>
              <input v-model="fuelData.price" type="text" class="form-control mb-2" placeholder="Rubles">
              <label class="form-label">Amount:</label>
              <input v-model="fuelData.amount" type="text" class="form-control" placeholder="Liters">
            </div>
          </div>
        </div>
      </div>
      <button type='submit' class="w-100 btn btn-warning btn-lg">Сохранить изменения</button>
    </form>
  </div>
</template>
