<template>
  <main class="archives-page">
    <h1 @click="test()">Archives</h1>
    <div class="hbox">
      <show-entry-form class="form-outer"></show-entry-form>
      <!-- <add-post-form></add-post-form> -->
      <show-categories v-if="this.selectedCategory.id == null" class="categories"></show-categories>
      <show-entries v-else class="categories"></show-entries>
      <show-post class="post"></show-post>
    </div>
  </main>
</template>

<script>
  import showEntryForm from '../components/archives/showEntryForm.vue';
  import showCategories from '../components/archives/showCategories.vue';
  import showEntries from '../components/archives/showEntries.vue';
  import showPost from '../components/archives/showPost.vue';

  export default {
    components: {
      'show-entry-form': showEntryForm,
      'show-categories': showCategories,
      'show-entries': showEntries,
      'show-post': showPost
    },

    data() {
      return {
        // categories: [
        //   {id: "0001", title: "Place"},
        //   {id: "0002", title: "Class"}
        // ],
        categories: [],
        entries: [
          {id: "0010", categoryId: "0", name: "Haven", visibleToPlayer: true},
          {id: "0011", categoryId: "0",name: "Docks", visibleToPlayer: true},
          {id: "0010", categoryId: "0", name: "Haven", visibleToPlayer: true},
          {id: "0011", categoryId: "0",name: "Docks", visibleToPlayer: true},
          {id: "0010", categoryId: "0", name: "Haven", visibleToPlayer: true},
          {id: "0011", categoryId: "0",name: "Docks", visibleToPlayer: true},
          {id: "0010", categoryId: "0", name: "Haven", visibleToPlayer: true},
          {id: "0011", categoryId: "0",name: "Docks", visibleToPlayer: true},
          {id: "0010", categoryId: "0", name: "Haven", visibleToPlayer: true},
          {id: "0011", categoryId: "0",name: "Docks", visibleToPlayer: true},
          {id: "0010", categoryId: "0", name: "Haven", visibleToPlayer: true},
          {id: "0011", categoryId: "0",name: "Docks", visibleToPlayer: true},
          {id: "0010", categoryId: "0", name: "Haven", visibleToPlayer: true},
          {id: "0011", categoryId: "0",name: "Docks", visibleToPlayer: true}
        ],
        postCategories: [
          {id: "0100", entryId:"0010", title: "Introduction"},
          {id: "0101", entryId:"0010", title: "History"},
          {id: "0102", entryId:"0010", title: "Social Structure"},
          {id: "0103", entryId:"0011", title: "Introduction"}
        ],
        posts: [
          {id: "1000", postCategoryId: "0100", visibleToPlayer: true, text: "Haven is a bunker underneath the City of Omen and was built by the Government right after the Darkness from the stars appeard on earths Surface."},
          {id: "1002", postCategoryId: "0100", visibleToPlayer: true, text: "The limited tickets to this facility were given to high-profile Scientists in hope of finding a niche for humanity to live in."},
          {id: "1003", postCategoryId: "0101", visibleToPlayer: true, text: "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "},
          {id: "1004", postCategoryId: "0102", visibleToPlayer: true, text: "At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."}
        ],
        selectedCategory: {},
        selectedEntry: {title: "Haven", categoryId: "0001", id: "0010"},

        entryFormHidden: true,
        PostFormHidden: true
      }
    },

    methods: {
      getCategories() {
        this.axios.get('http://localhost:8000/archive/categories')
          .then(response => this.categories = response.data.categories)
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
      },
      toggleEntryForm() {
        this.entryFormHidden = !this.entryFormHidden;
      },
      togglePostForm() {
        this.postFormHidden = !this.postFormHidden;
      },
      test() {debugger}
    },
        
    created() {
      this.getCategories()
    }
  }
</script>

<style>
  .form-outer {
    position: absolute; 
    left: 50%; 
    top: 20%; 
    z-index: 10;
  }
  .form-inner {
    position: relative;
    left: -50%;
    width: 350px;
    padding: 40px 40px 60px;
    background: #131419;
    border-radius: 10px;
    text-align: center;
    box-shadow: -5px -5px 10px rgba(255, 255, 255, 0.05),
                5px 5px 15px rgba(0, 0, 0, 0.5);
  }

  .categories {
    flex: 1;
  }

  .post{
    flex: 3;
  }
</style>