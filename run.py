"""
应用启动脚本
"""
import os
import sys
import subprocess
from pathlib import Path

# 确保工作目录正确
PROJECT_ROOT = Path(__file__).parent
os.chdir(PROJECT_ROOT)

# 添加 backend 到 Python 路径
sys.path.insert(0, str(PROJECT_ROOT / "backend"))


def check_requirements():
    """检查依赖是否已安装"""
    try:
        import fastapi
        import uvicorn
        import requests
        import apscheduler
        import aiosqlite
        import loguru
        return True
    except ImportError as e:
        print(f"❌ 缺少依赖包: {e}")
        print("\n请运行以下命令安装依赖:")
        print("  pip install -r requirements.txt")
        return False


def check_env_file():
    """检查环境变量文件"""
    env_file = PROJECT_ROOT / ".env"
    env_example = PROJECT_ROOT / ".env.example"

    if not env_file.exists():
        if env_example.exists():
            print("⚠️  未找到 .env 文件")
            print(f"\n请复制 {env_example} 为 .env 并填写您的配置:")
            print(f"  1. 复制: copy {env_example} .env")
            print("  2. 编辑 .env 文件，填写 DOUBAO_API_KEY 等配置")
            return False
        else:
            print("❌ 未找到 .env.example 文件")
            return False

    return True


def create_directories():
    """创建必要的目录"""
    dirs = ["data", "logs", "frontend/static"]

    for dir_path in dirs:
        full_path = PROJECT_ROOT / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ 目录已创建: {full_path}")


def main():
    """主函数"""
    print("=" * 60)
    print("Daily Paper Assistant - 启动中")
    print("=" * 60)

    # 检查依赖
    print("\n📦 检查依赖包...")
    if not check_requirements():
        sys.exit(1)
    print("✅ 依赖包检查通过")

    # 检查环境变量
    print("\n🔑 检查环境变量配置...")
    if not check_env_file():
        sys.exit(1)
    print("✅ 环境变量配置检查通过")

    # 创建目录
    print("\n📁 创建必要目录...")
    create_directories()

    # 启动应用
    print("\n🚀 启动应用...")
    print("=" * 60)

    os.chdir(PROJECT_ROOT / "backend")

    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn",
            "main:app",
            "--host", "127.0.0.1",
            "--port", "8000",
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n\n👋 应用已停止")
        sys.exit(0)


if __name__ == "__main__":
    main()
