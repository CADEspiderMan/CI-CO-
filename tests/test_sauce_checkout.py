import pytest
from playwright.sync_api import expect


class LoginPage:
    def __init__(self , page):
        self.page = page
        self.url = "https://www.saucedemo.com/"
        self.username = self.page.locator("#user-name")
        self.password = self.page.locator("#password")
        self.login_btn = self.page.locator("#login-button")
    def navigate(self):
        self.page.goto(self.url)

    def do_login(self , username , password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

class InventoryPage:
    def __init__(self , page):
        self.page = page
        self.backpack_btn = self.page.locator("#add-to-cart-sauce-labs-fleece-jacket")
        self.cart_badge = self.page.locator(".shopping_cart_link")

    def add_backpack_cart_btn(self):
        self.backpack_btn.click()
        self.cart_badge.click()

class checkoutPage:
    def __init__(self , page):
        self.page = page
        self.checkout_btn = self.page.locator("#checkout")
        self.first_name = self.page.locator("#first-name")
        self.last_name = self.page.locator("#last-name")
        self.postal_code = self.page.locator("#postal-code")
        self.continue_btn = self.page.locator("#continue")
        self.title_label = self.page.locator(".title")

    def do_checkout(self , f_name , l_name , postal_code):
        self.checkout_btn.click()
        self.first_name.fill(f_name)
        self.last_name.fill(l_name)
        self.postal_code.fill(postal_code)
        self.continue_btn.click()


def test_shopping_cart_page(page):
    print("1:实例化对象...")
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = checkoutPage(page)

    print("2:打开网页并登录...")
    login_page.navigate()
    login_page.do_login("standard_user" , "secret_sauce")

    print("3:登录成功，将物品放入购物车中...")
    inventory_page.add_backpack_cart_btn()

    print("4:写入收货信息...")
    checkout_page.do_checkout("San" , "Zhang" , "100000")
    print("4:智能断言...")
    expect(checkout_page.title_label).to_have_text("Checkout: Overview")











