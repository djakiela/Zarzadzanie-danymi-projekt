<template>
  <div class="post-list">
    <div v-for="post in posts" :key="post.id" class="post-item">
      <h3>{{ post.user.username }}</h3>
      <p>{{ post.description }}</p>
      <p><strong>Miejsce wyjazdu:</strong> {{ post.departure }}</p>
      <p><strong>Miejsce docelowe:</strong> {{ post.destination }}</p>
      <p><strong>Data:</strong> {{ post.date }}</p>
      <p><strong>Godzina:</strong> {{ post.time }}</p>
      <p><strong>Ilość pasażerów:</strong> {{ post.passengers }}</p>
      <button @click="showPhoneNumber(post.phone_number)">
        Skontaktuj się
      </button>
      <p v-if="phoneNumber === post.phone_number">
        <strong>Numer telefonu:</strong> {{ post.phone_number }}
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      posts: [],
      phoneNumber: null,
    };
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    fetchPosts() {
      axios
        .get("http://localhost:5000/api/rides")
        .then((response) => {
          this.posts = response.data;
        })
        .catch((error) => {
          console.error("Error fetching posts:", error);
        });
    },
    showPhoneNumber(phoneNumber) {
      this.phoneNumber = phoneNumber;
    },
  },
};
</script>

<style scoped>
.post-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.post-item {
  margin-bottom: 2rem;
}

.post-item h3 {
  font-size: 1.5rem;
  color: #3273dc;
}

.post-item p {
  font-size: 1rem;
  color: #4a4a4a;
}

.post-item p strong {
  color: #000;
}
</style>
