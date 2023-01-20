<template>
  <v-container>
    <Addpage @addPic="addPic"/>
    <v-row>
      <Picture
      v-for="picture in pics"
      v-bind:pic="picture"
      @openPic="openPic"
    />
    </v-row>
    <PicDialog :pic="currentPic" v-model="dialogVisible"/>

  </v-container>
</template>

<script>
import Picture from "@/components/pics/Picture";
import Addpage from "@/pages/Addpage";
import PicDialog from "@/components/PicDialog";
export default {
  name: "Showpage",
  components: {PicDialog, Addpage, Picture},
  data:()=> ({
    pics: [],
    currentPic: {},
    dialogVisible:false,
  }),
  mounted(){
    this.fetch_todo()
  },
  methods:{
    fetch_todo() {
      this.axios.get(`https://jsonplaceholder.typicode.com/photos?_limit=10`)
          .then(response=>this.pics=response.data)
    },
    addPic(pic){
      this.pics.push(pic)
    },
    openPic(pic) {
      this.currentPic=pic
      this.dialogVisible =true
    }
  }
}
</script>

<style scoped>

</style>