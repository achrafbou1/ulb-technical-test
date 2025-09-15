<script setup lang="ts">
interface NavLink {
  label: string
  to: string
}

const links: NavLink[] = [
  {label: 'Cours', to: '/cours'},
  {label: 'Inscriptions', to: '/inscriptions'},
  {label: 'Notes', to: '/notes'}
]
</script>

<template>
  <div class="max-h-screen flex flex-col">
    <!-- Navigation -->
    <header class="border-b bg-white">
      <UContainer class="flex items-center justify-between py-4">
        <!-- Logo -->
        <NuxtLink to="/" class="text-xl font-bold text-primary">
          PsyEL Interface
        </NuxtLink>

        <!-- Navigation links -->
        <nav class="hidden md:flex gap-6">
          <NuxtLink
              v-for="link in links"
              :key="link.to"
              :to="link.to"
              class="text-gray-700 hover:text-primary transition"
          >
            {{ link.label }}
          </NuxtLink>
        </nav>
      </UContainer>
    </header>

    <!-- Page content -->
    <UContainer class="max-h-screen grid grid-cols-12 gap-6 p-6">
      <!-- Main content, mx is done purposefully for responsiveness, less colspans on large screen doesn't look good -->
      <main class="md:col-span-12 sm:col-span-12 lg:col-span-12 mx-20 my-20">
        <NuxtPage/>
      </main>
    </UContainer>

    <!-- Footer -->
    <footer class="border-t py-4 text-center text-gray-500">
      © 2025 PsyEl Interface. All rights reserved.
    </footer>
  </div>
</template>