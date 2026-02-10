"""
Tests for Trae
Trae 测试
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from trae import Trae


def test_trae_init():
    """Test Trae initialization"""
    app = Trae()
    assert app.name == "Trae"

    app_custom = Trae("CustomTrae")
    assert app_custom.name == "CustomTrae"


def test_trae_run():
    """Test Trae run method"""
    app = Trae()
    result = app.run()
    assert result == "Hello from Trae!"

    app_custom = Trae("Test")
    result_custom = app_custom.run()
    assert result_custom == "Hello from Test!"


def test_trae_process():
    """Test Trae process method"""
    app = Trae()
    result = app.process("test data")
    assert result == "[Trae] Processed: test data"


if __name__ == "__main__":
    print("Running tests...")
    test_trae_init()
    print("✓ test_trae_init passed")
    
    test_trae_run()
    print("✓ test_trae_run passed")
    
    test_trae_process()
    print("✓ test_trae_process passed")
    
    print("\nAll tests passed! 所有测试通过！")
