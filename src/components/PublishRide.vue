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
        <input
          type="text"
          id="phone_number"
          v-model="phone_number"
          @input="validatePhoneNumber"
          required
        />
        <span v-if="phoneNumberError" class="error-message">{{
          phoneNumberError
        }}</span>
      </div>
      <div class="button-group">
        <button type="submit" class="btn btn-primary">
          Opublikuj przejazd
        </button>
        <button type="button" class="btn btn-secondary" @click="goBack">
          Powrót
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref } from "vue";

export default {
  setup() {
    const store = useStore();
    const router = useRouter();

    const departure = ref("");
    const destination = ref("");
    const date = ref("");
    const time = ref("");
    const passengers = ref(1);
    const phone_number = ref("");
    const phoneNumberError = ref("");

    // Funkcja walidująca numer telefonu
    const validatePhoneNumber = () => {
      let cleaned = phone_number.value.replace(/\D/g, "");
      if (cleaned.length > 9) {
        phoneNumberError.value = "Maksymalna liczba to 9 cyfr.";
        cleaned = cleaned.slice(0, 9);
      } else {
        phoneNumberError.value = "";
      }

      if (/\D/.test(phone_number.value)) {
        phoneNumberError.value = "Numer może składać się tylko z cyfr.";
      }

      phone_number.value = cleaned;
    };

    // Funkcja obsługująca publikację przejazdu
    const publishRide = async () => {
      const user = store.state.user;
      if (!user) {
        alert("Proszę zalogować się przed dodaniem przejazdu.");
        router.push("/login");
        return;
      }

      if (phone_number.value.length !== 9) {
        alert("Numer telefonu musi zawierać dokładnie 9 cyfr.");
        return;
      }

      try {
        const response = await fetch("http://localhost:8000/ride", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include",
          body: JSON.stringify({
            departure: departure.value,
            destination: destination.value,
            date: date.value,
            time: time.value,
            passengers: passengers.value,
            phone_number: phone_number.value,
          }),
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(
            `Nie udało się opublikować przejazdu: ${errorData.detail}`
          );
        }

        alert("Przejazd został opublikowany!");
        router.push("/");
      } catch (error) {
        console.error("Błąd podczas publikacji przejazdu:", error);
        alert("Błąd podczas publikacji przejazdu.");
      }
    };

    const goBack = () => {
      router.push("/");
    };

    return {
      departure,
      destination,
      date,
      time,
      passengers,
      phone_number,
      phoneNumberError,
      validatePhoneNumber,
      publishRide,
      goBack,
    };
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

.error-message {
  color: red;
  font-size: 0.875rem;
  margin-top: 0.5rem;
  display: block;
}

.button-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
}

.btn {
  background-color: #3273dc;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn-secondary {
  background-color: #6c757d;
}

.btn:hover {
  background-color: #275ba8;
}

.btn-secondary:hover {
  background-color: #5a6268;
}
</style>
