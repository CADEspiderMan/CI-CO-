from playwright.sync_api import sync_playwright
import time

print("==================================================")
print("  UI自动化终极考核：大满贯连击挑战")
print("==================================================")


def ultimate_challenge():
    # 1. 启动 Playwright 魔法阵 (with 语句)
    # TODO: 请写下你的代码...
    with sync_playwright() as p:
        # 2. 启动 Chromium 浏览器 (有头模式，稍微放慢点速度，比如 slow_mo=800)
        #    并新建一个 page
        # TODO: 请写下你的代码...
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()

        # ---------------- 关卡 1：复选框 ----------------
        print("▶️ 正在挑战关卡 1...")
        # 3. 访问复选框练习页: https://the-internet.herokuapp.com/checkboxes
        # TODO: 请写下你的代码...
        page.goto("https://the-internet.herokuapp.com/checkboxes")

        # 4. 页面上有两个复选框，请把 第一个 缺省未勾选的复选框给勾选上！
        # 提示：用 get_by_role 找到 "checkbox"，配合 .first 和 .check()
        # TODO: 请写下你的代码...
        checkbox = page.get_by_role("checkbox")
        checkbox.first.check()
        time.sleep(1)  # 停顿一下方便肉眼观察

        # ---------------- 关卡 2：系统弹窗 ----------------
        print("▶️ 正在挑战关卡 2...")
        # 5. 访问弹窗练习页: https://the-internet.herokuapp.com/javascript_alerts
        # TODO: 请写下你的代码...
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        # 6. 提前埋伏好弹窗处理逻辑，一旦出现 dialog，让它自动点击“确定”(accept)
        # 提示：用到 lambda 匿名函数
        # TODO: 请写下你的代码...
        page.once("dialog", lambda dialog: dialog.accept())

        # 7. 触发弹窗：点击页面上文字为 "Click for JS Confirm" 的按钮
        # TODO: 请写下你的代码...
        page.get_by_text("Click for JS Confirm").click()

        time.sleep(1)  # 停顿一下方便肉眼观察

        # ---------------- 关卡 3：多标签页 ----------------
        print("▶️ 正在挑战关卡 3...")
        # 8. 访问多标签页练习页: https://the-internet.herokuapp.com/windows
        # TODO: 请写下你的代码...
        page.goto("https://the-internet.herokuapp.com/windows")

        # 9. 准备接住新页面，并点击页面上文字为 "Click Here" 的链接
        # 提示：用到 with page.context.expect_page() 魔法
        # TODO: 请写下你的代码...
        with page.context.expect_page() as new_page_info:
            page.get_by_text("Click Here").click()

        # 10. 提取新页面对象，并给【新页面】截个图，保存为 "graduation.png"
        # TODO: 请写下你的代码...
        new_page = new_page_info.value
        new_page.screenshot(path="graduation.png")

        # 11. 优雅地关闭浏览器
        # TODO: 请写下你的代码...
        browser.close()


# 运行考核代码
ultimate_challenge()
