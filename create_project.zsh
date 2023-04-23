#!/bin/zsh

# Create app folder and subfolders
mkdir -p app/api/endpoints
mkdir -p app/api/models
mkdir -p app/core
mkdir -p app/db
mkdir -p app/tests/api/endpoints
mkdir -p app/tests/db

# Create empty __init__.py files
touch app/__init__.py
touch app/api/__init__.py
touch app/api/endpoints/__init__.py
touch app/api/endpoints/example.py
touch app/api/models/__init__.py
touch app/api/models/example.py
touch app/core/__init__.py
touch app/core/config.py
touch app/core/security.py
touch app/core/database.py
touch app/db/__init__.py
touch app/db/base.py
touch app/db/example.py
touch app/db/session.py
touch app/tests/__init__.py
touch app/tests/api/__init__.py
touch app/tests/api/endpoints/__init__.py
touch app/tests/api/endpoints/test_example.py
touch app/tests/db/__init__.py
touch app/tests/db/test_example.py

# Create remaining files
touch .env
touch .gitignore
touch Dockerfile
touch LICENSE
touch README.md
touch requirements.txt
touch setup.py

# Output success message
echo "Project folders and files created successfully!"