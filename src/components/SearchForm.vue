<template>
  <div class="search-form">
    <h1>Wyszukaj przejazd</h1>
    <form @submit.prevent="emitSearch">
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
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">Wyszukaj</button>
        <button type="button" class="btn btn-secondary" @click="goBack">
          Powrót
        </button>
      </div>
    </form>

    <div class="ride-results">
      <h2 v-if="rides.length">Wyniki wyszukiwania:</h2>
      <ul v-if="rides.length">
        <li v-for="ride in rides" :key="ride.id">
          <p>Miejsce wyjazdu: {{ ride.departure }}</p>
          <p>Miejsce docelowe: {{ ride.destination }}</p>
          <p>Data: {{ ride.date }}</p>
          <p>Godzina: {{ ride.time }}</p>
          <p>Ilość pasażerów: {{ ride.passengers }}</p>
          <p v-if="ride.showPhoneNumber">
            Numer telefonu: {{ ride.phone_number }}
          </p>
          <button @click="togglePhoneNumber(ride.id)" class="btn btn-primary">
            {{ ride.showPhoneNumber ? "Ukryj numer" : "Skontaktuj się" }}
          </button>
        </li>
      </ul>
      <p v-else-if="hasSearched">Brak przejazdów w danym terminie.</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

export default {
  setup(props, { emit }) {
    const departure = ref("");
    const destination = ref("");
    const date = ref("");
    const rides = ref([]);
    const hasSearched = ref(false);
    const router = useRouter();
    const route = useRoute();

    // Funkcja wyszukująca przejazdy na podstawie wprowadzonych danych
    const searchRides = async () => {
      try {
        const response = await fetch("http://localhost:8000/ride/search", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            departure: departure.value,
            destination: destination.value,
            date: date.value,
          }),
        });

        if (!response.ok) {
          throw new Error("Nie udało się wyszukać przejazdów.");
        }

        const data = await response.json();
        rides.value = data.map((ride) => ({
          ...ride,
          showPhoneNumber: false,
        }));
        hasSearched.value = true;
      } catch (error) {
        console.error("Błąd podczas wyszukiwania przejazdów:", error);
        hasSearched.value = true;
      }
    };

    // Funkcja przełączająca widoczność numeru telefonu dla wybranego przejazdu
    const togglePhoneNumber = (id) => {
      const ride = rides.value.find((ride) => ride.id === id);
      if (ride) {
        ride.showPhoneNumber = !ride.showPhoneNumber;
      }
    };

    const goBack = () => {
      router.push("/");
    };

    // Funkcja emitująca dane wyszukiwania
    const emitSearch = () => {
      emit("search", {
        departure: departure.value,
        destination: destination.value,
        date: date.value,
      });
      searchRides();
    };

    // Inicjalizacja danych na podstawie parametrów trasy
    onMounted(() => {
      if (
        route.query.departure &&
        route.query.destination &&
        route.query.date
      ) {
        departure.value = route.query.departure;
        destination.value = route.query.destination;
        date.value = route.query.date;
        searchRides();
      }
    });

    return {
      departure,
      destination,
      date,
      rides,
      hasSearched,
      searchRides,
      togglePhoneNumber,
      goBack,
      emitSearch,
    };
  },
};
</script>

<style scoped>
.search-form {
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

.form-group input {
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

.ride-results {
  margin-top: 2rem;
}

.ride-results h2 {
  margin-bottom: 1rem;
}

.ride-results ul {
  list-style: none;
  padding: 0;
}

.ride-results li {
  background-color: white;
  margin-bottom: 1rem;
  padding: 1rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  border-radius: 0.5rem;
}

.ride-results p {
  margin: 0.5rem 0;
}

.btn-secondary {
  background-color: gray;
}

.btn-secondary:hover {
  background-color: #5a6268;
}
</style>
