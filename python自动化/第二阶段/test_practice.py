import pytest
import requests
import sqlite3
import jsonpath

print("==================================================")
print("  🏆 第二阶段大考：API 自动化全链路闭环")
print("==================================================")


# =======================================================
# 📦 任务 1：数据库 Fixture 配置
# =======================================================
@pytest.fixture
def db_cursor():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # 建立用户表，初始状态为 "未激活"
    cursor.execute('''CREATE TABLE users
                      (
                          id     INT,
                          status TEXT
                      )''')
    cursor.execute('''INSERT INTO users
                      VALUES (1001, "未激活")''')
    conn.commit()

    # 【TODO 1】：使用魔法关键字把 cursor 游标交出去，并在这里暂停
    # 在下面写你的代码：
    yield cursor

    cursor.close()
    conn.close()


# =======================================================
# 🧪 任务 2-5：全链路测试用例
# =======================================================
def test_buy_vip_process(db_cursor, requests_mock):
    print("\n▶️ 1. 布置支付宝假基站...")
    alipay_url = "https://api.alipay.com/pay"

    # 【TODO 2】：使用 requests_mock 拦截上面的 alipay_url 的 POST 请求
    # 强制让它返回 status_code=200
    # 在下面写你的代码：
    requests_mock.post(alipay_url, status_code=200)

    print("▶️ 2. 带着 Token 请求购买接口...")
    shop_url = "https://api.shop.com/buy_vip"

    # 【TODO 3】：准备好请求头字典，携带 Bearer Token
    # 提示：键是 "Authorization"，值是 "Bearer super_vip_123"
    # 在下面写你的代码：
    header_dict = {
        "Authorization": "Bearer super_vip_123"
    }

    # 为了模拟后端，这里用 mock 造一个复杂的嵌套返回数据（模拟请求商品接口得到的数据）
    complex_data = {
        "code": 200,
        "data": {
            "order_info": {
                "order_id": "8888",
                "privilege": {"vip_level": "SVIP", "expire": "2099-01-01"}
            }
        }
    }
    requests_mock.get(shop_url, json=complex_data)

    # 真正发起 GET 请求！记得带上你刚才写的 headers
    # 在下面补充完整：
    # response = requests.get(shop_url, ___________)
    response = requests.get(shop_url, json=complex_data, headers=header_dict)

    print("▶️ 3. 拆快递并使用 JSONPath 提取数据...")
    res_dict = response.json()

    # 【TODO 4】：用 jsonpath 的双点号语法，直接挖出 "vip_level"
    # 在下面写你的代码 (提取出来是个列表，记得取第0个元素)：
    test_vip = jsonpath.jsonpath(res_dict, "$..vip_level")

    # 断言提取出来的 vip 等级是 SVIP
    # assert _________ == "SVIP"
    assert test_vip[0] == "SVIP"

    print("▶️ 4. 深入底层，进行数据库终极断言...")
    # 模拟后端代码成功执行后修改了数据库
    db_cursor.execute('''UPDATE users
                         SET status = "已激活"
                         WHERE id = 1001''')

    # 【TODO 5】：用游标执行 SQL 查询，查出 id 为 1001 的 status
    # 捞出数据，并断言状态是否等于 "已激活"
    # 在下面写你的代码：

    db_cursor.execute("SELECT status FROM users WHERE id = 1001")
    db_result = db_cursor.fetchone()
    assert db_result[0] == "已激活", "数据库中的状态更新失败！"

    print("✅ 恭喜！五项绝技全部通关，第二阶段完美毕业！")
