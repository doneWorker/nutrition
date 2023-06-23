<script setup>
import { useDisplay } from "vuetify";

const { xs } = useDisplay();

useHead({
  title: "Products | Main",
});
</script>
<template>
  <ClientOnly>
    <HeaderDesktopHeader v-if="!xs" />
    <HeaderMobileHeader v-if="xs" />
  </ClientOnly>
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
  <ClientOnly>
    <FooterMobileNav v-if="xs" />
  </ClientOnly>
</template>

<style lang="scss">
@import "../styles/variables.scss";

main {
  min-height: calc(100vh - 60px);
}

@media screen and (min-width: 400px) {
  main {
    min-height: calc(100vh - 66px);
    background-color: $green-light;
  }
}
</style>
