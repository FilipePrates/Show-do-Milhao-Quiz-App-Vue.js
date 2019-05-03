<template>
  <v-card height="50px">
    <v-bottom-nav
      :value="true"
      absolute
      dark
      shift
    >
      <v-btn to='/info' dark>
        <span>Info</span>
        <v-icon>info</v-icon>
      </v-btn>


    </v-bottom-nav>
  </v-card>
</template>


<script>
export default {
  name: 'BottomNav',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
