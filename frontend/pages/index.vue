<template>
    <div>
      <!-- <NuxtWelcome /> -->
       <p class="text-2xl font-bold text-red-400">Home Page</p>
       <div v-for="post in posts.post" :key="post.id">
        <p>Product</p>   
        {{ post.title }}
       
        </div>
{{ posts }}
    </div>
  </template>

<script setup>
    const {data: posts} =await useFetch('http://127.0.0.1:8000/api/')
</script>