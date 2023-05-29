import vuetify from "vite-plugin-vuetify";
import { createResolver } from "@nuxt/kit";
import svgLoader from "vite-svg-loader";

const { resolve } = createResolver(import.meta.url);

export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiUrl: "/api/v1",
    },
  },
  css: [
    "vuetify/lib/styles/main.sass",
    "@mdi/font/css/materialdesignicons.min.css",
  ],
  pages: true,
  build: {
    transpile: ["vuetify"],
  },
  hooks: {
    "vite:extendConfig": (config) => {
      config?.plugins?.push(
        vuetify({
          styles: { configFile: resolve("./settings.scss") },
        })
      );
    },
  },
  vite: {
    plugins: [svgLoader()],
  },
});
