#!/usr/bin/env python3
"""
Setup script for AI Coding Platform
This script helps set up the development environment
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            capture_output=True, 
            text=True,
            cwd=cwd
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking requirements...")
    
    # Check Python
    try:
        python_version = sys.version_info
        if python_version.major < 3 or python_version.minor < 8:
            print("❌ Python 3.8+ is required")
            return False
        print(f"✅ Python {python_version.major}.{python_version.minor}")
    except:
        print("❌ Python not found")
        return False
    
    # Check Node.js
    success, output = run_command("node --version")
    if success:
        print(f"✅ Node.js {output.strip()}")
    else:
        print("❌ Node.js not found. Please install Node.js 16+")
        return False
    
    # Check npm
    success, output = run_command("npm --version")
    if success:
        print(f"✅ npm {output.strip()}")
    else:
        print("❌ npm not found")
        return False
    
    return True

def setup_backend():
    """Set up the backend environment"""
    print("\n🔧 Setting up backend...")
    
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found")
        return False
    
    # Create virtual environment
    print("Creating virtual environment...")
    success, output = run_command("python -m venv venv", cwd=backend_dir)
    if not success:
        print(f"❌ Failed to create virtual environment: {output}")
        return False
    
    # Activate virtual environment and install dependencies
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate && pip install -r requirements.txt"
    else:  # Unix/Linux/macOS
        activate_cmd = "source venv/bin/activate && pip install -r requirements.txt"
    
    print("Installing Python dependencies...")
    success, output = run_command(activate_cmd, cwd=backend_dir)
    if not success:
        print(f"❌ Failed to install dependencies: {output}")
        return False
    
    print("✅ Backend setup complete")
    return True

def setup_frontend():
    """Set up the frontend environment"""
    print("\n🔧 Setting up frontend...")
    
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend directory not found")
        return False
    
    # Install npm dependencies
    print("Installing npm dependencies...")
    success, output = run_command("npm install", cwd=frontend_dir)
    if not success:
        print(f"❌ Failed to install npm dependencies: {output}")
        return False
    
    print("✅ Frontend setup complete")
    return True

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    
    directories = [
        "models",
        "logs",
        "temp"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created {directory}/")

def main():
    """Main setup function"""
    print("🚀 AI Coding Platform Setup")
    print("=" * 40)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Setup failed. Please install missing requirements.")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Setup backend
    if not setup_backend():
        print("\n❌ Backend setup failed.")
        sys.exit(1)
    
    # Setup frontend
    if not setup_frontend():
        print("\n❌ Frontend setup failed.")
        sys.exit(1)
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Start the backend: cd backend && python main.py")
    print("2. Start the frontend: cd frontend && npm start")
    print("3. Open http://localhost:3000 in your browser")
    print("\nNote: The first run may take time to download the LLM model.")

if __name__ == "__main__":
    main()
