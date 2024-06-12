<template>
  <div class="login-form">
    <h1>Logowanie</h1>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Hasło:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit" class="btn btn-primary">Zaloguj</button>
    </form>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref } from "vue";

export default {
  setup() {
    const username = ref("");
    const password = ref("");
    const store = useStore();
    const router = useRouter();

    const login = async () => {
      try {
        const response = await fetch("http://localhost:8000/user/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username.value,
            password: password.value,
          }),
        });

        if (response.ok) {
          const data = await response.json();
          store.commit("setUser", data);
          router.push("/");
        } else {
          alert("Logowanie nie powiodło się");
        }
      } catch (error) {
        console.error("Błąd podczas logowania:", error);
      }
    };

    return {
      username,
      password,
      login,
    };
  },
};
</script>

<style scoped>
.login-form {
  max-width: 400px;
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
