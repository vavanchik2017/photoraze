import Vue from 'vue'
import VueRouter from "vue-router";
import MainPage from "./pages/Mainpage";

Vue.use(VueRouter)

const routes =[
    {
        path: '/main',
        component: () => MainPage
    },
    {
        path: '/add',
        component: () => import('./pages/Addpage')
    },
    {
        path: '/show',
        component: () => import('./pages/Showpage')
    },
    {
        path: '/autotag',
        component: () => import('./pages/Autotag')
    }
]

export default new VueRouter({
    mode:'history',
    routes
})