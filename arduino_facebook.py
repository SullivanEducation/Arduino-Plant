#-*-coding: utf-8 -*-

#facebook-sdk가 설치되어있어야 합니다<pip install>
import facebook

#1. 페이스북 개발자 사이트에서 토큰을 발급받아야 합니다
#토큰 발급법은 글을 참조해 주시기 바랍니다

facebook_key = 'Facebook Token'

#2. 글을 쓰는 함수
def post(text) :
    graph = facebook.GraphAPI(facebook_key)
    resp = graph.get_object('me/accounts')

    graph.put_wall_post(text)
    pass

#3. 글쓰기!
post("안녕하세요 아두이노 센서를 알려주는 봇입니당")

#-----------------------------------------------------------------#
#pyserial이 설치되어있어야 합니다 <pip install>
import serial

#1.시리얼 포트 지정 (아두이노 툴->포트 에서 연결된 포트 확인)
#Mac
ser = serial.Serial('/dev/cu.usbmodem1411')
#윈도우
#ser = serial.Serial('COM9')

#2. 시리얼 값을 읽는 함수 <결과 문자열 출력>
def readData(ser):
    obj = ser.readline()
    str = obj[:-2].decode()

    return str

#3. 시리얼에 값을 쓰는 함수
def writeData(ser, data):
    ser.write([data])

#4. 함수를 사용해서 값을 읽어보자!
while True:
    str = readData(ser)
    val = int(str)
    #값을 읽어서 페이스북에 올리자아
    contents="[습도알리미]현재 습도는 "+val+"입니다!"
    post(contents)

