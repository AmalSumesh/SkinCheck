/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        gold: '#FFD700',
        'gold-dark': '#B8860B',
        'black': '#000000',
        'black-light': '#1a1a1a',
      },
    },
  },
  plugins: [],
}