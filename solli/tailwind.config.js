/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",     // todos os templates HTML
        "./static/**/*.js",          // scripts JS com classes Tailwind
        "./**/templates/**/*.html",  // para apps Django com templates próprios
        "./**/static/**/*.js",       // idem para JS nos apps
    ],

    theme: {
        extend: {},
    },
    plugins: [],

}

