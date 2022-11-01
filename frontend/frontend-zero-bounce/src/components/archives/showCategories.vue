<template>
    <div id="show-categories" class="all-categories">
        <h1>All Categories</h1>
        <div v-for="category in categories" :key="category.id" class="single-category">
            <h2>{{category.title}}</h2>
        </div>
    </div>
</template>

<script>
    export default {  
        data() {
            return {
                categories: [],
                articles: [],
                postCategories: [],
                posts: [],
            }
        },

        methods: {
            getCategories() {
                fetch('https://jsonplaceholder.typicode.com/posts')
                    .then(response => response.json())
                    .then(data => this.categories = data.slice(0,10))
            },
            getArticles() {
                fetch('https://jsonplaceholder.typicode.com/posts')
                    .then(response => response.json())
                    .then(data => this.articles = data)
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
            this.getCategories()
        }
    }
</script>

<style>
    .all-categories {
        height: 90vh;
        width: 15rem;
        overflow-y: scroll;
        overflow-x: hidden;
    }

    .single-category {
        background-color: var(--dark);
        margin-bottom: 0.5rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        width: 13.5rem;
    }
</style>