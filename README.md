# hello-world

## 部署指南

### 准备条件

- 命令行界面（macOS/Linux 的 Terminal，Windows 的 Command Prompt）
- 用于下载 Python、Makefile 和依赖项的网络连接

### 逐步指导

#### 1. 安装 Python

- **macOSx**: 使用 Homebrew
  ```bash
  brew install python3  # macOS
  ```

#### 2. 安装 Make

- **macOS**: Make 通常已预装。如果没有，使用 Homebrew。
  ```bash
  brew install make
  ```

#### 使用 makefile 自动运行应用程序

- 使用 Makefile 启动 `app.py`。
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  make run
  ```

#### 手动运行应用程序

##### 1. 设置虚拟环境

- 导航到项目的根目录。
  ```bash
  cd path/to/hello_world
  ```
- 创建并激活虚拟环境。
  ```bash
  python -m venv .venv  # macOS
  source .venv/bin/activate  # macOS
  ```
##### 2. 安装依赖项

- 确保项目目录中存在 `requirements.txt` 文件。
- 安装所需的包。
  ```bash
  pip install -r requirements.txt
  ```

##### 3. 启动服务器
```bash
python app.py
```

### 补充说明

- 在进行项目工作时，始终激活虚拟环境。
- 如果遇到依赖问题，请检查 `requirements.txt` 中的具体包版本。
- 查看项目的 README 文件，了解任何特定的设置指令或额外的命令。

### 故障排除

如果在设置或执行过程中遇到问题，请查阅项目的 README 或在 GitHub 仓库创建一个问题寻求帮助。

