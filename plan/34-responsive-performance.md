# Prompt 34 — Responsive Testing & Performance

## Goal

Verify responsive design and optimize performance.

## Prompt

```
Responsive testing and performance optimization for VTP:

1. RESPONSIVE CHECKS:
   - All templates work at: 375px, 768px, 1024px, 1280px, 1536px
   - Header: hamburger on mobile, full nav on desktop
   - Product grid: 1 col → 2 col → 3 col
   - Forms: full width on mobile, appropriate on desktop
   - Images: responsive with srcset (using Wagtail's {% image %} tag)
   - Text: readable at all sizes (no text-xs on body content)
   - Touch targets: min 44px for buttons/links on mobile

2. PERFORMANCE:
   - Tailwind CSS: run `npm run build` (minified output)
   - Images: use Wagtail renditions (fill/max) for appropriate sizes
   - Lazy loading: add loading="lazy" to below-fold images
   - WhiteNoise for static files (already configured)
   - Minimize external requests (only Google Fonts + Alpine.js CDN)

3. ACCESSIBILITY:
   - All images have alt text (from Wagtail image title)
   - Form labels present
   - Sufficient color contrast (white/sky blue passes AA)
   - Focus states on interactive elements
   - Semantic HTML (header, main, footer, nav, article)

4. Run Lighthouse audit — target:
   - Performance: 80+
   - Accessibility: 90+
   - Best Practices: 90+
   - SEO: 90+
```

## Expected Result

- Responsive, performant, accessible website
