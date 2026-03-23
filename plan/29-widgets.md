# Prompt 29 — WhatsApp Widget & Scroll to Top

## Goal

Add WhatsApp floating chat button and scroll-to-top feature.

## Prompt

```
Finalize the interactive widgets for VTP.

1. Update templates/includes/whatsapp_widget.html (from Prompt 12):
   - Fixed position: bottom-6 right-6 (z-50)
   - Green circle (#25D366) with WhatsApp SVG icon
   - Hover: scale-110 + shadow-lg
   - Links to: https://wa.me/{{ settings.common.SiteSettings.whatsapp_number }}
   - Only visible if whatsapp_number is set
   - Smooth pulse animation on idle (optional)

2. Add scroll-to-top button:
   File: templates/includes/scroll_top.html
   - Fixed position: bottom-6 right-20 (left of WhatsApp)
   - Sky blue circle with up-arrow icon
   - Only visible when scrolled down 300px+ (Alpine.js)
   - Smooth scroll to top on click
   - Transition: opacity + slide-up

3. Include both in base.html before closing </body>:
   {% include "includes/whatsapp_widget.html" %}
   {% include "includes/scroll_top.html" %}

Both use Alpine.js for show/hide logic.
```

## Verification

1. WhatsApp button visible (when number set)
2. Clicking opens WhatsApp chat
3. Scroll-to-top appears on scroll
4. Clicking scrolls smoothly to top
5. Both positioned correctly, not overlapping

## Expected Result

- Floating WhatsApp chat + scroll-to-top buttons
