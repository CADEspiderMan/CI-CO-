import pytest
from playwright.sync_api import expect

print("==================================================")
print("  第三阶段毕业设计：Swag Labs 电商全链路自动化")
print("==================================================")


# =======================================================
# 📦 页面层一：登录页面 (LoginPage)
# =======================================================
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"

        # 【任务 1：集中管理元素】
        # 提示：打开该网站按 F12，你会发现账号框 id="user-name"，密码框 id="password"，按钮 id="login-button"
        self.username_input = self.page.locator("#user-name")  # 老师修改：ID定位前面要加 #
        self.password_input = self.page.locator("#password")  # 老师修改：ID定位前面要加 #
        self.login_btn = self.page.locator("#login-button")  # 老师修改：ID定位前面要加 #

    def navigate(self):
        self.page.goto(self.url)

    def do_login(self, username, password):
        """【任务 2：封装登录动作】"""
        # TODO: 使用上面的元素，完成 输入账号 -> 输入密码 -> 点击登录 的动作
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()  # 老师修改：既然找了登录按钮，直接 click() 点它最稳妥！


# =======================================================
# 📦 页面层二：商品列表页面 (InventoryPage)
# =======================================================
class InventoryPage:
    def __init__(self, page):
        self.page = page

        # 【任务 3：定位加购按钮和购物车角标】
        # 提示1：背包的加购按钮的 id 是 "add-to-cart-sauce-labs-backpack"
        # 提示2：右上角那个显示数字的小红点(购物车角标)，它的 class 是 "shopping_cart_badge"
        self.add_backpack_btn = self.page.locator("#add-to-cart-sauce-labs-backpack")  # 老师修改：ID定位前面加 #
        self.cart_badge = self.page.locator(".shopping_cart_badge")  # 老师修改：class定位前面加小数点 .

    def add_backpack_to_cart(self):
        """点击加入购物车按钮"""
        self.add_backpack_btn.click()


# =======================================================
# 🧪 测试层：测试用例
# =======================================================
def test_shopping_cart_flow(page):
    """测试用户登录并成功将商品加入购物车"""

    print("\n▶️ 1. 实例化页面对象...")
    # TODO: 实例化 LoginPage 和 InventoryPage 两个对象
    login_page = LoginPage(page)  # 老师修改：等号旁边加个空格更规范
    inventory_page = InventoryPage(page)

    print("▶️ 2. 打开网页并登录...")
    # TODO: 调用 login_page 的方法打开网页，并使用 "standard_user" 和 "secret_sauce" 登录
    login_page.navigate()  # 老师修改：拼写错误 novigate -> navigate
    login_page.do_login("standard_user", "secret_sauce")  # 老师修改：对象名叫 login_page；账号密码必须是字符串，要加双引号

    print("▶️ 3. 登录成功，将背包加入购物车...")
    # TODO: 调用 inventory_page 的方法，将背包加入购物车
    inventory_page.add_backpack_to_cart()  # 老师修改：修正拼写错误 sinnventory_page

    print("⏳ 4. 终极智能断言！...")
    # 【任务 4：完成终极断言】
    # 预期：点击加购后，右上角的购物车红点里面应该包含文本 "1"
    # 请使用 expect 进行智能断言
    # TODO: 填入断言代码
    expect(inventory_page.cart_badge).to_have_text("1")  # 老师修改：修正 expect 和变量名的拼写，并使用 to_have_text("1")
    print("✅ 恭喜！第三阶段电商全链路自动化毕业！")