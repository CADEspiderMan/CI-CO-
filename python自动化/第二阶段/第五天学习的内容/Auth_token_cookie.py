import pytest
import requests

print("==================================================")
print("  第五天实战：Token 与 Cookie 鉴权")
print("==================================================")


def test_token_auth():
    """
    实战 1：使用 Bearer Token 访问受保护的接口
    """
    print("\n▶️ 1. 准备请求带锁的接口...")
    url = "https://httpbin.org/bearer"

    # 假设你刚刚调用登录接口，拿到了一个超级 Token
    fake_token = "abc_123_super_secret_token"

    # 【任务 1】：构造请求头 (Headers)
    # 根据大厂行规，键必须是 "Authorization"
    # 值必须是 "Bearer " 加上你的 Token（注意 Bearer 后面有一个空格！）
    headers_dict = {
        # TODO: 填入正确的键值对
        "Authorization": f"Bearer {fake_token}"
    }

    # 【任务 2】：发送请求并携带 headers
    # 请在 get 方法中，把刚刚准备好的 headers_dict 传给专属的 headers 参数
    response = requests.get(url, headers=headers_dict)

    # 智能断言
    actual_code = response.status_code
    assert actual_code == 200, f"Token验证失败！返回码是：{actual_code}"

    print("✅ Token 鉴权成功！服务器承认了你的身份！")
    print("服务器返回的数据：", response.json())


def test_cookie_auth():
    """
    实战 2：使用 Cookie 访问受保护的接口
    """
    print("\n▶️ 2. 准备请求需要 Cookie 的接口...")
    # 这个接口的规则是：如果你的 Cookie 里面有 k1=v1，它就会正常返回
    url = "https://httpbin.org/cookies"

    # 准备好你的 Cookie 字典
    my_cookies = {
        "user_session_id": "88889999",
        "k1": "v1"
    }

    # 【任务 3】：发送请求并携带 cookies
    # 请在 get 方法中，把 my_cookies 传给专属的 cookies 参数
    response = requests.get(url, cookies=my_cookies)

    actual_code = response.status_code
    assert actual_code == 200, f"Cookie验证失败！返回码是：{actual_code}"

    print("✅ Cookie 鉴权成功！服务器收到了你的饼干！")
    print("服务器返回的数据：", response.json())