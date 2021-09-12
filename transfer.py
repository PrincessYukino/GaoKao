import os
import time
import pydocx

for root, dirs, files in os.walk("./1错题"):  # 获取当前文件夹的信息
    for file in files:  # 扫描所有文件
        if os.path.splitext(file)[1] == ".docx" and "~" not in str(
            file) and "$" not in str(file):
            md = pydocx.PyDocX.to_html(f"{root}/{file}")
            path = f"./1错题/track/{os.path.splitext(file)[0]}.html"
            with open(path,"w",encoding="utf-8") as f:
                f.write(md)