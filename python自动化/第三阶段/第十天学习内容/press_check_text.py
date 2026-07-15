from playwright.sync_api import sync_playwright
import time

print("==================================================")
print("  第十一天实战：敲击键盘与勾选复选框")
print("==================================================")


def manage_todos():
    with sync_playwright() as p:
        print("1. 启动魔法浏览器...")
        browser = p.chromium.launch(headless=False, slow_mo=800)  # 放慢动作方便观察
        page = browser.new_page()

        # 访问经典的 TodoMVC 待办事项沙盒网站
        page.goto("https://demo.playwright.dev/todomvc/#/")

        print("2. 正在添加第一条待办事项...")
        # 网页中间有一个大大的输入框，里面灰色的提示字是 "What needs to be done?"
        input_box = page.get_by_placeholder("What needs to be done?")

        # 填入文字
        input_box.fill("学习 Playwright 表单交互")

        # 【任务 1】：请使用 page.keyboard 模拟按下回车键 (Enter)，把待办事项添加进去
        # 提示：按键名字叫 "Enter"
        page.keyboard.press("Enter")

        print("3. 正在添加第二条待办事项...")
        # 【任务 2】：请再次在这个输入框 (input_box) 里填入 "彻底消灭 bug"
        input_box.fill("彻底消灭 bug")

        # 再次敲击回车！
        page.keyboard.press("Enter")

        print("4. 干得漂亮！现在把第一条任务标记为'已完成'...")
        # 获取页面上所有的复选框（这里每个待办事项前面都有一个圆形的 checkbox）
        checkboxes = page.get_by_role("checkbox")

        # 【任务 3】：选中第一个复选框并勾选它
        # 提示1：使用 .nth(0) 或 .first 取第一个
        # 提示2：勾选动作叫 .check()
        checkboxes.first.check()

        print("5. 智能等待验收...")
        # 使用智能等待，确保第一条任务变成了“已划线”的完成状态
        # 网页底层设计：完成的任务会被加上 class="completed"
        page.locator("li.completed").wait_for()
        print("✅ 智能等待成功：系统已确认任务状态变更为'已完成'！")

        # 截图保存战果
        page.screenshot(path="my_todos.png")
        print("\n📸 截图已保存至 my_todos.png，下班！")

        browser.close()


# 运行魔法
manage_todos()