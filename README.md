# Python_Program

> 一个以 Python 语法练习为主的个人学习仓库，同时收录了两个体量较大的独立项目：旁挂 HIS 的医生侧 Agent「HIS Copilot」与临床副驾 Agent Runtime「MidAgent」。

---

## 一、项目名称与简介

**Python_Program** 是个人代码归档仓库，内容大致分为三类：

1. **Python 基础与练习**：变量、字符串格式化、列表 / 字典 / 元组、切片、推导式、异常、正则、自定义模块与包，以及牛客网入门题目的练习脚本。
2. **图形 / 自动化小实验**：`pygame + PyOpenGL` 的计算机图形学实验、`turtle` 雪花动画、基于截图 + OCR + 模拟鼠标的自动答题脚本。
3. **两个完整的 Agent 项目**：`HIS Copilot`（Chrome 扩展 + Java/Vue 联调靶场 + 大量设计文档）与 `MidAgent`（FastAPI Agent 服务 + React 工位页 + 自检/评测工具链），两者都是"旁挂医院 HIS、零侵入集成"的医疗场景 Agent 设计。

除两个 Agent 项目外，其余目录基本都是单文件 `test.py` 的练习脚本，没有统一的构建体系。

---

## 二、技术栈

以下信息均来自仓库内的配置文件与源码，未做推测。

### 1. 练习脚本部分

| 类别 | 实际使用的内容 |
| --- | --- |
| 语言 | Python 3（纯脚本，无根级 `requirements.txt` / `pyproject.toml`） |
| 标准库 | `random`、`time`、`re`、`sys`、`os`、`math` |
| 图形 / 界面 | `turtle`（`test/`）、`pygame` + `PyOpenGL`（`experiment/`） |
| 图像 / OCR / 自动化 | `cv2`（opencv-python）、`numpy`、`pyautogui`、`pytesseract`、`keyboard`（`小猿口算/`） |
| 版本控制 | Git（根目录 `.gitignore` 为 GitHub 官方 Python 模板，并在末尾追加了 `MidAgent/` 例外） |

### 2. HIS Copilot

| 部分 | 技术栈 |
| --- | --- |
| 浏览器扩展 | Chrome Extension **Manifest V3**（`minimum_chrome_version: 111`），原生 JS + `htm/preact` UMD，Shadow DOM，`world:"MAIN"` 与 `ISOLATED` 双世界注入 |
| mock 后端 | Java 17、Spring Boot **3.2.0**、MyBatis-Plus **3.5.9**、JSqlParser **5.4.2**（Manticore 构建）、Knife4j **4.5.0**（OpenAPI3 jakarta 版）、jjwt **0.12.6**、Lombok；构建工具 **Maven** |
| mock 前端 | Vue **3.5**、Vite **5.4**、Element Plus **2.8**、Pinia **2.2**、vue-router **4.4**、axios |
| 数据库 | MySQL（`mysql-connector-j` 运行时依赖）；文档中记录为 MySQL 8.0.40 |

### 3. MidAgent

| 部分 | 技术栈 |
| --- | --- |
| Agent 服务 | Python + FastAPI **0.128.0**、uvicorn、pydantic **2.12**、pydantic-settings、sse-starlette、httpx |
| Agent 编排 | LangChain **1.4.0**、LangGraph **1.2.11**、langchain-openai、langchain-chroma |
| 存储 / 检索 | SQLAlchemy **2.0**、PyMySQL、aiosqlite、chromadb **1.5.9** |
| SQL 安全 | sqlglot **30.18.0**（AST 解析校验） |
| 数据 / 评测 / 导出 | Faker、pytest、pytest-asyncio、openpyxl |
| 报表工位页 | React **18**、Ant Design **5**、ECharts **5**、Vite **5**；包管理 **pnpm**（有 `pnpm-workspace.yaml` 与 `pnpm-lock.yaml`） |
| 医生侧前端 | Chrome 扩展（`apps/web/extension`）+ 单文件悬浮球（`apps/web/demo_his/midagent-ball.js`） |
| mock 服务 | `services/his-mock`：Spring Boot 3 / Java 21（见其 README）；数据库 MySQL 8 |

