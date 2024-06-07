import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./components/HomePage.vue";
import LoginPage from "./components/LoginPage.vue";
import RegisterPage from "./components/RegisterPage.vue";
import PublishRide from "./components/PublishRide.vue";
import SearchForm from "./components/SearchForm.vue";

const routes = [
  { path: "/", name: "home", component: HomePage },
  { path: "/login", name: "login", component: LoginPage },
  { path: "/register", name: "register", component: RegisterPage },
  { path: "/publish", name: "publish", component: PublishRide },
  { path: "/search", name: "search", component: SearchForm },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
