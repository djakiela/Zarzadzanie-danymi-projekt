<template>
  <div class="form-container">
    <div class="form-card">
      <h1 class="form-title">Logowanie</h1>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username" class="form-label">Nazwa użytkownika:</label>
          <input
            type="text"
            class="form-control"
            id="username"
            v-model="username"
            required
          />
        </div>
        <div class="form-group">
          <label for="password" class="form-label">Hasło:</label>
          <input
            type="password"
            class="form-control"
            id="password"
            v-model="password"
            required
          />
        </div>
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Zaloguj</button>
          <button @click="goBack" type="button" class="btn btn-secondary">
            Powrót
          </button>
        </div>
      </form>
    </div>
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
    login() {
      axios
        .post("/api/login", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          alert("Logowanie zakończone sukcesem!");
          this.$router.push("/");
        })
        .catch((error) => {
          alert("Logowanie nie powiodło się: " + error.response.data.error);
        });
    },
    goBack() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.form-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  height: 100vh;
  padding-top: 5rem;
}

.form-card {
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  width: 24rem;
  background-color: white;
  border-radius: 0.5rem;
}

.form-title {
  text-align: center;
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-label {
  margin-bottom: 0.5rem;
  display: block;
}

.form-control {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.form-actions {
  display: flex;
  justify-content: space-between;
}
</style>
