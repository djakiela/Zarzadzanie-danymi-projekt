<template>
    <div>
      <div class="container">
        <h1 class="text-center my-4">Strona Główna</h1>
        <SearchForm />
        <h2>Ogłoszenia</h2>
        <ul class="list-group">
          <li v-for="post in posts" :key="post.id" class="list-group-item">
            <h3>{{ post.title }}</h3>
            <p>{{ post.body }}</p>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import SearchForm from './SearchForm.vue';
  
  export default {
    name: 'HomePage',
    components: {
      SearchForm
    },
    data() {
      return {
        posts: []
      };
    },
    created() {
      this.fetchPosts();
    },
    methods: {
      async fetchPosts() {
        try {
          const response = await axios.get('http://localhost:5000/posts');
          this.posts = response.data;
        } catch (error) {
          console.error('Error fetching posts:', error);
        }
      }
    }
  };
  </script>
  