---

## 三、目录结构

```
Python_Program/
├─ Python-3days/            # Python 基础语法练习（变量/字符串/列表/字典/元组/切片/自定义模块与包）
│  ├─ Practice/            # 综合小练习：九九乘法表、猜数字、股价计算、序列切片等
│  ├─ 自定义包/            # test_package 包与 __all__ 用法
│  └─ 自定义模块/          # 自定义模块导入
├─ Python-others/          # input()、print 参数、三元运算符、列表推导式、异常、正则表达式
├─ 牛客/                   # 牛客网「Python 入门语法」题目练习
├─ experiment/             # 计算机图形学实验（pygame + PyOpenGL，1/2/3/4 四组）
├─ test/                   # turtle 雪花飘落动画
├─ helloworld/             # 入门脚本
├─ 小猿口算/               # 截图 + OCR + 模拟鼠标的自动答题脚本
├─ HIS Copilot/            # 旁挂 HIS 的医生侧 Agent
│  ├─ extension-hiscopilot/  # MV3 悬浮球扩展（悬浮球 + 面板 + 报表 + 自检脚本）
│  ├─ his-mock/            # 联调靶场：Spring Boot 后端 + Vue 前端
│  ├─ docs/                # 架构、业务流程、技术选型、面试问答
│  ├─ specs/               # copilot-server 规格集 S00–S10
│  └─ document/            # 真实 HIS 系统识图结果与需求说明（只读参考）
└─ MidAgent/               # 独立 Git 仓库：临床副驾 Agent Runtime
   ├─ apps/                # agent（FastAPI）、web（报表工位页 / 扩展 / Demo HIS）
   ├─ config/              # 规则 YAML、指标口径、药品参考数据
   ├─ services/            # his-mock 只读 HTTP 封装
   ├─ tools/               # 数据工厂、评测、自检脚本
   ├─ sql/ eval/ contracts/ # 建表脚本、评测集与报告、接口契约
   └─ requirements.txt     # MidAgent 的 Python 依赖清单
```

---

## 四、主要功能 / 模块说明

### 1. 基础练习（`Python-3days/`、`Python-others/`、`牛客/`）

| 目录 | 内容 |
| --- | --- |
| `Python-3days/` | 变量输出、数据类型、字符串三种定义与格式化、复合赋值运算符、不定长参数、`list` 常用操作、自定义模块与自定义包 |
| `Python-3days/Practice/` | dict / list / tuple 综合练习、九九乘法表、猜数字、股价计算、字符串方法、序列切片 |
| `Python-others/` | `input()` 用法、`print()` 的 `sep`/`end` 参数、三元运算符、列表推导式、`try/except` 异常、`re` 正则匹配 |
| `牛客/Practice/python入门语法/` | 十六进制转换、`join()` 密码游戏、列表推导式嵌套三元运算符、生成数字列表、`for...else` 禁止重复注册、绩点学分、`dict.get(x, y)` 菜品价格等题目 |

### 2. 图形与自动化小工具

| 目录 | 说明 |
| --- | --- |
| `experiment/1/` | pygame + OpenGL 基础图形绘制（矩形 / 直线 / 三角形，按键切换背景色） |
| `experiment/2/` | GLUT 交互绘制：圆、多边形、粗圆、鼠标拖拽画线，含平移 / 缩放等变换 |
| `experiment/3/` | `test1.py`：2D 太阳系（太阳自转、地球公转自转、月球公转）；`test2.py`：Cohen–Sutherland 线段裁剪算法演示 |
| `experiment/4/` | 3D 基础物体（立方体 / 茶壶 / 圆环）、3D 机器人行走、WASD 交互式 3D 漫游，可切换正交/透视投影 |
| `test/test.py` | `turtle` 绘制的雪花飘落动画（雪花类 + 随机风偏移） |
| `小猿口算/test.py` | 截取屏幕左右两个区域 → OpenCV 预处理 + pytesseract OCR 识别数字 → 用 pyautogui 自动画出 ">" / "<" 符号；连续识别失败时按固定坐标点击"继续"重开 |
| `helloworld/helloworld.py` | 单行 `print("Hello World!")` |

