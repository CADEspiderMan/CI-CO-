import pytest
from playwright.sync_api import expect

print("==================================================")
print("  大厂架构实战：PO (Page Object) 设计模式重构")
print("==================================================")


# =======================================================
# 📦 第一部分：页面层 (Page Class) - 只管元素和动作，不管断言
# =======================================================
class TodoPage:
    def __init__(self, page):
        """
        ⭐ 新知识点 1：把 page 管家交给类
        把 pytest 传进来的 page 对象，绑定到 self.page 上，
        这样这个类里的所有方法（函数）都能使用浏览器了。
        """
        self.page = page
        self.url = "https://demo.playwright.dev/todomvc/#/"

        """
        ⭐ 新知识点 2：元素定位前置化 (集中管理)
        以前我们是用到的时候再去写 locator。在 PO 模式中，
        我们要在初始化时就把页面上所有的元素“身份证”找好，存成类的属性 (self.xxx)。
        这样以后即使界面改了，也只需要修改这里的一处代码！
        """
        self.new_todo_input = self.page.get_by_placeholder("What needs to be done?")
        self.todo_items = self.page.locator(".todo-list li")

    def navigate(self):
        """打开该页面的专属动作"""
        self.page.goto(self.url)

    def add_todo(self, task_name):
        """
        ⭐ 新知识点 3：封装业务动作
        这个方法将“输入文字”和“敲回车”这两个零碎的动作，
        打包成了一个高级的业务动作：添加待办 (add_todo)。
        测试人员调用时，根本不需要知道底层是怎么按键盘的。
        """
        self.new_todo_input.fill(task_name)
        self.page.keyboard.press("Enter")


# =======================================================
# 🧪 第二部分：测试层 (Test Case) - 负责传数据、调用页面、写断言
# =======================================================

def test_add_todo_with_po(page):
    """
    使用 PO 模式重构后的测试用例
    """
    print("\n▶️ 开始执行 PO 模式的测试用例...")

    # ⭐ 新知识点 4：类的实例化
    # 用 TodoPage 图纸，造出一个真正的页面对象，并把 page 管家塞给它
    todo_page = TodoPage(page)

    # 2. 调用页面的动作：打开网页
    todo_page.navigate()

    # ⭐ 新知识点 5：像说话一样写代码 (解耦)
    # 看这行代码：页面.添加任务("搞定PO模式")。
    # 完全看不到恶心的 CSS 或 XPath 定位器，代码可读性直接拉满！
    todo_page.add_todo("搞定PO模式")

    # ⭐ 新知识点 6：断言只在测试层做
    # 注意：TodoPage 类里面没有任何 assert 或 expect。
    # 断言是裁判干的活，页面对象只是运动员。必须把判断对错的逻辑留在 test_ 里面！
    print("⏳ 正在进行智能断言...")
    expect(todo_page.todo_items).to_contain_text("搞定PO模式")

    print("✅ 断言通过！代码重构极其完美！")