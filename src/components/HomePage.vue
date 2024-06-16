<template>
  <div class="home-page">
    <SearchForm @search="goSearch" />
    <div class="recent-rides">
      <PostList />
    </div>
  </div>
</template>

<script>
import SearchForm from "./SearchForm.vue";
import PostList from "./PostList.vue";
import { useRouter } from "vue-router";

export default {
  components: {
    SearchForm,
    PostList,
  },
  setup() {
    const router = useRouter();

    // Funkcja do nawigacji do strony wyszukiwania z przekazanymi parametrami wyszukiwania
    const goSearch = (searchParams) => {
      router.push({
        path: "/search",
        query: searchParams,
      });
    };

    return {
      goSearch,
    };
  },
};
</script>

<style scoped>
.home-page {
  padding: 2rem;
}
</style>
