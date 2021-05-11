export const SET_PRODUCTS = (state, products) => {
  state.products = products
}

export const SET_PRODUCT = (state, id) => {
  state.product = id
}

export const ADD_TO_CART = (state, { product, quantity }) => {

  let productCart = state.cart.find(item => {
    return item.product.id === product.id
  })

  if(productCart){
    productCart.quantity += quantity
    return
  }

  state.cart.push({
    product,
    quantity
  })
}