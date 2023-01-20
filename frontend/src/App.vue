<template>
  <v-app>
    <NavBar></NavBar>
    <router-view> </router-view>
  </v-app>
</template>

<script>
import NavBar from "@/components/NavBar";
export default {
  name: 'App',
  components:{
    NavBar
  }
};
</script>
