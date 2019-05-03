<template>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12>
          <h1>
            Bem vindo ao Jogo do Show do Milhão!<br>
          </h1>
          <p>
            Responda correntamente e concorra a prêmios em milhos!
           <a href="https://www.youtube.com/watch?v=eQuJuLq3SK4" target="_blank" rel="noopener">Vídeo Tutorial</a>.
          </p>

      </v-flex>
    </v-layout>
</template>

<script>
export default {
  name: 'Cabecario',
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
