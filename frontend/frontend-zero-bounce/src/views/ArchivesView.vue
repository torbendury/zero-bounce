<template>
  <main class="archives-page">
    <h1>Archives</h1>
    <div class="hbox">
      <show-categories class="categories"></show-categories>
      <show-post class="post"></show-post>
    </div>
  </main>
</template>

<script>
  import showCategories from '../components/archives/showCategories.vue';
  import showPost from '../components/archives/showPost.vue';

  export default {
    components: {
      'show-categories': showCategories,
      'show-post': showPost
    },

    data() {
      return {
        categories: [
          {id: "0001", title: "Place"},
          {id: "0002", title: "Class"}
        ],
        entries: [
          {id: "0010", categoryId: "0001", title: "Haven"},
          {id: "0011", categoryId: "0001",title: "Docks"},
          {id: "0020", categoryId: "0002", title: "Omen", categoryId: "0002", },
          {id: "0021", categoryId: "0002", title: "Prey"}
        ],
        postCategories: [
          {id: "0100", entryId:"0010", title: "Introduction"},
          {id: "0101", entryId:"0010", title: "History"},
          {id: "0102", entryId:"0010", title: "Social Structure"},
          {id: "0103", entryId:"0011", title: "Introduction"}
        ],
        posts: [
          {id: "1000", postCategoryId: "0100", text: "Haven is a bunker underneath the City of Omen and was built by the Government right after the Darkness from the stars appeard on earths Surface."},
          {id: "1002", postCategoryId: "0100", text: "The limited tickets to this facility were given to high-profile Scientists in hope of finding a niche for humanity to live in."},
          {id: "1003", postCategoryId: "0101", text: "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "},
          {id: "1004", postCategoryId: "0102", text: "At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."}
        ],
        selectedCategory: {title: "Place", id: "0001"},
        selectedEntry: {title: "Haven", categoryId: "0001", id: "0010"}
      }
    },

    methods: {
      getCategories() {
                this.axios.get('https://jsonplaceholder.typicode.com/posts')
                    .then(response => this.categories = response.data)
            },
            getArticles() {
                fetch('https://jsonplaceholder.typicode.com/posts')
                    .then(response => response.json())
                    .then(data => this.entries = data)
            },
            getPostCategories() {
                fetch('https://jsonplaceholder.typicode.com/posts')
                    .then(response => response.json())
                    .then(data => this.postCategories = data)
            },
            getPosts() {
                fetch('https://jsonplaceholder.typicode.com/posts')
                    .then(response => response.json())
                    .then(data => this.posts = data)
            }
    },
        
    created() {
      // this.getCategories()
    }
  }
</script>

<style>
  .archives-page {
    /* max-height: inherit; */
  }

  .categories {
    flex: 1;
  }

  .post{
    flex: 3;
  }
</style>