#!/bin/bash

# Save current environment packages
pip freeze > requirements.txt

git add .
git commit -m "Deploy to gowell.edu.np"
git push origin main

echo "🔐 Connecting to server via SSH..."

ssh prakash2@95.217.203.22 -p 1980 << 'EOF'

set -e

echo "🚀 Starting deployment on remote server..."

# Activate virtual environment and change to project directory
source /home3/prakash2/virtualenv/gowell.edu.np/3.11/bin/activate
cd /home3/prakash2/gowell.edu.np

# Install/update Python dependencies only if requirements.txt changed
git pull origin main
if [ requirements.txt -nt .requirements_installed ]; then
    echo "📦 Installing/updating requirements..."
    pip install -r requirements.txt
    touch .requirements_installed
fi

# Run migrations
echo "🛠️ Running makemigrations..."
python manage.py makemigrations --noinput

echo "⚙️ Applying migrations..."
python manage.py migrate --noinput

# Collect static files
echo "🎒 Collecting static files..."
python manage.py collectstatic --noinput

# Restart Passenger
echo "♻️ Restarting Passenger server..."
touch tmp/restart.txt

echo "✅ Deployment completed successfully."

deactivate
exit
EOF

echo "🔚 SSH session closed."
