<script lang="ts" setup>
import clsx from "clsx";

defineProps<{
  tags: {
    title: string;
    id: string;
    enabled: boolean;
  }[];
}>();
</script>

<template>
  <div class="tags">
    <div class="tags--inner">
      <VChip
        v-for="tag in tags"
        variant="outlined"
        :class="clsx('tag', tag.enabled && 'active')"
        prepend-icon="mdi-check"
        @click="() => (tag.enabled = !tag.enabled)"
      >
        {{ tag.title }}
      </VChip>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "styles/variables.scss";
@import "styles/mixins.scss";

.tags {
  margin: 5px 0;

  &--inner {
    display: flex;
    gap: 10px;

    .tag {
      position: relative;
      padding-left: 12px;

      font-size: 14px;
      font-weight: 500;
      color: $green-dark-active;
      background-color: transparent;
      border: 1.5px solid $green-dark-active;
      transition: padding 0.3s;

      &::v-deep .v-chip__prepend {
        position: absolute;
        left: 0;
        display: flex;
        justify-content: center;
        width: 34px;
        height: 100%;
        margin-right: 10px;

        transition: transform 0.3s;
        transform: translateX(-100%);
        background-color: $green-darker;

        i {
          margin: 0;
        }
      }

      &.active {
        padding-left: 46px;

        background-color: $green-dark-hover;
        border: none;
        color: $white;

        &::v-deep .v-chip__prepend {
          transform: translateX(0);
        }
      }
    }
  }
}
</style>
