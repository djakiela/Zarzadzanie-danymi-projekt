<template>
  <div class="post-list">
    <h1>Lista Przejazdów</h1>
    <ul>
      <li v-for="(ride, index) in rides" :key="ride.id">
        <p>Miejsce wyjazdu: {{ ride.departure }}</p>
        <p>Miejsce docelowe: {{ ride.destination }}</p>
        <p>Data: {{ ride.date }}</p>
        <p>Godzina: {{ ride.time }}</p>
        <p>Ilość pasażerów: {{ ride.passengers }}</p>
        <p v-if="ride.showPhoneNumber">
          Numer telefonu: {{ ride.phone_number }}
        </p>
        <button @click="togglePhoneNumber(index)" class="btn">
          {{ ride.showPhoneNumber ? "Ukryj numer" : "Skontaktuj się" }}
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rides: [],
    };
  },
  async created() {
    try {
      const response = await fetch("http://localhost:8000/ride", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
      });

      if (!response.ok) {
        throw new Error("Nie udało się pobrać listy przejazdów.");
      }

      const data = await response.json();
      this.rides = data.map((ride) => ({ ...ride, showPhoneNumber: false }));
    } catch (error) {
      console.error("Błąd podczas pobierania listy przejazdów:", error);
    }
  },
  methods: {
    togglePhoneNumber(index) {
      this.rides[index].showPhoneNumber = !this.rides[index].showPhoneNumber;
    },
  },
};
</script>

<style scoped>
.post-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.post-list ul {
  list-style-type: none;
  padding: 0;
}

.post-list li {
  background-color: white;
  margin-bottom: 1rem;
  padding: 1rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  border-radius: 0.5rem;
}

.post-list p {
  margin: 0.5rem 0;
}

button {
  background-color: #3273dc;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

button:hover {
  background-color: #275ba8;
}
</style>
