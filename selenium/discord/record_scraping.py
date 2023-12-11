from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()

        # 닥지지 접속
        mainpage = await page.goto('https://dak.gg')

        # 발로란트 선택
        select_valorant = await page.wait_for_selector('//*[@id="__next"]/div/div/main/div[3]/div[2]/div[1]/ul/li[3]/a/span')
        await select_valorant.click()

        # ID + 태그 입력
        input_inform = input("검색할 ID와 태그를 입력하세요 (예: firefox#5959): ")
        
        # ID + 태그 검색
        search = await page.wait_for_selector('//*[@id="content-top"]/div/div/div/form/input')
        await search.fill(input_inform)
        search_click = await page.click('//*[@id="content-top"]/div/div/div/form/button')

        # 전적 공개/비공개 확인
        open_profile = await page.wait_for_selector('//*[@id="content-container"]/dl/div[1]/div')
        text_open_profile = await open_profile.text_content()
        correct_open_profile = "경쟁전"
        close_profile = await page.query_selector('#__next > div > main > div > section > div > button > span')
        
        # 전적 공개 분기처리
        if text_open_profile == correct_open_profile: # 프로필 정보가 오픈일 때
            user_inform = {}
            text_open_profile = await open_profile.text_content()

            refresh = await page.wait_for_selector('//*[@id="content-top"]/div[1]/header/div[1]/div[2]/button[1]')
            await refresh.click()
            recent_update = await page.wait_for_selector('//*[@id="content-top"]/div[1]/header/div[1]/div[3]/p')
            await recent_update.click()
            recent_check = await page.wait_for_selector('//*[@id="content-top"]/div[1]/header/div[1]/div[3]/p')
            text_recent_check = await recent_check.text_content()

            # 최근 24게임 전적
            record_title = await page.wait_for_selector('//*[@id="content-container"]/section/section/h4')
            text_record_title = await record_title.text_content()

            win_rate = await page.wait_for_selector('//*[@id="content-container"]/section/section/div/section[1]/dl/div[1]/dd')
            t_win_rate = await win_rate.text_content()

            kd_rate = await page.wait_for_selector('//*[@id="content-container"]/section/section/div/section[1]/dl/div[2]/dd')
            t_kd_rate = await kd_rate.text_content()

            average_damage = await page.wait_for_selector('//*[@id="content-container"]/section/section/div/section[1]/dl/div[3]/dd')
            t_average_damage = await average_damage.text_content()

            average_point = await page.wait_for_selector('//*[@id="content-container"]/section/section/div/section[1]/dl/div[4]/dd')
            t_average_point = await average_point.text_content()

            print(f'{text_record_title}\n승률: {t_win_rate}\nKD: {t_kd_rate}\n평균딜량: {t_average_damage}\n평균점수: {t_average_point}')

        # 프로필 비공개 시
        else:
            hide_id = page.text_content('//*[@id="__next"]/div/main/div/section/p/span')
            print(hide_id)

asyncio.run(main())