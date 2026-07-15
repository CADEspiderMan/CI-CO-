import requests

print("===========================================")
print("  第一步：搞懂 params (GET请求的附加条件)")
print("===========================================")

# 目标：查询广州，未来3天的天气
url_get = "https://httpbin.org/get"

# params 就是你的“查询条件”，把它写成字典
my_params = {
    "city": "Guangzhou",
    "days": 3
}

# 发送 GET 请求，把条件塞给 params
response_get = requests.get(url_get, params=my_params)

# 我们可以打印一下最终实际发出去的 URL 到底长什么样
print(f"1. 实际请求的完整URL是: {response_get.url}")
# 你会发现，requests 自动帮我们拼成了：https://httpbin.org/get?city=Guangzhou&days=3


print("\n===========================================")
print("  第二步：搞懂 json= 和 .json() (POST请求与数据解析)")
print("===========================================")

# 目标：模拟登录，提交账号密码
url_post = "https://httpbin.org/post"

# 这是你在本地准备好的 Python 字典（你的表单数据）
my_login_data = {
    "username": "test_user",
    "password": "123456"
}

# 发送 POST 请求。使用 json= 参数，把 Python 字典打包成 JSON 发给服务器
response_post = requests.post(url_post, json=my_login_data)
print(f"2. 登录请求的HTTP状态码是: {response_post.status_code} (200代表成功)")

# 【重点来了：拆快递 .json()】
# 服务器返回的数据是纯文本，我们要调用 .json() 方法把它变成 Python 字典！
res_dict = response_post.json()

print("3. 服务器返回的完整字典数据是:")
print(res_dict)
print(f"数据类型是: {type(res_dict)}")  # 会显示 <class 'dict'>

# 变成字典后，提取数据就太简单了！
# httpbin 网站会把我们提交的数据放在一个叫 "json" 的键里面返回
extracted_username = res_dict["json"]["username"]
print(f"4. 我们从返回结果中提取出来的用户名是: {extracted_username}")

print("\n===========================================")
print("  第三步：加入断言 (Assert)，变成真正的测试用例")
print("===========================================")

try:
    print("开始执行自动化测试断言...")

    # 1. 断言状态码是不是 200
    assert response_post.status_code == 200, "状态码不对，请求可能失败了！"

    # 2. 断言服务器返回的数据中，用户名是不是我们刚才提交的 "test_user"
    assert res_dict["json"]["username"] == "test_user", "用户名校验失败！"

    print("✅ 恭喜！所有断言通过，测试用例执行成功！")

except AssertionError as e:
    # 如果上面的 assert 后面的条件不成立，就会跳转到这里
    print(f"❌ 测试用例执行失败，原因是：{e}")