<template>
    <div id="show-post">
        <div class="post-complete">
            <div class="post-meta">
                <h1>{{this.$parent.selectedEntry.name}}</h1>
                <h2>Referenced in</h2>
            </div>
            <div class="post-entries">
                <h1>{{this.$parent.selectedEntry.name}}</h1>
                <div 
                    v-for="postCategory in this.$parent.postCategories.filter(postCategory => postCategory.entryId == this.$parent.selectedEntry.id)"
                    :key="postCategory.id"
                >
                    <h2>{{postCategory.title}}</h2>
                    <!-- @todo Add Button to edit (&& delete) existing Posts -->
                    <div 
                        v-for="post in this.$parent.posts.filter(post => post.postCategoryId == postCategory.id)" 
                        :key="post.id"
                    >
                        <p>{{post.text}}<br><br></p>
                        <!-- @todo Add Button to edit (&& delete) existing Posts -->
                    </div>
                </div>
                <!-- @todo add button to add new Posts -> Opening the new Form needed -->
            </div>
            <div class="vbox">
                <div 
                    v-for="postCategory in this.$parent.postCategories.filter(postCategory => postCategory.entryId == this.$parent.selectedEntry.id)" 
                    :key="postCategory.id" 
                    class="post-scroll vbox"
                >
                    <div class="scroll-indicator">
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
</style>