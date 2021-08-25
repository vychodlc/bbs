<template>
  <div class="card">
    <div class="card-top">
      <span class="title">{{data.title}}</span>
    </div>
    <div class="card-middle">
      <div class="content">
        <div class="author">
          <div class="avatar">
            <img :src="data.user.avatar" alt="">
          </div>
          <div class="nickname">{{data.user.nickname}}</div>
        </div>
        <div class="text">{{data.content}}</div>
      </div>
      <div class="cover"><img :src="data.cover_img" alt=""></div>
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
    name: "PostCard",
    // props: ['data'],
    data () {
      return {
        data: {
          title: '这是一篇帖子红红火火恍恍惚惚这是一篇帖子红红火火恍恍惚惚',
          content: '这是一篇帖子红红火火恍恍惚惚是一篇帖子红红火火恍恍惚惚这是一篇帖子红红火火恍恍惚惚是一篇帖子红红火火恍恍惚惚这是一篇帖子红红火火恍恍惚惚是一篇帖子红红火火恍恍惚惚',
          user: {
            nickname: '匿名用户1',
            avatar: 'https://www.npmjs.com/npm-avatar/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXJVUkwiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci9iZWRhNDk2MjMzMGUwZGM4Yjg4MTQxMTVkNmU1NzRmNT9zaXplPTQ5NiZkZWZhdWx0PXJldHJvIn0.Wjo2Nee80wW1X6eKBGMeAAYjwTYpyTnPq5K3ifa7eg4'
          },
          star_num: 211,
          comment_num: 21,
          share_num: 0,
          cover_img: 'https://s3.bmp.ovh/imgs/2021/08/4cd4eea9269dbec2.png',
          // cover_img: 'https://img-blog.csdnimg.cn/202108111027472.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwMzIzMjU2,size_16,color_FFFFFF,t_70',
          menu: '十大',
          time: '2020/2/2 18:22:21',
        },
        post_tags: ['topic1','topic2'],
      }
    },
    methods:{},
    computed: {
      timeShow() {
        if(this.data.activity==1) {
          let now = new Date().getTime();
          let start = new Date(this.data.start_time).getTime();
          let end = new Date(this.data.end_time).getTime();
          let day = 24*60*60*1000;
          let hour = 60*60*1000;
          if(now<start) {
            let gap = start-now;
            if(gap>day) {
              return '距离开始还有' + parseInt(gap/day).toString() + '天'
            }else if(gap>hour) {
              return '距离开始还有' + parseInt(gap/hour).toString() + '小时'
            }
          }else if(now>start&&now<end) {
            let gap = end-now;
            if(gap>day) {
              return '距离结束还有' + parseInt(gap/day).toString() + '天'
            }else if(gap>hour) {
              return '距离结束还有' + parseInt(gap/hour).toString() + '小时'
            }
          }
        }
        return this.data.post_date.toString().slice(0,12) + ' by ' + this.data.author
      }  
    },
  }
</script>

<style scoped>
  .card {
    width: 100vw;
    /* height: 19vh; */
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
    height: 30px;
  }
  .card-top span {
    font-size: 16px;
    line-height: 30px;
    font-weight: 550;
    letter-spacing: 1px;

    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    overflow: hidden;
  }
  .card-middle {
    display: flex;
    height: 108px;
  }
  .card-middle .content {
    flex: 1;
  }
  .card-middle .content .author {
    display: flex;
    flex-direction: row;
    height: 30px;
  }
  .card-middle .content .author .avatar {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .card-middle .content .author .avatar img {
    width: 20px;
    height: 20px;
    border-radius: 50%;
  }
  .card-middle .content .author .nickname {
    line-height: 30px;
    margin-left: 10px;
    letter-spacing: 1px;
    color: #555;

    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    overflow: hidden;
  }
  .card-middle .content .text {
    font-size: 14px;
    letter-spacing: 1px;
    line-height: 20px;
    color: #555;

    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 4;
    overflow: hidden;
  }
  .card-middle .cover {
    width: 25vw;
    margin-left: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .card-middle .cover img {
    width: 100%;
    max-height: 100px;
    border-radius: 5px;
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