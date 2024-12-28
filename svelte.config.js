import { vitePreprocess } from '@sveltejs/vite-plugin-svelte'
import autoprefixer from "autoprefixer";
import tailwindcss from "tailwindcss";

export default {
  // Consult https://svelte.dev/docs#compile-time-svelte-preprocess
  // for more information about preprocessors
  preprocess: vitePreprocess({
      scss: {
          prependData: `@import 'src/styles/variables.scss';`
      },
      postcss: {
        plugins: [tailwindcss(), autoprefixer()],
      },
    }),
}
