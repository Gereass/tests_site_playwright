import asyncio
from playwright.async_api import async_playwright

async def test_valid_name():
    try:
        async with async_playwright() as p:
                browser = await p.firefox.launch()
                page = await browser.new_page()
                await page.goto('https://koshelek.ru/authorization/signup')
                await page.locator('#input-125').fill('asd')
                await page.locator('#username').fill('pihaf38709@mail.com')
                await page.locator('#new-password').fill('123qweQWE_')
                await page.click('button[type="submit"]')
                span_locator_name = page.locator('[specialtoken="k-text-k-typography-body-2-regular"]').nth(0)
                span_text_name = await span_locator_name.inner_text()
                assert span_text_name == 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
                await browser.close()
                message = 'Test valid name: \033[32mСomplete\033[0m'
    except Exception as exc_info:
        message = f'Test valid name: \x1b[31;1mFalled\x1b[0m \n {str(exc_info)}'
    return message
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test_valid_name()))
