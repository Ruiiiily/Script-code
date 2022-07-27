恭喜你完成oa高效办公课程呀。

完课不是终点，而是新的开始，希望你好好利用这七天里学习的知识点，好好想想如何解决自己工作中的“重复工作”噢。

现在我们好好回顾一下这7天里我们都学习了什么内容。

# -----第1关-----

第1关是导学课，主要学习了如何快速获取文件名，并复习了模块与库的概念和import语句。

我们先看看模块与库的概念。

模块与库是什么？

如果把Python比作手机，那库就像手机中的软件（app）。它可以实现各种各样的功能。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2F9SjTHsqQPG0Yit35%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

库一般分两种，它与手机中软件（app）的分类也很类似。

一种叫标准库，它像手机中的相机、图片、计算器等自带的软件一样，不用下载安装就可以使用。

第二种叫第三方库，它呢，就像从手机应用商店下载的社交、美图、支付等软件一样，是由其他人提供的，需要下载、安装之后才能使用。

python是有很多强大而又简单的库，但是我们该导入这些库呢。

import语句的作用：使用import语句来导入一个模块/库。

它的语法格式是import+模块名/库名。

例如，导入一个名为pandas的库，可以这么写：

```
import pandas
```

除此之外，还在案例中学习到了os库的一些简单的用法，例如os.listdir()

os.listdir()它的功能是将括号中路径下的所有**文件夹名**和**文件名**获取到。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FpMPmoFcfeFklIlI1%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

