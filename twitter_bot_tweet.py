from selenium import webdriver
import pyautogui
import time
import pyperclip


class TwitterBot:
    def __init__(self, contents, encoding="utf-8"):
        # 트위터 홈페이지로 이동합니다.
        self.go_to_twitter()
        # 컨텐츠 파일을 읽어옵니다. 인코딩이 utf-8이 아닌 파일을 읽으면 에러가 날 수 있음
        # 이 경우 인코딩을 명시해 주시면 됩니다. 기본값은 utf-8입니다.
        self.contents_file = open(contents, encoding=encoding)
        # 읽어온 파일을 쪼개 리스트로 만듭니다.
        self.contents = self.contents_file.read().split("\n")

    # 크롤러를 종료하는 메서드입니다.
    def kill(self):
        self.driver.quit()

    # 트위터 페이지에 접속하는 메서드입니다.
    def go_to_twitter(self):
        # 엣지 웹 드라이버
        self.driver = webdriver.Edge(executable_path="msedgedriver.exe")
        # 브라우저 해상도 설정
        self.driver.set_window_size(1600, 900)
        # 트위터 홈페이지로 이동합니다.
        self.driver.get("https://twitter.com/login")
        # 5초 대기
        time.sleep(5)

    # 로그인을 수행하는 메서드입니다.
    def login(self, id, ps):
        # 아이디 입력
        pyautogui.write(id)
        # tab 키
        pyautogui.press("tab")
        # 비밀번호 입력
        pyautogui.write(ps)
        # 엔터키 입력
        pyautogui.press("enter")
        # 5초 대기
        time.sleep(5)

    # 스크린샷을 저장하는 메서드
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # 트위터에 글을 올리는 메서드
    def tweet(self, text, interval=15):
        # 트위터 작성 페이지로 이동합니다.
        self.driver.get("https://twitter.com/intent/tweet")
        time.sleep(2)
        # 한글 입력을 위해 복사 붙여넣기 이용
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        # 컨트롤 키와 엔터키를 누르면 트윗이 입력됩니다.
        pyautogui.hotkey('ctrl','enter')
        # 로딩 될때까지 몇 초 기다립니다.
        time.sleep(interval)

    # 쪼개진 내용을 for문을 이용해 업로드 함수를 호출
    def tweet_all(self, interval=3):
        for el in self.contents:
            time.sleep(interval)
            self.tweet(el.strip(), interval)