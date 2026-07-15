from playwright.sync_api import sync_playwright
import time

print("==================================================")
print("  第十天实战：掌握元素定位，实现全自动登录")
print("==================================================")


def test_auto_login():
    with sync_playwright() as p:
        print("1. 启动 Chromium 浏览器...")
        # 依旧开启有头模式，放慢动作
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # 访问练习专用的沙盒登录页面
        print("2. 正在访问沙盒登录页面...")
        page.goto("http://quotes.toscrape.com/login")

        # ------------------- 定位实战开始 -------------------
        # 剧透：通过 F12 检查，这个网页的账号输入框有一段代码是 id="username"
        # 密码输入框有一段代码是 id="password"
        # 登录按钮上写着清晰的文本 "Login"

        print("3. 正在输入账号...")
        # 【任务 1】：使用 法宝 1 (ID定位) 找到账号输入框，并填入 "test_user"
        # 提示：ID 前面要加 #
        page.locator("#username").fill("test_user")

        print("4. 正在输入密码...")
        # 【任务 2】：使用 法宝 1 (ID定位) 找到密码输入框，并填入 "123456"
        page.locator("#password").fill("123456")

        print("5. 点击登录按钮！")
        # 【任务 3】：使用 法宝 3 (文本定位) 找到登录按钮，并点击它
        # 提示：按钮上的字叫 Login
        page.get_by_role("button",name = "Login").click()

        print("6. 等待页面跳转，进行断言...")
        time.sleep(2)  # 等待页面刷新

        # 【终极任务 4】：UI 自动化的断言
        # 登录成功后，页面右上角会出现一个 "Logout" (退出登录) 的按钮
        # 我们用 get_by_text 找一下这个按钮，判断它是不是可见的 (is_visible)
        is_success = page.get_by_text("Logout").is_visible()

        if is_success:
            print("✅ 断言通过：登录成功！找到了 Logout 按钮！")
        else:
            print("❌ 断言失败：登录似乎没有成功...")

        print("7. 截图留念并关闭浏览器。")
        page.screenshot(path="login_success.png")
        browser.close()


# 运行代码
test_auto_login()

# (1) with sync_playwright() as p:    魔法公式
# (2)browser = p.chromium.launch(headless=False, slow_mo=500)     访问chrom网页，每次操作减慢0.5s
# (3)page.goto()  开始进入网页
# (4)page.locator("#  " ).fill()     输入信息的格式    （输入）
# (5)page.get_by_text("  ").click()   寻找内容并且点击  （点击）
# (6)page.get_by_role("button", name = " ").click()   遇到名字相同的多个功能时使用
# (7)is_success = page.get_by_text(" ").is_visible()  判断网页是否成功登录 （is_visivle()为是否存在函数）
# (8)page.screenshot(path="  ")   截图功能
# (9)brower.close()   关闭网页
