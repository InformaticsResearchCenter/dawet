# dawet 
Database using Worksheet

# Installation
```sh
pip install -r requirements.txt 
```

# How to use
to using this program : 
```python
import dawet  
  
ws = dawet.Dawet()  

worksheet_number = 0
#getData  
vr = ws.getData("row name", "column name", worksheet_number)  

content = 10
#setData
vr = ws.setData("row name", "column name", worksheet_number, content)
```
