<template>
    <div id="show-post">
        <div class="post-complete">
            <div class="post-meta">
                <h1>{{this.$parent.selectedEntry.title}}</h1>
                <h2>Referenced in</h2>
            </div>
            <div class="post-entries">
                <h1>{{this.$parent.selectedEntry.title}}</h1>
                <div v-for="postCategory in this.$parent.postCategories" :key="postCategory.id">
                    <div v-if="postCategory.entryId === this.$parent.selectedEntry.id">
                        <h2>{{postCategory.title}}</h2>
                        <div v-for="post in this.$parent.posts" :key="post.id">
                            <p v-if="post.postCategoryId === postCategory.id">{{post.text}}<br><br></p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="post-scroll vbox">
                <div v-for="postCategory in this.$parent.postCategories" :key="postCategory.id" class="vbox">
                    <div v-if="postCategory.entryId === this.$parent.selectedEntry.id" class="scroll-indicator">
                        <p>{{postCategory.title}}</p>
                    </div>
                </div>
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
    .post-complete {
        height: 90vh;
        margin-left: 2rem;
        display: flex;
    }

    .post-meta {
        flex: 2;
    }

    .post-entries {
        flex: 3;
    }

    .post-scroll {
        flex: 1;
    }

    .scroll-indicator {
        flex: 1;
        border-left: 5px solid var(--light);
        padding-left: 1rem;
        margin-left: 1rem;
        align-items: center;
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