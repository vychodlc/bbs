<template>
  <div class="post-detail">
    <div class="post-head">
      <div class="back" @click="$router.go(-1)"><img src="~assets/images/icons/back_light.png" alt=""></div>
      <div class="right">
        <img src="~assets/images/icons/favor.png" alt="">
        <img src="~assets/images/icons/more.png" alt="">
      </div>
    </div>
    <scroller :on-refresh="refresh" ref="my_scroller" style="margin-top: 50px;" class="my_scroller">
      <friend-post :kind='kind' id="friendPost"></friend-post>
      <div class="comment-head" id="commentHead">
        <div :class="currentTab==0?'active':'item'" id="appreciate" @click="changeActive(0)">赞 {{data.star_num}}</div>
        <div :class="currentTab==1?'active':'item'" id="comment" @click="changeActive(1)">评论 {{data.comment_num}}</div>
        <div :class="currentTab==2?'active':'item'" id="share" @click="changeActive(2)">转发 {{data.share_num}}</div>
      </div>
      <div class="comment-content">
        <div class="content" v-if="currentTab==0 && data.star_num!=0">
          <div class="content-item" v-for="(item,index) in 10" :key="index">
            <div class="avatar">
              <img src="~assets/images/icons/favor.png" alt="">
            </div>
            <div class="userinfo">
              <div class="infoitem">
                <div class="nickname">匿名用户</div>
                <div class="time">匿名用户的23123123自我介绍</div>
              </div>
            </div>
          </div>
        </div>
        <div class="content" v-if="currentTab==1 && data.comment_num!=0">
          <div class="content-item" v-for="(item,index) in 10" :key="index">
            <div class="avatar">
              <img src="~assets/images/icons/favor.png" alt="">
            </div>
            <div class="userinfo">
              <div class="infoitem">
                <div class="nickname">匿名用户</div>
                <div class="time">8分钟前</div>
                <div class="appreciate"><img src="~assets/images/icons/appreciate.png" alt=""></div>
              </div>
              <div class="infoitem">
                <div class="intro">匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍</div>
              </div>
            </div>
          </div>
        </div>
        <div class="content" v-if="currentTab==2 && data.share_num!=0">
          <div class="content-item" v-for="(item,index) in 10" :key="index">
            <div class="avatar">
              <img src="~assets/images/icons/favor.png" alt="">
            </div>
            <div class="userinfo">
              <div class="infoitem">
                <div class="nickname">匿名用户</div>
                <div class="time">8分钟前</div>
              </div>
              <div class="infoitem">
                <div class="intro">匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍匿名用户的自我介绍</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </scroller>
    <div class="add-comment"></div>

    
    <div class="comment-head" id="commentHeadFixed" v-show="showCommentHead">
      <div :class="currentTab==0?'active':'item'" id="appreciate" @click="changeActive(0)">赞 {{data.star_num}}</div>
      <div :class="currentTab==1?'active':'item'" id="comment" @click="changeActive(1)">评论 {{data.comment_num}}</div>
      <div :class="currentTab==2?'active':'item'" id="share" @click="changeActive(2)">转发 {{data.share_num}}</div>
    </div>
  </div>
</template>

