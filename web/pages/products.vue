<script setup>
import { useDisplay } from "vuetify";

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

const tags = reactive([
  { id: "all", title: "All", enabled: true },
  { id: "fruits", title: "Fruits", enabled: false },
  { id: "vegetables", title: "Vegetables", enabled: true },
]);

const breadcrumbs = [
  { title: "Home", url: "/" },
  { title: "Products", url: "/products" },
  { title: "Fruits and vegetables", url: "/products/fruits-and-vegetables" },
];
</script>
<template>
  <ClientOnly>
    <HeaderDesktopHeader class="d-none d-md-flex" />
    <HeaderMobileHeader class="d-md-none" />
  </ClientOnly>

  <main>
    <VRow no-gutters justify="center">
      <VCol cols="12" sm="12" md="6" class="align-center">
        <ProductsFilters class="d-none d-md-block" :breadcrumbs="breadcrumbs" />
        <ProductsTags class="d-none d-md-block" :tags="tags" />
        <ProductsList :list="list" />
      </VCol>
      <VCol cols="12" sm="12" md="6" class="d-flex align-center">
        <ProductsShelves />
      </VCol>
    </VRow>
  </main>
  <ClientOnly>
    <FooterMobileNav v-if="xs" />
  </ClientOnly>
</template>

<style lang="scss" scoped>
@import "../styles/mixins.scss";

main {
  min-height: calc(100vh - 60px);
  padding: 10px;
}

@include from-breakpoint("sm") {
  main {
    min-height: calc(100vh - 66px);
    padding: 20px 30px;

    background-color: $green-light;
  }
}
</style>
