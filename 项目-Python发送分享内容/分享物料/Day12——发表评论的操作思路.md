在昨天的晚分享中，助教给大家讲解了如何在开发者工具里寻找 POST请求的请求网址、请求头、请求体，如果有还没来得及看的同学，可以看完今天的晚分享后补上噢~

[https://docs.forchange.cn/docs/WlArzBm08PIdeA2o/](https://docs.forchange.cn/docs/WlArzBm08PIdeA2o/)《Day11——如何查找请求体信息》

今天主要给大家讲解一下通过代码程序发表评论流程的详细步骤，包括怎么找请求网址、请求体，怎么写代码等。

正常在浏览器发表评论的步骤是：

1.在登录界面根据要求登录账号

2.找到评论框，根据评论框的要求写入内容

3.提交评论

4.在评论页面显示你的账号和评论的内容

在课程里提到，发表评论需要先登录账号，而且评论发表后会显示由哪位用户发表的评论。

那么通过代码程序发表评论的步骤是：

1.设置好账号密码的格式，通过 post()向服务器请求上传登录信息

2.登录成功后得到一个该账户的 Cookies

3.设置好评论的格式

4.结合 Cookies 通过post() 向服务器请求上传评论信息

5.查看评论是否发表成功

可能有同学不太理解如何通过人工操作的步骤演变成程序步骤，这是一种编程思维，说白了就是写的代码多了有感觉。

因为登录和发表都是一种上传数据的操作，所以程序执行需要通过post() 上传数据。发表评论时还需要用到用户信息，那么程序执行时也就需要用到 Cookies 啦。接着根据 post() 所需的参数，将步骤补齐即可。

大家在自行写代码时也可以把解题的思路列一列，培养一下自己的编程思维，代码本身是不难的~

接下来根据步骤来写代码，因为登录账号的操作在昨天的分享里有详细介绍过，这里助教就不过多解释哈~

打开登录页面（[https://wp.forchange.cn/wp-login.php](https://wp.forchange.cn/wp-login.php)）后，先按F12打开开发者工具，然后点击Network 面板，再按F5刷新一下网页页面后就会显示所有打开这个网页的请求信息。

![图片](https://docs.forchange.cn/uploader/f/VkVgfTER7H1Fr7Xg.png?fileGuid=erAdPgNX0nSDl8AG)

接着需要开启开发者工具里的保留日志功能，再输入账号密码进行登录。当POST请求成功时网页会跳转，如果不保留日志的话，就看不到 POST请求的相关信息。

在登录成功后找到登录的POST请求，查看对应的请求网址、请求体。

![图片](https://docs.forchange.cn/uploader/f/1lIpMrpaFxSmr6ya.png?fileGuid=erAdPgNX0nSDl8AG)

在确定好请求网址和请求体后，就可以先写登录账号的代码啦。因为请求体内包含我们输入的账号和密码，所以在代码内需要加多两个input()操作用来收集账号密码。

在写请求体的时候需要注意一下，字典里的键和值需要用引号括好，变量名和字符串要分开，不要在变量名上加引号噢~

![图片](https://docs.forchange.cn/uploader/f/e2iBPZSP4gi1jtEI.png?fileGuid=erAdPgNX0nSDl8AG)

接下来需要打开评论网页的页面（[https://wp.forchange.cn/psychology/11069/](https://wp.forchange.cn/psychology/11069/)），以及该网页的开发者工具。同样需要打开开发者工具的保留日志功能，找到评论栏写下内容后点击提交，在 Network 面板里就可以找到对应的POST请求信息啦~

![图片](https://docs.forchange.cn/uploader/f/chWgPSkqXUw9Bi3q.png?fileGuid=erAdPgNX0nSDl8AG)

同样的，确定好请求网址和请求体后就可以写发表评论的代码啦。因为发表评论需要带上用户信息，所以我们会用到post()登录账号时得到的 Cookies 信息。

在使用 post()登录账号时，我们把请求上传数据后的结果赋值给了变量 login_res，那么login_res 就变成了一个 Response 对象，我们可以通过 login_res.cookies 的形式调取对象的 cookies 属性信息。

接着把得到的 cookies 信息同请求体，分别传入post() 的 cookies参数和 data 参数即可。

![图片](https://docs.forchange.cn/uploader/f/dleKfWlsx7UlKT86.png?fileGuid=erAdPgNX0nSDl8AG)

在代码的最后可以通过打印查看 commit_res 的状态码来检验代码运行的情况，也可以直接在评论页面查看结果~

![图片](https://docs.forchange.cn/uploader/f/c0mJbdCuvKzwnefh.png?fileGuid=erAdPgNX0nSDl8AG)

![图片](https://docs.forchange.cn/uploader/f/VYJLkHjRJW442U0d.png?fileGuid=erAdPgNX0nSDl8AG)

至此整个发表评论的流程就走完啦，可以看到写代码的过程是不难的，比较难的点在于如何确认代码程序的执行流程。

助教想通过本次分享传达给大家的一点是，希望大家平时在练习时可以先梳理一下解题的思路，这样可以帮助大家更好地总结爬虫的处理思路，往后想爬取其他网站时就不会无从下手啦~

那么今天的晚分享就到这里啦，还没看昨天晚分享的同学记得看看噢，查找请求网址、请求体的具体方式在昨天的晚分享里，不能错过哈~

---

**【特别推荐】——****风变Python学堂公众号**

有Python知识干货、明星讲师直播、Python应用案例讲解等，帮大家学好Python，用好Python！

现在关注【风变Python学堂】，还可领取专属**【资料包】**，快扫下方二维码领取福利吧！

![图片](https://docs.forchange.cn/uploader/f/x8oxMihtofpF20xc.png?fileGuid=erAdPgNX0nSDl8AG)
