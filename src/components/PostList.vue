<template>
  <div class="post-list">
    <h1>Lista Przejazdów - ostatnio dodane</h1>
    <ul>
      <li v-for="ride in rides" :key="ride.id">
        <p>Miejsce wyjazdu: {{ ride.departure }}</p>
        <p>Miejsce docelowe: {{ ride.destination }}</p>
        <p>Data: {{ ride.date }}</p>
        <p>Godzina: {{ ride.time }}</p>
        <p>Ilość pasażerów: {{ ride.passengers }}</p>
        <p>Numer telefonu: {{ ride.phone_number }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const rides = ref([]);

    const fetchRides = async () => {
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

        rides.value = await response.json();
      } catch (error) {
        console.error("Błąd podczas pobierania listy przejazdów:", error);
      }
    };

    onMounted(() => {
      fetchRides();
    });

    return {
      rides,
    };
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
</style>
