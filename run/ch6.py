import sys


def ch6_print(str='call ch6_print'):
    print(str)


print('==========')
ch6_print('In ch6.py')
print(sys.path)
print('==========')


sys.path.append('..')
sys.path.append('.')
from mylib.lib2 import lib2_print


lib2_print()


"""
## CH6
## 本章重點: [[ __name__ ]]
  本檔案與 ch5.py 一樣，
  但是引用的是 lib2.py，
  由於 lib2.py 中加入了 __name__ 的判斷確認，
  __name__ 的值在檔案被直接執行時與被引用時是不同的，
  當檔案直接被執行時 __name__ 會等於 __main__，
  如果是被引用時 __name__ 不會等於 __main__，
  因此 lib2 是間接被引用，
  因此不會執行其 L9~L12 的程式碼
"""


"""
## 可執行指令:
```
  # 執行結果請參考 pic/ch6.png
  ~/Code/practice/python-import-example > python run/ch6.py
  ~/Code/practice/python-import-example/run > python ch6.py
```
"""