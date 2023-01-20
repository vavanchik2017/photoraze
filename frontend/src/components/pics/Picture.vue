<template>
  <v-col cols="4">
      <v-card @click="openPic">
        <v-card-title>{{pic.title}}</v-card-title>
        <v-card-text>
          <v-img width="600px" height="600px" :src="pic.url"></v-img>
        </v-card-text>
      </v-card>
  </v-col>

</template>

<script>
export default {
  name: "Picture",
  props:{
    pic:{
      type:Object,
      required: true
    }
  },
  methods:{
    openPic(){
      this.$emit('openPic',this.pic)
    }
  }
}
</script>

<style scoped>

</style>