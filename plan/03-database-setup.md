# Prompt 03 — Setup Database Connection

## Goal

Ensure database connection works for both dev (SQLite) and production (MySQL via PyMySQL).

## Prompt

```
Verify and finalize database configuration for the VTP project.

1. Dev (already in dev.py): SQLite — no changes needed.

2. Production (production.py): MySQL via PyMySQL.
   The production.py should have:

   import pymysql
   pymysql.install_as_MySQLdb()

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': os.environ.get('DATABASE_NAME', 'vtp'),
           'USER': os.environ.get('DATABASE_USER', 'root'),
           'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
           'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
           'PORT': os.environ.get('DATABASE_PORT', '3306'),
           'OPTIONS': {
               'charset': 'utf8mb4',
               'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
           },
       }
   }

3. Create .env.example file with all required environment variables documented.

4. Add .gitignore with standard Django ignores (db.sqlite3, __pycache__,
   media/, staticfiles/, .env, node_modules/, static/css/output.css).

IMPORTANT: We use PyMySQL (pure Python) instead of mysqlclient (requires C compiler).
```

## Verification

1. `python manage.py check` — passes
2. `.env.example` file created
3. `.gitignore` file created

## Expected Result

- Database config ready for both environments
- PyMySQL used for production MySQL (no C dependency)
