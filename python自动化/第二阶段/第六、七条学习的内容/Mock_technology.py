import pytest
import requests

print("==================================================")
print("  第七天实战：Mock 拦截与假数据伪造")
print("==================================================")


def test_mock_alipay_refund(requests_mock):
    """
    实战 1：模拟支付宝退款接口
    在括号里写了 requests_mock，Pytest 就会自动把假基站管家传进来！
    """
    print("\n▶️ 1. 正在布置假基站...")
    target_url = "https://api.alipay.com/refund"

    # 假设我们希望退款成功，支付宝应该返回这个 JSON
    fake_success_response = {
        "code": "10000",
        "msg": "Success",
        "refund_fee": "99.00"
    }

    # 【任务 1】：配置假基站进行拦截
    # 请使用 requests_mock.post() 方法
    # 拦截 target_url，并配置 json=fake_success_response，状态码 status_code=200
    requests_mock.post(
        target_url,
        json=fake_success_response,
        status_code=200
    )

    print("▶️ 2. 发起退款请求 (实际上会被拦截)...")
    # 这里我们正常发起 requests 请求。
    # 甚至你可以故意断开你电脑的网络，这个请求依然会秒成功！因为它根本没出门！
    response = requests.post(target_url, json={"order_id": "888888"})

    print("▶️ 3. 拆解服务器返回的数据...")
    res_data = response.json()
    print(f"收到的数据是: {res_data}")

    # 断言
    assert res_data["msg"] == "Success"
    assert res_data["refund_fee"] == "99.00"
    print("✅ 退款 Mock 测试通过！")


def test_mock_server_500(requests_mock):
    """
    实战 2：模拟极其难测的服务器 500 崩溃情况
    """
    print("\n▶️ 1. 正在布置让服务器 '崩溃' 的假基站...")
    target_url = "https://my-api.com/get_user"

    # 【任务 2】：配置假基站，模拟 500 错误
    # 请使用 requests_mock.get() 方法拦截 target_url
    # 并强制让它返回状态码 status_code=500，返回文本 text="Internal Server Error"
    requests_mock.get(
        target_url,
        status_code=500,
        text="Internal Server Error"
    )

    print("▶️ 2. 发起查询请求...")
    response = requests.get(target_url)

    # 断言：我们就是期望它报错 500！
    assert response.status_code == 500
    print(f"服务器返回的错误文本是: {response.text}")
    print("✅ 成功模拟了 500 崩溃场景！")