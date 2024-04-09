import asyncio
from playwright.async_api import async_playwright

async def test_short_password():
    try:
        async with async_playwright() as p:
                browser = await p.firefox.launch()
                page = await browser.new_page()
                await page.goto('https://koshelek.ru/authorization/signup')
                await page.locator('#input-125').fill('hjfuytfuy')
                await page.locator('#username').fill('pihaf38709@centerf.com')
                await page.locator('#new-password').fill('123')
                await page.click('button[type="submit"]')
                span_locator = page.locator('[data-pw="auth-widget-password-input-message"]')
                span_text = await span_locator.inner_text()
                assert span_text == 'Пароль должен содержать минимум 8 символов'
                await browser.close()
                message = 'Test short password: \033[32mСomplete\033[0m'
    except:
        message = 'Test short password: \x1b[31;1mFalled\x1b[0m'
    return message

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test_short_password()))
