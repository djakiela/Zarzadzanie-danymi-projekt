<template>
  <div class="search-form">
    <h1>Wyszukaj przejazd</h1>
    <form @submit.prevent="searchRides">
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
        <button
          v-if="isSearchPage"
          type="button"
          class="btn btn-secondary btn-grey"
          @click="goBack"
        >
          Powrót
        </button>
      </div>
    </form>

    <div class="ride-results" v-if="rides.length">
      <h2>Wyniki wyszukiwania:</h2>
      <ul>
        <li v-for="ride in rides" :key="ride.id">
          <strong>{{ ride.departure }}</strong> do
          <strong>{{ ride.destination }}</strong> w dniu
          <strong>{{ ride.date }}</strong> o godzinie
          <strong>{{ ride.time }}</strong
          >, pasażerów: <strong>{{ ride.passengers }}</strong
          >, numer telefonu: <strong>{{ ride.phone_number }}</strong>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { ref, computed } from "vue";

export default {
  setup() {
    const departure = ref("");
    const destination = ref("");
    const date = ref("");
    const rides = ref([]);
    const router = useRouter();

    const isSearchPage = computed(
      () => router.currentRoute.value.path === "/search"
    );

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
        rides.value = data;
      } catch (error) {
        console.error("Błąd podczas wyszukiwania przejazdów:", error);
      }
    };

    const goBack = () => {
      router.push("/");
    };

    return {
      departure,
      destination,
      date,
      rides,
      searchRides,
      goBack,
      isSearchPage,
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

.btn-grey {
  background-color: #6c757d;
  color: white;
}

.btn-grey:hover {
  background-color: #5a6268;
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
  padding: 0.5rem;
  border-bottom: 1px solid #ccc;
}
</style>
