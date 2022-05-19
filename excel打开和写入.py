# 导入xlwings库并重命名为xw
import xlwings as xw

# 创建app,开启实时进度可视化，关闭自动添加工作簿
app = xw.App(visible=True, add_book=False)

# 打开一个excel工作簿
wb = app.books.open(r"C:\Users\chenxia\Desktop\My_Excel.xlsx")

# 读取一张sheet
sht = wb.sheets["sheet-x"]

# 向sheet的指定范围添加数据
# 向指定单元格添加数据
sht.range("a2").value = "混世魔王二代"
# 添加一行数据
sht.range("a3").value = ["小明","小红","小亮"]
# 下面写法和上面是等效的
sht.range("a4:c4").value = [111,222,333]
# 添加一列数据
sht.range("a5").options(transpose=True).value = ["Tom","Jerry","David"]
# 添加行列数据
sht.range("a8").value = [[5,6,7,8],[55,66,77,88]]
# 保存工作簿
wb.save()

# 关闭工作簿
wb.close()

# 关闭app
app.quit()








