# Prompt 35 — deployment.sh Script

## Goal

Create a deployment script similar to the reference project.

## Prompt

```
Create deployment.sh for VTP production deployment.

File: deployment.sh

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

Make it executable: chmod +x deployment.sh

Also create:
File: deployment_first_time.sh
- First-time setup script:
  - Create venv
  - Install requirements
  - npm install
  - npm run build
  - Run migrations
  - Create superuser
  - Setup pages (python manage.py setup_pages)
  - Collect static
```

## Verification

1. deployment.sh exists and is executable
2. deployment_first_time.sh exists
3. Scripts have correct paths and commands

## Expected Result

- One-command deployment: `./deployment.sh`
- First-time setup: `./deployment_first_time.sh`
