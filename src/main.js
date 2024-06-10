import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import "@fortawesome/fontawesome-free/css/all.css";
import "@fortawesome/fontawesome-free/js/all.js";

axios.defaults.baseURL = "http://127.0.0.1:5000/api";
axios.defaults.withCredentials = true;

createApp(App).use(router).use(store).mount("#app");
