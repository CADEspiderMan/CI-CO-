
import pandas as pd
            #一、pandas基础概念与数据加载
#1、一维数据结构
# s = pd.Series([1,2,3,4,5,6,7] , name = "销售额")
# print(s)

#2、二维数据结构
# data = {
#     "姓名": ["张三" , "李四" , "王五" , "赵六" ],
#     "年龄": ["19" , "37" , "24" , "35" ],
#     "城市": ["杭州" , "广州" , "上海" , "福建" ],
# }
# df = pd.DataFrame(data)  #创建成二维数组来存储到df中
# print("\nDataFrame示例:\n" , df)

# pd.read_csv()   #读取csv文件
df = pd.read_excel(r"E:\study\python\data\学生表.xlsx") #读取excel文件
# try:
#     df = pd.read_excel(r"E:\study\python\data\学生表.xlsx")    #地址前面必须加r
#     print("\n从Excel加载数据:\n", df)
# except FileNotFoundError:
#     print("请确保'学生表.xlsx'文件位于项目根目录.")

# 也可以读取CSV文件 (如果你保存的是csv格式)
# df_csv = pd.read_csv('data.csv')
# print("\n从CSV加载数据:\n", df_csv.head())

#3、数据概览
# print(df.head(3))      #前三行
# print(df.info())       #查看数据类型
# print(df.describe())   #查看统计摘要
# print(df.shape[0] , df.shape[1])        #查看行数和列数




            #二、数据过滤(筛选特定行)
#1.单一条件过滤：
# 筛选出年龄大于等于25岁的人
# df_age_filtered = df[df["年龄"] >= 25]
# print("筛选：年龄大于25的人为：")
# print(df_age_filtered)
# print("-" * 30)
#
#2.多个条件过滤
#（1）AND 关系，用 & 连接
# 筛选出年龄大于25岁 并且 城市是北京的人
df_multi_and_filtered = df[(df["年龄"] > 25) & (df["城市"] == "北京")]
print("筛选：城市是北京并且年龄大于25的人:")
print(df_multi_and_filtered)
print("-" * 30)

#（2）OR 关系，用 | 连接
# 筛选出城市是上海 或者 收入大于10000的人
# df_multi_or_filtered = df[(df['城市'] == '上海') | (df['销售额'] > 100)]
# print("筛选：城市是上海或销售额大于100的人:")
# print(df_multi_or_filtered)
# print("-" * 30)

# 4. 使用 .isin() 方法过滤多个值
# 筛选出城市是北京 或 上海的人
# df_isin_filtered = df[df["城市"].isin(['上海', '北京'])]
# print("筛选：城市是北京 或 上海的人:")
# print(df_isin_filtered)
# print("-" * 30)

# 5. 字符串包含过滤 (针对文本列     使用“.str.contains()”)
# 筛选出姓名中包含“王”的人
# df_str_contains  = df[df["姓名"].str.contains("王" , na=False)]    #nan为忽略值
# print("筛选：姓名中包含'王'的人:")
# print(df_str_contains)
# print("-" * 30)

# 6.  "过滤缺失值 " (            使用.notna()  只能使用空的值)
# 筛选出订单状态“不”为空的行
# df_not_null_income = df[df['订单状态'].notna()]
# print("筛选：订单状态不为空的行:")
# print(df_not_null_income)
# print("-" * 30)

            #三、去重（去除重复项，保留一个实例）
# 注意：drop_duplicates() 默认会返回一个新的 DataFrame，
# 如果想直接修改原 DataFrame，需要添加 inplace=True 参数。

# 1. 去除所有列都完全重复的行 (默认行为)
# df_no_duplicates_all = df.drop_duplicates()
# print("去重：所有列都完全重复的行 (默认保留第一个):")
# print(df_no_duplicates_all)
# print("-" * 30)

# 2. 基于特定列去重
# 假设我们认为只要“姓名”和“城市”相同就认为是重复的，只保留第一个（(subset = [" "])）
# df_no_duplicates_subset = df.drop_duplicates(subset=['销售额', '城市'])
# print("去重：基于'销售额'和'城市'列 (保留第一个):")
# print(df_no_duplicates_subset)
# print("-" * 30)

# 3. 基于特定列去重，并保留最后一个重复项
# 假设我们认为只要“姓名”和“城市”相同就认为是重复的，但想保留最后一个
# df_no_duplicates_keep_last = df.drop_duplicates(subset=['销售额', '城市'], keep='last')  #first:保留第一项 last:保留最后一项 false:全部删除
# print("去重：基于'销售额'和'城市'列 (保留最后一个):")
# print(df_no_duplicates_keep_last)
# print("-" * 30)

# 4. 去除所有重复项 (即如果一个项出现了多次，全部删除，只留下只出现过一次的项)
# 这一操作在 pandas 中通过 keep=False 实现
# df_unique_only = df.drop_duplicates(keep=False)
# print("去重：只保留出现过一次的唯一项 (所有重复项都被删除):")
# print(df_unique_only)
# print("-" * 30)

