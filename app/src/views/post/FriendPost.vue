<template>
  <div class="friend-post">
    <div class="card-top">
      <div class="avatar">
        <img :src="data.author.avatar" alt="">
      </div>
      <div class="author">
        <div class="nickname">{{data.author.nickname}}</div>
        <div class="time">{{data.time}}</div>
      </div>
    </div>
    <div class="card-middle">
      <div class="content">{{data.content}}</div>
      <div class="images">
        <div class="imgOne" v-if="data.images.length==1">
          <div class="image">
            <img :src="data.images[0]" alt="">
          </div>
        </div>
        <div class="imgMuch" v-else>
          <div class="image" v-for="(item,index) in data.images.slice(0,9)" :key="index">
            <img :src="item" alt="">
          </div>
          <div class="moreimg" v-if="data.images.length>9">{{data.images.length-9}}+</div>
        </div>
      </div>
    </div>
    <div class="card-bottom">
      <div class="post-data">
        <img src="~/assets/images/icons/appreciate.png" alt="">
        <span class="number" v-if="data.star_num!=0">{{data.star_num}}</span>
      </div>
      <div class="post-data">
        <img src="~/assets/images/icons/comment.png" alt="">
        <span class="number" v-if="data.comment_num!=0">{{data.comment_num}}</span>
      </div>
      <div class="post-data">
        <img src="~/assets/images/icons/forward.png" alt="">
        <span class="number" v-if="data.share_num!=0">{{data.share_num}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "FriendPost",
    data () {
      return {
        data: {
          imgNum: 0,
          author: {
            nickname: '匿名用户1',
            avatar: 'https://www.npmjs.com/npm-avatar/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXJVUkwiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci9iZWRhNDk2MjMzMGUwZGM4Yjg4MTQxMTVkNmU1NzRmNT9zaXplPTQ5NiZkZWZhdWx0PXJldHJvIn0.Wjo2Nee80wW1X6eKBGMeAAYjwTYpyTnPq5K3ifa7eg4'
          },
          content: '这是一篇帖子红红火火恍恍惚惚是一篇帖子红红火火恍恍惚惚这是一篇帖子红红火火恍恍惚惚是一篇帖子红红火火恍恍惚惚这是一篇帖子红红火火恍恍惚惚是一篇帖子红红火火恍恍惚惚',
          time: '2020-02-12 19:22',
          images: [
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
            'https://i.bmp.ovh/imgs/2021/08/4e70049337310fc8.png',
          ],
          
          star_num: 211,
          comment_num: 21,
          share_num: 0,
        }
      }
    },
    methods:{},
    mounted() {
      let m = 15,n = 0;
      this.data.images = this.data.images.slice(0,parseInt(Math.random()*(m-n-1)+n+1))
      console.log(this.data.images.length);
    }
  }
</script>

<style scoped>
  .friend-post {
    width: 100vw;
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
    background-color: #fff;
    padding: 10px 20px;
    text-align: left;
    position: relative;

    padding-bottom: 30px;
  }

  .card-top {
    height: 50px;
    width: 100%;
    display: flex;
    flex-direction: row;
  }
  .card-top .avatar {
    width: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .card-top .avatar img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }
  .card-top .author {
    display: flex;
    flex-direction: column;
    padding-left: 10px;
    justify-content: center;
  }
  .card-top .nickname {
    font-size: 16px;
    font-weight: 550;
    line-height: 20px;
    color: #000;
    letter-spacing: 1px;
  }
  .card-top .time {
    font-size: 12px;
    line-height: 20px;
    color: #999;
  }
  
  .card-middle {}
  .card-middle .content {
    font-size: 14px;
    letter-spacing: 1px;
    line-height: 20px;
    color: #555;
    margin-bottom: 10px;

    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 8;
    overflow: hidden;
  }
  .card-middle .images {
    display: flex;
    flex-direction: row;
    width: 100%;
    flex-wrap: wrap;
  }
  .card-middle .imgOne img {
    width: 60vw;
    height: 60vw;
  }
  .card-middle .imgMuch {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    position: relative;
  }
  .card-middle .imgMuch img {
    width: calc((100vw - 40px - 20px) / 3);
    height: calc((100vw - 40px - 20px) / 3);
  }
  .card-middle .imgMuch .image:nth-child(1),
  .card-middle .imgMuch .image:nth-child(2),
  .card-middle .imgMuch .image:nth-child(4),
  .card-middle .imgMuch .image:nth-child(5),
  .card-middle .imgMuch .image:nth-child(7),
  .card-middle .imgMuch .image:nth-child(8) {
    margin-right: 10px;
  }
  .card-middle .imgMuch .image:nth-child(1),
  .card-middle .imgMuch .image:nth-child(2),
  .card-middle .imgMuch .image:nth-child(3),
  .card-middle .imgMuch .image:nth-child(4),
  .card-middle .imgMuch .image:nth-child(5),
  .card-middle .imgMuch .image:nth-child(6) {
    margin-bottom: 5px;
  }
  .card-middle .imgMuch .moreimg {
    position: absolute;
    bottom: 0;
    right: 0;
    background-color: rgba(0,0,0,0.2);
    color: #fff;
    font-size: 40px;
    line-height: calc((100vw - 40px - 20px) / 3);
    text-align: center;
    width: calc((100vw - 40px - 20px) / 3);
    height: calc((100vw - 40px - 20px) / 3);
  }

  .card-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .card-bottom .post-data {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .card-bottom .post-data img {
    width: 15px;
    height: 15px;
  }
  .card-bottom .post-data span {
    font-size: 12px;
    color: #aaa;
    margin-left: 5px;
  }
</style>