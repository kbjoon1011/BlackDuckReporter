import os
from datetime import datetime
from gettingMethod import GetInformation, CreatePrjListDict
from createReport import GenerateBOMReport

# Create a Report Directory
dateymd = datetime.now().strftime("%Y%m%d-%H%M%S")
if os.path.isdir(f'C:\\Users\\kim.bj\\Desktop\\HanaBank\\BlackDuckReport\\{dateymd}') is False:
    os.mkdir(f'C:\\Users\\kim.bj\\Desktop\\HanaBank\\BlackDuckReport\\{dateymd}')

# URL
baseUrl = f'https://tech.ensecure.kr:7009/api'

# Bearer Token
bearerToken = GetInformation.getBearerToken(f'{baseUrl}/tokens/authenticate')


if __name__ == "__main__":
    # 프로젝트 목록 획득
    prjListJSON = GetInformation.getProjectList(baseUrl, bearerToken)

    # Create a Project List Dictionary
    # prjListResult Design
    # {'번호':[프로젝트 이름, 프로젝트 ID, 버전 명, Component Risk Profile 주소, Component List 주소]}
    prjListResult = CreatePrjListDict.createProjectListDict(prjListJSON, bearerToken)

    # Report 생성 시작
    for i in range(0, len(prjListResult)):
        GenerateBOMReport.createBOMReport(prjListResult[i])





# fileList = glob("*.py")

# print(fileList)

# for f in fileList:
#    if re.findall("create(.*)Report.py", f):
#        os.system(f'python {f}')
