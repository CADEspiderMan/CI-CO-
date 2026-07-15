import jsonpath

print("==================================================")
print("  第六天实战：JSONPath 复杂数据解剖手术")
print("==================================================")

# 假设这是你用 requests.get() 跑完接口后，用 .json() 转换得到的一个超复杂字典
mock_response_data = {
    "code": 200,
    "message": "获取用户详情成功",
    "data": {
        "user_info": {
            "uid": "U_888999",
            "nickname": "测试狂魔",
            "vip_level": 3
        },
        "order_list": [
            {
                "order_id": "OD-001",
                "product_name": "机械键盘",
                "price": 399.0,
                "status": "已发货"
            },
            {
                "order_id": "OD-002",
                "product_name": "人体工学鼠标",
                "price": 129.0,
                "status": "待付款"
            },
            {
                "order_id": "OD-003",
                "product_name": "高刷显示器",
                "price": 1999.0,
                "status": "已完成"
            }
        ]
    }
}

print("\n--- 任务 1：提取用户的 VIP 等级 ---")
# 传统的噩梦写法：
tradition_vip = mock_response_data["data"]["user_info"]["vip_level"]
print(f"传统写法取出的VIP等级: {tradition_vip}")

# 请用 jsonpath 写法提取 vip_level
# 提示：层级是 根节点 -> data -> user_info -> vip_level
# 返回的是个列表，记得加 [0] 取出来
jp_vip_list = jsonpath.jsonpath(mock_response_data, "$data.user_info.vip_level")  # 【填空 1】在这里填入表达式
jp_vip = jp_vip_list[0]
print(f"JSONPath 取出的VIP等级: {jp_vip}")

print("\n--- 任务 2：提取第二个订单的商品名称 ---")
# 请提取出 "人体工学鼠标" 这个字符串
# 提示：根节点 -> data -> order_list -> 第2个元素(索引为1) -> product_name
jp_product_list = jsonpath.jsonpath(mock_response_data, "$..product_name")  # 【填空 2】在这里填入表达式
print(f"提取到的第二个商品名: {jp_product_list[0]}")

print("\n--- 任务 3：暴力开采！一次性提取所有订单价格 ---")
# 我们不管层级有多深，请用终极必杀技 `..` 把名字叫 price 的数据全部提取出来！
all_prices = jsonpath.jsonpath(mock_response_data, "$..price")  # 【填空 3】在这里填入表达式
print(f"提取到的所有价格: {all_prices}")

# 结合断言实战：
print("\n--- 任务 4：高阶多重断言 ---")
try:
    # 1. 基础状态码断言
    assert mock_response_data["code"] == 200, "接口状态码报错"

    # 2. 复杂业务断言：检查这个人到底有没有买过那台 "高刷显示器"？
    # 思路：先用 $..product_name 把所有商品名捞出来，然后判断 "高刷显示器" 在不在这个列表里！
    all_products = jsonpath.jsonpath(mock_response_data, "$..product_name")

    assert "高刷显示器" in all_products, "该用户没有购买过高刷显示器！"

    print("✅ 所有断言通过！这才是企业级的多重断言！")
except AssertionError as e:
    print(f"❌ 测试失败：{e}")