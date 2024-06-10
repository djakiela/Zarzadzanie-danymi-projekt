<template>
  <div class="search-form">
    <input
      type="text"
      placeholder="Miejsce wyjazdu"
      class="search-input"
      v-model="departure"
    />
    <input
      type="text"
      placeholder="Miejsce docelowe"
      class="search-input"
      v-model="destination"
    />
    <div class="date-picker-wrapper">
      <Datepicker
        v-model="date"
        :format="dateFormat"
        placeholder="dd.mm.rrrr"
        input-class="search-input"
      />
    </div>
    <select v-model="passengers" class="search-input">
      <option value="1">1 pasażer</option>
      <option value="2">2 pasażerów</option>
      <option value="3">3 pasażerów</option>
      <option value="4">4 pasażerów</option>
    </select>
    <button class="search-button" @click="search">Szukaj</button>
  </div>
</template>

<script>
import Datepicker from "vue3-datepicker";

export default {
  components: {
    Datepicker,
  },
  data() {
    return {
      departure: "",
      destination: "",
      date: "",
      passengers: 1,
      dateFormat: "dd.MM.yyyy",
    };
  },
  methods: {
    search() {
      console.log(
        "Searching for:",
        this.departure,
        this.destination,
        this.date,
        this.passengers
      );
    },
  },
};
</script>

<style scoped>
.search-form {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  max-width: 1000px;
  margin: 0 auto;
  margin-bottom: 2rem;
}

.search-input {
  flex: 1;
  margin-right: 1rem;
  padding: 0.5rem 1rem;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
  font-size: 1rem;
  color: #4a4a4a;
  background-color: #f5f5f5;
}

.search-input:last-child {
  margin-right: 0;
}

.date-picker-wrapper {
  flex: 1;
  margin-right: 1rem;
  padding: 0.5rem 1rem;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
  font-size: 1rem;
  color: #4a4a4a;
  background-color: #f5f5f5;
}

.search-button {
  background-color: #3273dc;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: #275ba8;
}

select.search-input {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}
</style>
