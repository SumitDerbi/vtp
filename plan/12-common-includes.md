# Prompt 12 — Create Common Includes (Breadcrumbs, CTA Banner)

## Goal

Create reusable template includes for breadcrumbs and call-to-action banner.

## Prompt

```
Create common template includes for VTP.

1. File: templates/includes/breadcrumbs.html
   - White background strip with subtle border-bottom
   - Shows: Home > Parent Page > Current Page
   - Use self.get_ancestors() for breadcrumb trail
   - Text-sm, text-steel color, links in text-primary
   - Container max-w-7xl mx-auto px-4

2. File: templates/includes/cta_banner.html
   - Full-width gradient banner (from primary to primary-dark)
   - Centered heading: "Need Precision Tooling Solutions?"
   - Sub-text: "Get in touch with our team for custom requirements"
   - "Contact Us" button (white bg, text-primary)
   - Padding: py-16, responsive text sizing
   - Can be included on any page: {% include "includes/cta_banner.html" %}

3. File: templates/includes/whatsapp_widget.html
   - Fixed bottom-right WhatsApp floating button
   - Shows only if whatsapp_number is set in SiteSettings
   - Green WhatsApp icon, circular, with hover animation
   - Links to wa.me/<number>

All includes use Tailwind classes. Clean, minimal design.
```

## Verification

1. All include files created
2. Can be included in base.html or individual templates
3. Breadcrumbs show correct page hierarchy
4. CTA banner renders with sky blue gradient
5. WhatsApp widget shows in bottom-right

## Expected Result

- Reusable includes ready for all page templates
