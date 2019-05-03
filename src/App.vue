  <template>
  <v-app style="
    background: #F0FFFF;
  ">
    <v-container>
      <router-view></router-view>
    </v-container>
  </v-app>
</template>

<script>


export default {
  name: 'App',

  components: {
  },

  data () {
    return {
    }
  },
}

</script>

<style>
  align-center: true,
  text-xs-center;
</style>
