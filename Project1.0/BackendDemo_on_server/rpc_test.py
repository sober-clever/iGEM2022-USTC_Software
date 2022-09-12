import rpyc


conn = rpyc.connect('124.220.19.232',9998)
#调用服务器端的方法，格式为：conn.root.xxx。xxx代表服务器端的方法名
# get_time是服务端的那个以"exposed_"开头的方法
result = conn.root.get_time()
print(result)

conn.close()
