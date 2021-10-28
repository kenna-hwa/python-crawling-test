import requests
import asyncio
import aiohttp

resp = requests.get("https://search.naver.com/search.naver?query=강남구+날씨")



async def main():
	async with aiohttp.ClientSession() as session:
		async with session.get("https://search.naver.com/search.naver?query=강남구+날씨") as resp:
			if resp.status == 200:
				html = resp.text()
				print(html)

loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음
loop.run_until_complete(main())    # hello가 끝날 때까지 기다림
loop.close()                        # 이벤트 루프를 닫음