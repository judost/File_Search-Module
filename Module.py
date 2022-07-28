import os

root_ = "./Root/" # 기본 폴더
folder = [] # 폴더 위치가 담길 배열

def FileSearch():
    for (root, dirs, files) in os.walk(root_):

        if len(files) > 0 and len(dirs) == 0:   # 위치가 폴더가 아닌 파일인 경우만
            file = []   # 임시 파일 위치 
            for file_name in files:
                if 'WantStr' in file_name:  # 원한 파일명일 경우만
                    txtlink = (root + '/' + file_name)
                    # print(txtlink)
                    file.append(txtlink)
            # print('-'*10)
            folder.append(file)
    print(folder)  
FileSearch()      
