<template>
  <v-container fluid>
    <v-app-bar
      color="green"
      flat
      outlined
      rounded
    > <v-spacer></v-spacer>
      <v-btn>
        <router-link to="/main">Главная</router-link>
      </v-btn>
      <v-btn>
        <router-link to="/show">Хранилище</router-link>
      </v-btn>
      <v-btn>
        <router-link to="/autotag">Автотэг</router-link>
      </v-btn>
    </v-app-bar>

  </v-container>
</template>
<script>
export default {
}
</script>

<style scoped>

</style>