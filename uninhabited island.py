# cording: euc-kr
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from tkinter import *
from tkinter.tix import *
from bs4 import BeautifulSoup
import webbrowser

def Map(coord):
    count = 0
    count_2 = 0

    coordinate = coord

    url = 'https://www.google.co.kr/maps/place/'
    queryParams = coordinate
    queryParams.split()
    Temp = list(queryParams)

    for i in Temp:
        if(i == "‘"):
            Temp[count] = "'"
        elif(i == '‘'):
            Temp[count] = "'"
        elif(i == "’"):
            Temp[count] = "'"
        elif (i == '’'):
            Temp[count] = "'"
        elif(i == "′"):
            Temp[count] = "'"
        elif (i == '′'):
            Temp[count] = "'"
        elif(i == '”'):
            Temp[count] = '"'
        elif(i == "“"):
            Temp[count] = '"'
        elif(i == '“'):
            Temp[count] = '"'
        elif(i == "”"):
            Temp[count] = '"'
        elif(i == '″'):
            Temp[count] = '"'
        elif(i == "″"):
            Temp[count] = '"'
        elif(i == '˚'):
            Temp[count] = '°'
        elif(i == "˚"):
            Temp[count] = '°'

        count += 1


    Temp_2 = ((''.join(Temp)).split( ))
    if(eval(Temp[0]) == 1):
        revise = Temp_2[3] + Temp_2[4] + Temp_2[5] + Temp_2[0] + Temp_2[1] + Temp_2[2]
        Temp_3 = list(revise)
        for i in Temp_3:
            if i == ',':
                Temp_3[count_2] = ' '
            elif i == ",":
                Temp_3[count_2] = ' '
            count_2 += 1
        webbrowser.open(url + ''.join(Temp_3))
    else:
        webbrowser.open(url + ''.join(Temp))
