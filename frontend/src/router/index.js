import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Registro from '@/components/Registro'
import ForgotPassword from '@/components/ForgotPassword'
import Product from '@/components/Product'
import AddProduct from '@/components/AddProduct'
import Main from '@/components/Main'
import EmailConfirmation from '@/components/EmailConfirmation'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/categoria/:categoria',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/products',
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
      path: '/product/:id',
      name: 'Product',
      component: Product
    },
    {
      path: '/catalog/add',
      name: 'AddProduct',
      component: AddProduct
    },
    {
      path: '/emailConfirmation/validation_token=:token',
      name: 'EmailConfirmation',
      component: EmailConfirmation
    }
  ]
})
