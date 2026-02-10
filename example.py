#!/usr/bin/env python3
"""
Example usage of Trae
Trae 使用示例
"""

import sys
import os

# Add src to path for direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from trae import Trae


def main():
    """Main example function"""
    print("=== Trae Example / Trae 示例 ===\n")

    # Create instance with default name
    print("1. Creating default Trae instance...")
    print("   创建默认 Trae 实例...")
    app = Trae()
    print(f"   Result: {app.run()}\n")

    # Create instance with custom name
    print("2. Creating custom Trae instance...")
    print("   创建自定义 Trae 实例...")
    custom_app = Trae("MyCustomApp")
    print(f"   Result: {custom_app.run()}\n")

    # Process some data
    print("3. Processing data...")
    print("   处理数据...")
    data = "Hello World"
    result = app.process(data)
    print(f"   Input: {data}")
    print(f"   Output: {result}\n")

    # Process with custom app
    print("4. Processing with custom app...")
    print("   使用自定义应用处理...")
    result2 = custom_app.process("测试数据")
    print(f"   Result: {result2}\n")

    print("=== Example completed successfully! ===")
    print("=== 示例成功完成！ ===")


if __name__ == "__main__":
    main()
