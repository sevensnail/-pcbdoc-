import os
import shutil

#file

def copyschpcb():
    n=1
  
    drive_l = input('请输入盘符(大写)后回车：')
    dirname = drive_l+':\\'

    print('请等待...')
    #'E:/'
    if(os.path.isdir(dirname)):



        for maindir, subdir,file_name_list in os.walk(dirname):

            #print("1:",maindir) #当前主目录
            #print("2:",subdir) #当前主目录下的所有目录
            #print("3:",file_name_list)  #当前主目录下的所有文件

            for filename in file_name_list:
                apath = os.path.join(maindir, filename)#合并成一个完整路径
                if((os.path.splitext(apath)[1] =='.SchDoc')|(os.path.splitext(apath)[1] =='.PcbDoc')):  # 获取文件后缀 [0]获取的是除了文件名以外的内容
                    with open ('汇总.txt','a') as file_handle:
                      file_handle.write(str(n)+'.'+apath)
                      file_handle.write('\n')
                    print(str(n)+'.'+apath)

                    file_dir = os.getcwd() +'/'+str(n)+'_'+filename 
                    file = apath
                    n=n+1
                    shutil.copy(file,file_dir) 
                    #  print(str(n)+'.'+'已复制'+filename)


                # result.append(apath)
            
    else:
        print("盘符错误")




'''
    for pathName in RbAddress:
        current_folder = os.listdir(pathName)#current_foder是‘模拟’文件夹下所有子文件名组成的一个列表   
        for fileName in current_folder:
        #拼接出要存放的文件夹的路径  
            for i in range(10):
                if os.path.split(fileName)[1] == Rbfile[i]:
                 #   file_dir = 'C:/Users/Administrator/Desktop/测试'+'/'+fileName    
                    file_dir = os.getcwd() +'/'+fileName              
            #将指定的文件file复制到file_dir的文件夹里面
                    file=pathName+'/'+Rbfile[i]
                    n=n+1
                    shutil.copy(file,file_dir)
                    print(str(n)+'.'+'已复制'+fileName)
                else:
                    continue
'''

if __name__ == '__main__':
    copyschpcb()
    os.system('pause')