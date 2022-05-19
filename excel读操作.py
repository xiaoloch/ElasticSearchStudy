# 导入xlwings库并重命名为xw
import xlwings as xw

# 创建app,开启实时进度可视化，关闭自动添加工作簿
app = xw.App(visible=True, add_book=False)

# 打开一个excel工作簿
wb = app.books.open(r"C:\Users\chenxia\Desktop\My_Excel.xlsx")

# 读取一张sheet
sht = wb.sheets["sheet-x"]

# 读取某个单元格的数据
print(sht.range("a2").value)
# 读取一行
print(sht.range("a4:c4").value)
# 读取一列
print(sht.range("a5:a7").value)
# 读取一个范围
print(sht.range("a1:d9").value)

# 关闭工作簿
wb.close()
# 关闭app
app.quit()








