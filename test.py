import pandas
a = ['Backend service responded with http NotFound but the response data could not be processed', 'Unhandled exception: {"Code":500,"Description":"DMS returned 5xx","CorrelationId":"2add3b25e33945b19afb4305b7beabcd","Resource":null}', 'DMS is down for maintenance', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'DMS is down for maintenance', 'DMS is down for maintenance', 'Backend service responded with http NotFound but the response data could not be processed', 'DMS is down for maintenance', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'DMS is down for maintenance', 'Failed to write data into tables', 'Backend service responded with http NotFound but the response data could not be processed', 'Backend service responded with http NotFound but the response data could not be processed', 'Failed to write data into tables', 'Backend service responded with http NotFound but the response data could not be processed', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'DMS is down for maintenance', 'Backend service responded with http NotFound but the response data could not be processed', 'DMS is down for maintenance', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'DMS is down for maintenance', 'Failed to write data into tables', 'Unhandled exception: {"Code":500,"Description":"DMS returned 5xx","CorrelationId":"2add3b25e33945b19afb4305b7beabcd","Resource":null}', 'Unhandled exception: {"Code":500,"Description":"DMS returned 5xx","CorrelationId":"2add3b25e33945b19afb4305b7beabcd","Resource":null}', 'Unhandled exception: {"Code":500,"Description":"DMS returned 5xx","CorrelationId":"2add3b25e33945b19afb4305b7beabcd","Resource":null}', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Failed to write data into tables', 'Backend service responded with http NotFound but the response data could not be processed']

result = pandas.value_counts(a)

print(type(result))


# 导入xlwings库并重命名为xw
import xlwings as xw

# 创建app,开启实时进度可视化，关闭自动添加工作簿
app = xw.App(visible=True, add_book=False)

# 手动添加一个excel工作簿
wb = app.books.open(r"C:\Users\chenxia\Desktop\elastic_ana_1652945237.700255.xlsx")

# 手动添加一张sheet，创建工作簿的时候默认会自动创建一个sheet1，使用after参数控制新sheet添加在sheet1后面
sht = wb.sheets.add(name="sheet-x",after="sheet1")

# 向sheet的指定范围添加数据
sht.range("a1").value = result

# 保存工作簿，同时设置保存路径和密码，注意给文件取名一定要设置后缀（.xlsx），否则报错
wb.save()

# 关闭工作簿
wb.close()

# 关闭app
app.quit()







