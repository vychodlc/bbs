<template>
  <div id="my">
    <div class="header">
      <div class="options">
        <div class="option"><img src="~assets/images/icons/send.png" alt=""></div>
        <div class="option"><img src="~assets/images/icons/search.png" alt=""></div>
      </div>
      <div class="avatar"><img src="~assets/logo.png" alt=""></div>
      <div class="nickname">匿名用户</div>
    </div>
    <div class="content">
      <div class="item">
        <div class="icon"><img src="~assets/images/icons/comment.png" alt=""></div>
        <span class="itemName">主题样式</span>
        <div class="icon"><img src="~assets/images/icons/back_light.png" alt=""></div>
      </div>
      <div class="item">
        <div class="icon"><img src="~assets/images/icons/comment.png" alt=""></div>
        <span class="itemName">主题样式</span>
        <div class="icon"><img src="~assets/images/icons/back_light.png" alt=""></div>
      </div>
      <div class="item">
        <div class="icon"><img src="~assets/images/icons/comment.png" alt=""></div>
        <span class="itemName">主题样式</span>
        <div class="icon"><img src="~assets/images/icons/back_light.png" alt=""></div>
      </div>
      <div class="item">
        <div class="icon"><img src="~assets/images/icons/comment.png" alt=""></div>
        <span class="itemName">主题样式</span>
        <div class="icon"><img src="~assets/images/icons/back_light.png" alt=""></div>
      </div>
      <div class="item">
        <div class="icon"><img src="~assets/images/icons/comment.png" alt=""></div>
        <span class="itemName">主题样式</span>
        <div class="icon"><img src="~assets/images/icons/back_light.png" alt=""></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "My",
    data () {
      return {}
    },
    methods:{}
  }
</script>

<style scoped>
  
  #my {
    width: 100%;
    height: calc(100vh - 50px);
  }
  .header {
    width: 100vw;
    height: 30vh;
    background-image: url('https://www.bing.com/th/id/ABTA524FDA95936E782CC7DAA2B8ABBD5AE39D9B220D1C2FBEB737AA78F3D758FE7?qlt=90&dpr=1.25&pid=InlineBlock');
    background-repeat: no-repeat;
    background-size: 100vw 30vh;
    position: relative;
    padding-top: 5vh;
    padding-left: 5vw;
  }
  .header .options {
    height: 5vh;
    width: 30vw;
    top: 2vh;
    right: 0;
    display: flex;
    position: absolute;
  }
  .header .options .option {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .header .options .option img {
    width: 30px;
    height: 30px;
  }
  .header .avatar {
    width: 15vh;
    height: 15vh;
  }
  .header .avatar img {
    background-color: #fff;
    height: 15vh;
    width: 15vh;
    border-radius: 50%;
  }
  .header .nickname {
    width: 15vh;
    margin-top: 2vh;
    color: #fff;
    text-align: center;
    font-size: 15px;
  }

  .item {
    display: flex;
    width: 100vw;
    height: 7vh;
    background-color: #fff;
  }
  .item .icon {
    width: 50px;
    height: 7vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .item .itemName {
    flex: 1;
    display: flex;
    align-items: center;
    font-size: 15px;
  }
  .item img {
    width: 25px;
    height: 25px;
  }
</style>