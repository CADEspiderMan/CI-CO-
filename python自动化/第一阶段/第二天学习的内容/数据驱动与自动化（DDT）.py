import pandas as pd
import requests

print("==================================================")
print("  实战：Pandas 数据驱动 + Requests + 异常处理整合")
print("==================================================")

# ----------------- 步骤 1：模拟数据准备 -----------------
# 这里模拟你用 Pandas 读取了一个 Excel 文件
# 里面有3条测试用例：第1条是正确的，第2条账号错了，第3条我们要测试它是否预期报错(401)
data = {
    'case_id': ['T01', 'T02', 'T03'],
    'test_username': ['admin_correct', 'wrong_user', 'admin_correct'],
    'test_password': ['123456', '123456', 'error_pwd'],
    'expected_status_code': [503, 401, 401] # 预期结果：第一条成功，后两条我们预期它会失败
}
df = pd.DataFrame(data)

# 【核心教学点】：将 DataFrame 转换为装满字典的列表
test_cases = df.to_dict(orient='records')       #df.to_dict(orient='records)   这个是将excel表格式改变为字典模式
# print("模拟的 Excel 数据已准备好：")
# print(test_cases)
# print("--------------------------------------------------\n")
url = "https://httpbin.org/post"

#开始遍历循环(数据驱动)       核心部分
for case in test_cases:     #case 则是每次循环取出来的一个“小字典"
    #   下面的数据是固定的
    case_id = case['case_id']
    expected_status_code = case['expected_status_code']
    print(f"正在执行用例：{case_id}...")
#   下面的数据是可以改变的
    payload = {
        'username' : case['test_username'],
        'password' : case['test_password'],
    }
    try:
        response = requests.post(url, json=payload)     #把字典变为json给服务器
        actual_code = response.status_code  #实际状态码
        assert actual_code == expected_status_code , f"预期结果为：{expected_status_code} , 实际结果为：{actual_code}"
        print(f"  --> ✅ 用例 {case_id} 测试通过！(实际返回码: {actual_code})")

    except AssertionError as e:
    # 如果断言失败了，会被这里的 except 捕获！
        print(f"  --> ❌ 用例 {case_id} 断言失败，原因：{e}")

    except Exception as e:
# 兜底捕获：万一断网了或者其他语法错误
        print(f"  --> ⚠️ 用例 {case_id} 发生未知异常：{e}")

print("- - - - - - - - - - - - - - - - -")

# 全部循环结束
print("\n🏁 所有数据驱动测试执行完毕！")



