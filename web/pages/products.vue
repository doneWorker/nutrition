<template>
  <div>
    <Header />
    <main>
      <VRow no-gutters justify="center">
        <VCol cols="12" sm="12" md="6" class="d-flex align-center py-2">
          <ProductsList />
        </VCol>
        <VCol cols="12" sm="12" md="6" class="d-flex align-center py-2">
          <ProductsShelves />
        </VCol>
      </VRow>
    </main>
  </div>
</template>

<style lang="scss">
@import "../styles/variables.scss";

main {
  min-height: calc(100vh - 66px);

  background-color: $green-light;
}

/* .product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-gap: 1rem;
} */
</style>
