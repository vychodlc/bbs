<template>
  <div id="app">
    <keep-alive exclude="PostDeatail">
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
export default({
  name: 'App',
  created() {
    const Height = window.innerHeight;
    window.onresize = () => {
      return (() => {
        window.innerHeight = Height
      })()
    }
  },
})
</script>


<style>
  @import "assets/css/base.css";
  @import "assets/css/custom.css";
  #app {
    width: 100vw;
    height: 100vh;
    position: relative;
  }
</style>