### 3. HIS Copilot

产品形态：悬浮球旁挂在 HIS 页面之上，点击展开面板，按科室能力展示功能；有后台管理端。

| 模块 | 说明 |
| --- | --- |
| `extension-hiscopilot/` | MV3 扩展骨架：右下角悬浮球 + 420×640 面板、身份/上下文展示、能力卡片与空态、流式对话（含桩适配器）、自定义报表（字段勾选 → 查询 → 表格 → 新标签页预览 → CSV 导出）、三级降级读取（`window.HISBridge` → DOM `data-*`）、自检脚本（`check-manifest.mjs` / `check-store.mjs` / `check-report.mjs` / `verify.mjs`） |
| `his-mock/his-mock-server/` | Spring Boot mock 后端：JWT 登录与科室能力、基础数据（科室/医生/药品字典）、患者与过敏史、挂号/接诊、门诊病历与诊断、处方、账单，以及 `BridgeController` 提供的上下文读取接口；按包划分 `auth/base/patient/record/prescription/bill/bridge/common/config` |
| `his-mock/his-mock-web/` | Vue 3 mock 前端：登录页、接诊列表、门诊首页、门诊病历、西医处方、患者账单（`src/views/clinic/`），带 `src/bridge/` 用于向页面注入 `window.HISBridge` 与 locator |
| `docs/` | 架构设计、业务流程、技术选型与实现方案、C1–C4 功能流程设计、NL2SQL 口径、面试问答材料 |
| `specs/copilot-server/` | S00 规格总览 ~ S10 任务分解，覆盖 C1 NL2SQL、C2 病历质控、C3 用药安全、LLM 封装、知识库检索、可观测与评测 |

四大能力（见 `HIS Copilot/需求功能描述.md` 与 `docs/README.md`）：**C1 自定义报表（NL2SQL）**、**C2 病历质控**、**C3 用药安全核对**、**C4 管理端与入口**。

### 4. MidAgent

设计原则：**确定性代码负责判定，大模型只负责解释与措辞**；Agent 侧不直连数据库，唯一数据出口是 `HISClient` 的 HTTP 调用。

| 模块 | 说明 |
| --- | --- |
| `apps/agent/api/` | FastAPI 接入层，按角色解析数据范围，错误透出 traceId |
| `apps/agent/his/` | `HISClient` 与报表执行器（唯一数据出口） |
| `apps/agent/nl2sql/` | 语义层、`ReportSpec` 契约、SQL 校验链（sqlglot）、xlsx 导出 |
| `apps/agent/skills/rules/` | 三功能共享的 Finding 契约、YAML 规则装载、detector 注册 |
| `apps/agent/skills/clinical/` | 患者全景摘要 + 病历质控 |
| `apps/agent/skills/medication/` | 用药安全核对 + 药品知识库 |
| `apps/web/report_console/` | 报表工位页（React + AntD + ECharts） |
| `apps/web/extension/`、`apps/web/demo_his/` | 医生侧 Chrome 扩展与自带 Demo HIS 页面（含单文件悬浮球） |
| `config/` | `rules/`（质控与用药规则 YAML）、`semantic/metrics/`（指标口径）、`reference/`（药品字典、剂量范围、相互作用、诊断-计费对照） |
| `tools/` | 数据工厂、评测（`eval_runner.py` / `eval_ablation.py`）、二十余个 `verify_*` 自检脚本 |
| `sql/`、`eval/`、`contracts/` | 建表与索引对照脚本、评测集与报告、冻结的接口契约 |

四个功能：患者全景摘要、病历质控自查、用药安全核对、自定义报表查询（`ReportSpec` → 语义层编译 → SQL 校验链 → xlsx 导出）。

---

## 五、运行 / 构建方式

> 本仓库没有统一的根级构建入口，各目录需单独运行。以下命令来自各子项目的配置文件与 README。

### 1. Python 练习脚本

