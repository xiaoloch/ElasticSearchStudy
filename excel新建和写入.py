# 导入xlwings库并重命名为xw
import xlwings as xw

# 创建app,开启实时进度可视化，关闭自动添加工作簿
app = xw.App(visible=True, add_book=False)

# 手动添加一个excel工作簿
wb = app.books.add()

# 手动添加一张sheet，创建工作簿的时候默认会自动创建一个sheet1，使用after参数控制新sheet添加在sheet1后面
sht = wb.sheets.add(name="sheet-x",after="sheet1")

# 向sheet的指定范围添加数据
sht.range("a2").value = "混世魔王"

# 保存工作簿，同时设置保存路径和密码，注意给文件取名一定要设置后缀（.xlsx），否则报错
wb.save(path = r"C:\Users\chenxia\Desktop\My_Excel2.xlsx",password="123")

# 关闭工作簿
wb.close()

# 关闭app
app.quit()







