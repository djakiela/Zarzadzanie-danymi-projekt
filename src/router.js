import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./components/HomePage.vue";
import LoginPage from "./components/LoginPage.vue";
import RegisterPage from "./components/RegisterPage.vue";
import PublishRide from "./components/PublishRide.vue";
import SearchForm from "./components/SearchForm.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/login", component: LoginPage },
  { path: "/register", component: RegisterPage },
  { path: "/publish", component: PublishRide },
  { path: "/search", component: SearchForm },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
