import json
import xlwings as xw
import time
import pandas

error_list = []


# 创建app,开启实时进度可视化，关闭自动添加工作簿
app = xw.App(visible=True, add_book=False)
# 手动添加一个excel工作簿,即打开一个excel
wb = app.books.add()
# 读取sheet1，准备接收原始数据
sht = wb.sheets["sheet1"]
sht.range("a1").value = ["enterpriseId", "enterpriseId", "result", "message"]
# 创建sheet2,准备接收统计数据
sht2 = wb.sheets.add(name="sheet-x",after="sheet1")


with open ('es_json_out.json') as es_file:
    file_str_ini = es_file.read()               # 将原始json字符串形式的elastic search输出结果读进来
    file_str = file_str_ini.replace('"""','')   # 纠正原始json字符串中的一个格式错误
    file_dict = json.loads(file_str)            # 把json字符串转换成字典


value = file_dict["hits"]["total"]["value"]     # 获取error message的数量
print(value)

"""
通过一个for循环针对每条错误信息提取它的result，correlationId，enterpriseId，message字段。
并且将每条错误信息的这四个字段写到excel中的一行。
并且将错误信息添加到error_list列表中。
"""
for i in range(0,value):
    try:
        result = file_dict["hits"]["hits"][i]["_source"]["@result"]
        correlationId = file_dict["hits"]["hits"][i]["_source"]["@correlationId"]
        enterpriseId = file_dict["hits"]["hits"][i]["_source"]["@enterpriseId"]
        message = file_dict["hits"]["hits"][i]["_source"]["context"]["response"]["body"]["message"]

    except Exception as result:
        print(result)

    j = i+2                                                             # 设置写入excel的哪一行
    sht.range(j,1).value = [result,correlationId,enterpriseId,message]  # 写入excel的一行
    error_list.append(message)                                          # 追加到error_list这个列表

"""
对excel中sheet1进行格式操作
"""
range = sht.range("a1:d1").expand('down')   # 选中要操作的范围
print(range.get_address())                  # 获取选中的范围的地址（只是看一下）
range.rows.autofit()                        # 设置行高自适应
range.columns.autofit()                     # 设置列宽自适应
range.api.HorizontalAlignment = -4131       # 设置单元格水平居左
range.api.VerticalAlignment = -4108         # 设置单元格上下居中

"""
统计错误信息，并写入excel中sheet-x
"""
summary = pandas.value_counts(error_list)
sht2.range("a1").value = summary

"""
excel保存退出
"""
clock = time.time()
wb.save(path = r"C:\Users\chenxia\Desktop\elastic_ana_%f.xlsx" %(clock))
wb.close()
app.quit()






