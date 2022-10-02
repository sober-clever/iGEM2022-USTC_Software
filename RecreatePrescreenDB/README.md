## Recreate Prescreen DB File Description

- data
  
  - `EC-RT.json`：每个EC编码对应的反应类型列表
  
  - `RT-EC.json`：每个反应类型对应的EC编码列表
  
  - `RTList.txt`：反应类型列表，每个反应类型附其对应的EC编码个数
  
  - `RTinDB-EC.txt`：每个具体反应类型对应的大反应类型（1-6）
  
  - `ErrorRows.txt`：`RTinDB-EC.txt`中有问题的行，原样打出来
  
  - `ErrorRowsFinal.txt`：`RTinDB-EC.txt`中有问题的行，已经被手动修复
  
  - `RTinDB-EC_DB.sql`：将新数据导入数据库。

- python
  
  - `Brenda_EC-RT.py`：读取Brenda数据库，创建`EC-RT.json` 
  
  - `EC-RT_RT-EC.py`：读取`EC-RT.json`，创建`RT-EC.json`
  
  - `RT-EC_RTList.py`：读取`RT-EC.json`，创建`RTList.txt`
  
  - `RTinDB-EC_DB.py`：读取`RTinDB-EC.txt`，创建`RTinDB-EC_DB.sql`