#-----------------------------------------------------------------------------------------------------------------------
def Detail(manidx):
    value = 0
    window_4 = Tk()
    window_4.title("섬 상세정보")
    window_4.geometry("480x480")
    window_4.resizable(False, False)

    frame = Frame(window_4, width=480, height=480)
    frame.pack()

    scoledwin = ScrolledWindow(frame, width=480, height=480)
    scoledwin.pack()

    service_key = unquote(
        '38A4at0LQiHV7hKEvBkQT00%2BFbJj4BgIlH7o1ImrlWFUb2moXZhYL9N5XWmsgarJafORH%2FLKK4At4OP83RmZaw%3D%3D')
    uniManageIdx_1 = manidx
    url = 'http://apis.data.go.kr/1192000/uninhabitableIslandsSearchService/UninhabitableIslandsSearchItem'
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): service_key, quote_plus('uniManageIdx'): uniManageIdx_1})
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()


    soup = BeautifulSoup(response_body, 'html.parser')
    data = soup.find_all('item')

    for item in data:
        name = item.find('name')
        manageno = item.find('manageno')
        nauticalchartno = item.find('nauticalchartno')
        researchagency = item.find('researchagency')
        ownerstatus = item.find('ownerstatus')
        managearea = item.find('managearea')
        distancefromland = item.find('distancefromland')
        jibun = item.find('jibun')
        coordinate = item.find('coordinate')
        usefor = item.find('usefor')
        jimok = item.find('jimok')
        developmentplan = item.find('developmentplan')
        infra = item.find('infra')
        closedseamuin = item.find('closedseamuin')
        residenthistory = item.find('residenthistory')
        residentpossibility = item.find('residentpossibility')
        residentpurpose = item.find('residentpurpose')
        historicvalue = item.find('historicvalue')
        aroundseas = item.find('aroundseas')
        otherlawstatus = item.find('otherlawstatus')
        environment = item.find('environment')
        sealivingthing = item.find('sealivingthing')
        landlivingthing = item.find('landlivingthing')
        insect = item.find('insect')
        plant = item.find('plant')
        landscape = item.find('landscape')


        if (name in item):
            name_l = Label(scoledwin.window, text="섬 이름 : " + (name.get_text()), wraplength=450, justify="left")
            name_l.pack(anchor="w")
        if (manageno in item):
            manageno_l = Label(scoledwin.window, text="섬 관리번호 : " + (manageno.get_text()), wraplength=450,
                               justify="left")
            manageno_l.pack(anchor="w")

        if (nauticalchartno in item):
            nauticalchartno_l = Label(scoledwin.window, text="섬 해도번호 : " + (nauticalchartno.get_text()),
                                      wraplength=450, justify="left")
            nauticalchartno_l.pack(anchor="w")

        if (researchagency in item):
            researchagency_l = Label(scoledwin.window, text="섬 실태조사기관 : " + (researchagency.get_text()),
                                     wraplength=450, justify="left")
            researchagency_l.pack(anchor="w")
        if (ownerstatus in item):
            ownerstatus_l = Label(scoledwin.window, text="섬 토지소유현황 : " + (ownerstatus.get_text()),
                                  wraplength=450,
                                  justify="left")
            ownerstatus_l.pack(anchor="w")
        if (ownerstatus in item):
            managearea_l = Label(scoledwin.window, text="섬 관리면적 : " + (managearea.get_text()), wraplength=450,
                                 justify="left")
            managearea_l.pack(anchor="w")
        if (distancefromland in item):
            distancefromland_l = Label(scoledwin.window, text="섬 육지와의거리 : " + (distancefromland.get_text()),
                                       wraplength=450, justify="left")
            distancefromland_l.pack(anchor="w")
        if (jibun in item):
            jibun_l = Label(scoledwin.window, text="섬 지번 : " + (jibun.get_text()), wraplength=450,
                            justify="left")
            jibun_l.pack(anchor="w")
        if (coordinate in item):
            coordinate_l = Label(scoledwin.window, text="섬 좌표 : " + (coordinate.get_text()), wraplength=450,
                                 justify="left")
            coordinate_l.pack(anchor="w")
            map = Button(scoledwin.window, text="지도로 보기", command=lambda x=coordinate.get_text(): Map(x))
            map.pack(anchor="w")
        if (usefor in item):
            usefor_l = Label(scoledwin.window, text="섬 용도구분 : " + (usefor.get_text()), wraplength=450,
                             justify="left")
            usefor_l.pack(anchor="w")
        if (jimok in item):
            jimok_l = Label(scoledwin.window, text="섬 지목 : " + (jimok.get_text()), wraplength=450,
                            justify="left")
            jimok_l.pack(anchor="w")
        if (developmentplan in item):
            developmentplan_l = Label(scoledwin.window, text="섬 지자체개발계획 : " + (developmentplan.get_text()),
                                      wraplength=450, justify="left")
            developmentplan_l.pack(anchor="w")
        if (infra in item):
            infra_l = Label(scoledwin.window, text="섬 시설물 이용현황 : " + (infra.get_text()), wraplength=450,
                            justify="left")
            infra_l.pack(anchor="w")
        if (closedseamuin in item):
            closedseamuin_l = Label(scoledwin.window, text="섬 영해기점무인도서 : " + (closedseamuin.get_text()),
                                    wraplength=450, justify="left")
            closedseamuin_l.pack(anchor="w")
        if (residenthistory in item):
            residenthistory_l = Label(scoledwin.window, text="섬 과거 주민거주여부 : " + (residenthistory.get_text()),
                                      wraplength=450, justify="left")
            residenthistory_l.pack(anchor="w")
        if (residentpossibility in item):
            residentpossibility_l = Label(scoledwin.window,
                                          text="섬 향후 주민거주가능성 : " + (residentpossibility.get_text()),
                                          wraplength=450,
                                          justify="left")
            residentpossibility_l.pack(anchor="w")
        if (residentpurpose in item):
            residentpurpose_l = Label(scoledwin.window, text="섬 사람 거주시 거주 목적 : " + (residentpurpose.get_text()),
                                      wraplength=450, justify="left")
            residentpurpose_l.pack(anchor="w")
        if (historicvalue in item):
            historicvalue_l = Label(scoledwin.window, text="섬 역사적 가치 : " + (historicvalue.get_text()),
                                    wraplength=450, justify="left")
            historicvalue_l.pack(anchor="w")
        if (aroundseas in item):
            aroundseas_l = Label(scoledwin.window, text="섬 주변해역 이용현황 : " + (aroundseas.get_text()),
                                 wraplength=450,
                                 justify="left")
        aroundseas_l.pack(anchor="w")
        if (otherlawstatus in item):
            otherlawstatus_l = Label(scoledwin.window, text="섬 타법에 의한 관리현황 : " + (otherlawstatus.get_text()),
                                     wraplength=450, justify="left")
            otherlawstatus_l.pack(anchor="w")
        if (environment in item):
            environment_l = Label(scoledwin.window, text="섬 환경일반 (지형, 지질): " + (environment.get_text()),
                                  wraplength=450, justify="left")
            environment_l.pack(anchor="w")
        if (sealivingthing in item):
            sealivingthing_l = Label(scoledwin.window, text="섬 주요해양생물 : " + (sealivingthing.get_text()),
                                     wraplength=450, justify="left")
            sealivingthing_l.pack(anchor="w")
        if (landlivingthing in item):
            landlivingthing_l = Label(scoledwin.window, text="섬 주요육상동물 : " + (landlivingthing.get_text()),
                                      wraplength=450, justify="left")
            landlivingthing_l.pack(anchor="w")
        if (insect in item):
            insect_l = Label(scoledwin.window, text="섬 조류 및 곤충 : " + (insect.get_text()), wraplength=450,
                             justify="left")
            insect_l.pack(anchor="w")
        if (plant in item):
            plant_l = Label(scoledwin.window, text="섬 식생 및 식물 : " + (plant.get_text()), wraplength=450,
                            justify="left")
            plant_l.pack(anchor="w")
        if (landscape in item):
            landscape_l = Label(scoledwin.window, text="섬 주변해역(해중)및 경관 : " + (landscape.get_text()),
                                wraplength=450,
                                justify="left")
            landscape_l.pack(anchor="w")

        wall_l = Label(window_4, text="-----------------------------------------------------------------\n")
        wall_l.pack(anchor="w")

    frame.pack()
