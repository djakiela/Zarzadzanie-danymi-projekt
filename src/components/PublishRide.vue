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
        <input type="date" id="date" v-model="date" required />
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
      <div class="form-group">
        <label for="phone_number">Numer telefonu:</label>
        <input type="text" id="phone_number" v-model="phone_number" required />
      </div>
      <button type="submit" class="btn btn-primary">Opublikuj przejazd</button>
      <button @click="goHomePage" type="button" class="btn btn-secondary">
        Powrót
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      departure: "",
      destination: "",
      date: "",
      time: "",
      passengers: 1,
      phone_number: "",
    };
  },
  methods: {
    publishRide() {
      if (!this.isLoggedIn()) {
        alert("Proszę zalogować się przed dodaniem posta.");
        return;
      }

      axios
        .post("http://localhost:5000/api/rides", {
          departure: this.departure,
          destination: this.destination,
          date: this.date,
          time: this.time,
          passengers: this.passengers,
          phone_number: this.phone_number,
          user_id: this.getUserId(), // Zakładamy, że istnieje metoda zwracająca ID zalogowanego użytkownika
        })
        .then(() => {
          alert("Przejazd został opublikowany!");
          this.$router.push("/");
        })
        .catch((error) => {
          console.error("Error publishing ride:", error);
        });
    },
    goHomePage() {
      this.$router.push("/");
    },
    isLoggedIn() {
      // Zakładamy, że istnieje metoda sprawdzająca, czy użytkownik jest zalogowany
      return !!localStorage.getItem("user");
    },
    getUserId() {
      // Zakładamy, że ID użytkownika jest przechowywane w localStorage
      const user = JSON.parse(localStorage.getItem("user"));
      return user ? user.id : null;
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
