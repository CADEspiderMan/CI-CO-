import pytest


# ----------------- 步骤 1：定义数据库 Fixture -----------------

# 【任务 1】：给下面的函数戴上 Fixture 魔法帽子
# ---- 请补全下方代码 ----
@pytest.fixture
def db_connection():
    """
    模拟连接数据库的 Fixture，前后置清理的好帮手
    """
    print("\n[DB前置] 🚀 正在建立数据库连接...")

    # 模拟一个数据库对象（字典）
    mock_db = {"status": "connected", "db_name": "ecommerce_test"}
    print(f"[DB前置] 数据库 {mock_db['db_name']} 连接成功！")

    # 【任务 2】：使用魔法关键字交出 mock_db，并在此暂停
    # ---- 请补全下方代码 ----
    yield mock_db

    # ---------------------------------------------------------
    # 等测试用例执行完毕后，会回到下面继续执行断开连接的操作
    print("\n[DB后置] 🛑 测试结束，正在断开数据库连接...")
    print("[DB后置] 数据库已安全释放。")


# ----------------- 步骤 2：在多个测试用例中使用 Fixture -----------------

# 【任务 3】：在测试用例括号中召唤 Fixture
# ---- 请补全下方代码 ----
def test_query_order(db_connection):
    """测试用例 1：查询订单"""
    print(f"\n---> [用例 1] 开始执行业务逻辑：查询订单")

    # 【任务 4】：用一个变量接住传进来的数据库对象
    # 提示：括号里叫什么，这里就用什么名字接收
    db = db_connection
    print(f"---> [用例 1] 检查当前数据库状态：{db['status']}")

    # 断言数据库是否真的连上了
    assert db['status'] == "connected", "数据库竟然没连上！"


# 【任务 5】：给第二个用例也安排上同样的 Fixture
# ---- 请补全下方代码 ----
def test_create_order(db_connection):
    """测试用例 2：创建新订单"""
    print(f"\n---> [用例 2] 开始执行业务逻辑：创建新订单")

    # 提取传进来的数据库名字并断言
    db = db_connection
    print(f"---> [用例 2] 数据将写入数据库：{db['db_name']}")

    assert db['db_name'] == "ecommerce_test", "连错数据库啦，数据写错地方了！"