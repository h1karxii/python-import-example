import sys


def quiz1_print(str='call quiz1_print'):
    print(str)


print('==========')
quiz1_print('In quiz1.py')
print(sys.path)
print('==========')


# ############### [     ERROR     ] ###############
from run.quiz1 import quiz1_print
quiz1_print()
###################################################


"""
## QUIZ
  Q:
  希望這樣「from run.quiz1 import quiz1_print」import quiz1_print 的話，
  該怎麼修改程式使之正確？

  A:
  看到「from run.quiz1」就知道，
  sys.path 中必須要有資料夾 run 的上一層('/Users/kingroyalx/Code/practice/python-import-example')，
  所以可以用
    ```
      sys.path.append('.')
      # 或是
      sys.path.append('/Users/kingroyalx/Code/practice/python-import-example')
    ```
"""