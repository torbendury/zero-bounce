<template>
    <div id="show-entries">
          <div class="all-entries">
            <div class="single-entry-clicked" @click="this.deselectCategory()">
                <h2>{{this.$parent.selectedCategory.name}}</h2>
            </div>
            <div 
                v-for="entry in this.$parent.entries.filter(entry => entry.categoryId == this.$parent.selectedCategory.id)" 
                :key="entry.id" 
                @click="this.selectEntry($event)" 
                class="single-entry"
            >
                <h2>{{entry.name}}</h2>
            </div>
            <!-- @todo Button only visible for GM -->
        </div>
        <button class="add-new-entry" @click="this.$parent.toggleEntryForm()">+</button>
    </div>
</template>

<script>
    export default {  
        data() {
            return {

            }
        },

        methods: {
            selectEntry(event) {
                this.$parent.selectedEntry = this.$parent.entries.find(obj => {return obj.name === event.target.firstChild.innerHTML});
            },
            deselectCategory() {
                this.$parent.selectedCategory = {};
                this.$parent.selectedEntry = {};
            }
        }
    }

</script>

<style>
    .all-entries {
        height: 80vh;
        overflow-y: scroll;
        overflow-x: hidden;
   }

    .add-new-entry {
        background-color: var(--button-default);
        color: white;
        border-radius: 1.5rem;
        font-size: x-large;
        height: 4rem;
        width: 100%;
        display: block;
    }

    .add-new-entry:hover {
        background-color: var(--button-hover);
        color: white;
        border-radius: 1.5rem;
        font-size: x-large;
        height: 4rem;
        width: 100%;
        display: block;
    }

    .add-new-entry:active {
        background-color: var(--button-clicked);
        color: white;
        border-radius: 1.5rem;
        font-size: x-large;
        height: 4rem;
        width: 100%;
        display: block;
        box-shadow: inset -2px -2px 6px rgba(255, 255, 255, 0.1),
                inset 2px 2px 6px rgba(0, 0, 0, 0.8);
    }

    .single-entry {
        margin-bottom: 0.5rem;
        padding: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        justify-content: center;
        height: 4rem;
        display: flex;
    }

    .single-entry:hover{
        background-color: var(--button-hover);
        margin-bottom: 0.5rem;
        padding: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        justify-content: center;
        display: flex;
        cursor: pointer;
    }

    .single-entry-clicked{
        background-color: var(--button-clicked);
        margin-bottom: 0.5rem;
        padding: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        justify-content: center;
        display: flex;
        cursor: pointer;
        box-shadow: inset -2px -2px 6px rgba(255, 255, 255, 0.1),
                inset 2px 2px 6px rgba(0, 0, 0, 0.8);
    }

    .single-entry:active{
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

    .single-entry:focus{
        background-color: var(--light-clicked);
        margin-bottom: 0.5rem;
        padding: 1rem;
        padding-left: 1rem;
        border-radius: 1.5rem;
        justify-content: center;
        display: flex;
        box-shadow: inset -2px -2px 6px rgba(255, 255, 255, 0.1),
                inset 2px 2px 6px rgba(0, 0, 0, 0.8);
    }

    .new-entry-form {
        position: absolute;
        left: 50%;
        /* right: 50%; */
        top: 50%;
        height: 300px;
        width: 500px;
        background-color: white;
        z-index: 10;
    }
</style>