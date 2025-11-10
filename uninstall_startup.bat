@echo off
chcp 65001 > nul
echo ================================
echo Daily Paper Assistant
echo Windows 开机自启动卸载脚本
echo ================================
echo.
echo 此脚本将从 Windows 任务计划程序中删除开机自启动任务
echo.

pause

set TASK_NAME=DailyPaperAssistant

echo.
echo 正在删除任务计划...
echo.

schtasks /Delete /TN "%TASK_NAME%" /F

if %errorlevel% equ 0 (
    echo.
    echo ✅ 开机自启动任务已成功删除！
    echo.
) else (
    echo.
    echo ❌ 任务删除失败！
    echo 可能原因：
    echo   1. 任务不存在
    echo   2. 权限不足（请以管理员身份运行）
    echo.
)

pause
