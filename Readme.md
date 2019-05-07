# python-import-example

## 閱讀順序
- ch1.py
- ch2.py
- ch3.py
- ch4.py
- ch5.py
- quiz1.py
- ch6.py


## __ name __
- [Python - if __name__ == '__main__' 涵義](https://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html)

## __ init __.py
Python 的 package 其實視為一個資料夾包起來的所有東西，
但是這個資料夾裡面一定要有一個檔案__init__.py (內容是空的也沒關係)，
Python 在 import的時候才不會出錯，
Python 在解譯的時候才會把這個資料夾視為一個 package，
而裡面的每一個檔案都是一個 module。
(更新: python 3.3 以後不強制要有__init__.py 檔案)

在__init__.py中還有一個重要的變量，叫做__all__，
我們有時會使出一招 “全部導入”，
也就是這樣：from PackageName import *
這時 import就會把註冊在包__init__.py文件中__all__列表中的子模塊和子包導入到當前作用域中來

- [Is __init__.py not required for packages in Python 3?](https://stackoverflow.com/questions/37139786/is-init-py-not-required-for-packages-in-python-3)
- [__init__.py 文件的作用以及意义](https://blog.csdn.net/xiaocaibai/article/details/80542920)
- [[问与答]Python中__all__的作用 ？](https://blog.csdn.net/orangleliu/article/details/49848413)


## sys.modules
既然python是在sys.path中搜索模塊的，
那載入的模塊存放在何處？答案就是sys.modules，是存放已載入模塊的地方。
模塊一經載入，python會把這個模塊加入sys.modules中供下次載入使用，
這樣可以加速模塊的引入，起到緩存的作用。

python在執行import語句時的步驟
  1. 創建一個新的，空的module對象（它可能包含多個module）；
  2. 把這個module對象插入sys.module中
  3. 裝載module的代碼（如果需要，首先必須編譯）
  4. 執行新的module中對應的代碼。

在執行第3步時，首先要找到module程序所在的位置，其原理為：
如果需要導入的module的名字是module1，則解釋器必須找到module1.py。

它首先在當前目錄查找，然後是在環境變量PYTHONPATH中查找。
PYTHONPATH可以視為系統的PATH變量一類的東西，其中包含若干個目錄。
如果PYTHONPATH沒有設定，或者找不到module1.py，
則繼續搜索與python的安裝設置相關的默認路徑，
在Unix下，通常是/usr/lib64/python2.6/。

事實上，搜索的順序是：當前路徑（以及從當前目錄指定的sys.path），
然後是PYTHONPATH，然後是python的安裝設置相關的默認路徑。
正因為存在這樣的順序，
如果當前路徑或PYTHONPATH中存在與標準module同樣的module，
則會覆蓋標準module。
也就是說，如果當前目錄下存在xml.py，
那麼執行import xml時，導入的是當前目錄下的module，而不是系統標準的xml。

- [python的模块加载和路径查找](https://wecatch.me/blog/2016/05/28/python-module-path-find/)
- [Python : __init__.py的作用](https://my.oschina.net/cloudcoder/blog/201271)


## import 的相對與絕對路徑
不是 sys.path 時的相對與絕對路徑喔

絕對導入的格式為import A.B或from A import B，
相對導入格式為from . import B 或 from ..A import B，
.代表當前模塊，..代表上層模塊，...代表上上層模塊，依次類推。

相對導入可以避免硬編碼帶來的維護問題，
例如我們改了某一頂層包的名，
那麼其子包所有的導入就都不能用了。
但是存在相對導入語句的模塊，不能直接運行，否則會有異常

在沒有明確指定包結構的情況下，Python是根據__name__來決定一個模塊在包中的結構的，
如果是__main__則它本身是頂層模塊，沒有包結構，
如果是A.B.C結構，那麼頂層模塊是A。基本上遵循這樣的原則：

  1. 如果是絕對導入，一個模塊只能導入自身的子模塊或和它的頂層模塊同級別的模塊及其子模塊
  2. 如果是相對導入，一個模塊必須有包結構且只能導入它的頂層模塊內部的模塊

如果一個模塊被直接運行，則它自己為頂層模塊，不存在層次結構，所以找不到其他的相對路徑。

- [Python 相對導入與絕對導入](http://kuanghy.github.io/2016/07/21/python-import-relative-and-absolute)


## python 的 import
- [[Python] 解決 import 相對路徑執行問題](https://medium.com/bryanyang0528/python-%E8%A7%A3%E6%B1%BA%E7%9B%B8%E5%B0%8D%E8%B7%AF%E5%BE%91%E5%9F%B7%E8%A1%8C%E5%95%8F%E9%A1%8C-5cb157d22ab0)
- [Python 的 Import 陷阱](https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3)
- [Python import 簡易教學](https://medium.com/@alan81920/python-import-%E7%B0%A1%E6%98%93%E6%95%99%E5%AD%B8-c98e8e2553d3)