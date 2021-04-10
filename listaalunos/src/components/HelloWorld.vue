<template>
  <div class="lista">
    <h1>Teste Lead Tracker</h1>
    <ul v-for="aluno in alunos" v-bind:key="aluno.id">
        <li>{{aluno.id}}</li>
        <li>{{aluno.nome}}</li>
        <li>{{aluno.nota}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return{
      titulo: "Lista de Alunos",
      alunos:[
        {id:1, nome:'Luiz', nota:'6.7'},
        {id:2, nome:'Flavio', nota:'7.8'},
        {id:3, nome:'Rafael', nota:'8.0'},
        {id:4, nome:'Giovani', nota: '6.1'},
        {id:5, nome:'Felipe', nota:'7.2'}
      ]
    }
  }
}
</script>

<style scoped>

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  padding:5px;
}

</style>
