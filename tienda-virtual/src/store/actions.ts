import axios from 'axios'

export const getProducts = ({ commit }) => {
  axios.get('http://localhost:8000/api/v1/product/')
  .then(response => {
    commit('SET_PRODUCTS', response.data)
  })
}

export const getProduct = ({ commit }, id) => {
  axios.get(`http://localhost:8000/api/v1/product/${id}`)
  .then(response => {
    commit('SET_PRODUCT', response.data)
  })
}

export const addProductToCart = ({ commit }, {product, quantity}) =>{
  commit('ADD_TO_CART', { product, quantity })

  axios.post('http://localhost:8000/api/v1/product/')
}