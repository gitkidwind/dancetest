/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js',
    './node_modules/daisyui/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

module.exports = {

    plugins: [
        require('flowbite/plugin'),
    ]

}

module.exports = {

    plugins: [
        require('tailwind-scrollbar'),
    ]

}

module.exports = {

    plugins: [require("daisyui")],
  }

