import json

with open ('es_json_out.json') as es_file:
    file_str = es_file.read()
    file_dict = json.loads(file_str)


value = file_dict["hits"]["total"]["value"]

print(value)

for i in range(0,value):
    try:
        print(file_dict["hits"]["hits"][i]["_source"]["@result"])
    except Exception as result:
        print(result)
    # print(file_dict["hits"]["hits"][i]["_source"]["@enterpriseId"])