#-----------------------------------------------------------------------------------------------------------------------
def Search_Address():
    numstr = []
    count = 0
    window_2 = Tk()
    window_2.title("주소로 섬 검색하기")
    window_2.geometry("480x480")
    window_2.resizable(False, False)


    frame = Frame(window_2, width=480, height=480)
    frame.pack()

    scoledwin = ScrolledWindow(frame, width=480, height=480)
    scoledwin.pack()

    service_key = unquote('38A4at0LQiHV7hKEvBkQT00%2BFbJj4BgIlH7o1ImrlWFUb2moXZhYL9N5XWmsgarJafORH%2FLKK4At4OP83RmZaw%3D%3D')
    (address_1, address_2) = str(e1.get()), str(e2.get())


    url = 'http://apis.data.go.kr/1192000/uninhabitableIslandsSearchService/UninhabitableIslandsSearchAddrList'

    queryParams = '?' + urlencode({quote_plus('ServiceKey'): service_key, quote_plus('uniSido'): address_1, quote_plus('uniSigungu'): address_2})

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    soup = BeautifulSoup(response_body, 'html.parser')
    data = soup.find_all('item')

    for item in data:
        name = item.find('name')
        jibun = item.find('jibun')
        managearea = item.find('managearea')
        ownerstatus = item.find('ownerstatus')
        manageidx = item.find('manageidx')
        name_l = Label(scoledwin.window, text="섬 이름 : " + (name.get_text()))
        name_l.pack(anchor="w")
        jibun_l = Label(scoledwin.window, text="섬 주소 : " + (jibun.get_text()))
        jibun_l.pack(anchor="w")
        managearea_l = Label(scoledwin.window, text="섬 면적 : " + (managearea.get_text()))
        managearea_l.pack(anchor="w")
        ownerstatus_l = Label(scoledwin.window, text="섬 소유 현황 : " + (ownerstatus.get_text()))
        ownerstatus_l.pack(anchor="w")
        manageidx_l = Label(scoledwin.window, text="섬 고유 코드 : " + (manageidx.get_text()))
        manageidx_l.pack(anchor="w")
        numstr.insert(count, manageidx.get_text())

        information = Button(scoledwin.window, text="상세정보 보기", command=lambda x=numstr[count]: Detail(x))
        information.pack(anchor="w")

        wall_l = Label(scoledwin.window, text="-----------------------------------------------------------------\n")
        wall_l.pack(anchor="w")
        count += 1

    frame.pack()
