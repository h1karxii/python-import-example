import sys


def ch2_print(str='call ch2_print'):
    print(str)


print('==========')
ch2_print('In ch2.py')
print(sys.path)
print('==========')


# ############### [import method 1] ###############
# import ch1                   # 第一種 import 方式
# ch1.ch1_print()            # 相對應第一種 import 方式的呼叫方式
###################################################

# ############### [import method 2] ###############
from ch1 import ch1_print        # 第二種 import 方式
ch1_print()                      # 相對應第二種 import 方式的呼叫方式
###################################################


"""
## CH2
## 本章重點: [[ 同層 import 原理 ]]
  sys.path 陣列裡本身就會包含執行的檔案所在的資料夾，
  也就是該 module 所在的 package 位置，
  以此檔案 ch2.py 為例，
  sys.path 陣列會包含 '/Users/kingroyalx/Code/practice/python-import-example/run'，
  因為 sys.path 陣列包含 '/Users/kingroyalx/Code/practice/python-import-example/run'，
  所以只要是在 '/Users/kingroyalx/Code/practice/python-import-example/run' 下的所有檔案，
  或稱為同個 package(run) 下的所有 module，
  就可以透過以下兩種方式 import，

  ```
    # [import method 1]
    import module名(檔案名)

    # [import method 2]
    from module名(檔案名) import 該module中的函式名
  ```

  詳細範例可參考 L14 ~ L22 的程式，
  簡言之，所以對於 sys.path 陣列中所包含的位置(或稱路徑、package)，
  在 import 其之下的 module 時，
  import 方式只有上面兩種。
"""


"""
## 可執行指令
```
  # 執行結果請參考 pic/ch2.png
  ~/Code/practice/python-import-example > python run/ch2.py
  ~/Code/practice/python-import-example/run > python ch2.py
```
"""