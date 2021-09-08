'''
    描述：打开对应文件下的所有文件，获取文件路径名,并调用对应的修改函数进行修改
    参数：path文件路径
'''
def getFile(path):
    for parent,dirnames,filenames in os.walk(path):

        # filename是文件夹下的所有文件的名字
        for filename in filenames:
            filePath = path+"\\"+filename
            addMark(filePath)
