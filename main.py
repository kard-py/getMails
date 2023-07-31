from playwright.sync_api import sync_playwright

tema = str(input("Digite o tema: "))
email = str(input("Digite o tipo do email: "))

url = f'https://www.google.com/search?q=%22{tema}%22+and+%22%40{email}%22'
extrator_url = 'https://www.extrator.com.br/extrator-de-emails/'


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    listRaw = page.locator('//*[@id="search"]').all_text_contents()

    page.goto(extrator_url)
    page.locator('//*[@id="exdados"]').fill(''.join(listRaw))

    page.locator('//*[@id="extrair"]').click()

    emails = page.locator('//*[@id="exdados"]').value
    
    print(emails)
    browser.close()



