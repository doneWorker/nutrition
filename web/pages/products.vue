<script setup>
import { useDisplay } from "vuetify";
// import { fetchProducts } from "~/api/products";

const { xs } = useDisplay();

useHead({
  title: "Products | Main",
});

const { data: products, error } = await $fetch("/api/products", {
  method: "GET",
  params: {
    limit: 10,
  },
}).catch((error) => error.data);

const list = (products || []).map((_product) => ({
  ..._product,
  id: _product.id,
  title: _product.name,
  image: _product.image_url,
}));
</script>
<template>
  <ClientOnly>
    <HeaderDesktopHeader v-if="!xs" />
    <HeaderMobileHeader v-if="xs" />
  </ClientOnly>
  <main>
    <VRow no-gutters justify="center">
      <VCol cols="12" sm="12" md="6" class="d-md-flex align-center py-2">
        <ProductsList :list="list" />
      </VCol>
      <VCol cols="12" sm="12" md="6" class="d-flex align-center py-2">
        <ProductsShelves />
      </VCol>
    </VRow>
  </main>
  <ClientOnly>
    <FooterMobileNav v-if="xs" />
  </ClientOnly>
</template>

<style lang="scss">
@import "../styles/variables.scss";
@import "../styles/mixins.scss";

main {
  min-height: calc(100vh - 60px);
}

@include from-breakpoint("sm") {
  main {
    min-height: calc(100vh - 66px);
    background-color: $green-light;
  }
}
</style>
