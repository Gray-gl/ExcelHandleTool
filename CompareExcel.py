import pandas as pd
from pandas import DataFrame

'''
    description:list all the columns of the excel
    parameter:path is the path of the excel
    return:the list which contains all the columns of the excel
    attention:the return is Dataframe ,you can not directly handle it
'''
def ListExcel(path):
    target = pd.read_excel(path)
    return target

'''
    description:return the list containing all the elements in the column of the sheet data
    parameter:data is the Dataframe of the sheet
              column is the name of the column you want in the sheet
    return:the list contains all the element in the sheet you want
    attention:the elements in the list may be duplicate
'''
def getList(data,column):
    name = list()
    for i in data[column]:
        name.append(i)
    return name


'''
    description:save all the changes you did to the sheet
    parameter:
        data is dataframe you have chagned
        target is the path you want to save the excel
    return:none return
    attention:the sheet is default one
'''
def saveExcel(data,target):
    DataFrame(data).to_excel(target, sheet_name='Sheet1',
                               index=False, header=True)


baseA = ListExcel('baseData.xls')
#print(baseA)
compare = ListExcel('compare1.xls')
nameA = getList(baseA,'姓名')
print(nameA)
nameB = getList(compare,'姓名')
print(nameB)

result = list()
for i in nameA:
    if i not in nameB:
        result.append(i)

for i in result:
    print('@'+i)

# 打开需要的填写的文件excel文件
target = pd.read_excel('.//a.xls')

