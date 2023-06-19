<script lang="ts" setup>
import { clsx } from "clsx";
const isFavorite = ref(true);
</script>

<template>
  <div class="item">
    <VIcon
      :icon="isFavorite ? 'mdi-heart' : 'mdi-heart-outline'"
      :class="clsx('favorite', isFavorite && 'active')"
      @click="isFavorite = !isFavorite"
    />
    <div class="image">
      <img src="https://picsum.photos/200/300" alt="Product image" />
    </div>
    <h2 class="name">Bananas, good quality</h2>
    <div class="nutriments"></div>
    <div class="order-detail">
      <div class="quantity">
        <button class="decrease">-</button>
        <span>3</span>
        <button class="increase">+</button>
      </div>
      <div class="price">
        <span class="amount">£1.00</span>
        <span class="unit">per kg</span>
      </div>
    </div>
    <VBtn
      class="add-to-cart text-capitalize"
      color="${green-normal-hover}"
      rounded
      >Add To Basket</VBtn
    >
  </div>
</template>

<style lang="scss" scoped>
@import "../styles/variables.scss";

.item {
  position: relative;
  padding: 15px 12px 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  aspect-ratio: 165 / 236;

  border-radius: 8px;
  box-shadow: 0px 3px 7px rgba(0, 0, 0, 0.25);
  background-color: $white;
}

.favorite {
  position: absolute;
  top: 12px;
  left: 12px;

  color: $grey-normal;

  &.active {
    color: $red-normal-hover;
  }
}

.add-to-cart {
  font-size: 11px;
  background: $green-normal-hover;
  color: $white;
}

.name {
  font-size: 14px;
  line-height: 14/16;
}

.image {
  width: 100%;
  height: 80px;

  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
}
</style>
