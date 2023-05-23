import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { setup, $fetch } from "@nuxt/test-utils";

import svgLoader from "vite-svg-loader";

export default defineConfig({
  plugins: [vue(), svgLoader()],
  resolve: {
    alias: {
      "~/": "/",
    },
  },
  test: {
    globals: true,
    environment: "jsdom",
    coverage: {
      all: true,
      reporter: ["text", "json", "html"],
    },
  },
});
