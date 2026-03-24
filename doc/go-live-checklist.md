# VTP Website — Go-Live Checklist

## Pre-Launch ✅

| #   | Task                       | Status        | Notes                                                                          |
| --- | -------------------------- | ------------- | ------------------------------------------------------------------------------ |
| 1   | All pages created          | ✅ Done       | 13 pages in tree (Home, About, Facility, Products×7, Blog, Downloads, Contact) |
| 2   | Product images uploaded    | ⬜ Pending    | Upload via Wagtail Admin → Images, then assign to each ProductPage             |
| 3   | Logo (PNG + SVG) uploaded  | ⬜ Pending    | Upload via Settings → Site Settings → Company section                          |
| 4   | Favicon set                | ⬜ Pending    | Upload via Settings → Site Settings → Favicon (renders 32×32 + 16×16)          |
| 5   | Contact info filled        | ⬜ Pending    | Settings → Site Settings → Contact (phone, email, address)                     |
| 6   | Social media links set     | ⬜ Pending    | Settings → Site Settings → Social Media                                        |
| 7   | WhatsApp number configured | ⬜ Pending    | Settings → Site Settings → WhatsApp (format: 919876543210)                     |
| 8   | Contact form tested        | ✅ Code Ready | Saves to DB + email notification. Test on live after content setup             |
| 9   | Enquiry form tested        | ✅ Code Ready | Links to product page. Test on live after content setup                        |
| 10  | Blog has at least 1 post   | ⬜ Pending    | Add via Pages → Blog → Add Child Page                                          |
| 11  | Downloads section has file | ⬜ Pending    | Add via Snippets → Download Items                                              |
| 12  | Admin listings working     | ✅ Done       | Contact Responses + Product Enquiries in Admin sidebar                         |

## SEO ✅

| #   | Task                    | Status     | Notes                                                    |
| --- | ----------------------- | ---------- | -------------------------------------------------------- |
| 1   | Meta descriptions set   | ⬜ Pending | Edit each page → Promote tab → Search Description        |
| 2   | OG images set           | ⬜ Pending | Edit each page → Promote tab → Search Image              |
| 3   | sitemap.xml accessible  | ✅ Done    | Verified: `/sitemap.xml` returns 200                     |
| 4   | robots.txt accessible   | ✅ Done    | Verified: `/robots.txt` returns 200 with proper content  |
| 5   | Google Analytics ID set | ⬜ Pending | Settings → Site Settings → Analytics → GA Measurement ID |
| 6   | JSON-LD structured data | ✅ Done    | Organization schema in base.html                         |
| 7   | Canonical URLs          | ✅ Done    | `<link rel="canonical">` on every page                   |
| 8   | wagtailmetadata tags    | ✅ Done    | OG + Twitter meta tags via `{% meta_tags %}`             |

## Production Configuration

| #   | Task                   | Status      | Notes                                                                                                                  |
| --- | ---------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1   | SECRET_KEY changed     | ⬜ Required | Generate: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| 2   | DEBUG = False          | ✅ Done     | Set in `production.py`                                                                                                 |
| 3   | ALLOWED_HOSTS set      | ⬜ Required | Set `ALLOWED_HOSTS` env var to actual domain(s)                                                                        |
| 4   | Database configured    | ⬜ Required | Set `DATABASE_HOST`, `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD` env vars (MySQL + PyMySQL)                  |
| 5   | Static files collected | ⬜ Required | Run `python manage.py collectstatic --noinput`                                                                         |
| 6   | Media files served     | ✅ Done     | Nginx config serves `/media/` from container volume                                                                    |
| 7   | HTTPS configured       | ✅ Done     | `SECURE_SSL_REDIRECT=True`, `HSTS=31536000`, secure cookies                                                            |
| 8   | Email SMTP configured  | ⬜ Required | Set `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` env vars                                      |
| 9   | deployment.sh ready    | ✅ Done     | Both `deployment.sh` and `deployment_first_time.sh` created                                                            |
| 10  | Docker files ready     | ✅ Done     | Dockerfile, docker-compose.yml, nginx/default.conf                                                                     |

## Performance

| #   | Task                  | Status     | Notes                                                                       |
| --- | --------------------- | ---------- | --------------------------------------------------------------------------- |
| 1   | Tailwind CSS minified | ✅ Done    | `npm run build` produces minified output.css                                |
| 2   | Images optimized      | ✅ Done    | Wagtail image renditions auto-resize, lazy loading on all below-fold images |
| 3   | Lazy loading          | ✅ Done    | `loading="lazy"` on all images except hero                                  |
| 4   | Lighthouse audit      | ⬜ Pending | Run after deployment with real content                                      |
| 5   | Mobile responsive     | ✅ Done    | All templates use Tailwind responsive classes                               |
| 6   | Focus states          | ✅ Done    | All interactive elements have focus-visible styles                          |
| 7   | ARIA attributes       | ✅ Done    | Lightbox, navigation, modals have proper ARIA labels                        |

## Post-Launch

| #   | Task                                    | Notes                                             |
| --- | --------------------------------------- | ------------------------------------------------- |
| 1   | Submit sitemap to Google Search Console | `https://yourdomain.com/sitemap.xml`              |
| 2   | Test all forms on production            | Contact form + Product enquiry form               |
| 3   | Monitor error logs                      | Check gunicorn/nginx logs regularly               |
| 4   | Set up regular backups                  | Database (mysqldump) + media files                |
| 5   | Set up SSL certificate                  | Use Let's Encrypt / Certbot or cloud provider SSL |
| 6   | Test email delivery                     | Verify contact/enquiry notification emails arrive |

## Quick Deployment Commands

### Docker (Recommended)

```bash
# First time
cp .env.example .env
# Edit .env with production values
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py setup_pages
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py collectstatic --noinput

# Updates
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py collectstatic --noinput
```

### Manual (VPS)

```bash
# First time
bash deployment_first_time.sh

# Updates
bash deployment.sh
```

## Environment Variables Required

```
SECRET_KEY=<generate-a-strong-key>
DJANGO_SETTINGS_MODULE=vtp.settings.production
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_HOST=db          # 'db' for Docker, 'localhost' for manual
DATABASE_NAME=vtp_db
DATABASE_USER=vtp_user
DATABASE_PASSWORD=<strong-password>
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=<app-password>
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
```
