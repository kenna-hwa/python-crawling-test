import sys
import time
import twitter_bot_tweet as tb


print("Process Start.")

start_time = time.time()

# 아이디 입력
id = sys.argv[1]

# 패스워드 입력
ps = sys.argv[2]

# 트윗 내용 적인 파일명 입력
filename = sys.argv[3]

# 크롤러를 불러옵니다.
BOT = tb.TwitterBot(filename)

# 로그인 시도
BOT.login("bvotest", "bvoat123")

# 스크린샷
BOT.save_screenshot(str(time.time) + ".png")

# 트위터에 모든 멘션을 올립니다.
BOT.tweet_all()

# 10초 딜레이
time.sleep(10)

# 크롤러를 닫아줍니다.
BOT.kill()

print("Process Done.")

end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")