<script>
  import FriendPost from "@/views/post/FriendPost"
  import { swiper, swiperSlide } from "vue-awesome-swiper";

  import "swiper/dist/css/swiper.css";
  export default {
    name: "PostDeatail",
    components: {
      swiper,
      swiperSlide,
      FriendPost
    },
    data () {
      return {
        data: {
          id: 1,
        },
        isRefresh: false,
        currentTab: 0,
        kind: 'postdetail',

        showCommentHead: false,
      }
    },
    methods:{
      refresh(){this.isRefresh=true;this.data={};this.getData()},
      getData() {
        this.data = {
          id: 1,
          author: {
            nickname: '匿名用户',
            avatar: 'https://www.npmjs.com/npm-avatar/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXJVUkwiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci9iZWRhNDk2MjMzMGUwZGM4Yjg4MTQxMTVkNmU1NzRmNT9zaXplPTQ5NiZkZWZhdWx0PXJldHJvIn0.Wjo2Nee80wW1X6eKBGMeAAYjwTYpyTnPq5K3ifa7eg4'
          },
          title: '',
          content: 'ajdskjasdkjkadkjasdkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkjkaskdakjsfhkjahkjfhakjsfhkahf',
          time: '2020-09-21 12:22',
          star_num: 221,
          comment_num: 21,
          share_num: 1,
          images: [],
        };
        if(this.isRefresh==true) {
          this.isRefresh = false;
          setTimeout(() => {
            this.$refs.my_scroller.finishPullToRefresh()
          }, 1000);
        }
      },
      changeActive(index) {
        if(index!=this.currentTab) {
          this.currentTab = index;
          if(document.getElementById('appreciate'))document.getElementById('appreciate').className = index==0?'active':'item';
          if(document.getElementById('comment'))document.getElementById('comment').className = index==1?'active':'item';
          if(document.getElementById('share'))document.getElementById('share').className = index==2?'active':'item';

          this.$refs.my_scroller.scrollTo(0,0);
          this.showCommentHead = false;
        }
      },
      showHead() {
        if(this.$refs.my_scroller) {
          let pos = this.$refs.my_scroller.getPosition().top;
          if(document.getElementById('friendPost')) {
            let height = document.getElementById('friendPost').clientHeight;
            this.showCommentHead = pos > height;
          }
        }
      }
    },
    mounted() {
      this.data.id = this.$route.params.id?this.$route.params.id:2;
      this.getData()
      // window.addEventListener('scroll',this.showHead,true)
      // document.getElementsByClassName('my_scroller')[0].addEventListener("transitionend",this.showHead,true)
      let showHeadInterval = setInterval(()=>this.showHead(),100)
    },
    destroyed() {
      // window.removeEventListener('scroll',this.showHead)
      clearInterval(showHeadInterval)
    }
  }
</script>

<style scoped>
  .post-detail {
    width: 100%;
    height: 100%;
    background-color: var(--color-background);
    position: relative;
    overflow: hidden;
  }

  .post-head {
    width: 100vw;
    height: 50px;
    background-color: #fff;
    z-index: 1000;
    border-bottom: 1px solid #ddd;
  }
  .post-head .back {
    position: absolute;
    left: 0;
    top: 0;
    width: 50px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .post-head .back img {
    width: 30px;
    height: 30px;
  }
  .post-head .right {
    position: absolute;
    right: 10px;
    top: 0;
    width: 80px;
    height: 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .post-head .right img {
    width: 30px;
    height: 30px;
  }
  .post-content {
  }
  .comment-head {
    height: 40px;
    width: 100%;
    display: flex;
    flex-direction: row;
    background-color: #fff;
  }
  .comment-head .item {
    font-size: 14px;
    text-align: center;
    padding: 0 5px;
    color: #999;
    width: 100px;
    height: 40px;
    line-height: 40px;
  }
  .comment-head .item:nth-child(3) {
    float: right;
  }
  .comment-head .active {
    font-size: 15px;
    text-align: center;
    padding: 0 5px;
    color: var(--color-all);
    width: 100px;
    height: 40px;
    line-height: 40px;
    border-bottom: 1px solid var(--color-all);
    font-weight: 550;
  }
  #commentHeadFixed {
    position: fixed;
    z-index: 8000;
    left: 0;
    top: 48px;
  }
  #share {
    /* position: absolute;
    right: 0;
    top: 0; */
  }

  .comment-content {
    padding-bottom: 50px;
  }
  .comment-content .content {
    
  }
  .comment-content .content .content-item {
    width: 100%;
    background-color: #fff;
    padding: 5px 10px;
    display: flex;
    flex-direction: row;
  }
  .comment-content .content .content-item .avatar {
    width: 40px;
    height: 40px;
  }
  .comment-content .content .content-item .avatar img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }
  .comment-content .content .content-item .userinfo {
    padding-left: 10px;
    /* height: 100px; */
    display: flex;
    flex-direction: column;
  }
  .comment-content .content .content-item .userinfo .infoitem:nth-child(1) {
    height: 40px;
    display: flex;
    flex-direction: column;
    line-height: 20px;
    position: relative;
  }
  .comment-content .content .content-item .userinfo .infoitem:nth-child(1) .appreciate {
    position: absolute;
    right: 0;
    top: 0;
  }
  .comment-content .content .content-item .userinfo .infoitem:nth-child(1) img {
    width: 20px;
    height: 20px;
  }
  .comment-content .content .content-item .userinfo .nickname {
    font-weight: 550;
    letter-spacing: 1px;
  }
  .comment-content .content .content-item .userinfo .time {
    color: #999;
  }
  .comment-content .content .content-item .userinfo .intro {
    letter-spacing: 1px;
    line-height: 18px;
    padding: 10px 0;
    border-bottom: 0.5px solid #ccc;
  }
</style>