# Daily Paper Assistant - AI 论文每日精读助手

一个自动化的 AI 论文精读工具，每天自动从 HuggingFace Daily Papers 获取最新论文，利用大语言模型进行初筛和深度解读。

## ✨ 核心功能

- 🤖 **自动获取**：每天定时从 HuggingFace 获取最新 AI 论文
- 🔍 **智能初筛**：用 LLM 为每篇论文生成 2 句话简介
- 📚 **人工选择**：浏览所有论文简介，选择感兴趣的论文
- 📖 **深度精读**：用 LLM 生成详细的论文解读报告
- 🖥️ **图形界面**：美观的 Web 界面，操作简单
- ⏰ **定时任务**：支持开机自启和每日定时运行

## 📋 系统要求

- **操作系统**：Windows 10/11
- **Python**：3.9 或更高版本
- **浏览器**：Chrome、Edge、Firefox 等现代浏览器
- **网络**：可访问 HuggingFace 和豆包 API

## 🚀 快速开始

### 1. 安装 Python 依赖

打开命令行，进入项目目录，运行：

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env`：

```bash
copy .env.example .env
```

编辑 `.env` 文件，填写您的配置：

```ini
# 豆包 API 配置（必填）
DOUBAO_API_KEY=your_doubao_api_key_here
DOUBAO_BASE_URL=https://ark.cn-beijing.volces.com/api/v3

# 豆包模型 ID
DOUBAO_CHEAP_MODEL=ep-20241110162735-pdq2w    # 用于初筛的模型
DOUBAO_PREMIUM_MODEL=ep-20241110162735-pdq2w  # 用于精读的模型

# 定时任务配置
SCHEDULE_TIME=11:00          # 每天检查时间（24小时制）
CHECK_ON_STARTUP=true        # 开机时是否检查

