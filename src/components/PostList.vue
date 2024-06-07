<template>
  <div class="post-list">
    <div v-for="post in posts" :key="post.id" class="post-item">
      <h2>{{ post.username }}</h2>
      <p>{{ post.description }}</p>
      <p><strong>Miejsce wyjazdu:</strong> {{ post.departure }}</p>
      <p><strong>Miejsce docelowe:</strong> {{ post.destination }}</p>
      <p><strong>Data:</strong> {{ post.date }}</p>
      <p><strong>Godzina:</strong> {{ post.time }}</p>
      <p><strong>Ilość pasażerów:</strong> {{ post.passengers }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      posts: [
        {
          id: 1,
          username: "użytkownik1",
          description: "To jest przykładowy opis przejazdu.",
          departure: "Warszawa",
          destination: "Kraków",
          date: "2023-06-10",
          time: "14:00",
          passengers: 3,
        },
        {
          id: 2,
          username: "użytkownik2",
          description: "Drugi przykładowy opis przejazdu.",
          departure: "Gdańsk",
          destination: "Wrocław",
          date: "2023-06-12",
          time: "09:00",
          passengers: 2,
        },
        // Dodaj więcej przykładowych postów, jeśli to konieczne
      ],
    };
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

.post-item h2 {
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