总结：![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FCUox0RlJsCMijnrA%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

# -----第2关-----

我们在第一关讲到了txt文件的筛选与读写

我们先来看看这一关的思维导图

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FKKyzkV3TEWgNFlNq%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

首先我们讲了相对路径跟绝对路径。

绝对路径是文件或文件夹在硬盘上的完整路径。永远都是磁盘根目录开头，具体的文件或文件夹名称做结尾。

我们来看看绝对路径的例子：

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2F7ifQHM8vhVwEo01N%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

相对路径是文件相对于当前代码文件所在的文件夹的相对位置。其中，使用./来表示当前文件夹，用../来表示上一级的文件夹。

可以看看这张图来理解一下相对路径：

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FbQHSuI2pET06pYlA%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

然后我们讲了os模块中的os.listdir()方法，利用这个方法我们可以以【列表】形式获得某个路径下的所有文件的名称。

接着是我们对于文件的操作。我们文件的操作顺序为：打开->读取/写入->关闭

我们打开文件用open()函数来打开一个文件。直接来看语法：

```
file = open(file_path, mode, encoding='utf-8')
# file: 将文件打开后获得的文件对象用file代表
# file_path: 打开的文件路径
# mode: 打开文件的模式（r、a、w）
# encoding: 用什么编码方式打开，课程的所有文件都是以utf-8编码
```

当中的mode是文件的打开方式，有r/w/a/r+/w+/a+几种模式

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FLlZaSp326GYcmgiV%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

打开完文件后我们获得了一个文件对象file。我们对打开文件获得的文件对象file进行后续操作。

读取文件的语法是：

```
content = file.read()  # 将读取到的文件储存在content变量中
```

写入文件的语法是：

```
file.write('要写入的文件内容')
```

关闭文件的语法是：

```
file.close()
```

打开文件后一定要养成关闭的好习惯，否则会一直占用电脑内存的资源。

# -----第3关-----

到了第三关我们接触openpyxl库，这个库是oa高效自动化办公的重点，可以说我们自动化很大一部分是建立在openpyxl库上的。

在回顾openpyxl库前，我们先回顾一下三个概念👇

关于Excel的三个概念：工作簿（workbook），工作表（worksheet）和单元格（cell）。

工作簿像一本小册子。

而工作表像这本册子中一页一页的内容。

单元格则是表格中的方块。

在写代码前需要先导入模块，这样才能调用相应的方法。

通过from…import…语句可以直接导入模块里的函数、类或变量。

```
# 同时导入openpyxl模块中的load_workbook和Workbook方法
from openpyxl import load_workbook, Workbook
```

使用openpyxl.load_workbook()可以打开已有工作簿，使用openpyxl.Workbook()创建新工作簿。

下面我们先尝试打开已有工作簿，并定位到工作表中。

```
from openpyxl import load_workbook
# 打开工作簿
wb = load_workbook('财务报表.xlsx')
# 用 wb.active 打开工作表
ws = wb.active
# 接下面代码👇
```

在获取表头时，我们需要定位到某一行、某一列、某一单元格，方法如下：

获取**某行**语法：ws[行值]，例如：获取第一行：ws[1]；行值是整数，从 1 开始。

获取**某列**语法：ws[列值]，例如：获取第一列：ws['A']，或ws['a']。

获取**某单元格**语法：ws[单元格坐标]，单元格坐标是行列的组合，类型是字符串。

例如：获取第一行第一列的'A1'单元格，语法是ws['A1']，或ws['a1']。

```
# 接上面代码👆
# 获取第一行
header = ws[1]
# 打印查看
print('表格第一行：')
print(header)
# 获取第一列
column_a = ws['A']
# 打印查看
print('表格第一列：')
print(column_a)
# 获取单元格C2
cell_c2 = ws['C2']
# 打印查看
print('单元格C2:')
print(cell_c2)
```

通过定位获得的单元格只是个对象，即Cell 对象。需要通过**cell.value**来进一步获取单元格里面的值。

```
# 获取单元格C2
cell_c2 = ws['C2']
# 打印查看单元格的值
print('查看单元格C2的值:')
print(cell_c2.value)
```

除了单独定位的方法，也有取多行多列的方法。

如果我们需要取出，除了第一行（表头）以外的数据，也就是从第二行开始取，可以使用iter_rows()方法。

iter_rows() 是工作表对象的一个方法，其功能是：通过行列序号指定遍历范围。

ws.iter_rows()可以与 for 循环结合使用，指定行列区域，按行遍历工作表，常用的参数包括：

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FOllf15JgntYMofBk%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

min_row，max_row，min_col，max_col四个参数可以顾名思义，限定了行列的范围；

values_only决定了我们是获取单元格对象、还是单元格的值。最终以元组的形式返回。

```
# 遍历从第2行开始的每行内容，values_only=True可以直接获取单元格的值
for row in ws.iter_rows(min_row=2, values_only=True):
    # 遍历每一行内的单元格
    for r in row:
        print(r)
```

在得到想要的内容后，就得写入新的表格之中。工作表对象的**append()**方法 能在表格的末尾**追加一行**数据，语法是：ws.append()，参数可以是一个元组或列表。

ws.append()会将元组或列表中的每个元素，从左向右，依次填入各个单元格中。

```
from openpyxl import load_workbook
# 打开工作簿
wb = load_workbook('财务报表.xlsx')
# 用 wb.active 打开工作表
ws = wb.active
new_list = [1, 2, 3]
# 将new_list添加如工作表中
ws.append(new_list)
```

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FTSXbk0UFVNUvN0PO%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

成功写入后，剩下的是修改工作表的名字以及保存工作簿了，修改的工作表需要工作表对象.title='更改后的名字'

```
# 打印工作表名
print(ws.title)
# 修改工作表标题
ws.title = '工作表1'
```

而利用openpyxl库对表格进行修改后，要记得使用save()方法进行保存，否则修改的excel表格是不会自动保存。

```
# 保存工作簿
wb.save('拆分表格.xlsx')
```

最后还有一个len()方法，len()是Python的一个内置函数，功能是返回对象的长度。将数据作为参数传入len()中就能返回对象的长度，例如：len([1,2,3])，可以返回值3。

```
# 列表的长度
print("列表['陈知枫', '廖雨', '王晴']的长度：")
print(len(['陈知枫', '廖雨', '王晴']))
```

总结：

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FVfPSMMhhpc4U7nGm%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

# -----第4、5关-----

进入第4关的学习，这一关没有新的知识点，通过四个小案例、对第三关所学的知识点进行巩固、解析。

这四个小案例分别是获取个人工资信息、生成前十行绩效信息表、计算并打印奖金信息、创建薪资信息字典

根据四个小案例，我们对“单元格读写”、“按行读写”、“按行取数计算”、“按行取数存为字典”等不同的模式进行熟悉。

我们看看这四个小案例的目的分解表格👇

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FmEnsp7ufQ9s8MFB9%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

通过分析上述案例，我们清晰认识到要解决现实中某些重复性工作，少不了这三步。

第一步👇，确认目的。明确自己的目前所遇到的问题是什么，并进行拆解，例如四个小案例的目的：获取个人工资信息、取前十行绩效信息表、计算奖金信息...等 你应该也有属于的目的，那么请先思索一下。

在确认目的的基础上，才能进行下一步思考。

第二步👇，你所需要是哪部分数据，利用openpyxl库处理excel表格，对单元格的处理主要有两种方法。

|      取值      | 方法                     |   |   |
| :------------: | :----------------------- | :-: | :- |
| 某些坐标里的值 | 工作表对象【单元格坐标】 |   |   |
| 某个几行的数据 | iter_rows（）方法        |   |   |

在处理数据时，需要我们去斟酌，自己想要实现的结果是什么？根据想要的结果来选择如何去写代码。

例如：我想要把工资表中的坐标A1~A30单元格数据读取来。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FagFvV6jk4ZgFiDjp%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

那我们想要的结果既然已经知道了，就可以根据前面所学的知识点，利用iter_rows进行取值。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FiKwjyWwe5dMR5gSR%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

再复杂一些，把坐标为A1~A30单元格数据读取出来，同时不打印坐标为A11单元的内容

举两种实现这种结果的代码👇

①可以加入if语句进行判断。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FLPkijBHjV6Mo0D95%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

②也可以将表格分为两部分进行读取,先读取坐标为A1~A10单元里的内容，再读取A11~A30的内容。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2Fl4ZxdvKVEAURTTZo%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

自动化办公的难点也就在于此，你通过什么代码，把自己的想要数据取出来并满足原先设想的结果。

第三步👇处理好的数据要放到哪里？ 第三步关系到目的了，若目的是将一个表格中的数据，读取出来处理、筛选后，写入到另一个表格中。

那在构写代码时，就需要考虑的是新建一个工作簿，而不是直接通过print()函数，打印在终端出来。

根据自己的需求要写代码，改代码。

# -----第6关-----

在第6关中我们则进一步学习如何修改Excel的样式。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2F6YZF6OFcbjktB4hW%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

首先我们还是需要导入模块，我们使用的方法都在openpyxl.styles模块下。

```
from openpyxl.styles import PatternFill, Alignment, Side, Border, Font
```

然后就可以通过openpyxl修改表格的列宽、单元格的颜色、对齐方式和边框。

使用openpyxl修改Excel表格样式的步骤是：

1、选择样式属性；

2、定义该属性的样式值 ；

3、赋值修改（具体各个）单元格的样式值。

调整工作表的列宽，需要用到Sheet.column_dimensions['列位置'].width。这条语句可以确定列位置，并用 width 属性，对该列的列宽进行修改。

比如说我想让第1列的列宽为20个单位，那么我就可以用 ws.column_dimensions['A'] 先确定找到第1列。然后使用ws.column_dimensions['A'].width = 20进行赋值。

除了列宽，其实也可以设置行高。

ws.column_dimensions['列名'].width = 数值类型，设置列宽。

ws.row_dimensions['行数'].height = 数值类型，设置行高。

```
# 打开工作簿
wb = load_workbook(file_path)
# 打开工作表
sheet = wb.active
# 调整列宽
sheet.column_dimensions['A'].width = 10
# 调整行高
sheet.row_dimensions[1].height = 30
```

刚刚提到openpyxl修改Excel表格样式步骤的第1点是——选择样式属性。即是选择关于单元格的样式属性。

cell单元格的常见用法有：cell.value、cell.font、cell.fill、cell.alignment、cell.border

* cell.value：获取单元格内的值；
* cell.font：设置单元格内的字体样式；
* cell.fill：设置单元格内的填充颜色；
* cell.alignment：设置单元格内的对齐方式；
* cell.border：设置单元格内的边框样式。

代码中的表示是：

```
# 定位到工作表的第1行，遍历里面的所有单元格
for cell in sheet[1]:
    # 设置单元格填充颜色
    cell.fill = # 使用定义好的样式
    # 设置单元格对齐方式
    cell.alignment = # 使用定义好的样式
    # 设置单元格边框
    cell.border = # 使用定义好的样式
```

大基调定下后，就需要处理小细节，比如样式是怎么定义的。先看思维导图。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FHruke1FA76UGPisS%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)

