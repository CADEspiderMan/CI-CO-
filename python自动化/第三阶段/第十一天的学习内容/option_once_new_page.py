from playwright.sync_api import sync_playwright
import time

print("==================================================")
print("  第十二天实战：下拉框、系统弹窗与多标签页")
print("==================================================")


def conquer_challenges():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # ------------------- 挑战 1：下拉框 -------------------
        print("\n▶️ 挑战 1：搞定下拉框 (Dropdown)")
        page.goto("https://the-internet.herokuapp.com/dropdown")

        # 页面上有一个 id 为 "dropdown" 的下拉框。
        # 【任务 1】：请使用专属的 select_option 方法，选中里面的 "Option 2" 或者 value值 "2"
        page.locator("#dropdown").select_option("2")
        print("✅ 下拉框已成功选中 Option 2！")
        time.sleep(1)

        # ------------------- 挑战 2：系统弹窗 -------------------
        print("\n▶️ 挑战 2：拦截并确认系统弹窗 (JS Alert)")
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        # 【任务 2】：在点击按钮之前，先“埋伏”好！
        # 请使用 page.once 监听 "dialog" 事件，并使用 lambda 表达式让它自动点击确定 (accept)
        # 提示：lambda dialog: dialog.XXXX()
        page.once("dialog", lambda dialog: dialog.accept())

        # 触发弹窗的按钮
        page.get_by_text("Click for JS Confirm").click()

        # 网页底层设计：如果你点了确定，页面上会出现绿色的 "You clicked: Ok"
        page.get_by_text("You clicked: Ok").wait_for()
        print("✅ 弹窗已被成功拦截，并点击了确定！")
        time.sleep(1)

        # ------------------- 挑战 3：多标签页 -------------------
        print("\n▶️ 挑战 3：驾驭新标签页 (New Window)")
        page.goto("https://the-internet.herokuapp.com/windows")

        # 【任务 3】：准备捕获新开的页面！
        # 使用 with page.context.xxxxx() 魔法
        with page.context.except_page() as new_page_info:
            # 点击页面上的 "Click Here" 链接，这会导致浏览器新开一个标签页
            page.get_by_text("Click Here").click()

        # 提取接住的新页面对象
        new_page = new_page_info.value

        # 验证我们是否成功控制了新页面（打印新页面的标题，应该是 "New Window"）
        print(f"✅ 成功捕获新标签页！新页面的标题是: {new_page.title()}")

        # 给新页面拍个照证明我们来过！
        new_page.screenshot(path="new_tab_success.png")
        print("\n📸 截图已保存至 new_tab_success.png，大满贯通关！")

        browser.close()


# 运行魔法
conquer_challenges()