<template>
  <div id="post">
    <div class="navtab">
      <div @click="changeTab(0)" class="navtabItem"><span :class="this.currentTab==0?'active':''">论坛十大</span></div>
      <div @click="changeTab(1)" class="navtabItem"><span :class="this.currentTab==1?'active':''">好友圈</span></div>
    </div>
    <div class="content" style="padding-top:0px">
      <swiper :options="swiperOption" ref="tabSwiper" style="transform: translateY(-0px);">
        <swiper-slide class="tabSlide">
          <scroller :on-refresh="refresh1" ref="my_scroller1">
            <div class="PostCards">
              <post-card v-for="(item,index) in top10Posts" :key="index" :data="item"></post-card>
              <!-- <div v-for="(item,index) in top10Posts" :key="index" :data="item">{{item}}</div> -->
            </div>
          </scroller>
        </swiper-slide>
        <swiper-slide class="tabSlide">
          <scroller :on-infinite="infinite2" :on-refresh="refresh2" ref="my_scroller2">
            <div class="PostCards">
              <!-- <post-card v-for="(item,index) in friendsPosts" :key="index" :data="item"></post-card> -->
              <div v-for="(item,index) in friendsPosts" :key="index" :data="item">{{item}}</div>
            </div>
          </scroller>
        </swiper-slide>
        
      </swiper>
    </div>
  </div>
</template>

<script>
  import PostCard from "@/views/post/PostCard"
  import { swiper, swiperSlide } from "vue-awesome-swiper";

  import "swiper/dist/css/swiper.css";
  
  export default {
    name: "Post",
    components: {
      swiper,
      swiperSlide,
      PostCard
    },
    data () {
      return {
        currentTab: 0,
        currentPage: 0,
        swiperOption: {
          on: {
            slideChange: () => {
              this.currentTab = this.tabSwiper.activeIndex;
            }
          },
        },
        top10Posts: [],
        friendsPosts: [],
        
        hasMore: [false,false,false,false],
        loadflag: [false,false,false,false],
        _refreshText: [],
        isRefresh: false,

        totop: [0,0,0,0],
        showTotop: false,
        listenTotop: null,
      }
    },
    methods:{
      getData(index) {
        if(index==0) {
          setTimeout(()=>{
            this.top10Posts = ['a','b','c','d','f','e','g','h','i','j']
            if(this.isRefresh==true) {
              this.isRefresh = false;
              this.$refs.my_scroller1.finishPullToRefresh()
            }
          },1000)
        }
        if(index==1) {
          this.friendsPosts = ['aa','bb','cc','dd','ff','ee','gg','hh','ii','jj']
          if(this.isRefresh==true) {
            this.isRefresh = false;
            this.$refs.my_scroller2.finishPullToRefresh()
          }
        }
      },
      changeTab(tabIndex) {
        this.currentTab = tabIndex;
        this.tabSwiper.slideTo(tabIndex,300,false)
      },
      refresh1(){this.isRefresh=true;this.top10Posts=[];this.getData(0)},
      refresh2(){this.isRefresh=true;this.friendsPosts=[];this.currentPage=1;this.getData(1)},
      infinite2(){if(this.hasMore[2]==true){this.getData(1)}else{this.$refs.my_scroller2.finishInfinite(true)}},
    },
    computed: {
      tabSwiper() {
        return this.$refs.tabSwiper.swiper;
      },
    },
    mounted() {
      this.getData(0)
      this.getData(1)
      this.changeTab(1);
    },
  }
</script>

<style scoped>
  #post {
    width: 100%;
    height: calc(100vh - 50px);
  }
  
  .navtab {
    width: 100vw;
    display: flex;
    height: 50px;
    line-height: 50px;
    background-color: #fff;
  }
  .navtabItem {
    flex: 1;
    text-align: center;
  }
  .navtabItem span {
    font-size: 16px;
  }
  .active {
    color: var(--color-all);
    border-bottom: 2px solid var(--color-all);
    padding: 8px 20px;
    font-weight: bold;
  }

  .content .swiper-container{
    position: relative;
    width: 100%;
    height: calc(100vh - 90px);
  }  
  .content .swiper-container .swiper-slide{
    width: 100%;
    color: #000;
    font-size: 16px;
    text-align: center;
  }
</style>