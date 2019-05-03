<template>
  <v-app style="
    background: #F0FFFF;
  ">
    <v-container>
        <v-flex text-xs-center>
          <img alt="Milhao" src="./assets/Show_do_Milhão_logo.gif" height="250" width="350">
        </v-flex>

        <Quiz/>

        <!-- <Cabecario/> -->
        <!-- <BottomNav/> -->

        
        <!-- <router-view></router-view> -->
    </v-container>
  </v-app>
</template>

<script>
import Cabecario from './components/Cabecario.vue'
import Pergunta from './components/Pergunta.vue'
import Ajudas from './components/Ajudas.vue'
import Respostas from './components/Respostas.vue'
import Quiz from './components/Quiz.vue'
import BottomNav from './components/BottomNav'

export default {
  name: 'App',

  components: {
    Cabecario,
    Pergunta,
    Ajudas,
    Respostas,
    Quiz,
    BottomNav
  },

  data () {
    return {
      dialog: false
    }
  },
  methods: {

  }
}

</script>

<style>
  align-center: true,
  text-xs-center;
</style>
