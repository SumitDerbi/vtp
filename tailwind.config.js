/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/templates/**/*.html",
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#0284C7",
          light: "#38BDF8",
          dark: "#0369A1",
        },
        secondary: "#1E3A5F",
        accent: "#F59E0B",
        surface: "#F0F9FF",
        steel: "#64748B",
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};
