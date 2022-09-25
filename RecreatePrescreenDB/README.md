## Recreate Prescreen DB File Description

- data
  
  - `EC-RT.json`：每个EC编码对应的反应类型列表
  
  - `RT-EC.json`：每个反应类型对应的EC编码列表
  
  - `RTList`：反应类型列表，每个反应类型附其对应的EC编码个数

- python
  
  - `Brenda_EC-RT.py`：读取Brenda数据库，创建`EC-RT.json` 
  
  - `EC-RT_RT-EC.py`：读取`EC-RT.json`，创建`RT-EC.json`
  
  - `RT-EC_RTList`：读取`RT-EC.json`，创建`RTList.txt`