在对应目录下直接运行，例如：

```bash
cd Python-3days/数据类型
python test.py
```

无根级 `requirements.txt`；只有 `MidAgent/requirements.txt` 存在。运行图形 / 自动化脚本前需自行安装对应第三方库：

```bash
pip install pygame PyOpenGL
pip install opencv-python numpy pyautogui pytesseract keyboard
```

`小猿口算/test.py` 中硬编码了 Tesseract 路径 `D:\Tesseract-OCR\tesseract.exe`，换机器需先修改该常量。

### 2. HIS Copilot

```powershell
# mock 后端（端口 8080）
cd "HIS Copilot\his-mock\his-mock-server"
mvn spring-boot:run
# 健康检查：http://localhost:8080/actuator/health
# 接口文档：http://localhost:8080/doc.html

# mock 前端（scripts: dev / build / preview）
cd "HIS Copilot\his-mock\his-mock-web"
npm install
npm run dev
```

浏览器扩展：打开 `chrome://extensions` → 开启开发者模式 → 「加载已解压的扩展程序」→ 选择 `HIS Copilot/extension-hiscopilot`。改动扩展代码后需重新加载扩展并刷新 HIS 页面（content script 不热更新）。

### 3. MidAgent

```bash
cd MidAgent

python -m pip install -r requirements.txt
bash scripts/init_his_db.sh --yes                                    # 建库（一次）
python -m tools.data_factory.factory --scale 0.05 --round all        # 灌数
bash scripts/his_mock.sh start                                       # 启动 his-mock（Java）
python -m uvicorn apps.agent.api:app --port 8000                     # 启动 Agent 服务

cd apps/web/report_console && pnpm install && pnpm run dev           # 报表工位页
```

医生侧演示：打开 `http://localhost:8000/demo-his/`（悬浮球由页面自身引入）；或手工加载 `apps/web/extension`（Chrome ≥137 已移除 `--load-extension`）。自检入口：`python -m tools.startup`、`python -m tools.run_all_checks`。

---

## 六、备注

- **性质**：这是一个**个人学习 / 练习仓库**，多数目录是单文件 `test.py`，代码风格与注释以学习记录为主，不追求工程化。
- **课程作业痕迹**：`experiment/` 下的图形学实验脚本带学号姓名标注（如 `pygame.display.set_caption("20231797王旭东")`），应为课程实验作业，非通用工具。
- **两个子项目并非普通练习**：`HIS Copilot` 与 `MidAgent` 体量大、文档齐全（架构文档、规格集、评测报告、面试问答），且都包含针对求职准备的简历与面试材料，带有明显的作品集 / 求职准备属性。
- **仓库边界**：
  - `MidAgent/` 自带独立 `.git`，已被根目录 `.gitignore` 显式忽略（第 164 行 `MidAgent/`），属于**独立仓库**而非本仓库的一部分；
  - `HIS Copilot/`、`experiment/`、`test/`、`Python-others/正则表达式/` 在当前工作区处于**未跟踪（untracked）** 状态，尚未提交到本仓库。
- **他人代码 / 外部资源**：
  - `HIS Copilot/extension-hiscopilot/vendor/htm-preact.standalone.umd.js` 为第三方 UMD 构建产物；
  - `HIS Copilot/his-mock/his-mock-web/node_modules`、`target`、`dist`、`__pycache__`、`*.pyc` 等为构建 / 缓存产物，按 `.gitignore` 规则不应入库；
  - `HIS Copilot/document/` 记录的是对真实 HIS 系统的识图结果与需求说明，属只读参考资料。
- **敏感信息提示**：`HIS Copilot/his-mock/README.md`、`MidAgent/.env*` 等文件中写有本机数据库账号 / 密码与环境变量示例；`MidAgent/.gitignore` 已忽略 `.env`，如需公开仓库请自行核查并清理凭据。
- **未验证事项**：仓库内没有 CI 配置，也没有统一的测试入口；`MidAgent` 的评测数字与通过率来自其自身 README 与 `eval/reports`，本 README 未重新运行验证。
