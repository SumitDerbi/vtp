# Prompt 06 — First Migration & Superuser Creation

## Goal

Run initial migrations and create the admin superuser.

## Prompt

```
1. Run initial migrations:
   python manage.py makemigrations
   python manage.py migrate

2. Create superuser:
   python manage.py createsuperuser
   - Username: admin
   - Email: admin@vtp.com
   - Password: (set during prompt)

3. Run the development server:
   python manage.py runserver

4. Verify:
   - Visit http://localhost:8000/admin/ — Wagtail admin loads
   - Login with admin credentials
   - Default "Welcome to Wagtail" page exists
```

## Verification

1. All migrations run without errors
2. Wagtail admin is accessible
3. Can log in with superuser credentials
4. Default page tree exists

## Expected Result

- Database initialized with all Django/Wagtail tables
- Superuser created
- Wagtail admin accessible at /admin/
- **MILESTONE: Foundation complete, ready for templates!**