# 其他配置（可选）
HOST=127.0.0.1
PORT=8000
```

#### 获取豆包 API Key 的步骤：

1. 访问 [豆包 AI 控制台](https://console.volcengine.com/ark)
2. 注册/登录账号
3. 创建 API Key
4. 复制 API Key 到 `.env` 文件

### 3. 启动应用

#### 方式一：双击运行（推荐）

直接双击 `run.bat` 文件即可启动应用。

#### 方式二：命令行运行

```bash
python run.py
```

### 4. 访问应用

启动后，浏览器会自动打开 http://127.0.0.1:8000

如果没有自动打开，请手动访问该地址。

## 📖 使用说明

### 基本流程

1. **自动获取论文**
   - 应用启动后会自动检查是否有新论文
   - 每天 11:00（可配置）自动运行一次
   - 也可以点击"手动获取最新论文"按钮立即获取

2. **浏览论文列表**
   - 查看所有论文的标题、作者、点赞数
   - 阅读 AI 生成的 2 句话简介
   - 可以按日期范围和排序方式筛选

3. **选择感兴趣的论文**
   - 勾选最多 6 篇感兴趣的论文
   - 选中的论文会高亮显示

4. **生成精读报告**
   - 点击"生成精读报告"按钮
   - AI 会并行生成 6 篇论文的深度解读
   - 浏览器会自动打开 6 个标签页，每个显示一篇论文的精读

5. **阅读精读报告**
   - 报告包含：研究背景、问题、核心洞察、方法、结论、关键术语
   - 可以点击链接查看原文或下载 PDF

### 高级功能

#### 设置开机自启动

如果希望电脑开机时自动启动应用，请：

1. 右键 `install_startup.bat`，选择"以管理员身份运行"
2. 按提示完成安装
3. 下次开机时应用会自动启动

卸载开机自启动：

1. 右键 `uninstall_startup.bat`，选择"以管理员身份运行"

#### 修改定时时间

编辑 `.env` 文件中的 `SCHEDULE_TIME`：

```ini
SCHEDULE_TIME=14:30  # 改为下午 2:30
```

#### 查看日志

日志文件保存在 `logs/` 目录下：

- `app_YYYY-MM-DD.log`：应用主日志
- `scheduler_YYYY-MM-DD.log`：定时任务日志

## 📁 项目结构

```
dailypaper/
├── backend/                    # 后端代码
│   ├── main.py                # FastAPI 主程序
│   ├── scheduler.py           # 定时任务调度器
│   ├── huggingface_api.py    # HuggingFace API 客户端
│   ├── llm_service.py        # 豆包 LLM 服务
│   ├── database.py           # SQLite 数据库操作
│   └── config.py             # 配置管理
├── frontend/                  # 前端代码
│   ├── index.html            # 论文列表页面
│   ├── report.html           # 精读报告模板
│   └── static/
│       ├── style.css         # 样式文件
│       └── script.js         # JavaScript 逻辑
├── data/                      # 数据目录
│   └── papers.db             # SQLite 数据库
├── logs/                      # 日志目录
├── .env                       # 环境变量配置（需自行创建）
├── .env.example              # 环境变量示例
├── requirements.txt          # Python 依赖
├── run.py                    # 启动脚本
├── run.bat                   # Windows 启动脚本
├── install_startup.bat       # 安装开机自启动
├── uninstall_startup.bat     # 卸载开机自启动
└── README.md                 # 说明文档
```

## 🔧 技术栈

- **后端**：FastAPI + Python 3.9+
- **前端**：原生 HTML/CSS/JavaScript
- **数据库**：SQLite
- **定时任务**：APScheduler
- **LLM**：豆包（字节跳动）
- **数据源**：HuggingFace Daily Papers API

## ⚙️ 配置说明

### 环境变量详解

| 变量名 | 说明 | 默认值 | 必填 |
|--------|------|--------|------|
| `DOUBAO_API_KEY` | 豆包 API Key | - | ✅ |
| `DOUBAO_BASE_URL` | 豆包 API 地址 | https://ark.cn-beijing.volces.com/api/v3 | ❌ |
| `DOUBAO_CHEAP_MODEL` | 初筛模型 ID | ep-20241110162735-pdq2w | ❌ |
| `DOUBAO_PREMIUM_MODEL` | 精读模型 ID | ep-20241110162735-pdq2w | ❌ |
| `HF_TOKEN` | HuggingFace Token | - | ❌ |
| `SCHEDULE_TIME` | 定时任务时间 | 11:00 | ❌ |
| `CHECK_ON_STARTUP` | 开机检查 | true | ❌ |
| `HOST` | 服务地址 | 127.0.0.1 | ❌ |
| `PORT` | 服务端口 | 8000 | ❌ |
| `MAX_PAPERS_PER_DAY` | 每天最多获取论文数 | 50 | ❌ |
| `SELECTED_PAPERS_COUNT` | 可选择论文数 | 6 | ❌ |

### 自定义 Prompt

如需自定义 LLM 的 prompt，请编辑 `backend/config.py` 文件中的：

- `INITIAL_SCREENING_PROMPT`：初筛 prompt
- `DEEP_READING_PROMPT`：精读 prompt

## 🐛 常见问题

### 1. 无法启动应用

**问题**：运行 `run.bat` 后提示找不到模块

**解决**：
```bash
# 确保已安装所有依赖
pip install -r requirements.txt
```

### 2. API 调用失败

**问题**：提示豆包 API 调用失败

**解决**：
- 检查 `.env` 文件中的 `DOUBAO_API_KEY` 是否正确
- 确认 API Key 有足够的额度
- 检查网络连接

### 3. 论文列表为空

**问题**：打开页面后没有论文显示

**解决**：
- 点击"手动获取最新论文"按钮
- 检查 HuggingFace 是否可访问
- 查看 `logs/` 目录下的日志文件

### 4. 周末没有论文

**说明**：HuggingFace Daily Papers 通常在工作日更新，周末可能没有新论文。应用会自动检查最近 2 天的论文。

### 5. 精读报告生成失败

**问题**：点击生成按钮后报错

**解决**：
- 检查豆包 API 额度
- 减少选择的论文数量
- 查看 `logs/` 目录下的错误日志

## 📝 更新日志

### v1.0.0 (2025-01-10)

- 🎉 首次发布
- ✅ 支持自动获取 HuggingFace 论文
- ✅ 支持 LLM 初筛和精读
- ✅ 支持 Web 图形界面
- ✅ 支持定时任务和开机自启
- ✅ 支持豆包 LLM

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

如有问题或建议，请通过以下方式联系：

- GitHub Issues
- Email: your-email@example.com

---

**Enjoy your daily AI paper reading! 📚✨**
