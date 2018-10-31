# map_concept
Dylib with python3 interface for concept mapping

安装方法：
解压、进入目录、安装
```bash
pip3 install --upgrade .
```

例子：
``` python3
import tsunagi
tsunagi.get_disease_concept_id("糖尿病")
tsunagi.get_concept_id("eeg", "顶区异常波")
第一个参数为查询的domain，第二个参数为查询的输入。
现有domain有'ucg' (心脏超声检查), 'eeg' (脑电图检查), 'disease' （疾病（包含snomedct、meddra））
```
