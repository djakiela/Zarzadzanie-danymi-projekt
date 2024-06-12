<template>
  <div class="register-form">
    <h1>Rejestracja</h1>
    <form @submit.prevent="register">
      <div class="form-group">
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Hasło:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit" class="btn btn-primary">Zarejestruj</button>
    </form>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { ref } from "vue";

export default {
  setup() {
    const username = ref("");
    const email = ref("");
    const password = ref("");
    const router = useRouter();

    const register = async () => {
      try {
        const response = await fetch("http://localhost:8000/user", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username.value,
            email: email.value,
            password: password.value,
          }),
        });

        if (response.ok) {
          alert("Rejestracja zakończona sukcesem!");
          router.push("/login");
        } else {
          const errorData = await response.json();
          alert(`Rejestracja nie powiodła się: ${errorData.detail}`);
        }
      } catch (error) {
        console.error("Błąd podczas rejestracji:", error);
        alert("Rejestracja nie powiodła się.");
      }
    };

    return {
      username,
      email,
      password,
      register,
    };
  },
};
</script>

<style scoped>
.register-form {
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
