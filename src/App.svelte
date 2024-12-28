<script lang="ts">
  import Counter from './lib/Counter.svelte'
  import "./app.css"
  import Barchart from './lib/Barchart.svelte';
</script>

<main class="min-h-screen min-w-full flex flex-col justify-evenly items-center">
  <h1 class="text-6xl font-bold text-theme font-serif">DoTLMViz</h1>
  <p class="text-sm font-light font-sans uppercase tracking-widest border border-theme p-2 px-4 rounded-md hover:bg-theme hover:text-theme-w transition-all duration-300 cursor-pointer">This is tailwind test for style</p>
  <Counter />
  <Barchart />
</main>
