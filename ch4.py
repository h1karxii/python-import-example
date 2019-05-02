import sys


def ch4_print(str='call ch4_print'):
    print(str)


print('==========')
ch4_print('In ch4.py')
print(sys.path)
print('==========')


# ############### [     ERROR     ] ###############
# Fix method 1
# sys.path.append('/Users/kingroyalx/Code/practice/python-import-example/run')

# Fix method 2
# sys.path.append('./run')

from run.ch2 import ch2_print
ch2_print()
###################################################


"""
## CH4
## 本章重點: [[ import 視角 ]]
  本檔案跟 ch3.py 一樣，
  除了 ch3.py import 的是 ch1.py，
  而 ch4.py import 的是 ch2.py，
  但是 ch4.py 執行後會報錯，
  原因是找不到 module ch1，
  這是因為在 ch2.py 中 import ch1.py 的方式的預設前提為
  「sys.path 陣列會包含 '/Users/kingroyalx/Code/practice/python-import-example/run'」，

  但是對於 python 的執行環境來說，
  除了 python 內建的 package 以及手動下指令使 package 成為 sys.path 的預設成員(手動設定環境變數)以外，
  不管這些 python 檔案往下 import 了幾層，
  sys.path 陣列只會包含執行的檔案所在的資料夾的位置，
  也就是 sys.path 中沒有 '/Users/kingroyalx/Code/practice/python-import-example/run'，
  因此如果要修正使 ch4.py 可以執行的話有兩個方法，

  [方法一] 修改ch4.py
    在 ch4.py 中讓 sys.path 新增 '/Users/kingroyalx/Code/practice/python-import-example/run'，
    L16 的寫法是絕對路徑，如果要用相對路徑的話，寫成以下
    ```
      sys.path.append('./run')
    ```
    相對路徑中的「.」指的是 ch1.py 中提到的「執行位置」，
    在此處是指 '/Users/kingroyalx/Code/practice/python-import-example'。

  [方法二] 修改ch2.py
    在 ch2.py 中，
    要更改引用 ch1.py 時的預設視角，
    也就是預設「執行位置」，
    我們預設執行位置為專案最上層資料夾，
    也就是 python-import-example，
    因此在 ch2.py 中 import ch1.py 的時候，
    就要寫成
    ```
      from run.ch1 import ch1_print
    ```

  基於以上原因，在寫 python 的工具或是 package 時，
  建議所有檔案不管是直接或間接被引用或執行都要站都同一視角來寫 import，
  也就是要假設「執行位置」是同一個地方(通常是最上層資料夾)，
  這樣引用來引用去的時候才不容易出錯。
"""


"""
## 可執行指令:
```
  # 執行結果請參考 pic/ch4.png
  ~/Code/practice/python-import-example > python ch4.py
```
"""