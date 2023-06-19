<template>
  <main><Header /></main>
</template>

<style lang="scss">
@import "../styles/variables.scss";

main {
  background-color: $green-light;
}

.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-gap: 1rem;
}
</style>
