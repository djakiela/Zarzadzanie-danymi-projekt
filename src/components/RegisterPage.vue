<template>
  <div>
    <h1>Rejestracja</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Hasło:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Zarejestruj się</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post(
          "/register",
          {
            username: this.username,
            email: this.email,
            password: this.password,
          },
          { withCredentials: true }
        );
        console.log("Registration successful:", response);
        this.$router.push("/login");
      } catch (error) {
        console.error("Error registering:", error);
        alert(
          "Rejestracja nie powiodła się: " +
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
