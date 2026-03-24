#!/bin/bash
set -e

echo "=== VTP First-Time Setup ==="
echo ""

# 1. Create virtual environment
echo "→ Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 2. Install Python dependencies
echo "→ Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements/production.txt

# 3. Install Node dependencies
echo "→ Installing Node dependencies..."
npm install

# 4. Build Tailwind CSS
echo "→ Building CSS..."
npm run build

# 5. Run migrations
echo "→ Running migrations..."
python manage.py migrate --settings=vtp.settings.production

# 6. Create superuser
echo "→ Creating superuser..."
python manage.py createsuperuser --settings=vtp.settings.production

# 7. Setup default pages
echo "→ Setting up default pages..."
python manage.py setup_pages --settings=vtp.settings.production

# 8. Collect static files
echo "→ Collecting static files..."
python manage.py collectstatic --noinput --settings=vtp.settings.production

echo ""
echo "=== First-time setup complete! ==="
echo "→ Start the server with: gunicorn vtp.wsgi:application --bind 0.0.0.0:8000"
