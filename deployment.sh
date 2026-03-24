#!/bin/bash
set -e

echo "=== VTP Deployment Script ==="
echo ""

# 1. Pull latest code
echo "→ Pulling latest code..."
git pull origin main

# 2. Activate virtual environment
echo "→ Activating virtual environment..."
source venv/bin/activate

# 3. Install/update dependencies
echo "→ Installing dependencies..."
pip install -r requirements/production.txt

# 4. Build Tailwind CSS
echo "→ Building CSS..."
npm run build

# 5. Run migrations
echo "→ Running migrations..."
python manage.py migrate --settings=vtp.settings.production

# 6. Collect static files
echo "→ Collecting static files..."
python manage.py collectstatic --noinput --settings=vtp.settings.production

# 7. Restart gunicorn
echo "→ Restarting application..."
sudo systemctl restart vtp

echo ""
echo "=== Deployment complete! ==="
