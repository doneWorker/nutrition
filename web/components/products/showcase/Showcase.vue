<script lang="ts" setup>
import ShowcaseTotal from "./ShowcaseTotal.vue";
import ShowcaseBasket from "./ShowcaseBasket.vue";
import ShowcaseFooter from "./ShowcaseFooter.vue";

defineProps<{
  total: { totalItems: number; totalBudget: number; totalSpent: number };
}>();
</script>

<template>
  <div class="showcase">
    <ShowcaseTotal />
    <ShowcaseBasket />
    <ShowcaseFooter />
  </div>
</template>

<style lang="scss" scoped>
.showcase {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 15px;
}
</style>