#-----------------------------------------------------------------------------------------------------------------------
def Search_Name():
    numstr = []
    count = 0
    window_3 = Tk()
    window_3.title("이름으로 섬 검색하기")
    window_3.geometry("480x480")
    window_3.resizable(False, False)
    frame = Frame(window_3, width=480, height=480)
    frame.pack()

    scoledwin = ScrolledWindow(frame, width=480, height=480)
    scoledwin.pack()


    service_key = unquote('38A4at0LQiHV7hKEvBkQT00%2BFbJj4BgIlH7o1ImrlWFUb2moXZhYL9N5XWmsgarJafORH%2FLKK4At4OP83RmZaw%3D%3D')
    (Name_1) = str(e3.get())
    url = 'http://apis.data.go.kr/1192000/uninhabitableIslandsSearchService/UninhabitableIslandsSearchNameList'
    queryParams = '?' + urlencode({quote_plus('ServiceKey'): service_key, quote_plus('uniName'): Name_1})
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    soup = BeautifulSoup(response_body, 'html.parser')
    data = soup.find_all('item')

    for item in data:
        name = item.find('name')
        jibun = item.find('jibun')
        managearea = item.find('managearea')
        ownerstatus = item.find('ownerstatus')
        manageidx = item.find('manageidx')
        name_l = Label(scoledwin.window, text="섬 이름 : " + (name.get_text()))
        name_l.pack(anchor = "w")
        jibun_l = Label(scoledwin.window, text="섬 주소 : " + (jibun.get_text()))
        jibun_l.pack(anchor = "w")
        managearea_l = Label(scoledwin.window, text="섬 면적 : " + (managearea.get_text()))
        managearea_l.pack(anchor = "w")
        ownerstatus_l = Label(scoledwin.window, text="섬 소유 현황 : " + (ownerstatus.get_text()))
        ownerstatus_l.pack(anchor = "w")
        manageidx_l = Label(scoledwin.window, text="섬 고유 코드 : " + (manageidx.get_text()))
        manageidx_l.pack(anchor = "w")
        numstr.insert(count, manageidx.get_text())

        information = Button(scoledwin.window, text="상세정보 보기", command= lambda x = numstr[count] : Detail(x))
        information.pack(anchor = "w")

        wall_l = Label(scoledwin.window, text="-----------------------------------------------------------------\n")
        wall_l.pack(anchor="w")
        count += 1

    frame.pack()

#-----------------------------------------------------------------------------------------------------------------------
window = Tk()
window.title("전국 무인도 찾기")
window.geometry("800x480+100+100")
window.resizable(False, False)
#-----------------------------------------------------------------------------------------------------------------------
l1 = Label(window, text="전국 무인도 찾기")
l1.pack(expand=True)

#-----------------------------------------------------------------------------------------------------------------------
l2 = Label(window, text="주소 입력(시, 도)")
l2.pack()

e1 = Entry(window, bg = "yellow", fg = "black")
e1.pack()

l3 = Label(window, text="주소 입력(시, 군, 구)")
l3.pack()

e2 = Entry(window, bg = "yellow", fg = "black")
e2.pack()

b1 = Button(window, text="주소로 검색 하기", command = Search_Address)
b1.pack(expand=True)
#-----------------------------------------------------------------------------------------------------------------------

l3 = Label(window, text="섬 이름 입력")
l3.pack()

e3 = Entry(window, bg = "yellow", fg = "black")
e3.pack()

b2 = Button(window, text="섬이름으로 검색 하기", command = Search_Name)
b2.pack(expand=True)
#-----------------------------------------------------------------------------------------------------------------------
window.mainloop()