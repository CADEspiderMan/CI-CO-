import pymysql
import pandas as pd
import ttkbootstrap as ttk
from PIL.ImageChops import offset
from ttkbootstrap.constants import *
from tkinter import messagebox
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'port': 3306,
    'password': 'zhh20050811',
    'database': 'PropertyRepairDB',
    'charset': 'utf8mb4',
}
def get_db_connection():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        messagebox.showerror('数据库连接失败',f"请检查数据库配置：{e}")
        return None


def open_main_window(role):
    main_win = ttk.Window(themename="superhero")
    main_win.title(f"物业管理后台 - 当前权限: {role}")
    main_win.geometry("800x600")

    # --- 核心功能函数区（这里就是和数据库通电的地方） ---
    def load_data():
        """从数据库读取数据并显示到表格中"""
        conn = get_db_connection()
        if not conn: return
        cursor = conn.cursor()

        # 1. 先清空当前表格里的旧数据
        for item in tree.get_children():
            tree.delete(item)

        # 2. 获取搜索框的关键字
        search_kw = entry_search.get()

        # 3. 去数据库模糊查询
        sql = "SELECT resident_id, room_number, name, phone FROM Residents WHERE name LIKE %s"
        cursor.execute(sql, (f"%{search_kw}%",))
        rows = cursor.fetchall()

        # 4. 把查到的数据一行行塞进表格
        for row in rows:
            # 取出字典里的值放进表格
            values = row
            tree.insert('', END, values=values)

        conn.close()

    def add_data():
        """添加新数据到数据库"""
        name = entry_name.get()
        phone = entry_phone.get()
        room = entry_room.get()

        if not name or not phone or not room:
            messagebox.showwarning("提示", "请填写完整信息！")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Residents (room_number, name, phone) VALUES (%s, %s, %s)", (room, name, phone))
            conn.commit()  # 提交保存到数据库
            messagebox.showinfo("成功", "业主添加成功！")
            # 添加完清空输入框
            entry_name.delete(0, END)
            entry_phone.delete(0, END)
            entry_room.delete(0, END)
            load_data()  # 刷新表格看到最新数据
        except Exception as e:
            messagebox.showerror("错误", f"添加失败: {e}")
        finally:
            conn.close()

    def delete_data():
        """删除选中的数据"""
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showinfo("提示", "请先在上方表格点击选中要删除的记录！")
            return

        # 获取选中的那行数据的 ID (第0列)
        resident_id = tree.item(selected_item)['values'][0]

        if messagebox.askyesno("确认", "确定要删除该业主吗？"):
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM Residents WHERE resident_id = %s", (resident_id,))
                conn.commit()
                load_data()  # 刷新表格
            except Exception as e:
                messagebox.showerror("删除失败", str(e))
            finally:
                conn.close()

    def export_excel():
        """导出为 Excel"""
        conn = get_db_connection()
        query = "SELECT resident_id AS '编号', room_number AS '房号', name AS '姓名', phone AS '电话' FROM Residents"
        try:
            df = pd.read_sql(query, conn)
            df.to_excel("业主数据报表.xlsx", index=False)
            messagebox.showinfo("成功", "数据已导出至代码所在文件夹的 '业主数据报表.xlsx'")
        except Exception as e:
            messagebox.showerror("导出失败", str(e))
        finally:
            conn.close()

    # --- 界面排版区 ---
    # 顶部操作区
    top_frame = ttk.Frame(main_win)
    top_frame.pack(pady=10, fill=X, padx=20)

    ttk.Label(top_frame, text="姓名模糊搜索:").pack(side=LEFT)
    entry_search = ttk.Entry(top_frame)
    entry_search.pack(side=LEFT, padx=5)
    # 注意这里绑定了 command=load_data
    ttk.Button(top_frame, text="查询", command=load_data).pack(side=LEFT)
    ttk.Button(top_frame, text="导出Excel报表", bootstyle=INFO, command=export_excel).pack(side=RIGHT)

    # 中间表格区
    columns = ('ID', '房号', '姓名', '电话')
    tree = ttk.Treeview(main_win, columns=columns, show='headings', height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor=CENTER)
    tree.pack(pady=10, fill=BOTH, expand=True, padx=20)

    # 底部录入/修改区
    bottom_frame = ttk.Frame(main_win)
    bottom_frame.pack(pady=10, fill=X, padx=20)

    ttk.Label(bottom_frame, text="房号:").grid(row=0, column=0, padx=5)
    entry_room = ttk.Entry(bottom_frame, width=10)
    entry_room.grid(row=0, column=1)

    ttk.Label(bottom_frame, text="姓名:").grid(row=0, column=2, padx=5)
    entry_name = ttk.Entry(bottom_frame, width=10)
    entry_name.grid(row=0, column=3)

    ttk.Label(bottom_frame, text="手机:").grid(row=0, column=4, padx=5)
    entry_phone = ttk.Entry(bottom_frame, width=15)
    entry_phone.grid(row=0, column=5)

    # 绑定了 command
    ttk.Button(bottom_frame, text="添加记录", bootstyle=SUCCESS, command=add_data).grid(row=0, column=6, padx=15)
    ttk.Button(bottom_frame, text="删除选中", bootstyle=DANGER, command=delete_data).grid(row=0, column=7, padx=5)

    # 【关键！】窗口一打开，就立刻执行一次查询，把数据加载出来
    load_data()

    main_win.mainloop()


