from playwright.sync_api import sync_playwright
import time

print("==================================================")
print("  第十天大考：自己动手，丰衣足食")
print("==================================================")


def run_my_test():
    # 1. 【修复】开启 Playwright 魔法阵！这是所有操作的前提
    with sync_playwright() as p:
        # 2. 【修复】统一下变量名，都叫 browser
        browser = p.chromium.launch(headless=True, slow_mo=500)
        page = browser.new_page()

        page.goto("http://quotes.toscrape.com")

        print("1. 寻找页面上的作者介绍并点击：")
        # 3. 【核心修复】定位实战！
        # 找文本包含 "(about)" 的所有元素，取第一个 (.first)，然后点击它 (.click())
        page.get_by_text("(about)").first.click()

        print("等待页面加载：")
        time.sleep(2)

        print("2. 拍照保存：")
        # 4. 【修复】截图加上 path= 参数
        page.screenshot(path="about_page.png")

        browser.close()


# 运行代码
run_my_test()