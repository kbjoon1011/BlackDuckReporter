from gettingMethod import GetInformation

if __name__ == "__main__":
    # URL
    baseUrl = f'https://tech.ensecure.kr:7009/api'

    # Bearer Token
    bearerToken = GetInformation.getBearerToken(f'{baseUrl}/tokens/authenticate')

    result = GetInformation.sendingCommonRequest('https://tech.ensecure.kr:7009/api/projects/358ef0bf-f7dc-490c-9223-fc4f846b1500/versions/8c7ade79-5540-465f-b6ca-4c7e872286e1/components',bearerToken).json()
    print(result)