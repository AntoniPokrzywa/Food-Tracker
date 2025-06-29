#!/usr/bin/env python3
"""
Development startup script for Food Tracker backend
This script sets up the environment and starts the Flask development server
"""

import os
import sys

# Set environment variables for development
os.environ.setdefault('SECRET_KEY', 'dev-secret-key-change-in-production')
os.environ.setdefault('FLASK_ENV', 'development')

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

if __name__ == "__main__":
    app = create_app()
    print("🚀 Starting Food Tracker Backend...")
    print("📊 Using SQLite database for development")
    print("🔗 API available at: http://localhost:5000")
    print("👤 Test user: test@example.com / password123")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000) 