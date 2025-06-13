# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 14:17:48 2025

@author: lenovo
"""

import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import os

class CleanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("问卷数据清洗工具 (简洁版)")
        self.root.geometry("600x400")
        
        self.df = None

        # --- UI 布局 ---
        main_frame = ttk.Frame(root, padding="15")
        main_frame.pack(fill="both", expand=True)

        # 1. 文件选择
        file_btn = ttk.Button(main_frame, text="1. 选择Excel文件", command=self.select_file)
        file_btn.pack(fill="x", pady=5)
        self.file_label = ttk.Label(main_frame, text="尚未选择文件", foreground="blue")
        self.file_label.pack()

        # 2. 列选择
        cols_frame = ttk.Frame(main_frame)
        cols_frame.pack(fill="x", pady=15)
        
        ttk.Label(cols_frame, text="起始题目:").pack(side="left", padx=5)
        self.start_combo = ttk.Combobox(cols_frame, state="disabled")
        self.start_combo.pack(side="left", expand=True, fill="x")
        
        ttk.Label(cols_frame, text="结束题目:").pack(side="left", padx=10)
        self.end_combo = ttk.Combobox(cols_frame, state="disabled")
        self.end_combo.pack(side="left", expand=True, fill="x")

        # 3. 运行按钮
        run_btn = ttk.Button(main_frame, text="2. 开始处理", command=self.run_analysis)
        run_btn.pack(fill="x", pady=5)
        
        # 4. 结果显示区域
        self.result_text = tk.Text(main_frame, height=10, wrap=tk.WORD, relief="solid", borderwidth=1)
        self.result_text.pack(fill="both", expand=True, pady=10)
        self.update_result("欢迎！请先选择一个Excel文件。")

    def update_result(self, message):
        """清空并更新结果区域的文本"""
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", message)

    def select_file(self):
        """选择文件并加载列名到下拉框"""
        path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if not path:
            return

        try:
            self.df = pd.read_excel(path)
            self.file_path = path
            self.file_label.config(text=os.path.basename(path))

            # 填充下拉框
            columns = list(self.df.columns)
            self.start_combo.config(values=columns, state="readonly")
            self.end_combo.config(values=columns, state="readonly")
            self.start_combo.set(columns[0])
            self.end_combo.set(columns[-1])
            
            self.update_result("文件加载成功。\n请确认题目范围，然后点击“开始处理”。")
        except Exception:
            self.update_result("错误：无法读取此文件。\n请确认它是一个有效的Excel文件。")

    def run_analysis(self):
        """执行核心的筛选逻辑并显示最终报告"""
        if self.df is None:
            self.update_result("错误：请先选择一个有效的Excel文件。")
            return

        start_col = self.start_combo.get()
        end_col = self.end_combo.get()

        try:
            # 获取题目列
            start_idx = self.df.columns.get_loc(start_col)
            end_idx = self.df.columns.get_loc(end_col)
            question_cols = self.df.columns[start_idx : end_idx + 1]

            # 核心逻辑
            is_straight_liner = self.df[question_cols].nunique(axis=1) == 1
            cleaned_df = self.df[~is_straight_liner]
            
            # 生成报告
            report = f"""--- 处理完成 ---

原始样本数量:    {len(self.df)}
剔除的样本数量:  {len(self.df) - len(cleaned_df)}
清洗后的样本数量:  {len(cleaned_df)}
"""
            # 保存文件
            base, ext = os.path.splitext(self.file_path)
            output_path = f"{base}_cleaned{ext}"
            cleaned_df.to_excel(output_path, index=False)
            
            report += f"\n清洗后的数据已保存至:\n{output_path}"
            self.update_result(report)

        except Exception:
            self.update_result("处理失败！\n请检查您选择的起始和结束列是否正确。")


# --- 启动程序 ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CleanApp(root)
    root.mainloop()