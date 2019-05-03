<template>
      <v-layout
      text-xs-center
      wrap
    >

      <v-flex text-xs-center>

        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn  @click = "selectUniver" fab dark color="primary" v-on="on">Univer</v-btn>
          </template>
          <span>Peça ajuda aos universitários!</span>
        </v-tooltip>

        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn  @click = "select50" fab dark color="primary" v-on="on">50/50</v-btn>
          </template>
          <span>Remova 2 alternativas!</span>
        </v-tooltip>

        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn  @click = "selectPlat" fab dark color="primary" v-on="on">Plat</v-btn>
          </template>
          <span>Pergunte para a platéia!</span>
        </v-tooltip>

      </v-flex>


    </v-layout>
</template>

<script>
export default {
  name: 'Ajudas',
  props: ['flagUniver','flag50','flagPlat'],

  data() {
    return{
    }
  },
  methods : {
    selectUniver() {
      // console.log('Univer');
      this.$emit('flagUniver', 1);
    },

    select50() {
      // console.log('50');
      this.$emit('flag50', 1);
    },

    selectPlat() {
      // console.log('Plat');
      this.$emit('flagPlat', 1);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
