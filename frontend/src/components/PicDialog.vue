<template>
    <v-dialog
      v-model="value"
      max-width="600"
    > bbjj
      <v-card>
        <v-card-title>{{full_title}}</v-card-title>
        <v-card-text>
          <v-img :src="pic.url"></v-img>
        </v-card-text>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  name: "PicDialog",
  props: {
    pic: {
      type:Object,
      required: true
    },
    value: {
      type: Boolean,
      default: false
    }
  },
  created() {
    this.dialogVisible = this.value
  },
  data: ()=> ({
      dialogVisible: false
  }),
  watch:{
    value(newValue){
      this.dialogVisible = newValue
    },
    dialogVisible(newValue){
      this.$emit('input', newValue)
    }
  },
  computed:{
    full_title(){
      return `Название фотографии - ${this.pic.title}`
    }
  }
}
</script>

<style scoped>

</style>