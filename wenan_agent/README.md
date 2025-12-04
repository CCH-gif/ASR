# 🔥 AI 爆款文案生成器

基于 **LangChain** 和 **通义千问（Qwen）** 的智能文案生成工具，支持多种社交媒体平台风格，一键生成高质量营销文案。

---

## ✨ 功能特点

- 🎨 **多风格支持**：小红书种草风、抖音口播风、朋友圈营销风
- 🚀 **快速生成**：输入关键词，秒级生成专业文案
- 🎯 **精准定位**：针对不同平台特点优化文案结构
- 💡 **智能提示**：内置多种 Prompt 模板，确保输出质量
- 🌐 **Web 界面**：友好的 Streamlit 界面，操作简单
- 💻 **命令行版本**：支持脚本调用，方便集成

---

## 📋 项目结构

```
wenan_agent/
├── app.py          # Streamlit Web 界面版本（推荐）
├── main.py         # 命令行版本
└── README.md       # 项目说明文档
```

---

## 🚀 快速开始

### 1. 环境要求

- Python 3.8 - 3.12（推荐 3.10 或 3.11）
- 阿里云 DashScope API Key（用于调用通义千问）

### 2. 安装依赖

```powershell
# 创建虚拟环境（推荐）
python -m venv .venv
.\.venv\Scripts\activate

# 安装依赖
pip install streamlit langchain langchain-community
```

### 3. 配置 API Key

**方式一：在 Web 界面中配置（推荐）**

运行 `app.py` 后，在左侧侧边栏直接输入 API Key，无需修改代码。

**方式二：环境变量配置**

```powershell
# Windows PowerShell
setx DASHSCOPE_API_KEY "你的_DASHSCOPE_API_KEY"

# 或在代码中直接配置（见 main.py 第 7 行）
```

**获取 API Key：**
1. 访问 [阿里云 DashScope 控制台](https://dashscope.console.aliyun.com/)
2. 注册/登录账号
3. 创建 API Key

---

## 🎮 使用方法

### 方式一：Web 界面（推荐）

```powershell
streamlit run app.py
```

浏览器会自动打开 `http://localhost:8501`，界面包含：

- **左侧侧边栏**：
  - API Key 输入框
  - 模型选择（qwen-plus / qwen-max / qwen-turbo）
  
- **主界面**：
  - 关键词输入框
  - 文案风格选择
  - 生成按钮
  - 结果展示区

**使用步骤：**
1. 在侧边栏输入 DashScope API Key
2. 选择模型（qwen-plus 性价比高，qwen-max 效果最好）
3. 输入产品或主题关键词（如：平价洗面奶、杭州旅游攻略）
4. 选择文案风格
5. 点击"开始生成 ✨"

### 方式二：命令行版本

```powershell
python main.py
```

按提示输入关键词，程序会自动生成小红书风格的爆款文案。

**示例：**
```
请输入文案关键词（例如：防晒霜、职场穿搭、减肥食谱）：平价洗面奶

正在生成爆款文案...

--------------------------------------
【生成的文案内容】
--------------------------------------
```

---

## 📝 支持的文案风格

### 1. 小红书种草风

**特点：**
- 标题带 Emoji，使用"震惊体"或"干货体"
- 正文多用 Emoji，口语化，像闺蜜聊天
- 包含痛点+解决方案
- 文末加 Tags

**适用场景：** 产品种草、旅游攻略、美妆分享、穿搭推荐

### 2. 抖音口播风

**特点：**
- 开头前 3 秒必须有黄金钩子（引起好奇）
- 句式短促有力，适合快节奏朗读
- 结尾有明确的引导点赞关注话术

**适用场景：** 短视频脚本、口播内容、知识分享

### 3. 朋友圈营销风

**特点：**
- 亲切自然，不要太硬广
- 突出限时福利或核心价值
- 引导私聊或评论

**适用场景：** 私域营销、朋友圈推广、社群运营

---

## 🛠️ 技术栈

- **前端框架**：Streamlit
- **LLM 框架**：LangChain
- **大语言模型**：通义千问（Qwen）
- **核心组件**：
  - `ChatTongyi`：LangChain 的通义千问集成
  - `ChatPromptTemplate`：Prompt 模板管理
  - `StrOutputParser`：输出解析器

---

## 📊 模型选择建议

| 模型 | 特点 | 适用场景 |
|------|------|----------|
| **qwen-turbo** | 速度快，成本低 | 快速生成，批量处理 |
| **qwen-plus** | 平衡性能与成本 | 日常使用（推荐） |
| **qwen-max** | 效果最好，质量高 | 重要内容，追求极致效果 |

---

## 💡 使用技巧

1. **关键词要具体**：越具体的关键词，生成的文案越精准
   - ❌ 不好：洗面奶
   - ✅ 好：平价氨基酸洗面奶、敏感肌专用洗面奶

2. **多次生成**：同一关键词可以多次生成，选择最满意的版本

3. **结合场景**：根据实际使用场景选择合适的风格

4. **二次编辑**：生成的文案可以作为初稿，根据实际情况进行调整

---

## ⚠️ 常见问题

### 1. 提示 "No module named 'langchain_community'"

**解决方案：**
```powershell
pip install langchain-community
```

### 2. API Key 错误

**检查项：**
- API Key 是否正确（注意不要有多余空格）
- 是否在 DashScope 控制台开通了对应服务
- 账户余额是否充足

### 3. 生成速度慢

**优化建议：**
- 使用 `qwen-turbo` 模型（速度最快）
- 检查网络连接
- 避免在高峰期使用

### 4. 生成内容不符合预期

**改进方法：**
- 尝试更具体的关键词
- 更换模型（如从 qwen-plus 升级到 qwen-max）
- 在 Prompt 中添加更多约束条件（修改 `get_prompt_template` 函数）

---

## 🔧 自定义开发

### 添加新的文案风格

在 `app.py` 的 `get_prompt_template` 函数中添加新的风格：

```python
def get_prompt_template(style):
    if style == "小红书种草风":
        return """..."""
    elif style == "你的新风格":
        return """
        你的 Prompt 模板
        """
    # ...
```

然后在 `style_option` 的 `selectbox` 中添加选项。

### 修改 Prompt 模板

直接编辑 `get_prompt_template` 函数中的模板字符串，调整生成规则。

---

## 📄 许可证

本项目仅供学习和个人使用。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📧 反馈

如有问题或建议，欢迎通过 Issue 反馈。

