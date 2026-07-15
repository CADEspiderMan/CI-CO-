import pytest
import pandas as pd
import requests

data = {
    'case_id' : ['search_01' , 'search_02' , 'search_03'],
    'keyword' :['python工具' , '键盘' , ''],
    'expected_word' : ['200' , '200' , '400']
}
df = pd.DataFrame(data)
test_case = df.to_dict(orient = 'records')
url = 'http://httpbin.org/post'

@pytest.mark.parametrize("case_data" , test_case)
def test_case_data(case_data):
    case_id = case_data['case_id']
    keyword = case_data['keyword']
    expected_code = int(case_data['expected_word'])
    print(f"\n▶️ [厂长发车] 开始执行 {case_id}，搜索词：'{keyword}'")

    payload = {
        "query_word": keyword
    }
    response = requests.post(url , json = payload)
    actual_code = response.status_code
    assert actual_code == expected_code, f"状态码错误！预期 {expected_code}，实际 {actual_code}"
    res_dict = response.json()
    actual_keyword = res_dict['json']['query_word']
    assert actual_keyword == keyword, f"数据丢失！实际返回 '{actual_keyword}'"