# 演示 inplace=True (直接修改原 DataFrame)
# df.drop_duplicates(subset=['姓名'], inplace=True)
# print("去重（inplace）：基于'姓名'列直接修改原DataFrame:")
# print(df)
# print("-" * 30)
# inplace=True：如果你希望直接修改原始 DataFrame 而不是创建一个新的 DataFrame，可以使用此参数。


# 关键点：
# subset 参数：指定在哪些列上检查重复项。
# keep 参数：
    # 'first' (默认)：保留第一次出现的重复项。
    # 'last'：保留最后一次出现的重复项。
    # False：删除所有重复项，只保留唯一的行。

            #三、缺失值处理 (填充空白单元格---NaN)
# print(df)   #含有NaN
# print("-" * 30)
# 1. 检测缺失值
# df.isnull() 或 df.isna()：返回一个布尔型 DataFrame，True 表示缺失
# df.notnull() 或 df.notna()：返回一个布尔型 DataFrame，True 表示非缺失
# 统计每列的缺失值数量: df.isnull().sum()    统计整个缺失值数量df.isnull().sum().sum()
# print("检测缺失值 (df.isnull()):")
# print(df.isnull())
# print("-" * 30)

# 2. 填充缺失值 (fillna())
# 注意：fillna() 默认会返回一个新的 DataFrame
# (1)用固定值填充
# df_filled_const = df.copy()     #创建副本
# df_filled_const["订单状态"] = df_filled_const["订单状态"].fillna(0)
# df_filled_const["销售额"] = df_filled_const["销售额"].fillna(1000)
# print("填充缺失值：用固定值填充:")
# print(df_filled_const)
# print("-" * 30)
# 使用 groupby 按部门分组，然后用 transform 计算各部门平均值并填充
# df_data["绩效得分"] = df_data.groupby("部门")["绩效得分"].transform(lambda x: x.fillna(x.mean()))
# (2)用列来计算(均值、中位数、众数)
# df_data = df.copy()
# df_score =df["销售额"].mean()
# df_data["销售额"] = df_data["销售额"].fillna(df_score)
# print("新的表格为：")
# print(df_data)
#  (3)用销售额的中位数填充销售额的NaN      中位数：median()
# median_income = df_filled_stats['销售额'].median()
# df_filled_stats['销售额'] = df_filled_stats['销售额'].fillna(median_income)
# print(df_filled_stats)
# (4)用城市列的众数填充城市的NaN (mode() 返回一个Series，取第一个值)
# mode_city = df_filled_stats['城市'].mode()[0]
# df_filled_stats['城市'] = df_filled_stats['城市'].fillna(mode_city)
# print(df_filled_stats)
# print("-" * 30)

# (5) 用前一个或后一个非缺失值填充 (向前填充 ffill / 向后填充 bfill)
# df_filled_fwd_bwd = df.copy()
# df_filled_fwd_bwd['年龄'].fillna(method='ffill', inplace=True) # 用前一个有效值填充
# df_filled_fwd_bwd['收入'].fillna(method='bfill', inplace=True) # 用后一个有效值填充
# print("填充缺失值：向前填充 (ffill) 和向后填充 (bfill):")
# print(df_filled_fwd_bwd)
# print("-" * 30)


# 3. 删除缺失值 (dropna())

# (1)删除任何包含缺失值的行 (默认行为)
# df_dropped_any_nan_row = df.dropna()
# print("删除缺失值：删除任何包含NaN的行:")
# print(df_dropped_any_nan_row)
# print("-" * 30)
#
# # (2)删除所有值都是缺失值的行 (很少见)
# df_dropped_all_nan_row = df.dropna(how='all')
# print("删除缺失值：删除所有值都是NaN的行:")
# print(df_dropped_all_nan_row)
# print("-" * 30)
#
# # (3)删除特定列中包含缺失值的行
# df_dropped_subset_nan_row = df.dropna(subset=['年龄', '收入'])
# print("删除缺失值：删除'年龄'或'收入'列中包含NaN的行:")
# print(df_dropped_subset_nan_row)
# print("-" * 30)
#
# #(4)删除任何包含缺失值的列 (axis=1 或 axis='columns')
# df_dropped_any_nan_col = df.dropna(axis=1) # 或 axis='columns'
# print("删除缺失值：删除任何包含NaN的列:")
# print(df_dropped_any_nan_col)
# print("-" * 30)


# 关键点：
# isnull() / isna()：检测缺失值。
# fillna()：填充缺失值。
# 参数可以是单个值、Series（例如df['列名'].mean()）、method='ffill' (forward fill) 或 method='bfill' (backward fill)。
# dropna()：删除缺失值。
# axis：0 (默认) 为行，1 为列。
# how：'any' (默认) 表示只要有任意一个NaN就删除，'all' 表示只有所有值都是NaN才删除。
# subset：指定在哪些列中检查NaN。
# inplace=True：与 drop_duplicates 类似，fillna 和 dropna 默认返回新 DataFrame。使用 inplace=True 直接修改原 DataFrame。