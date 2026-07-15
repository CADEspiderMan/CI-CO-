from playwright.sync_api import expect

print("==================================================")
print("  综合复习大考：Pytest + Playwright + 智能断言")
print("==================================================")


# 【任务 1】：这个测试函数需要操作网页，请在括号里召唤 Pytest 为你准备好的专属浏览器管家
# 提示：就四个字母
def test_add_todo_item(page):
    """
    测试用例：验证用户能否正常添加一条待办事项
    """

    # 1. 访问我们前两天用过的 TodoMVC 练习网站
    page.goto("https://demo.playwright.dev/todomvc/#/")

    # 2. 找到输入框
    input_box = page.get_by_placeholder("What needs to be done?")

    # 【任务 2】：向输入框填入文字 "拿下大厂Offer"
    input_box.fill("拿下大厂Offer")

    # 【任务 3】：敲击键盘的回车键，把任务添加进去
    # 提示：用到 keyboard 和 "Enter"
    page.keyboard.press("Enter")

    # 3. 准备断言
    # 刚添加进去的任务，页面上肯定会显示 "拿下大厂Offer" 这几个字
    new_item = page.get_by_text("拿下大厂Offer")

    # 【任务 4】：使用 Playwright 的智能断言 expect
    # 请断言这个刚添加的新任务，在页面上是“可见的” (to_be_visible)
    expect(new_item).to_be_visible()

    print("✅ 智能断言通过，Todo添加功能正常！")