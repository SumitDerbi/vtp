# Prompt 24 — DownloadIndexPage Template

## Goal

Create the downloads page listing all downloadable files.

## Prompt

```
Create the DownloadIndexPage template for VTP.

File: apps/downloads/templates/downloads/download_index_page.html

{% extends "base.html" %}
{% load wagtailcore_tags wagtailimages_tags %}

Sections:

1. BREADCRUMBS
2. PAGE HEADER: heading + intro, bg-surface

3. DOWNLOADS LIST:
   - Container max-w-5xl mx-auto px-4 py-12
   - Each download item as a card/row:
     - Left: File icon (PDF icon, or thumbnail if available)
     - Middle:
       - Title (font-semibold, text-secondary)
       - Description (text-gray-600)
       - Category badge if set (small pill, bg-primary/10 text-primary)
     - Right: Download button/link (btn-outline, small)
       - Links to file.url for direct download
       - File size shown if available
   - Cards: white bg, rounded-lg, shadow-sm, border
   - Gap between items: space-y-4

4. EMPTY STATE:
   - "No downloads available yet" with icon

Filter by category if categories exist (optional — simple version first).
Clean, organized file listing. Easy to scan.

Use: {{ download.file.url }} for download link.
Use: {{ download.file.title }} for file info.
```

## Verification

1. Downloads page renders
2. Download items listed with title, description, file link
3. Download links work (file downloads)
4. Responsive layout
5. Empty state shown when no downloads

## Expected Result

- Clean downloads section with organized file listing