样式分为边框设置、颜色填充、对齐方式，分别对应Border对象、PatternFill对象、Alignment对象。

——————————

Border()方法可以给单元格设置边框，可以同时设置上下左右四个方向。而设置的样式则需要通过Side()方法来进行。

语法：Border(top=Side(style= , color= ) , bottom=Side(style= , color= ) , left=Side(style= , color= ) , right=Side(style= , color= ))

* style参数需要加入样式类型：thin（细条）、medium（中等）、double（双重）等等。
* color参数需要加入十六进制颜色码。
* top、bottom、lef、right是单元格的位置，后面接样式。

——————————

PatternFill()类其实就是对表格颜色的一个填充。

语法：PatternFill(patternType='', fgColor='')

* patternType参数表示填充形式，一般为'solid'纯色填充
* fgColor参数需要传入一个十六进制的颜色码，可在以下链接查询

[https://baike.baidu.com/item/%E5%8D%81%E5%85%AD%E8%BF%9B%E5%88%B6%E9%A2%9C%E8%89%B2%E7%A0%81/10894232?fr=aladdin](https://baike.baidu.com/item/%E5%8D%81%E5%85%AD%E8%BF%9B%E5%88%B6%E9%A2%9C%E8%89%B2%E7%A0%81/10894232?fr=aladdin)

——————————

Alignment()类可以实现自动换行及字符串对齐方式修改，然后应用到指定的cell上。

语法：Alignment(horizontal='', vertical='')

* horizontal代表水平方向，可以左对齐left，还有居中center和右对齐right，等等。
* vertical代表垂直方向，可以居中center，还可以靠上top，靠下bottom，等等。

——————————

代码整合起来的话，如下所示：

```
# 定义表头颜色样式为橙色
header_fill = PatternFill(patternType='solid', fgColor='FF7F24')
# 定义数据部分颜色样式为淡黄色
content_fill = PatternFill(patternType='solid', fgColor='FFFFE0')
# 定义表尾颜色样式为淡桔红色
bottom_fill = PatternFill(patternType='solid', fgColor='EE9572')
# 定义边样式为细条
side = Side('thin')
# 定义表头边框样式，有底边和右边
header_border = Border(bottom=side, right=side)
# 定义数据部分边框样式，有左边
content_border = Border(left=side)
# 循环第一行单元格，调整表头样式
for cell in sheet['1']:
    # 用定义好的样式，去设置单元格填充颜色
    cell.fill = header_fill
    # 设置单元格对齐方式
    cell.alignment = align
    # 设置单元格边框
    cell.border = header_bord
```

可能有部分同学看到这么多内容、这么多行代码就会头疼，就会被吓唬到。其实不用担心的，代码不需要你背诵，只需要先留个印象，等到需要使用到的时候，再去查找，随查随用就可以了。

至于代码，每一行代码的作用都很清楚，根据openpyxl修改Excel表格样式的步骤来，先确定好哪个部分需要修改样式，再确定什么样式，最后根据需求把代码直接填上去就可以了。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FmcHO32G2YKYQQiZw%2Fimage.png&fileGuid=293DVZGJlXiLFyk4)
