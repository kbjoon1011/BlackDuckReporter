from openpyxl import Workbook
from createReport import WriteReportFiles
from gettingMethod.GetInformation import sendingCommonRequest
import blackduck

"""
logger = logging.getLogger(__name__)
fileHandler = RotatingFileHandler(f'C:\\Users\\kim.bj\\Desktop\\업무\\BlackDuck\\Reporting_Tool\\CompReportLog.log',
                                  maxBytes=1024 * 10000, backupCount=5)
fileHandler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)s] >> %(message)s'))
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)
"""


def createBOMReport(componentList):
    wb = Workbook()
    ws = wb.create_sheet('Overall Report', 0)

    # 기본 틀 생성
    WriteReportFiles.writeProjectName(ws, componentList[0], componentList[2])
    WriteReportFiles.writeToday(ws, 'j1', 'k1')

    WriteReportFiles.createDefaultForm(ws, 'a2', 'a3', 'Components')
    WriteReportFiles.createDefaultForm(ws, 'b2', 'b3', 'Versions')
    WriteReportFiles.createDefaultForm(ws, 'c2', 'c3', 'Licenses')
    WriteReportFiles.createDefaultForm(ws, 'd2', 'd3', 'Match Types')
    WriteReportFiles.createDefaultForm(ws, 'e2', 'g2', 'Vulnerabilities')
    WriteReportFiles.createDefaultForm(ws, 'e3', 'e3', 'Critical')
    WriteReportFiles.createDefaultForm(ws, 'f3', 'f3', 'Hight')
    WriteReportFiles.createDefaultForm(ws, 'g3', 'g3', 'Medium')
    WriteReportFiles.createDefaultForm(ws, 'h2', 'i2', 'Short Terms')
    WriteReportFiles.createDefaultForm(ws, 'h3', 'h3', 'Versions', 'dce6f1')
    WriteReportFiles.createDefaultForm(ws, 'i3', 'i3', 'Vuln', 'dce6f1')
    WriteReportFiles.createDefaultForm(ws, 'j2', 'k2', 'Long Terms')
    WriteReportFiles.createDefaultForm(ws, 'j3', 'j3', 'Versions', 'dce6f1')
    WriteReportFiles.createDefaultForm(ws, 'k3', 'k3', 'Vuln', 'dce6f1')

    ws.column_dimensions['a'].width = 30
    ws.column_dimensions['b'].width = 16
    ws.column_dimensions['c'].width = 24
    ws.column_dimensions['d'].width = 30
    ws.column_dimensions['h'].width = 16
    ws.column_dimensions['j'].width = 16

    # 프로젝트 갯 수
    rowNum = 4

    # 해당 프로젝트 버전의 Components json 저장
    # prjListResult[0][4]['href'] = Components 목록을 리턴 받기 위한 URL
    components = sendingCommonRequest(f"{componentList[3]['href']}?limit=100000", blackduck.bearerToken).json()

    # Component 정보 엑셀에 입력
    for i in range(0, components['totalCount']):
        WriteReportFiles.writeData(ws, components['items'][i], rowNum)
        rowNum = rowNum + 1

    # 엑셀 선 그리기
    WriteReportFiles.drawBorders(ws, rowNum)
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    wb.save(f'C:\\Users\\kim.bj\\Desktop\\HanaBank\\BlackDuckReport\\{blackduck.dateymd}\\{componentList[0]}-{componentList[2]}.xls')
    wb.close()
