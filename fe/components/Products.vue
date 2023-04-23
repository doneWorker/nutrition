<template>
  <div>
    <div>Products page</div>
    <span>{{ greetingMessage }}</span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'NuxtProducts',
  props: {
    greetingMessage: String,
  },
  setup(props) {
    return props.greetingMessage // type: string | undefined
  },
})

// export default {
//   name: 'NuxtProducts',
//   props: {
//     greetingMessage: String,
//   },
// }
</script>

<style>
.nuxt-logo {
  height: 180px;
}
</style>
