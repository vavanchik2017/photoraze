<template>
  <v-container>
    <v-row class="d-flex">
      <v-text-field v-model="title"/>
      <v-file-input v-model="img"/>
      <v-btn @click="addPic">Добавить</v-btn>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: "Addpage",
  data: () => ({
    title: '',
    img: null
  }),
  methods: {
    addPic() {
      const reader = new FileReader()
      reader.onload = () => {
        let pic = {
          id: 21,
          title: this.title,
          url: reader.result
        }
        this.$emit('addPic',pic)
      }
      reader.readAsDataURL(this.img)
    },

  }

}
</script>

<style scoped>

</style>