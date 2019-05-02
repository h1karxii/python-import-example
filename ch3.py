import sys


def ch3_print(str='call ch3_print'):
    print(str)


print('==========')
ch3_print('In ch3.py')
print(sys.path)
print('==========')


# ############### [import method 1] ###############
# import run.ch1                 # 第一種 import 方式
# run.ch1.ch1_print()            # 相對應第一種 import 方式的呼叫方式
###################################################

# ############### [import method 2] ###############
from run.ch1 import ch1_print    # 第二種 import 方式
ch1_print()                      # 相對應第二種 import 方式的呼叫方式
###################################################


"""
## CH3
## 本章重點: [[ 上下層 import 原理 ]]
  因為 ch3.py 不在資料夾 run 中，
  所以 sys.path 陣列不包含 '/Users/kingroyalx/Code/practice/python-import-example/run'，
  所以不能用 ch2.py 裡的 import 方法，

  但是 ch3.py 在 run 資料夾的上一層，
  也就是資料夾 python-import-example 中，
  因此 sys.path 陣列包含 '/Users/kingroyalx/Code/practice/python-import-example'，
  對於要 import sys.path 陣列中所包含的位置的子資料夾中的檔案，
  或稱 sys.path 陣列中所包含的 package 的 子package 中的 module，
  也就是 python-import-example 下的 子package(run) 裡的 module時，
  要透過以下兩種方式 import，

  ```
    # [import method 1]
    import 子package名.module名

    # [import method 2]
    from 子package名.module名 import 該module中的函式名
  ```

  詳細範例可參考 L14 ~ L22 的程式，
  當有更多層資料夾架構時，
  import 原理同上，
  以下為例：

  my_project
  |---- moduleZ.py
  |---- packageX
        |---- moduleA.py
        |---- moduleB.py
        |---- packageY
              |---- moduleC.py
              |---- moduleD.py

  當 moduleZ.py 要 import moduleC.py時，
  就要寫：

  ```
    from packageX.packageY.moduleC import moduleC中的函式名
  ```

"""


"""
## 可執行指令
```
  # 執行結果請參考 pic/ch3.png
  ~/Code/practice/python-import-example > python ch3.py
```
"""