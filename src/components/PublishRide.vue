<template>
  <div class="publish-ride-form">
    <h1>Opublikuj przejazd</h1>
    <form @submit.prevent="publishRide">
      <div class="form-group">
        <label for="departure">Miejsce wyjazdu:</label>
        <input type="text" id="departure" v-model="departure" required />
      </div>
      <div class="form-group">
        <label for="destination">Miejsce docelowe:</label>
        <input type="text" id="destination" v-model="destination" required />
      </div>
      <div class="form-group">
        <label for="date">Data:</label>
        <Datepicker v-model="date" :format="dateFormat" required />
      </div>
      <div class="form-group">
        <label for="time">Godzina:</label>
        <input type="time" id="time" v-model="time" required />
      </div>
      <div class="form-group">
        <label for="passengers">Ilość pasażerów:</label>
        <select id="passengers" v-model="passengers" required>
          <option value="1">1 pasażer</option>
          <option value="2">2 pasażerów</option>
          <option value="3">3 pasażerów</option>
          <option value="4">4 pasażerów</option>
        </select>
      </div>
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">
          Opublikuj przejazd
        </button>
        <button @click="goHomePage" type="button" class="btn btn-secondary">
          Powrót
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import Datepicker from "vue3-datepicker";

export default {
  name: "PublishRide",
  components: {
    Datepicker,
  },
  data() {
    return {
      departure: "",
      destination: "",
      date: new Date(),
      time: "",
      passengers: 1,
      dateFormat: "dd.MM.yyyy",
    };
  },
  methods: {
    publishRide() {
      console.log("Publishing ride:", {
        departure: this.departure,
        destination: this.destination,
        date: this.date,
        time: this.time,
        passengers: this.passengers,
      });
      // Implement the logic to publish the ride here
    },
    goHomePage() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.publish-ride-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 0.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.form-actions {
  display: flex;
  justify-content: space-between;
}

.btn {
  background-color: #3273dc;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn:hover {
  background-color: #275ba8;
}

.btn-secondary {
  background-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #5a6268;
}
</style>
