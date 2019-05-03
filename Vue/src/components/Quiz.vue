<template>
  <v-container>
    <v-layout
      align-center
      wrap
    >

      <Pergunta :pergDaVez="pergDaVez"/>

      <!-- <v-flex>
        <v-btn dark @click="sortearPergunta">NewPerg</v-btn>
      </v-flex> -->

      <v-flex align-center v-if="flagflagPlat">
        <div class="text-xs-center">
          <h1 class="headline">A platéia votou!</h1>
          <!-- <br><br><  br> -->
            <v-progress-circular :value=percPlatVote1 color="#e13026" size="65" width="10"></v-progress-circular>
            <v-progress-circular :value=percPlatVote2 color="#ff6633" size="65" width="10"></v-progress-circular>
            <v-progress-circular :value=percPlatVote3 color="#dcac26" size="65" width="10"></v-progress-circular>
            <v-progress-circular :value=percPlatVote4 color="#669933" size="65" width="10"></v-progress-circular>
        </div>
      </v-flex>

      <v-flex xs12>
        <Respostas @altSelecionada = "checkAcerto"
                   :pergDaVez = "pergDaVez"
                   :disable = "disable"/>
      </v-flex>
      <!-- <Plateia/> -->


      <Ajudas @flagUniver = "ajudaUniver"
              @flag50 = "ajuda50"
              @flagPlat = "ajudaPlat"
              :flagUniver = "flagUniver" :flag50 = "flag50" :flagPlat = "flagPlat"/>



      <h1>Valendo {{pontos}} reais</h1>

      <p>{{disable}}</p>

      <!-- <h1>{{pergDaVez}}</h1> -->
      <!-- <h1>flagUniver: {{flagUniver}}</h1>
      <h1>flag50: {{flag50}}</h1>
      <h1>flagPlat: {{flagPlat}}</h1> -->

    </v-layout>
    <BottomNav/>

  </v-container>
</template>

<script>
  import Ajudas from './Ajudas.vue';
  import Pergunta from './Pergunta.vue';
  import Respostas from './Respostas.vue';
  import BottomNav from './BottomNav.vue';

  export default {
    name: 'Quiz',

    components: {
      Ajudas,
      Pergunta,
      Respostas,
      BottomNav
    },

    data() {
      return {
        listaPerg: [
          {
            id:1,
            title: "Quem era o homem mais sedutor do mundo?",
            alts: ["Dom Juan","Dom Antonio","Dom Marco","Dom Carlos"],
            vista: false,
            resp: 0
          },
          {
            id:2,
            title: "De quantos anos é constituído um século?",
            alts: ["50","100","1000","1500"],
            vista: false,
            resp: 1
          },
          {
            id:3,
            title: "Qual é o coletivo de cães?",
            alts: ["Matilha","Rebanho","Cardume","Manada"],
            vista: false,
            resp: 0
          },
          {
            id:4,
            title: "Qual a maior floresta do planeta?",
            alts: ["Floresta Negra","Floresta Andina","Floresta da Tijuca","Floresta Amazônica"],
            vista: false,
            resp: 3
          },
          {
            id:5,
            title: "Segundo a Bíblia, em que rio Jesus foi batizado por João Batista?",
            alts: ["Rio Nilo","Rio Sena","Rio Reno","Rio Jordão"],
            vista: false,
            resp: 3
          },
          {
            id:6,
            title: "Qual é o naipe do baralho que tem o desenho de coração?",
            alts: ["Ouros","Espadas","Copas","Paus"],
            vista: false,
            resp: 2
          }

        ],
        pergDaVez: {
          title: "PLACEHOLDER",
          alts: ["1","2","3","4"],
        },

        disable: [false,false,false,false],

        pergId: 0,
        pontos: 0,
        flagUniver: 0,
        flag50: 0,
        flagPlat: 0,
        flagflagPlat: 0,

        percPlatVote1: 25,
        percPlatVote2: 25,
        percPlatVote3: 25,
        percPlatVote4: 25

      }
    },
    methods:{

      checkAcerto(altSelecionada) {
        if (this.listaPerg[this.pergId].resp == altSelecionada) {
          this.pontos+= 100;

        }else{
          this.pontos = 0;
          this.flagUniver = 0;
          this.flag50 = 0;
          this.flagPlat = 0;
          this.flagflagPlat = 0;

        }
        this.sortearPergunta();
      },

      sortearPergunta() {
        // const indexSorteado = Math.floor(Math.random() * this.listaPerg.length)
        this.pergId = (this.pergId+1) % 6;

        this.pergDaVez.title = this.listaPerg[this.pergId].title;
        this.pergDaVez.alts = this.listaPerg[this.pergId].alts;

        this.disable = [false,false,false,false];

        this.flagflagPlat = 0;

      },

      ajudaUniver(flagUniver) {
        // console.log('Univer');
        this.flagUniver = flagUniver;
      },

      ajuda50(flag50) {
        // console.log('50');
        if (this.flag50 == 0) {
          switch (this.listaPerg[this.pergId].resp) {
            case 0:
              this.disable[1] = true
              this.disable[3] = true
              console.log(0)
              break;
            case 1:
              this.disable[0] = true
              this.disable[3] = true
              console.log("mudando o disable")

              break;
            case 2:
              this.disable[1] = true
              this.disable[0] = true
              console.log(2)

              break;
            case 3:
              this.disable[0] = true
              this.disable[2] = true
              console.log(3)

              break;
            }
          this.pergDaVez.title = "Essas são as escolhas que sobraram!";
          this.flag50 = flag50;

          // console.log(this.pergDaVez);
          // console.log(this.listaPerg[this.pergId]);
        }
      },

      votosPlateia() {
        var vote1 = 0
        var vote2 = 0
        var vote3 = 0
        var vote4 = 0

        var randPlat1 = Math.random()
        var votosPlat = 0
        var valorMinAcertoPlat = randPlat1*0.55 + 0.25

        while (votosPlat < 100) {
            var randPlat2 = Math.random()
            if (randPlat2 < valorMinAcertoPlat) {
                vote1 += 1
            }else{
                var randPlat3 = Math.floor((Math.random() * 3805)%3)
                if (randPlat3 == 0) { vote2 += 1 }
                if (randPlat3 == 1) { vote3 += 1 }
                if (randPlat3 == 2) { vote4 += 1 }
            }
            votosPlat += 1
        }
        if (this.listaPerg[this.pergId].resp == 0) {
            this.percPlatVote1 =  vote1
            this.percPlatVote2 =  vote2
            this.percPlatVote3 =  vote3
            this.percPlatVote4 =  vote4
        }else if (this.listaPerg[this.pergId].resp == 1) {
            this.percPlatVote1 =  vote2
            this.percPlatVote2 =  vote1
            this.percPlatVote3 =  vote3
            this.percPlatVote4 =  vote4
        }else if (this.listaPerg[this.pergId].resp == 2) {
            this.percPlatVote1 =  vote3
            this.percPlatVote2 =  vote2
            this.percPlatVote3 =  vote1
            this.percPlatVote4 =  vote4
        }else if (this.listaPerg[this.pergId].resp == 3) {
            this.percPlatVote1 =  vote4
            this.percPlatVote2 =  vote2
            this.percPlatVote3 =  vote3
            this.percPlatVote4 =  vote1
        }
      },

      ajudaPlat(flagPlat) {
        // console.log('Plat');
        if(this.flagPlat == 0){
          this.votosPlateia()
          this.flagPlat = flagPlat;
          this.flagflagPlat = flagPlat;
        }
      }
    }
  }
</script>

<style>
</style>
