<script lang="ts">
  let count: number = $state(0)
  const increment = () => {
    count += 1
  }
  import { Icon } from 'svelte-icons-pack';
  import { AiFillHeart } from 'svelte-icons-pack/ai';
</script>

<button class="bg-btn-theme text-theme-w p-2 px-4 rounded-md text-2xl font-bold font-sans" onclick={increment}>
  Count is 
  <span class="min-w-[4rem] inline-block text-center">
    \{count}\
  </span>
  |
  <Icon className="inline-block fill-theme-r mx-2 w-8 h-8" src={AiFillHeart} />
  <span class="text-sm ">- Icons test</span>
</button>
