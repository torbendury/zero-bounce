<template>
    <div id="show-categories">
        <div class="all-categories">
            <div v-for="category in this.$parent.categories" :key="category.id" class="single-category" @click="this.selectCategory($event)">
                <h2>{{category.name}}</h2>
                <!-- @todo Add a Edit-Button only visible for the DM -->
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
            selectCategory(event) {
                // @Todo Make sure that the correct record is found -> It makes a difference between clicking the div and clicking the h2
                this.$parent.selectedCategory = this.$parent.categories.find(obj => {return obj.name === event.target.firstChild.innerHTML});
            }
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
        margin-bottom: 0.5rem;
        padding: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        justify-content: center;
        display: flex;
    }

    .single-category:hover{
        background-color: var(--button-hover);
        margin-bottom: 0.5rem;
        padding: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        justify-content: center;
        display: flex;
        cursor: pointer;
   }

    .single-category:active{
        background-color: var(--button-clicked);
        margin-bottom: 0.5rem;
        padding: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        justify-content: center;
        display: flex;
        box-shadow: inset -2px -2px 6px rgba(255, 255, 255, 0.1),
                inset 2px 2px 6px rgba(0, 0, 0, 0.8);
    }
</style>