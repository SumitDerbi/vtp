# Prompt 07 — Install and Configure Tailwind CSS

## Goal

Set up Tailwind CSS with the VTP brand theme: white base + sky blue.

## Prompt

```
Set up Tailwind CSS for the VTP Wagtail project.

1. Create package.json with:
   {
     "name": "vtp",
     "version": "1.0.0",
     "scripts": {
       "dev": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch",
       "build": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify"
     },
     "devDependencies": {
       "tailwindcss": "^3.4"
     }
   }

2. Create tailwind.config.js:
   - Content paths:
     - './templates/**/*.html'
     - './apps/**/templates/**/*.html'
     - './static/js/**/*.js'
   - Theme extend with VTP brand colors:
     - primary: '#0284C7'    (sky-600 — main sky blue)
     - 'primary-light': '#38BDF8'  (sky-400 — lighter sky blue)
     - 'primary-dark': '#0369A1'   (sky-700 — darker blue for hover)
     - secondary: '#1E3A5F'  (dark navy — for headings/contrast)
     - accent: '#F59E0B'     (amber — for CTAs and highlights)
     - 'surface': '#F0F9FF'  (sky-50 — light blue tinted backgrounds)
     - 'steel': '#64748B'    (slate-500 — for manufacturing feel)
   - Custom font: 'sans' → ['Inter', 'system-ui', 'sans-serif']

3. Create static/css/input.css with:
   @tailwind base;
   @tailwind components;
   @tailwind utilities;

   @layer components {
     .btn-primary {
       @apply bg-primary text-white px-6 py-3 rounded-lg font-semibold
              hover:bg-primary-dark transition-colors duration-200;
     }
     .btn-accent {
       @apply bg-accent text-white px-6 py-3 rounded-lg font-semibold
              hover:bg-amber-600 transition-colors duration-200;
     }
     .btn-outline {
       @apply border-2 border-primary text-primary px-6 py-3 rounded-lg font-semibold
              hover:bg-primary hover:text-white transition-colors duration-200;
     }
     .section-heading {
       @apply text-3xl font-bold text-secondary mb-6;
     }
     .card {
       @apply bg-white rounded-xl shadow-md overflow-hidden
              hover:shadow-lg transition-shadow duration-200;
     }
   }

4. Run: npm install && npm run build

Theme rationale:
- White (#FFFFFF) base for clean, professional manufacturing look
- Sky blue (#0284C7) as primary — bright, trustworthy, modern
- Dark navy (#1E3A5F) for headings — authority, precision
- Amber (#F59E0B) accent — draws attention to CTAs
- Surface (#F0F9FF) — subtle sky-blue tinted sections
```

## Verification

1. `package.json` and `tailwind.config.js` exist
2. `npm install && npm run build` succeeds
3. `static/css/output.css` generated

## Expected Result

- Tailwind CSS configured with white + sky blue theme
- Build pipeline working
