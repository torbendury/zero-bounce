<template>
    <div id="show-categories">
        <div class="all-categories">
            <div v-for="category in this.$parent.categories" :key="category.id" class="single-category">
                <h2>{{category.title}}</h2>
            </div>
        </div>
    
    </div>
</template>

<script>
    export default {  
        data() {
            return {

            }
        },

        methods: {
            
        }
    }
</script>

<style>
    .all-categories {
        height: 80vh;
        overflow-y: scroll;
        overflow-x: hidden;
   }

    .single-category {
        background-color: var(--dark);
        margin-bottom: 0.5rem;
        margin-right: 0.5rem;
        padding: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        justify-content: center;
        display: flex;
    }

    /* width */
    ::-webkit-scrollbar {
        width: 0.5rem;
    }

    /* Track */
    ::-webkit-scrollbar-track {
        background-color: var(--dark); 
        border-radius: 10px;
    }
 
    /* Handle */
    ::-webkit-scrollbar-thumb {
        background: var(--grey); 
        border-radius: 10px;
    }
</style>