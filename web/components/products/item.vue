<script lang="ts" setup>
import { clsx } from "clsx";
const isFavorite = ref(true);
const total = ref(0);
const loading = ref(false);

const nutriments = ref({
  energy: 0,
  protein: 0,
  carbs: 0,
  fats: 0,
});

setTimeout(() => {
  nutriments.value = {
    energy: 90,
    protein: 10,
    carbs: 30,
    fats: 70,
  };
}, 1_000);

const onAddToCart = () => {
  loading.value = true;

  setTimeout(() => {
    total.value = 0;
    loading.value = false;
  }, 1_000);
};
</script>

<template>
  <div class="item">
    <VIcon
      :icon="isFavorite ? 'mdi-heart' : 'mdi-heart-outline'"
      :class="clsx('favorite', isFavorite && 'active')"
      @click="isFavorite = !isFavorite"
    />
    <div class="image">
      <img src="/images/bananas.png" alt="Product image" />
    </div>
    <h2 class="name">Bananas, good quality</h2>
    <div class="nutriments">
      <div class="nutriment-item energy">
        <VProgressCircular
          rotate="180"
          :model-value="nutriments.energy"
          class="nutriment-stat"
          ><div class="nutriment-stat--inner">
            550<br />kcal
          </div></VProgressCircular
        >
        <div class="stat-name">Energy</div>
      </div>
      <div class="nutriment-item protein">
        <VProgressCircular
          rotate="180"
          :model-value="nutriments.protein"
          class="nutriment-stat"
          ><div class="nutriment-stat--inner">33g</div></VProgressCircular
        >
        <div class="stat-name">Protein</div>
      </div>
      <div class="nutriment-item fat">
        <VProgressCircular
          rotate="180"
          :model-value="nutriments.fats"
          class="nutriment-stat"
          ><div class="nutriment-stat--inner">10g</div></VProgressCircular
        >
        <div class="stat-name">Fat</div>
      </div>
      <div class="nutriment-item carbs">
        <VProgressCircular
          rotate="180"
          :model-value="nutriments.carbs"
          class="nutriment-stat"
          ><div class="nutriment-stat--inner">10g</div></VProgressCircular
        >
        <div class="stat-name">Carbs</div>
      </div>
    </div>
    <div class="order-detail">
      <div class="quantity">
        <VBtn
          rounded
          elevation="0"
          icon="mdi-minus-thick"
          size="extra-small"
          class="qnt-btn decrease"
          @click="total > 0 && total--"
        />

        <span class="qnt-amount">{{ total }}</span>
        <VBtn
          rounded
          elevation="0"
          icon="mdi-plus-thick"
          size="extra-small"
          class="qnt-btn increase"
          @click="total = total + 1"
        />
      </div>
      <div class="price">
        <span class="amount"><span class="currency">£&nbsp</span>0.55</span>
        <span class="sep">&nbsp/&nbsp</span>
        <span class="unit">kg</span>
      </div>
    </div>
    <VBtn
      class="add-to-cart text-capitalize"
      color="${green-normal-hover}"
      size="small"
      :loading="loading"
      :disabled="loading"
      rounded
      @click="onAddToCart"
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

.nutriments {
  display: flex;
  justify-content: space-between;

  .nutriment-item {
    $item: &;

    width: 32px;
    display: flex;
    flex-direction: column;
    text-align: center;

    .stat-name {
      margin-top: 2px;
      font-size: 7px;
      font-weight: bold;
    }
    .nutriment-stat {
      &::v-deep .v-progress-circular__overlay {
        stroke-linecap: round;
        transition-duration: 0.8s;
      }

      &--inner {
        font-size: 6px;
        font-weight: 600;
        line-height: 1;
      }
    }

    &.energy {
      .stat-name {
        color: $red-normal;
      }

      .nutriment-stat {
        &::v-deep .v-progress-circular__underlay {
          color: $red-light-active;
        }

        &::v-deep .v-progress-circular__overlay {
          color: $red-normal-hover;
        }
      }

      .nutriment-stat--inner {
        color: $red-dark-hover;
      }
    }

    &.protein {
      .stat-name {
        color: $green-normal;
      }

      .nutriment-stat {
        &::v-deep .v-progress-circular__underlay {
          color: $green-light-active;
        }

        &::v-deep .v-progress-circular__overlay {
          color: $green-normal-active;
        }
      }

      .nutriment-stat--inner {
        color: $green-dark-active;
      }
    }

    &.fat {
      .stat-name {
        color: $yellow-normal;
      }

      .nutriment-stat {
        &::v-deep .v-progress-circular__underlay {
          color: $yellow-light-active;
        }

        &::v-deep .v-progress-circular__overlay {
          color: $yellow-normal-hover;
        }
      }

      .nutriment-stat--inner {
        color: $yellow-dark-active;
      }
    }

    &.carbs {
      .stat-name {
        color: $blue-normal;
      }

      .nutriment-stat {
        &::v-deep .v-progress-circular__underlay {
          color: $blue-light-active;
        }

        &::v-deep .v-progress-circular__overlay {
          color: $blue-normal-hover;
        }
      }

      .nutriment-stat--inner {
        color: $blue-dark-active;
      }
    }
  }
}

.order-detail {
  display: flex;
  justify-content: space-between;
  align-items: center;

  font-size: 12px;
  font-weight: 500;
  color: $violet-dark;

  .quantity {
    display: flex;
    align-items: center;
    gap: 1ch;

    .qnt-amount {
      display: flex;
      justify-content: center;
      width: 2ch;
      font-size: 12px;
    }

    .qnt-btn {
      width: 20px;
      height: 20px;
      line-height: 20px;
      font-weight: 600;

      font-size: 8px;
      color: $green-dark;
      background-color: $green-light-hover;
    }
  }

  .price {
    font-weight: 500;
  }
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
  max-width: 100%;
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
