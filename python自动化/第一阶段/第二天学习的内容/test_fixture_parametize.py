import pytest
import pandas as pd
import requests

print("==================================================")
print("  三天阶段大考：从零构建企业级数据驱动测试")
print("==================================================")

# ==========================================
# 1. 测试数据准备 (老师仅提供模拟 Excel 数据)
# ==========================================
data = {
    'case_id': ['Cart_01', 'Cart_02', 'Cart_03'],
    'goods_name': ['MacBook Pro', 'iPhone 15', 'AirPods'],
    'expected_code': [200, 200, 200]
}
df = pd.DataFrame(data)

url = "https://httpbin.org/post"

# ==========================================
# 2. 请在下方开始你的全代码编写！
# ==========================================
# 【挑战清单】
# [ ] 1. 将 df 转换为字典列表 test_cases
# [ ] 2. 定义一个 fixture，名为 login_token，打印前置信息，并 yield 一个字符串 "super_token_999"
# [ ] 3. 使用 parametrize 将 test_cases 注入测试函数
# [ ] 4. 定义测试函数 test_add_cart()，接收 fixture 和 单条 case 数据
# [ ] 5. 提取 case 数据，将 goods_name 和 login_token 组装成 payload
# [ ] 6. 发送 POST 请求
# [ ] 7. 第一重断言：实际状态码 == expected_code
# [ ] 8. 第二重断言：返回的 json 里的 goods_name 是否与发送的一致

# 👇 大神，请开始你的表演：

test_cases = df.to_dict(orient='records')


@pytest.fixture
def login_token():
    print("\n[前置操作] 正在生成测试用户的登录Token...")
    yield "super_token_999"  # 老师修改1：这里必须是字符串，要加上双引号
    print("\n[后置操作] 测试完成，清理Token释放资源...")


# 🌟 老师修改核心：将 Fixture 和 参数化 完美结合！
@pytest.mark.parametrize("data", test_cases)
def test_add_cart(login_token, data):  # <--- 看这里！两个参数同时放进括号里！

    # 1. 从 data (单行字典) 中提取数据
    case_id = data["case_id"]
    goods_name = data["goods_name"]
    expected_code = int(data["expected_code"])

    print(f"\n---> 开始执行 {case_id}，准备添加商品：{goods_name}")
    print(f"---> 当前使用的Token是：{login_token}")

    # 2. 组装 Payload (老师修改2：字典的键值对必须用冒号 : ，不能用等号 =)
    payload = {
        "goods_name": goods_name,  # 将商品名装进去
    }

    # 3. 发送 POST 请求
    response = requests.post(url, json=payload , hearders = login_token)
    actual_code = response.status_code

    # 4. 第一重断言：先判断网络和服务器状态
    assert actual_code == expected_code, f"状态码错误，预期{expected_code}，实际{actual_code}"

    # 5. 拆解包裹，进行第二重断言
    res_dict = response.json()
    actual_name = res_dict['json']['goods_name']
    assert actual_name == goods_name, f"数据校验失败，预期为{goods_name}，实际为{actual_name}"