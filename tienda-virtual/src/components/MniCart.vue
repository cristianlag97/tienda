<template>
  <v-list class="container" style="min-width:320px">
    <v-list-item>
      <v-row>
        <v-col>
          <strong class="ml-auto">Product Title</strong>
        </v-col>
      </v-row>
      <br>
      <v-row>
        <v-col>
          <v-list-item-title> 1 x $3000 <v-btn text>Remove</v-btn></v-list-item-title>
        </v-col>
      </v-row>
    </v-list-item>
    <hr>
    <div class="container text-center">
      <span>Total: $3000</span>
      <v-btn text>Limpiar carrito</v-btn>
    </div>
  </v-list>
</template>