<template>
  <main class="archives-page">
    <h1>Archives</h1>
    <div>
      <show-categories></show-categories>
    </div>
  </main>
</template>

<script>
  import showCategories from '../components/archives/showCategories.vue';

  export default {
    components: {
      'show-categories': showCategories
    },

    data() {
      return {

      }
    },

    methods: {

    }
  }
</script>

<style>
  body{
    margin: 0;
  }
</style>