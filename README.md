# 问卷数据清洗工具 (Survey Data Cleaner)

这是一个简洁高效的桌面应用程序，旨在帮助研究人员、学生或任何处理问卷数据的人员，快速识别并剔除无效的“直线型”作答样本。

“直线型”作答就是所有题目都选择同样答案。

本工具通过用户友好的图形界面（GUI）实现，无需任何编程知识即可轻松上手。

---

## ✨ 主要功能 (Key Features)

- **图形用户界面**: 操作直观，无需接触代码。
- **自动检测**: 智能识别在所有指定题目中选择了完全相同答案的问卷。
- **灵活选择**: 用户可以自由定义需要检测的题目范围（从起始题目到结束题目）。
- **安全导出**: 程序会生成一份新的、已清洗的Excel文件，不会修改您的原始数据。
- **无需安装**: 下载`.exe`文件后直接双击即可运行。

## 💻 软件截图 (Screenshot)

![](file:///C:/Users/lenovo/AppData/Roaming/marktext_specialedition/images/2025-06-13-14-53-28-image.png?msec=1749797938221)

## 🚀 如何使用 (For End-Users)

如果您只想使用本工具，请按照以下步骤操作：

1. 前往本项目的 [**Releases 页面**](https://github.com/ks-c/Straight_Liner_Remover/releases)。
2. 在最新的版本下，下载名为 `横向去重复.exe` 的文件。
3. 双击运行 `横向去重复.exe`。
4. **步骤 1:** 点击“选择Excel文件”按钮，加载您的问卷数据。
5. **步骤 2:** 在“起始题目”和“结束题目”的下拉菜单中，选择您要检测的题目范围。
6. **步骤 3:** 点击“开始处理”按钮。
7. 处理完成后，软件界面会显示结果报告。同时，在您原始文件的相同目录下，会生成一个以 `_cleaned.xlsx` 结尾的已清洗文件。

## 🔧 开发与贡献 (For Developers)

如果您想查看源代码、进行二次开发或为本项目做出贡献，请按以下步骤操作。

### 环境要求

- Python 3.8+
- pip

### 本地运行

1. **克隆仓库**
  
  ```bash
  git clone https://github.com/ks-c/Straight_Liner_Remover.git
  cd Straight_Liner_Remover
  ```
  
2. **创建并激活虚拟环境 (推荐)**
  
  ```bash
  # 创建虚拟环境
  python -m venv venv
  # 激活虚拟环境 (Windows)
  venv\Scripts\activate
  ```
  
3. **安装依赖库**
  
  ```bash
  pip install pandas openpyxl
  ```
  
4. **运行程序**
  
  ```bash
  python [Straight_Liner_Remover.py]
  ```
  

### 如何打包成 .exe

本项目使用 `PyInstaller` 进行打包。

```bash
pyinstaller --onefile --windowed --name "问卷清洗工具" [去重复.py]
```

## 📄 开源许可 (License)

本项目采用 [MIT License](LICENSE) 开源许可。
