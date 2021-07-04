<template>
  <div class="Home">
    <div class="Title">
      <h1>Hello</h1>
      <p class="Secondary"></p>
    </div>
    <div class="Main">
      <div class="Mainbar">
        <div class="Stream">
          <div id="twitch-embed"></div>
        </div>
        <div class="Clips"></div>
        <div class="Archive"></div>
      </div>
      <div class="Sidebar">
        <div class="Twitter"></div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Home',
};
</script>

<style scoped>
h1 {
  display: flex;
  flex-direction: column;
}
.Main {
  display: flex;
}
.Mainbar {
  flex-grow: 2;
}
.Sidebar {
  flex-grow: 1;
}
.Stream {
  display: flex;
  justify-content: flex-start;
}
</style>
