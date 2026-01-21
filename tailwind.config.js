// tailwind.config.js
module.exports = {
  darkMode: 'class',          // Enables dark: prefix
  content: [
    './templates/**/*.html',
    './core/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#10b981',   // emerald-500 like Supabase/Turborepo green
      },
    },
  },
  plugins: [],
}