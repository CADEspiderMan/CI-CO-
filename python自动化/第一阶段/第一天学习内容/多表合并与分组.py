# import pandas as pd
#一、连接多个表格（pd.concat）
# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})      #A为
# df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
# df3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})
# df4 = pd.DataFrame({'A': [13, 14], 'E': [15, 16]})
# print("--- 原始 DataFrame ---")
# print("df1:\n", df1)
# print("df2:\n", df2)
# print("df3:\n", df3)
# print("df4:\n", df4)
# print("-" * 30)
# 示例 1: 行拼接 (axis=0, 默认)
# 默认情况下，索引会保留，可能导致重复
# result1 = pd.concat([df1,df2])
# print("行拼接后为:")
# print("result1:\n", result1)

# 示例 2: 行拼接并重置索引
# 使用 ignore_index=True 创建一个新的连续索引
# result_concat_0_reset_index = pd.concat([df1, df2], ignore_index=True)
# print("示例 2: 行拼接并重置索引 (pd.concat([df1, df2], ignore_index=True))")
# print(result_concat_0_reset_index)
# print("-" * 30)
# # 示例 3: 列拼接 (axis=1)
# # 默认按索引匹配，如果索引不完全相同，不匹配的部分会填充 NaN
# result_concat_1 = pd.concat([df1, df3], axis=1)
# print("示例 3: 列拼接 (pd.concat([df1, df3], axis=1))")
# print(result_concat_1)
# print("-" * 30)
# s1 = pd.Series([100, 200], name='S')
# result_concat_series_df = pd.concat([df1, s1], axis=1)
# print("示例 6: Series 和 DataFrame 的列拼接 (pd.concat([df1, s1], axis=1))")
# print(result_concat_series_df)
# print("-" * 30)

# ```python
# import pandas as pd
#
# # 创建示例 DataFrame
# employees_df = pd.DataFrame({
#     'employee_id': [101, 102, 103, 104],
#     'name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'department_id': [1, 2, 1, 3]
# })
#
# departments_df = pd.DataFrame({
#     'department_id': [1, 2, 4],
#     'department_name': ['HR', 'IT', 'Marketing']
# })
#
# sales_df = pd.DataFrame({
#     'employee_id': [101, 103, 105],
#     'sales_amount': [1000, 1500, 2000]
# })

# print("--- 原始 DataFrame ---")
# print("employees_df:\n", employees_df)
# print("departments_df:\n", departments_df)
# print("sales_df:\n", sales_df)
# print("-" * 30)

# 示例 1: 基本内连接 (默认行为)
# 合并 employees_df 和 departments_df，基于 'department_id'
# result_merge_inner = pd.merge(employees_df, departments_df, on='department_id')
# print("示例 1: 基本内连接 (pd.merge(employees_df, departments_df, on='department_id'))")
# print(result_merge_inner)
# print("-" * 30)

#   左连接（how = 'left'）
# result_left = pd.merge(employees_df , departments_df , on = 'department_id' , how = 'left')
# print("示例 2: 左连接 (pd.merge(employees_df, departments_df, on='department_id', how='left'))")
# print(result_left)
# print("-" * 30)
# #   右连接（how = 'right'）
# result_right = pd.merge(employees_df , departments_df , on = 'department_id' , how = 'right')
# print("示例 3: 右连接 (pd.merge(employees_df, departments_df, on='department_id', how='right'))")
# print(result_right)
# print("-" * 30)
# #   外连接（how = "outer"）
# result_outer = pd.merge(employees_df , departments_df , on = 'department_id' , how = 'outer')
# print("示例 4: 外连接 (pd.merge(employees_df, departments_df, on='department_id', how='outer'))")
# print(result_outer)
# print("-" * 30)

#   重命名('表名'.rename(columns = {'原名' : '新名' )})
# sales_df_renamed = sales_df.rename(columns={'employee_id' : 'emp_id'})
#   基于不同列名的合并（left_on = '' , right_on = ''）
# result_left_right = pd.merge(employees_df , sales_df_renamed , left_on = 'employee_id' , right_on = 'emp_id', how = 'left')
# print("示例 5: 基于不同列名的合并 (pd.merge(..., left_on, right_on))")
# print(result_left_right)
# print("-" * 30)

#   处理列名冲突 (suffixes = ('_left' , '_right'))
# df_a = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
# df_b = pd.DataFrame({'key': ['A', 'C'], 'value': [3, 4]})
# result_merge_suffixes = pd.merge(df_a, df_b, on='key', how='outer', suffixes= ('_left', '_right'))
# print("示例 6: 处理列名冲突 (suffixes)")
# print(result_merge_suffixes)
# print("-" * 30)

# 3. groupby - 数据透视表功能

import pandas as pd

# 创建示例 DataFrame
data = {
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Food', 'Clothing', 'Food'],
    'Sales': [100, 150, 200, 50, 120, 80],
    'Quantity': [1, 2, 1, 1, 1, 2]
}
df = pd.DataFrame(data)

# print("--- 原始 DataFrame ---")
# print(df)
# print("-" * 30)

# 示例 1: 单列分组并求和     df.groupby('  ')["  "].sum()
# 按照 'City' 分组，计算每个城市的总销售额
# result_groupby_city_sum = df.groupby('City')["Sales"].sum()
# print(f"每个城市的总销售额为:{result_groupby_city_sum}")
# print("-" * 30)

# 示例 2: 单列分组并计算多个聚合统计量      agg([' ' , ' ' , ' '])
# 按照 'City' 分组，计算每个城市的销售额平均值、最大值和计数    mean ,  max , count
result_groupby_city_all = df.groupby("City")['Sales'].agg(['mean' , 'max' , 'count'])
print(f"每个城市的销售额平均值、最大值和计数为:\n{result_groupby_city_all}")
print("-" * 30)


# **pd.concat:**
# *   用于垂直（`axis=0`）或水平（`axis=1`）拼接 DataFrame 或 Series。
# *   `ignore_index=True` 用于生成新的连续索引。
# *   `join` 参数控制不同列的处理方式（`'outer'` 默认，保留所有；`'inner'` 保留共同列）。
#
# **pd.merge:**
# *   用于通过一个或多个键（列）组合两个 DataFrame 的行。
# *   `on` 参数指定合并键。
# *   `how` 参数指定合并类型：
#     *   `'inner'` (默认): 只保留两个 DataFrame 中键值都存在的行。
#     *   `'left'`: 保留左侧 DataFrame 的所有行。
#     *   `'right'`: 保留右侧 DataFrame 的所有行。
#     *   `'outer'`: 保留两个 DataFrame 中的所有行。
# *   `left_on`, `right_on`: 当左右 DataFrame 的合并键列名不同时使用。
# *   `suffixes`: 处理合并后相同列名的冲突。
#
# **groupby:**
# *   实现“分割-应用-合并”策略，功能类似数据透视表。
# *   **分割：** `df.groupby('列名')` 或 `df.groupby(['列名1', '列名2'])`。
# *   **应用：** 对分组后的数据应用聚合函数（`sum()`, `mean()`, `count()`, `agg()` 等）。
# *   **转换：** `transform()` 对组内数据进行转换，返回与原 DataFrame 相同形状的 Series/DataFrame。
# *   **过滤：** `filter()` 根据组的属性过滤整个组。