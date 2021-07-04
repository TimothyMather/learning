<template>
  <Home />
</template>

<script>
import Home from './components/Home.vue';

export default {
  name: 'App',
  components: {
    Home,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #239d83;
}

html {
  background-color: #0e0e10;
}

.secondary {
  color: #2cc7a6;
}
</style>
