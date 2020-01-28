# 파이썬 메뉴얼을 재귀적으로 다운받는 프로그램
# 모듈 읽어들이기
import os.path
import re
import time
from os import makedirs
from urllib.parse import *
from urllib.request import *

from bs4 import BeautifulSoup as bs

# 이미 처리한 파일인지 확인하기 위한 변수
proc_files = {}


# HTML 내부에 있는 링크를 추출하는 함수
def enum_links(html, base):
    soup = bs(html, "html.parser")
    # css 링크 추가
    links = soup.select("link[rel='stylesheet']")
    # a 링크 추가 -> 위의 객체 리스트에 리스트를 추가한다.
    links += soup.select("a[href]")
    # 링크 페이지(links:태그)를 절대 주소로 받아서 추가 시키는 리스트
    result = []
    # href 속성을 추출하고, 링크를 절대 경로로 변환
    for a in links:
        # 링크 걸린 url 을 가져오기
        href = a.attrs['href']
        # 가져온 url 을 절대주소로 변환
        url = urljoin(base, href)
        # result 에 추가 -> 가져와야할 페이지 저장
        result.append(url)
    return result


# 파일을 다운 받고 저장하는 함수
# url은 다운로드 받아야할 절대 페이지
def download_file(url):
    o = urlparse(url)
    # 내 컴퓨터의 위치 정한다. -> 파일포함
    # "./" -> 실행이 되고 있는 현재 -> ch11data
    # o.netloc -> 서버의 위치(docs.python.org)
    # o.path -> 서버 뒤에 있는 내용
    savepath = "./" + o.netloc + o.path
    # savepath의 내용이 "/"로 끝나면 페이지가 없다.-> 기본페이지 추가
    # 폴더라면 index.html
    if re.search(r"/$", savepath):
        savepath += "index.html"
    # 저장 폴더가 있는지 확인하기 위해서 폴더를 찾아낸다.
    savedir = os.path.dirname(savepath)
    # 폴더가 존재하면 이미 처리한 것으로 추정해서 바로 리턴한다.
    # 모두 다운 됐는지 확인
    if os.path.exists(savepath):
        return savepath
    # 폴더가 존재하지 않으면 폴더를 만들고 다운로드를 실행한다.
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        # 폴더 만들기 실행
        makedirs(savedir)
    # 파일 다운받기
    try:
        print("download=", url)
        # 다운로드 실행
        urlretrieve(url, savepath)
        # 0.05초 휴식
        time.sleep(0.05)
        # 다운로드된 페이지 이름을 돌려준다.
        return savepath
    except:
        print("다운실패 : ", url)
        return None


# HTML을 분석하고 다운받는 함수
def analyze_html(url, root_url):
    # 분석하려는 페이지 -> download_file 함수 다운로드 받는다. : 처음에는 기본 페이지 다운
    savepath = download_file(url)
    # 다운로드 받은 페이지가 None -> 다운로드를 다 받았다.
    if savepath is None:
        return
    # 다운로드를 받을 페이지에 존재하면 리턴
    if savepath in proc_files:
        # 이미 처리됐다면 실행하지 않음
        return
    # proc_files -> 다운받은 페이지를 키로 해서 저장한다.
    proc_files[savepath] = True
    # 다운로드 받는 페이지 분석
    print("analyze_html=", url)
    # html 로 읽어오기 -> 다운로드된 파일을 읽기전용으로 열고 전체를 읽어온다.
    # 링크추출
    html = open(savepath, "r", encoding="utf-8").read()
    # 다운로드 받은 페이지에 링크가 걸려있는 목록을 가져온다. enum_links() 호출
    links = enum_links(html, url)

    for link_url in links:
        # 링크가 루트 이외의 경로를 나타낸다면 무시
        # link_url.find(root_url) != 0 -> link_url 이 root_url 로 시작하지 않는다.
        if link_url.find(root_url) != 0:
            # link_url 이 .css 로 끝나지 않는다. -> css 파일이 아니다.
            if not re.search(r".css$", link_url):
                continue
        # link_url 의 페이지가 HTML 이나 HTM 이라면 다시 링크를 분석해야한다.
        if re.search(r".(html|htm)$", link_url):
            # 재귀적으로 HTML 파일 분석하기
            analyze_html(link_url, root_url)
            continue
        # link_url 가 HTML, HTM이 아니고 다른 사이트의 url 이 아닌 경우
        # 기타파일
        download_file(link_url)


if __name__ == "__main__":
    # URL 에 있는 모든 것 다운 받기
    url = "https://docs.python.org/3.5/library/"
    # 페이지 분석 -> 기본페이지 분석 -> link 를 리스트로 만든다. -> 다운받는다.
    analyze_html(url, url)




