<template>
    <div>
      <h2>Ogłoszenia</h2>
      <ul>
        <li v-for="post in posts" :key="post.id">
          <h3>{{ post.title }}</h3>
          <p>{{ post.body }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'PostList',
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
  