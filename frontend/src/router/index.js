import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Registro from '@/components/Registro'
import ForgotPassword from '@/components/ForgotPassword'
import EmailConfirmation from '@/components/EmailConfirmation'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Registro',
      component: Registro
    },
    {
      path: '/forgotPassword',
      name: 'ForgotPassword',
      component: ForgotPassword
    },
    {
      path: '/emailConfirmation/validation_token=:token',
      name: 'EmailConfirmation',
      component: EmailConfirmation
    }
  ]
})
