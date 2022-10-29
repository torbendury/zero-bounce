<script setup>
import { RouterLink, RouterView } from "vue-router";
import Sidebar from "./components/Sidebar.vue"
</script>

<template>
  <div class="app">
    <Sidebar />

    <!-- <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav> -->
    <RouterView />
  </div>
</template>

<style lang="scss">
:root {
  --primary: #51B1E8;
  --primary-alt: #308abe;
  --grey: #64748b;
  --dark: #1F2029;
  --dark-alt: #181922;
  --light: #f1f5f9;
  --sidebar-width: 300px;

  background-color: var(--dark-alt);
  color: white;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: var(--light);
}

button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

.app {
  display: flex;

  main {
    flex: 1 1 0;
    padding: 2rem;

    @media (max-width: 768px) {
      padding-left: 6rem;
    }
  }
}
</style>
