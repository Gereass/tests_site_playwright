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

async def test_valid_password():
    try:
        async with async_playwright() as p:
            browser = await p.firefox.launch()
            page = await browser.new_page()
            await page.goto('https://koshelek.ru/authorization/signup')
            await page.locator('#input-125').fill('hjfuytfuy')
            await page.locator('#username').fill('pihaf38709@centerf.com')
            await page.locator('#new-password').fill('111111123')
            await page.click('button[type="submit"]')
            span_locator = page.locator('[data-pw="auth-widget-password-input-message"]')
            span_text = await span_locator.inner_text()
            assert span_text == 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'
            await browser.close()
            message = 'Test valid password: \033[32mСomplete\033[0m'
    except:
        message = 'Test valid password: \x1b[31;1mFalled\x1b[0m'
    return message

async def test_empty_input():
    try:
        async with async_playwright() as p:
            browser = await p.firefox.launch()
            page = await browser.new_page()
            await page.goto('https://koshelek.ru/authorization/signup')
            await page.locator('#input-125').fill('')
            await page.locator('#username').fill('')
            await page.locator('#new-password').fill('')
            await page.click('button[type="submit"]')
            span_locator_pass = page.locator('[specialtoken="k-text-k-typography-body-2-regular"]').nth(2)
            span_text_pass = await span_locator_pass.inner_text()
            span_locator_name = page.locator('[specialtoken="k-text-k-typography-body-2-regular"]').nth(0)
            span_text_name = await span_locator_name.inner_text()
            span_locator_email = page.locator('[specialtoken="k-text-k-typography-body-2-regular"]').nth(1)
            span_text_email = await span_locator_email.inner_text()
            aria_checked = await page.locator('#input-177').evaluate('(element) => element.getAttribute("aria-checked")')

            assert span_text_pass and span_text_name and span_text_email == 'Поле не заполнено' and aria_checked == 'false'
            await browser.close()
            message = 'Test empty input: \033[32mСomplete\033[0m'
    except:
        message = 'Test empty input: \x1b[31;1mFalled\x1b[0m'
    return message

async def test_valid_email():
    try:
        async with async_playwright() as p:
                browser = await p.firefox.launch()
                page = await browser.new_page()
                await page.goto('https://koshelek.ru/authorization/signup')
                await page.locator('#input-125').fill('hjfuytfuy')
                await page.locator('#username').fill('pihaf38709@.com')
                await page.locator('#new-password').fill('123qweQWE_')
                await page.click('button[type="submit"]')
                span_locator = page.locator('[specialtoken="k-text-k-typography-body-2-regular"]').nth(1)
                span_text = await span_locator.inner_text()
                assert span_text == 'Формат e-mail: username@test.ru'
                await browser.close()
                message = 'Test valid email: \033[32mСomplete\033[0m'
                a=1+1
    except:
        message = 'Test valid email: \x1b[31;1mFalled\x1b[0m'
    return message  

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
    except:
        message = 'Test valid name: \x1b[31;1mFalled\x1b[0m'
    return message

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test_short_password()))
    print(loop.run_until_complete(test_valid_password()))
    print(loop.run_until_complete(test_empty_input()))
    print(loop.run_until_complete(test_valid_email()))
    print(loop.run_until_complete(test_valid_name()))
