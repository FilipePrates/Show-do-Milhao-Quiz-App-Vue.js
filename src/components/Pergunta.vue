<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex text-xs-center>
        <h1>{{pergDaVez.title}}</h1>
      </v-flex>

      <!-- <v-flex xs12>
        <v-btn @click = "sortearPergunta">{{perg}}
      </v-btn>
          <v-card-text class="headline">{{}}</v-card-text>
      </v-flex> -->
      
    </v-layout>
  </v-container>
</template>

<script>

export default {
  name: 'Pergunta',
  props: ['pergDaVez'],
  data() {
    return{
    }
  },

  //computed: {
  //  sortearPergunta() {
  //    const indexSorteado = Math.floor(Math.random() * this.listaPerg.length) + 1
  //    this.perg = this.listaPerg[indexSorteado].title
  //  }
  //},
  methods: {
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
