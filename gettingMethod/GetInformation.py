# import Libraries
import requests
from requests.adapters import HTTPAdapter
import re
import urllib3

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# 운영자 토큰
access_token = 'MTBkNTUzNDQtMWQzYS00Mjg4LTkwNDEtNDAzNzJlZTZiNGJjOjVkMzJmZTkwLWUyNTEtNDliZC05MGE0LTBiZmIxYzgwZmEzNA=='

# Getting the BearerToken
def getBearerToken(url):
    headers = {'Accept': 'application/json', 'Authorization': 'token {}'.format(access_token)}
    session = requests.Session()
    result = session.request('POST', url, headers=headers, verify=False)
    return result.json()["bearerToken"]


def sendingCommonRequest(url, bearerToken):
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(bearerToken)}
    session = requests.Session()
    flag = True
    while flag:
        result = session.request('GET', url, headers=headers, verify=False)
        if 'The application has encountered an unknown error.' not in result.text:
            flag = False
    return result


# Getting Projects Scanned
def getProjectList(url, bearerToken):
    return sendingCommonRequest(f'{url}/projects?limit=999999&offset=0', bearerToken).json()


# Getting Project Information
# def getProjectInfo(name):
#     bToken = getBearerToken()
#     headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(bToken)}
#     url = f'{baseUrl}/projects/?q=name:{name}'
#     session = requests.Session()
#     result = session.request('GET', url, headers=headers, verify=root_cert, cert=(serverCert, serverKey))
#     return result.json()

# Getting Latest Project Versions
def getLatestVersion(url, bearerToken):
    return sendingCommonRequest(url, bearerToken).json()

def removeSameList(myList, cnt):
    i = 0
    while i < cnt - 1:
        if myList[i] == myList[i + 1]:
            myList.remove(myList[i + 1])
            cnt = cnt - 1
            i = i - 1
        i = i + 1
    return myList
