<template>
  <div id="home">
    <keep-alive>
      <router-view/>
    </keep-alive>
    <div class="navbar">
      <div :class="$route.name=='Post'?'navbarActive':'navbarItem'">
        <router-link :to="{path:'/post'}" replace>
          <div class="icon" v-show="$route.name=='Post'"><img src="~/assets/images/icons_color/home.png" alt=""></div>
          <div class="icon" v-show="$route.name!='Post'"><img src="~/assets/images/icons/home.png" alt=""></div>
        </router-link>
      </div>
      <div :class="$route.name=='Search'?'navbarActive':'navbarItem'">
        <router-link :to="{path:'/search'}" replace>
          <div class="icon" v-show="$route.name=='Search'"><img src="~/assets/images/icons_color/search.png" alt=""></div>
          <div class="icon" v-show="$route.name!='Search'"><img src="~/assets/images/icons/search.png" alt=""></div>
        </router-link>
      </div>
      <div class="navbarActive">
        <router-link :to="{path:'/post/edit'}">
          <div class="addIcon">
            <span>+</span>
          </div>
        </router-link>
      </div>
      <div :class="$route.name=='Message'?'navbarActive':'navbarItem'">
        <router-link :to="{path:'/message'}" replace>
          <div class="icon" v-show="$route.name=='Message'"><img src="~/assets/images/icons_color/message.png" alt=""></div>
          <div class="icon" v-show="$route.name!='Message'"><img src="~/assets/images/icons/message.png" alt=""></div>
        </router-link>
      </div>
      <div :class="$route.name=='My'?'navbarActive':'navbarItem'">
        <router-link :to="{path:'/my'}" replace>
          <div class="icon" v-show="$route.name=='My'"><img src="~/assets/images/icons_color/my.png" alt=""></div>
          <div class="icon" v-show="$route.name!='My'"><img src="~/assets/images/icons/my.png" alt=""></div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Home",
    data () {
      return {}
    },
    methods:{}
  }
</script>

<style scoped>
  #home {
    width: 100vw;
    height: 100vh;
    position: relative;
  }
  .navbar {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 100vw;
    height: 50px;
    background-color: #fff;
    border-top: 1px solid #ccc;
    display: flex;
    flex-direction: row;
    text-align: center;
    z-index: 1000;
  }
  .navbarItem,
  .navbarActive {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .navbarActive .name {
    color: var(--color-all);
  }
  .icon img {
    width: 25px;
    height: 25px;
  }

  .addIcon {
    border: 2px solid var(--color-all);
    border-radius: 5px;
    width: 35px;
    height: 35px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .addIcon span {
    font-size: 35px;
    color: var(--color-all);
  }
</style>