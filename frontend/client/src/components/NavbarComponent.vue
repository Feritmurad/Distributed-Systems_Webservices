<template>

<nav class="bg-white bg-gray-900 fixed w-full z-20 top-0 left-0 border-b border-gray-200 border-gray-600">
  <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
  <a  class="flex items-center">
      <img src="./icons/tmdb.svg" class="h-8 mr-3" alt="Tmdb Logo">
  </a>
  <div class="flex md:order-2">
      <button data-collapse-toggle="navbar-sticky" type="button" class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 text-gray-400 hover:bg-gray-700 focus:ring-gray-600" aria-controls="navbar-sticky" aria-expanded="false">
        <span class="sr-only">Open main menu</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
      </button>
  </div>
  <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
    <ul class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white bg-gray-800 md:bg-gray-900 border-gray-700">
      <li>
        <a href="/" class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:hover:text-blue-500 text-black hover:bg-gray-700 hover:text-white md:hover:bg-transparent border-gray-700">Home</a>
      </li>
      <li>
        <a href="/genres" class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:hover:text-blue-500 text-black hover:bg-gray-700 hover:text-white md:hover:bg-transparent border-gray-700">Genres</a>
      </li>
      <li>
        <a href="/actors" class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:hover:text-blue-500 text-black hover:bg-gray-700 hover:text-white md:hover:bg-transparent border-gray-700">Actors</a>
      </li>
      <li>
        <a href="/runtime" class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:hover:text-blue-500 text-black hover:bg-gray-700 hover:text-white md:hover:bg-transparent border-gray-700">Runtime</a>
      </li>
      <li>
        <a href="/likes" class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:hover:text-blue-500 text-black hover:bg-gray-700 hover:text-white md:hover:bg-transparent border-gray-700">Likes</a>
      </li>
      <li>
        <a href="/average_score" class="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:hover:text-blue-500 text-black hover:bg-gray-700 hover:text-white md:hover:bg-transparent border-gray-700">Average Score</a>
      </li>
    </ul>
  </div>
  </div>
</nav>

</template>