import sys


def ch1_print(str='call ch1_print'):
    print(str)


print('==========')
ch1_print('In ch1.py')
print(sys.path)
print('==========')


"""
## CH1
## 本章重點: [[ sys.path 陣列 ]]
  python 的函式庫稱為 package，
  可理解為存放一堆 python 檔案的資料夾，
  這堆 python 檔案就是該 package 下的 module，
  而 package 下可能還有子 package，
  如下所示：

  package
  |---- moduleX.py
  |---- moduleY.py
  |---- subpackage
        |---- moduleA.py
        |---- moduleB.py

  python 在 import package 時，
  會去找 sys.path 陣列看有沒有 import 指令所要找的 package，
  如果 sys.path 陣列裡找不到 import 指令所要找的 package 的話就會報錯。
  (sys.path 陣列中也存有 python 的內建 package 位置，所以 python 的內建函式庫才可直接 import)
"""


"""
## 可執行指令
  ```
    # 執行結果請參考 pic/ch1.png
    ~/Code/practice/python-import-example > python run/ch1.py
    ~/Code/practice/python-import-example/run > python ch1.py
  ```
  執行位置 > 檔案位置，
  > 以前為執行位置，
  > 以後為檔案位置，
  不管執行位置在哪 sys.path 陣列內一定會包含執行的檔案所在之資料夾，
  也就是該 module 所在的 package 路徑。
"""