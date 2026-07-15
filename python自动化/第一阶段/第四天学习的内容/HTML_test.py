import pytest
import requests


# 定义一个获取环境地址的 Fixture
@pytest.fixture
def env_url():
    """模拟获取测试环境的请求地址"""
    return "https://httpbin.org"


# ===============================================
# 以下是 3 个测试用例
# ===============================================

def test_case_01_success(env_url):
    """
    用例1：测试 GET 请求能够正常返回 200 状态码
    （这条用例预期会通过 ✅）
    """
    print("\n---> 执行用例1：获取正常数据")
    url = f"{env_url}/get"
    response = requests.get(url, params={"test": "hello"})

    # 正常断言
    assert response.status_code == 200
    print("---> 用例1：通过！")


def test_case_02_fail_demo(env_url):
    """
    用例2：故意制造失败的用例！
    （这条用例一定会失败 ❌，这样你生成的报告才会好看，有红有绿）
    """
    print("\n---> 执行用例2：模拟一个 Bug 的产生")
    url = f"{env_url}/status/500"  # 请求一个必定返回 500 服务器错误的接口
    response = requests.get(url)

    actual_code = response.status_code

    # 故意要求它等于 200，它实际是 500，所以这里一定会断言失败报错！
    assert actual_code == 200, f"发现严重 Bug！预期状态码是200，但服务器实际返回了 {actual_code}"


def test_case_03_post_success(env_url):
    """
    用例3：测试 POST 请求功能
    （这条用例预期会通过 ✅）
    """
    print("\n---> 执行用例3：测试提交数据")
    url = f"{env_url}/post"
    payload = {"username": "tester", "role": "admin"}
    response = requests.post(url, json=payload)

    assert response.status_code == 200

    # 解析数据并断言
    res_dict = response.json()
    assert res_dict['json']['role'] == "admin", "身份权限校验失败"
    print("---> 用例3：权限校验通过！")