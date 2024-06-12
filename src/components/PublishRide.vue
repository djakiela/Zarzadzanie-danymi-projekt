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
    </form>
  </div>
</template>

<script>
import { useRouter } from "vue-router";

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
    async publishRide() {
      const router = useRouter();
      try {
        const response = await fetch("http://localhost:8000/ride/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include",
          body: JSON.stringify({
            departure: this.departure,
            destination: this.destination,
            date: this.date,
            time: this.time,
            passengers: this.passengers,
            phone_number: this.phone_number,
          }),
        });

        if (!response.ok) {
          throw new Error("Nie udało się opublikować przejazdu.");
        }

        alert("Przejazd został opublikowany!");
        router.push("/");
      } catch (error) {
        console.error("Błąd podczas publikacji przejazdu:", error);
        if (error.message.includes("401")) {
          alert("Proszę zalogować się przed dodaniem posta.");
          router.push("/login");
        } else {
          alert("Błąd podczas publikacji przejazdu.");
        }
      }
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
</style>
