import sys


def ch5_print(str='call ch5_print'):
    print(str)


print('==========')
ch5_print('In ch5.py')
print(sys.path)
print('==========')


# ############### [import method 1] ###############
# for 執行位置: /run
# exec command: python ch3.py
sys.path.append('..')
# 實際上 append 的是「執行位置」的上一層

# for 執行位置: /python-import-example
# exec command: python run/ch3.py
sys.path.append('.')
from mylib.lib1 import lib1_print
# 實際上 append 的是「執行位置」的路徑
###################################################

# ############### [import method 2] ###############
# sys.path.append('/Users/kingroyalx/Code/practice/python-import-example')
# from mylib.lib1 import lib1_print
###################################################

# ############### [import method 3] ###############
# sys.path.append('/Users/kingroyalx/Code/practice/python-import-example/lib1')
# from mylib import lib1_print
###################################################

lib1_print()


"""
## CH5
## 本章重點: [[ 同母層(兄弟層) import 原理 ]]
  [思路一] 希望用「from mylib.lib import lib_print」來 import
    要用這個指令來 import 的話，
    參考 CH3 的 上下層 import 原理逆推回去，
    代表 sys.path 中必須要有 mylib 的上一層的路徑，
    也就是 sys.path 中必須要有 '/Users/kingroyalx/Code/practice/python-import-example'，
    那方法有兩個第一就是直接在 sys.path 加入 '/Users/kingroyalx/Code/practice/python-import-example'，
    ```
      sys.path.append('/Users/kingroyalx/Code/practice/python-import-example')
    ```

    第二就是，在加入 sys.path 時使用相對路徑，
    由於相對路徑是相對於「執行位置」，
    所以當執行位置為 /python-import-example 時，
    需要這樣寫:
    ```
      sys.path.append('.')
    ```
    這樣寫代表把執行位置(python-import-example)加入 sys.path 中。

    當執行路徑為 /python-import-example/run 時，
    需要這樣寫:
    ```
      sys.path.append('..')
    ```
    這樣寫代表把執行位置(run)的上一層(python-import-example)加入 sys.path 中。

    由此可以看出，當執行位置不同時，
    加入 sys.path 時使用的相對路徑也不一樣，
    在程式閱讀及撰寫上會造成困擾，
    因此如 CH4 所說的，
    建議在寫 python 的工具或是 package 時
    對於所有可執行的 py 檔而言，
    「執行位置」要是同一個地方(通常是最上層資料夾)。

  [思路二] 希望用「from mylib import lib_print」來 import(較不建議)
    能用這個指令的只有一個情況，
    就是要跟 lib.py 同層，
    也就是要在 mylib 之下，
    換句話說就是 sys.path 中必須要有 '/Users/kingroyalx/Code/practice/python-import-example/lib'，
    這樣的話就只能這樣寫:
    ```
      sys.path.append('/Users/kingroyalx/Code/practice/python-import-example/lib')
    ```
"""


"""
## 可執行指令:
```
  # 執行結果請參考 pic/ch5.png
  ~/Code/practice/python-import-example > python run/ch5.py
  ~/Code/practice/python-import-example/run > python ch5.py
```
"""