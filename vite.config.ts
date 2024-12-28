/// <reference types="vite/client" />

import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import postcss from 'postcss';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  css:{
    postcss
  }
})