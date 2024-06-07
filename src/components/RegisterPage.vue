<template>
  <div class="form-container">
    <div class="form-card">
      <h1 class="form-title">Rejestracja</h1>
      <form @submit.prevent="register">
        <div class="form-group">
          <label for="username" class="form-label">Nazwa użytkownika:</label>
          <input type="text" class="form-control" v-model="username" required />
        </div>
        <div class="form-group">
          <label for="email" class="form-label">Email:</label>
          <input type="email" class="form-control" v-model="email" required />
        </div>
        <div class="form-group">
          <label for="password" class="form-label">Hasło:</label>
          <input type="password" class="form-control" v-model="password" required />
        </div>
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Zarejestruj</button>
          <button @click="goHomePage" type="button" class="btn btn-secondary">Powrót</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://localhost:5000/register', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        console.log('Registration successful:', response.data);
        this.$router.push('/login');
      } catch (error) {
        console.error('Error registering:', error);
      }
    },
    goHomePage() {
      this.$router.push('/');
    }
  }
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
