import pytest
import sqlite3
import requests


# =======================================================
# 👨‍🔧 仓库管理员 (Fixture)
# =======================================================
@pytest.fixture
def db_cursor():
    # 1. 打开仓库大门 (连接数据库)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # 准备初始数据：存入 10 台 iPhone
    cursor.execute('''CREATE TABLE products
                      (
                          id    INT,
                          name  TEXT,
                          stock INT
                      )''')
    cursor.execute('''INSERT INTO products
                      VALUES (1, "iPhone", 10)''')
    conn.commit()

    # 【填空 1：把手电筒交出去，并在这里暂停等候】
    # 提示：使用 yield 关键字把 cursor 交给测试用例
    # TODO: 在下一行写代码
    yield cursor

    # 4. 测试结束后，收回手电筒，关上大门
    cursor.close()
    conn.close()


# =======================================================
# 🕵️‍♂️ 质检员 (测试用例)
# =======================================================
def test_buy_iphone(db_cursor, requests_mock):
    # 模拟 API 告诉前端：购买成功！
    target_url = "http://api.shop.com/buy"
    requests_mock.post(target_url, json={"msg": "购买成功"})

    res = requests.post(target_url)
    assert res.json()["msg"] == "购买成功"
    print("✅ API 表面上说购买成功了。")

    # (模拟后端底层代码去扣减了库存)
    db_cursor.execute("UPDATE products SET stock = 9 WHERE id = 1")

    print("▶️ 开始深入仓库，查明真相...")

    # 【填空 2：拿手电筒照向货架 (执行SQL)】
    # 请让 db_cursor 执行 (execute) 以下 SQL 语句：
    # "SELECT stock FROM products WHERE id = 1"
    # TODO: 在下一行写代码
    db_cursor.execute("SELECT stock FROM products WHERE id = 1")

    # 【填空 3：让机器人把数据装在盒子里拿过来】
    # 提示：调用捞取第一条数据的方法 fetchone()，并赋值给变量 result
    # TODO: 在下一行写代码
    result = db_cursor.fetchone()

    print(f"📦 拿到了数据库返回的快递盒：{result}")
    # 此时打印出来绝对是 (9,) 这样的元组！

    # 【填空 4：拆快递盒进行终极断言！】
    # 断言：取出 result 里面的第 0 个数据，判断它是否等于数字 9
    # TODO: 在下一行写代码
    assert result[0] == 9

    print("✅ 数据库库存确实变成了 9，测试完美闭环！")
    # # 步骤 1：建立连接通道 (Connection)
    # conn = sqlite3.connect("my_database.db")
    #
    # # 步骤 2：生成游标 (Cursor) —— 相当于帮你敲 SQL 的“鼠标光标”
    # cursor = conn.cursor()
    #
    # # 步骤 3：让游标执行 SQL 语句并拿回数据
    # cursor.execute("SELECT status FROM orders WHERE id='888'")
    # result = cursor.fetchone()  # fetchone() 意思是：把查到的第一条数据捞出来
    #
    # # 用完关闭通道！
    # conn.close()