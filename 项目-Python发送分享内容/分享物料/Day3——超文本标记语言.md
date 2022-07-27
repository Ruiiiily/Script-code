今天的第3关我们学习了一种全新的语言——HTML语言，要注意它跟我们所学的Python是不同的哦

HTML是一种神奇的计算机语言，称为超文本标记语言，英文名字为：Hyper Text Markup Language

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2Fz82HybOgrrsBRwBs%2Fimage.png&fileGuid=ZzkLVrea7Mugo23Q)

说白了，网页显示的界面是因为它背后的语言：HTML，这是IT领域做前端的必备技能。如图所示(豆瓣主页的网页源代码)：

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FogIHlzqYCgoYQRW7%2Fimage.png&fileGuid=ZzkLVrea7Mugo23Q)

我们在html文件中编写代码，其实编写的是超文本。所谓超文本，即超出文本，比文本更高一级，就是的音频、视频以及超链接，甚至小游戏等。

至于存在文章里的一级标题、二级标题、列表、选项也不在话下。

那么如何在网页编辑器里面书写 HTML 代码呢？

以下面这个html网页编辑器为例:

![图片](https://docs.forchange.cn/uploader/f/Yq2V6MWvYYccqyLv.png?fileGuid=ZzkLVrea7Mugo23Q)

我们先点击右上角的重做，然后再点放大：

![图片](https://docs.forchange.cn/uploader/f/xXntfnMPpWXF4ad7.png?fileGuid=ZzkLVrea7Mugo23Q)

这个时候我们就可以在左侧书写HTML代码，并在右侧实时查看结果。（注意：缩进与结构要手动控制）

![图片](https://docs.forchange.cn/uploader/f/4uorRk5j0niRSZvG.png?fileGuid=ZzkLVrea7Mugo23Q)

而在本地vscode编辑器里面书写html代码，可以参考下面的步骤。

以下是一个最简单的html代码：

```
<html>
<head>
<meta charset="utf-8">
<title>大川神的爬虫世界</title>
</head>
<body>
<h1>静夜思</h1>
<h2>李白 唐</h2>
<p> 床前明月光，疑是地上霜。<br>举头望明月，低头思故乡。 </p>
</body>
</html>
```

在vscode里新建一个文件写入以上代码，注意文件保存的后缀名为.html

![图片](https://docs.forchange.cn/uploader/f/Ll1rAiSVYI8rkWhk.png?fileGuid=ZzkLVrea7Mugo23Q)

然后我们在文件夹找到该文件，并右键点击文件选择打开方式通过浏览器打开即可。

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FKKN2Em5I2UIokZWU%2Fimage.png&fileGuid=ZzkLVrea7Mugo23Q)

用一张图说明代码的原理：

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2Ff379YacW8PgYdZ4Z%2Fimage.png&fileGuid=ZzkLVrea7Mugo23Q)

最后我们来用Python来下载闪光读书网页并保存为本地的HTML文件。

```
import requests
 
url='https://wp.forchange.cn'
res=requests.get(url)
res.encoding='utf-8'
# w模式写成html文件
f1=open('闪光读书.html','w',encoding='utf-8')
f1.write(res.text)
 
f2=res.text
print(f2)#打印网页源代码
```

运行之后就可以生产一个html文件，然后通过浏览器打开就可以显示成网页啦。如下图：

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2FDLGTNeQ5y44JvtgX%2Fimage.png&fileGuid=ZzkLVrea7Mugo23Q)

![图片](https://docs.forchange.cn/uploader/proxy?url=http%3A%2F%2Fminio-service%3A9000%2Fshimo-images%2F2qxkoK7aH3MQsKGI%2Fimage.png&fileGuid=ZzkLVrea7Mugo23Q)

如果觉得上面比较麻烦，可以安装插件。

![图片](https://docs.forchange.cn/uploader/f/MUoZXe4eYPeHiCg4.png?fileGuid=ZzkLVrea7Mugo23Q)

然后在html代码栏里按 ctrl+k v，就可以预览对应的内容啦~

![图片](https://docs.forchange.cn/uploader/f/0XeMWImwHg3whXtx.png?fileGuid=ZzkLVrea7Mugo23Q)

当然我们学习的是爬虫并不是前端，所以对于HTML语言我们只需作为了解能够看懂它的结构然后找到对应的标签就可以啦，不需要在如何书写HTML上花费过多时间！

---

**【特别推荐】——****风变Python学堂公众号**

有Python知识干货、明星讲师直播、Python应用案例讲解等，帮大家学好Python，用好Python！

现在关注【风变Python学堂】，还可领取专属**【资料包】**，快扫下方二维码领取福利吧！

![图片](https://docs.forchange.cn/uploader/f/x8oxMihtofpF20xc.png?fileGuid=ZzkLVrea7Mugo23Q)
