<template>
  <div class="post-detail">
    <div class="post-head">
      <div class="back" @click="$router.go(-1)"><img src="~assets/images/icons/back_light.png" alt=""></div>
      <div class="right">
        <img src="~assets/images/icons/send.png" alt="">
      </div>
    </div>
    <div class="edit-content">
      <textarea name="text" id="text" placeholder="写点什么..."></textarea>
      <div class="add-icon">
        <img src="~assets/images/icons/add.png" alt="">
      </div>
    </div>
    <div class="footer">
      <div class="footer-box">
        <div class="footer-item"><img src="~assets/images/icons/xiangji.png" alt=""></div>
        <div class="footer-item"><img src="~assets/images/icons/aite.png" alt=""></div>
        <div class="footer-item"><img src="~assets/images/icons/huati.png" alt=""></div>
        <div class="footer-item"><img src="~assets/images/icons/biaoqing.png" alt=""></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Edit",
    data () {
      return {}
    },
    methods:{}
  }
</script>

<style scoped>
  .post-detail {
    background-color: #fff;
  }
  .post-head .right {
    position: absolute;
    right: 0;
    top: 0;
    width: 40px;
    height: 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .edit-content {
    width: 100vw;
    background-color: #fff;
    padding: 10px 20px;
  }
  #text {
    border: none;
    width: 100vw;
    min-height: 15vh;
    outline: none;
    font-size: 16px;
  }
  .edit-content .add-icon {
    width: 25vw;
    height: 25vw;
    border: 1px dotted #aaa;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .edit-content .add-icon img {
    width: 15vw;
    height: 15vw;
  }

  .footer {
    width: 100vw;
    height: 40px;
    position: absolute;
    bottom: 0;
    left: 0;
    border-top: 1px solid #ddd;
    display: flex;
    align-items: center;
  }
  .footer-box {
    width: 60vw;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .footer-item {
    width: 80px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .footer-item img {
    width: 25px;
    height: 25px;
  }
</style>