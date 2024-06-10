<template>
  <div>
    <h1>Logowanie</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Hasło:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Zaloguj</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(
          "/login",
          {
            username: this.username,
            password: this.password,
          },
          { withCredentials: true }
        );
        console.log("Logowanie zakończone sukcesem", response);
        this.$store.dispatch("fetchCurrentUser");
        this.$router.push("/");
      } catch (error) {
        console.error("Error logging in:", error);
        alert(
          "Logowanie nie powiodło się: " +
            (error.response?.data.error || error.message)
        );
      }
    },
  },
};
</script>

<style scoped>
/* Przywrócenie stylów */
form {
  max-width: 300px;
  margin: auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}
div {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}
button {
  width: 100%;
  padding: 0.5rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
}
</style>
