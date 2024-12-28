/** @type {import('tailwindcss').Config} */

export default {
  plugins: [],
  content: ["./index.html",'./src/**/*.{svelte,js,ts}'], // for unused CSS
  theme: {
    extend: {
      colors: {
        "theme" : "#665191",
        "btn-theme" : "#2f4b7c",
        "theme-w" : "#efefef",
        "theme-r" : "#fb5a68",
      }
    },
  },
  variants: {
    extend: {},
  },
  darkMode: false, // or 'media' or 'class'
}

