import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  { path: '/', name: 'Index',redirect: '/login'},
  { path: '/login',name: 'Login',component: () => import('../views/login/index.vue')},
  {
    path: '/home',name: 'Home',redirect: '/post',component: () => import('../views/home/index.vue'),
    children: [
      { path: '/post',name: 'Post',component: () => import('../views/home/post.vue')},
      { path: '/search',name: 'Search',component: () => import('../views/home/search.vue')},
      { path: '/message',name: 'Message',component: () => import('../views/home/message.vue')},
      { path: '/my',name: 'My',component: () => import('../views/home/my.vue')},
    ]
  },
  { path: '/post/edit',name: 'PostEdit',component: () => import('../views/post/edit.vue')},
  { path: '/post/detail',name: 'PostDetail',component: () => import('../views/post/PostDetail.vue')},
]

const router = new VueRouter({
  // mode: 'history',
  mode: 'hash',
  routes
})

export default router
