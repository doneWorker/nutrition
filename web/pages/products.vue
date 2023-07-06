<script lang="ts" setup>
import { useDisplay } from "vuetify";

const { xs } = useDisplay();

useHead({
  title: "Products | Main",
});

const { data: products, error } = await $fetch<{ data: unknown }>(
  "/api/products",
  {
    method: "GET",
    params: {
      limit: 20,
    },
  }
).catch((error) => error.data);

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

const viewMode = reactive<SortOptions["viewMode"]>({ view: "grid" });
type SortOptions = {
  viewMode: { view: "grid" | "list" };
  sortOptions: {
    sortBy: "relevance" | "protein" | "carbs" | "fats";
    sortOrder: "none" | "asc" | "desc";
  };
};
const sortOptions = reactive<SortOptions["sortOptions"]>({
  sortBy: "protein",
  sortOrder: "none",
});

const onSortOrder = () => {
  if (sortOptions.sortOrder === "none") sortOptions.sortOrder = "asc";
  else if (sortOptions.sortOrder === "asc") sortOptions.sortOrder = "desc";
  else if (sortOptions.sortOrder === "desc") sortOptions.sortOrder = "none";
};
</script>
<template>
  <ClientOnly>
    <HeaderDesktopHeader class="d-none d-md-flex" />
    <HeaderMobileHeader class="d-md-none" />
  </ClientOnly>

  <main>
    <VRow no-gutters justify="center">
      <VCol
        cols="12"
        sm="12"
        md="6"
        class="align-center py-3 px-3 px-md-8"
        id="products"
      >
        <ProductsFilters
          class="d-none d-md-block"
          :breadcrumbs="breadcrumbs"
          :viewMode="viewMode"
          :sortOptions="sortOptions"
          @sortOrder="onSortOrder"
        />
        <ProductsTags class="d-none d-md-block" :tags="tags" />
        <ProductsList :list="products" :variant="viewMode.view" />
      </VCol>
      <VCol
        cols="12"
        sm="12"
        md="6"
        class="d-none align-center py-3 px-3 px-md-8 d-md-flex"
      >
        <ProductsShowcase
          :total="{ totalItems: 15, totalBudget: 1000, totalSpent: 500 }"
        />
      </VCol>
    </VRow>
  </main>
  <ClientOnly>
    <FooterMobileNav v-if="xs" />
  </ClientOnly>
</template>

<style lang="scss" scoped>
@import "styles/mixins.scss";

main {
  min-height: calc(100vh - 60px);
}

@include from-breakpoint("sm") {
  main {
    min-height: calc(100vh - 66px);
    padding: 20px 0;

    background-color: $green-light;
  }

  #products {
    overflow: scroll;
    height: calc(100vh - 66px - 12px - 20px);
  }
}
</style>
