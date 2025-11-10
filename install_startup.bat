@echo off
chcp 65001 > nul
echo ================================
echo Daily Paper Assistant
echo Windows 开机自启动安装脚本
echo ================================
echo.
echo 此脚本将在 Windows 任务计划程序中创建开机自启动任务
echo.

pause

cd /d "%~dp0"

set TASK_NAME=DailyPaperAssistant
set PYTHON_SCRIPT=%cd%\run.py
set PYTHON_EXE=python

echo.
echo 正在创建任务计划...
echo 任务名称: %TASK_NAME%
echo Python 脚本: %PYTHON_SCRIPT%
echo.

schtasks /Create /TN "%TASK_NAME%" /TR "\"%PYTHON_EXE%\" \"%PYTHON_SCRIPT%\"" /SC ONLOGON /RL HIGHEST /F

if %errorlevel% equ 0 (
    echo.
    echo ✅ 开机自启动任务创建成功！
    echo.
    echo 说明：
    echo   - 任务名称: %TASK_NAME%
    echo   - 触发时机: 用户登录时自动运行
    echo   - 您可以在"任务计划程序"中查看和管理此任务
    echo.
    echo 如需删除自启动，请运行: uninstall_startup.bat
    echo 或在任务计划程序中手动删除"%TASK_NAME%"任务
    echo.
) else (
    echo.
    echo ❌ 任务创建失败！
    echo 请尝试以管理员身份运行此脚本
    echo.
)

pause
