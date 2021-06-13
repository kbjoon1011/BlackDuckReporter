from gettingMethod import GetInformation

baseUrl = f'https://tech.ensecure.kr:7009/api'

# Release Version Report 생성을 위한 Dictionary 생성
def createProjectListDict(prjListJSON, bearerToken):
    prjCount = prjListJSON['totalCount']
    bearerToken = bearerToken
    # prjListResult Design
    # {'번호':[프로젝트 이름, 프로젝트 ID, Release 버전 명, Component Risk Profile 주소, Component List 주소]}
    prjListResult = {}

    for num in range(0, prjCount):
        # 프로젝트 이름, ID 주소 추가
        prjListResult[num] = [prjListJSON['items'][num]['name'], prjListJSON['items'][num]['_meta']['href']]

        # 프로젝트 Version 명 추가
        projectVersion = GetInformation.getLatestVersion(prjListResult[num][1] + '/versions?offset=0&limit=100&sort=versionName%20DESC', bearerToken)
        prjListResult[num].append(projectVersion['items'][0]['versionName'])

        # 프로젝트 버전 Component Risk Profile 주소 추가
        #prjListResult[num].append(projectVersion['items'][0]['_meta']['links'][2])

        # 프로젝트 버전 Component List 주소 추가
        prjListResult[num].append(projectVersion['items'][0]['_meta']['links'][5])

    return prjListResult