def login(event = None):
    username = entry_user.get()
    password = entry_pwd.get()

    if not username or  not password:
        messagebox.showerror('提示',"用户名或密码不能为空！")
        return None
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sql = "select * from System_Users where username = %s AND password = %s;"
        cursor.execute(sql,(username,password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo('成功',f'欢迎回来,{user["role"]}{user["username"]}')
            login_window.destroy()
            open_main_window(user['role'])
        else:
            messagebox.showerror('错误',"用户名或密码不正确")
login_window = ttk.Window(themename = "cosmo")
login_window.title("社区物业保修系统--登录")
login_window.geometry('400x250')
ttk.Label(login_window, text = "系统登录",font=("微软雅黑" , 18 , "bold")).pack(pady = 20)
frame = ttk.LabelFrame(login_window)
ttk.Label(frame, text = "账号").grid(row = 0, column = 0, pady = 10)
entry_user = ttk.Entry(frame)
entry_user.grid(row = 0, column = 1)
frame.pack()
ttk.Label(frame, text = "密码").grid(row = 1, column = 0 , pady = 10)
entry_pwd= ttk.Entry(frame, show = "*")
entry_pwd.grid(row = 1, column = 1)
btn_login = ttk.Button(login_window, text = "登录" , command = login , bootstyle= SUCCESS)
btn_login.pack(pady = 15)
login_window.bind('<Return>',login )
login_window.mainloop()

def open_main_window(role):
    main_win = ttk.Window(themename = "cosmo")
    main_win.title(f"物业管理后台 - 当前权限:{role}")
    main_win.geometry('800x600')

    current_page = 1
    page_size = 10
    def load_data(page = 1):
        conn = get_db_connection()
        if not conn: return
        cursor = conn.cursor()

        for item in tree.get_children():
            tree.get_children(item)
        offset = (page - 1) * page_size
        search_kw = entry_pwd.get()
        sql = "SELECT resident_id , room_number , name , phone FROM Residents where name = LIKE %s OFFSET %s"
        cursor.execute(sql,(f"%{search_kw}%",page_size , offset))
        rows = cursor.fetchall()

        for row in rows:
            tree.insert('' , END, values=row)

        conn.close()
    def add_data():
        name = entry_name.get()
        phone = entry_phone.get()
        room = entry_room.get()

        if not phone.isdigit() or len(phone) != 11:
            messagebox.showwarning("格式错误","手机号必须是11位数字！")
            return
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Residents (room_number, name, phone) VALUES (%s, %s, %s)" , (room, name, phone))
            conn.commit()
            messagebox.showinfo("成功","业主添加成功")
            load_data()
        except Exception as e:
            messagebox.showerror("错误",f"添加失败: {e}")
        finally:
            conn.close()

    def delete_data():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择要删除的记录！")
            return

        resident_id = tree.item(selected_item)['values'][0]

        if messagebox.askyesno("确认", "确定要删除该业主吗？"):
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                # 对应要求4：删除时考虑参照完整性约束
                cursor.execute("DELETE FROM Residents WHERE resident_id = %s", (resident_id,))
                conn.commit()
                load_data()
            except pymysql.err.IntegrityError:
                # 捕获MySQL外键约束报错
                messagebox.showerror("受限删除警告", "该业主名下还有未处理的报修单，无法直接删除！请先清理报修记录。")
            finally:
                conn.close()

    def export_excel():
        """对应要求7：数据导出为Excel"""
        conn = get_db_connection()
        query = "SELECT resident_id AS '编号', room_number AS '房号', name AS '姓名', phone AS '电话' FROM Residents"
        try:
            df = pd.read_sql(query, conn)
            df.to_excel("业主数据报表.xlsx", index=False)
            messagebox.showinfo("成功", "数据已成功导出至当前目录下的 '业主数据报表.xlsx'")
        except Exception as e:
            messagebox.showerror("导出失败", str(e))
        finally:
            conn.close()

    top_frame = ttk.Frame(main_win)
    top_frame.pack(pady=10, fill=X, padx=20)

    ttk.Label(top_frame, text="姓名模糊搜索:").pack(side=LEFT)
    entry_search = ttk.Entry(top_frame)
    entry_search.pack(side=LEFT, padx=5)
    ttk.Button(top_frame, text="查询", command=lambda: load_data(current_page)).pack(side=LEFT)
    ttk.Button(top_frame, text="导出Excel报表", command=export_excel, bootstyle=INFO).pack(side=RIGHT)

    # 中间表格区
    columns = ('ID', '房号', '姓名', '电话')
    tree = ttk.Treeview(main_win, columns=columns, show='headings', height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor=CENTER)
    tree.pack(pady=10, fill=BOTH, expand=True, padx=20)

    # 底部录入/修改区
    bottom_frame = ttk.Frame(main_win)
    bottom_frame.pack(pady=10, fill=X, padx=20)

    ttk.Label(bottom_frame, text="房号:").grid(row=0, column=0, padx=5)
    entry_room = ttk.Entry(bottom_frame, width=10)
    entry_room.grid(row=0, column=1)

    ttk.Label(bottom_frame, text="姓名:").grid(row=0, column=2, padx=5)
    entry_name = ttk.Entry(bottom_frame, width=10)
    entry_name.grid(row=0, column=3)

    ttk.Label(bottom_frame, text="手机:").grid(row=0, column=4, padx=5)
    entry_phone = ttk.Entry(bottom_frame, width=15)
    entry_phone.grid(row=0, column=5)

    ttk.Button(bottom_frame, text="添加记录", command=add_data, bootstyle=SUCCESS).grid(row=0, column=6, padx=15)
    ttk.Button(bottom_frame, text="删除选中", command=delete_data, bootstyle=DANGER).grid(row=0, column=7, padx=5)

    # 初始化加载第一页数据
    load_data(current_page)

    main_win.mainloop()





