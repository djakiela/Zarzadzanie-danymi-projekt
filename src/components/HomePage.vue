<template>
  <div class="home-page">
    <SearchForm />
    <div class="recent-rides">
      <h2>Ostatnio dodane</h2>
      <PostList />
    </div>
  </div>
</template>

<script>
import SearchForm from "./SearchForm.vue";
import PostList from "./PostList.vue";

export default {
  components: {
    SearchForm,
    PostList,
  },
};
</script>

<style scoped>
.home-page {
  padding: 2rem;
}

.recent-rides {
  margin-top: 2rem;
}
</style>
