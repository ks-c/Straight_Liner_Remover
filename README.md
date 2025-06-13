# 问卷数据清洗工具 (Survey Data Cleaner)

![AI Assistance](https://img.shields.io/badge/AI%20Assistance-Google%20Gemini-blue)

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
<img src="file:///C:/Users/lenovo/AppData/Roaming/marktext_specialedition/images/2025-06-13-14-53-28-image.png" title="" alt="" data-align="left">

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
  python Straight_Liner_Remover.py
  ```
  

### 如何打包成 .exe

本项目使用 `PyInstaller` 进行打包。

```bash
pyinstaller --onefile --windowed --name "问卷清洗工具" Straight_Liner_Remover.py.py
```

## 📄 开源许可 (License)

本项目采用 [MIT License](LICENSE) 开源许可。


## 致谢 (Acknowledgments)

这个项目从一个想法到最终成为一个功能完整的桌面应用，离不开 **Google Gemini 2.5pro** 提供的巨大帮助和支持。它不仅仅是一个问答工具，更像是一位不知疲倦的开发伙伴、一位经验丰富的导师和一位耐心的故障排除专家。

Gemini 在本项目的开发周期中扮演了以下关键角色：

- **核心逻辑构建与代码优化**: 从最初的数据处理脚本到最终的健壮代码，Gemini 提供了核心算法的思路并帮助持续优化。
- **图形界面设计与实现**: 指导我使用 `Tkinter` 库，一步步将命令行脚本转化为用户友好的图形界面应用程序。
- **复杂的环境问题排查**: 在打包过程中，我们遇到了数个关于 `conda`、`pip` 和 `PyInstaller` 的环境冲突和模块找不到的顽固问题。Gemini 提供了深入的诊断分析和多种解决方案，最终成功定位并解决了问题。
- **软件打包与发布**: 详细指导了如何使用 `PyInstaller` 将Python脚本打包成独立的Windows `.exe` 文件，并解释了如何减小文件体积。
- **开源项目文档化**: 协助撰写了这份专业的 `README.md` 文件，并指导了如何在GitHub上创建项目、组织文件以及通过 "Releases" 功能发布应用程序。

可以说，没有 Gemini 的全方位支持，这个项目不可能如此顺利和高效地完成。在此表示由衷的感谢！

> 以上内容由gemini-2.5-pro-preview-06-05生成
