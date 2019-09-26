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
  
ws = dawet.Dawet(filename)  

worksheet_number = 0
#getData  
vr = ws.getData("row name", "column name", worksheet_number)  

content = 10
#setData
vr = ws.setData("row name", "column name", worksheet_number, content)
```
# NOTE
Please add **client_secret.json**
