import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'


export const constantRouterMap = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/register',
    component: () => import('@/views/register/index'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  }
]

export const asyncRouterMap = [
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'dashboard', roles: ['admin','editor'] }
    }]
  },
  {
    path: '/studentlecture',
    component: Layout,
    name: 'studentlecture',
    redirect: '/studentlecture/signuplecture',
    meta: { title: '讲座管理', icon: 'example',roles: ["editor"] },
    children: [{
      path: 'signuplecture',
      name: 'Signuplecture',
      component: () => import('@/views/signuplecture/index'),
      meta: { title: '讲座报名', icon: 'bm', roles: ["editor"] }
    },
    {
      path: 'signupstudent',
      name: 'Signupstudent',
      component: () => import('@/views/signupstudent/index'),
      meta: { title: '已报名讲座', icon: 'ybm', roles: ["editor"] }
    }]
  },

  {
    path: '/studentmanager',
    component: Layout,
    redirect: '/studentManager/studentmanager',
    name: 'StudentManager',
    children: [
      {
        path: 'studentmanager',
        name: 'Studentmanager',
        component: () => import('@/views/studentmanager/index'),
        meta: { title: '学生管理', icon: 'stu2', roles: ['admin'] }
      }
    ]
  },
  {
    path: '/lecturemanager',
    component: Layout,
    name: 'Lecturemanager',
    children: [{
      path: 'lecturemanager',
      name: 'lecturemanager',
      component: () => import('@/views/lecturemanager/index'),
      meta: { title: '讲座管理', icon: 'jz', roles: ['admin'] }
    }
    ]
},
{
  path: '/signupadmin',
  component: Layout,
  children: [{
    path: 'signupadmin',
    name: 'Signupadmin',
    component: () => import('@/views/signupadmin/index'),
    meta: { title: '报名管理', icon: 'bmgl', roles: ['admin'] }
  }
  ]
},
  {
    path: '/alterstudent',
    component: Layout,
    children: [
      {
        path: 'alterstudent',
        name: 'Alterstudent',
        component: () => import('@/views/alterstudent/index'),
        meta: { title: '修改个人信息', icon: 'stu',roles: ['editor'] }
      }
    ]
  },
  {
    path: '/alterpwd',
    component: Layout,
    children: [
      {
        path: 'alterpwd',
        name: 'Alterpwd',
        component: () => import('@/views/alterpwd/index'),
        meta: { title: '修改密码', icon: 'passwd',roles: ['editor','admin'] }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
