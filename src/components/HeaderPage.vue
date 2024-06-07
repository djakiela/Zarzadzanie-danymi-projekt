<template>
  <header class="navbar">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item brand-title">
        Wirtualna Tablica Ogłoszeń Przejazdów
      </router-link>
      <router-link to="/search" class="navbar-item">
        <i class="fas fa-search"></i> Szukaj
      </router-link>
      <router-link to="/publish" class="navbar-item">
        <i class="fas fa-plus"></i> Opublikuj przejazd
      </router-link>
    </div>
    <div class="navbar-end">
      <div
        class="navbar-item has-dropdown"
        :class="{ 'is-active': isDropdownActive }"
      >
        <a class="navbar-link" @click="toggleDropdown">
          <i class="fas fa-user"></i>
        </a>
        <div class="navbar-dropdown is-right" v-show="isDropdownActive">
          <router-link to="/login" class="navbar-item" @click="closeDropdown"
            >Logowanie</router-link
          >
          <router-link to="/register" class="navbar-item" @click="closeDropdown"
            >Rejestracja</router-link
          >
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      isDropdownActive: false,
    };
  },
  methods: {
    toggleDropdown(event) {
      event.stopPropagation();
      this.isDropdownActive = !this.isDropdownActive;
    },
    closeDropdown() {
      this.isDropdownActive = false;
    },
    handleClickOutside(event) {
      if (this.isDropdownActive && !this.$el.contains(event.target)) {
        this.closeDropdown();
      }
    },
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleClickOutside);
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #f5f5f5;
}

.navbar-brand {
  display: flex;
  align-items: center;
}

.navbar-item {
  margin-right: 1rem;
  color: #4a4a4a;
  text-decoration: none;
}

.navbar-item:hover {
  color: #3273dc;
}

.brand-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #4a4a4a;
}

.navbar-end {
  display: flex;
  align-items: center;
}

.has-dropdown {
  position: relative;
}

.navbar-link {
  cursor: pointer;
  color: #4a4a4a;
}

.navbar-dropdown {
  position: absolute;
  right: 0;
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  border-radius: 4px;
  margin-top: 0.5rem;
  display: none;
}

.navbar-dropdown.is-right {
  right: 0;
}

.navbar-item {
  padding: 0.5rem 1rem;
  white-space: nowrap;
}

.navbar-item:hover {
  background-color: #f5f5f5;
}

.is-active .navbar-dropdown {
  display: block;
}
</style>
