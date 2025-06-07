#!/usr/bin/env python3
"""
Test script for AI Coding Platform
This script performs basic tests to verify the platform is working correctly
"""

import requests
import json
import time
import sys
from pathlib import Path

def test_backend_health():
    """Test if the backend is running and healthy"""
    try:
        response = requests.get("http://localhost:8000/", timeout=5)
        if response.status_code == 200:
            print("✅ Backend health check passed")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend not accessible: {e}")
        return False

def test_code_execution():
    """Test code execution endpoint"""
    try:
        test_code = """
print("Hello, AI Coding Platform!")
x = 5 + 3
print(f"5 + 3 = {x}")
"""
        
        payload = {
            "code": test_code,
            "timeout": 10
        }
        
        response = requests.post(
            "http://localhost:8000/execute",
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get("status") == "success":
                print("✅ Code execution test passed")
                print(f"   Output: {result.get('output', '').strip()}")
                return True
            else:
                print(f"❌ Code execution failed: {result}")
                return False
        else:
            print(f"❌ Code execution endpoint failed: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Code execution test failed: {e}")
        return False

def test_code_explanation():
    """Test code explanation endpoint"""
    try:
        test_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
        
        payload = {
            "code": test_code,
            "detail_level": "medium"
        }
        
        response = requests.post(
            "http://localhost:8000/explain",
            json=payload,
            timeout=30  # LLM might take longer
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get("status") == "success":
                print("✅ Code explanation test passed")
                explanation = result.get("explanation", "")
                if explanation:
                    print(f"   Explanation preview: {explanation[:100]}...")
                return True
            else:
                print(f"❌ Code explanation failed: {result}")
                return False
        else:
            print(f"❌ Code explanation endpoint failed: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Code explanation test failed: {e}")
        return False

def test_frontend_accessibility():
    """Test if the frontend is accessible"""
    try:
        response = requests.get("http://localhost:3000/", timeout=5)
        if response.status_code == 200:
            print("✅ Frontend accessibility test passed")
            return True
        else:
            print(f"❌ Frontend not accessible: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Frontend not accessible: {e}")
        return False

def check_project_structure():
    """Check if all necessary files and directories exist"""
    required_files = [
        "backend/main.py",
        "backend/requirements.txt",
        "backend/app/services/code_executor.py",
        "backend/app/services/llm_service.py",
        "frontend/package.json",
        "frontend/src/App.js",
        "frontend/src/components/CodeEditor.js",
        "docker-compose.yml",
        ".env"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ Project structure check passed")
        return True

def main():
    """Run all tests"""
    print("🧪 AI Coding Platform Test Suite")
    print("=" * 40)
    
    tests = [
        ("Project Structure", check_project_structure),
        ("Backend Health", test_backend_health),
        ("Code Execution", test_code_execution),
        ("Code Explanation", test_code_explanation),
        ("Frontend Accessibility", test_frontend_accessibility)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name} test...")
        if test_func():
            passed += 1
        time.sleep(1)  # Brief pause between tests
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your AI Coding Platform is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the setup and try again.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
