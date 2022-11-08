<template>
    <div id="show-entry-form">
        <div :class="this.$parent.entryFormHidden ? 'form-inner hidden' : 'form-inner'">
            <h2>Add a new entry</h2>
            <!-- @todo Add Form Validation! -->
            <div class="input">
                <div class="inputBox">
                    <label>Name</label>
                    <input type="text" name="nameInput" placeholder="Haven" v-model="entryName">
                </div>
                <div class="inputBox hbox">
                    <!-- @todo Check if its possible to use this Form but change the submit function depending on whether a new entry is added or a existing one is edited 
                            -> When Form is opened via edit Button -> render a delete button (Edit-Form can edit && delete in order to display less icons in the overview)-->
                    <input type="submit" name="save" value="Save" @click="createEntry()">
                    <input type="reset" name="cancel" value="Cancel" @click="closeEntryForm()">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {  
        data() {
            return {
                entryName: ''
            }
        },

        methods: {
            createEntry() {
                if (this.entryName && this.$parent.selectedCategory) {
                    this.axios.post('http://localhost:8000/archive/categories/' + this.$parent.selectedCategory.id + '/entries', {
                        name: this.entryName
                    })
                    .then(function (response) {
                        this.$parent.entryFormHidden = !this.$parent.entryFormHidden;
                    })
                    .catch(function (error) {
                        // @todo Should Errors be displayed?
                        console.log(error);
                    });
                } 
            },
            closeEntryForm() {
                this.entryName = '';
                this.$parent.entryFormHidden = !this.$parent.entryFormHidden;
            }
        }
    }
</script>

<style>
/* @todo clean up styles,  */
    #show-entry-form *{
        box-sizing: border-box;
    }
    #show-entry-form body
    {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: #131419;
    }
    .form-inner h2
    {
        color: #c7c7c7;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 4px;
    }
    .form-inner .input
    {
        text-align: left;
        margin-top: 40px;
    }
    .form-inner .input .inputBox
    {
        margin-top: 20px;
    }
    .form-inner .input .inputBox label
    {
        display: block;
        color: #868686;
        margin-bottom: 5px;
        font-size: 18px;
    }
    .form-inner .input .inputBox input
    {
        width: 100%;
        height: 50px;
        background: #131419;
        border: none;
        outline: none;
        border-radius: 40px;
        padding: 5px 15px;
        color: #fff;
        font-size: 18px;
        color: #03a9f4;
        box-shadow: inset -2px -2px 6px rgba(255, 255, 255, 0.1),
                    inset 2px 2px 6px rgba(0, 0, 0, 0.8);
    }
    .form-inner .input .inputBox input[type="submit"]
    {
        margin-top: 20px;
        margin-right: 10px;
        box-shadow:  -2px -2px 6px rgba(255, 255, 255, 0.1),
                     2px 2px 6px rgba(0, 0, 0, 0.8);
    }
    .form-inner .input .inputBox input[type="submit"]:active
    {
        color: #006c9c;
        margin-top: 20px;
        margin-right: 10px;
        box-shadow:  inset -2px -2px 6px rgba(255, 255, 255, 0.1),
                     inset 2px 2px 6px rgba(0, 0, 0, 0.8);
    }
    .form-inner .input .inputBox input[type="reset"]
    {
        margin-top: 20px;
        margin-left: 10px;
        box-shadow:  -2px -2px 6px rgba(255, 255, 255, 0.1),
                     2px 2px 6px rgba(0, 0, 0, 0.8);
    }
    .form-inner .input .inputBox input[type="reset"]:active
    {
        color: #006c9c;
        margin-top: 20px;
        margin-left: 10px;
        box-shadow:  inset -2px -2px 6px rgba(255, 255, 255, 0.1),
                     inset 2px 2px 6px rgba(0, 0, 0, 0.8);
    }
    .form-inner .input .inputBox input::placeholder
    {
        color: #555;
        font-size: 18px;
    }

</style>