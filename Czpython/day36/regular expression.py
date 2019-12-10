import re

#正则表达式是处理字符串的强大工具，有特定的语法结构，可以实现字符串的检索，替换，匹配验证
#对于URL来说,可以用  [a-zA-Z]+://[^\s]*  来匹配 这个正则表达式看上去是乱糟糟的一团，其实不然这里面都有特定的】
#语法规则，例 a-z 代表匹配任意的小写字母 A-Z 代表匹配任意大写字母  [a-zA-Z]+ 可以匹配一个不分大小写的英文单词
#可以是无限多个字母,至少是一个字母 \s表示匹配任意的空白字符, ^匹配一行字符串的开头  [^\s]* 表示 [ ]中的内容可以出现一次或无数次
#写好正则表达式后就可以拿它去一个长字符串里面匹配查找了,不论这个字符串里面有什么,只要符合我们写的规则,就可以找出来

'''
常用的匹配规则
\w   匹配字母,数字及下划线
\W   匹配不是字母，数字及下滑下划线的内容
\s   匹配任意空白字符,等价于 [\t\n\r\f]
\S   匹配任意非空字符
\d   匹配任意数字,等价于[0-9]
\D   匹配任意非数字的字符
\A   匹配字符串开头
\Z   匹配字符串结尾,如果存在换行,只匹配到换行前的结束字符串
\z   匹配字符串结尾，如果存在换行,同时还会匹配换行符
\G   匹配最后匹配完成的位置
\n   匹配一个换行符
\t   匹配一个制表符
^    匹配一个字符串的开头
$    匹配一行字符串的结尾
.    匹配任意字符串,除了换行符，当re.S被指定时，则可以匹配包括换行符在内的任意字符
[....]  用来表示一组字符单独列出,比如[amk]匹配a,m或k
[^...]  不在[]中的字符,比如[^abc]匹配除了a,b,c之外的字符
*    匹配0个或多个表达式
+    匹配1个或多个表达式 
？   匹配0个或1个前面正则表达式定义的片段，非贪婪方式
{n}  精确匹配n个前面的表达式
{n,m} 匹配n到m次由前面正则表达式定义的片段,贪婪方式
a|b  匹配a或b
()   匹配括号内的表达式,也表达一个组
'''
#正则表达式不是python独有的,它也可以用在其它编程语言中,python的re库提供了整个正则表达式的实现

#第一个常用的匹配方法   match(a,b) 两个参数,第一个参数 a : 接收正则表达式,第二个参数 b : 接收字符串
#向它传入要匹配的字符串以及正则表达式,就可以检测这个正则表达式是否匹配字符串,match（）方法会尝试从字符串起始位置匹配正则表达式.
#如果匹配就返回匹配成功的结果,如果不匹配就返回none
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())
'''
这里首先声明了一个字符串 content = 'Hello 123 4567 World_This is a Regex Demo'
正则表达式 ^Hello\s\d\d\d\s\d{4}\s\w{10}   
开头的 ^ 匹配的是字符串开头,也就是以hello开头,然后\s匹配空白字符，用来匹配目标字符串中的空格,\d匹配数字，3个\d匹配123，\s匹配空格
4个\d匹配4567，可以使用4个\d来匹配，但繁琐,后面可以跟一个{4}以代表匹配前面的规则4次，也就是匹配4个数字,紧接一个空白字符\s,最后\w{10}
匹配10个字母及下划线，这样并没有把目标字符串匹配完,不过这样依然可以匹配，只不过匹配结果短了一点
'''
#在match()的方法中，第一个参数传入了正则表达式，第二个参数传入了要匹配的字符串
#打印结果可以看出是re,Match对象，这证明成匹配,该对象有两个方法,
# group() 方法可以输出匹配到的内容
#span()方法可以输出匹配的范围,结果是(0,25),这就是匹配到的结果字符串在原字符串中的位置范围

#匹配目标
#刚才用match()方法匹配到字符串内容，但是如果想要从字符串中截取一部分怎么办？
#可以使用 () 将想要提取的子字符串括起来。() 实际上标记了一个子表达式开始和结束的位置，被标记的每一个子表达式会依次对应每一个分组，
#调用group方法传入分组的索引，即可获取结果

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
'''
可以看到我们成功得到了1234567.这里用的是group(1),它与group()有所不同，后者会输出完整的匹配结果，而前者会输出第一个被()包围的匹配结果
假如正则表达式后面还有()包围的匹配结果,那么可以依次用group(2),group(3)等来获取
'''

#通用匹配
'''
刚才写的正则表达式比较复杂,出现空白字符就写\s匹配,出现数字就用\d匹配,这样的工作量很大，其实完全没必要这么做,因为还有一个万能匹配可以用
那就是.*(点星)。其中.(点)可以匹配任意字符除了换行符 *(星)代表匹配前面的字符无限次,合在一起就可以匹配任意字符,有了它，就不用挨个字符的
匹配了,接着上面的例子，可以改写一下正则表达式
'''
#这里将中间部分全部省略，全部用.*来代替最后加一个结尾字符串就好了
result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())
#可以用.*来简化正则表达式的书写

#贪婪与非贪婪

#使用上面的.*匹配时,可能有时候匹配到的不是我们想要的结果
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('Hello .*(\d+).*Demo$',content)
print(result)
print(result.group(1))
#这次我们依然想获取中间的数字，所以中间依然写的是(\d+)。而数字两侧的内容比较杂乱，所以向省略来写都写成.*。最后组成^Hello,*(\d+).*Demo$
#看上去没问题，直接运行代码发现，只得到了7这个数字
'''
这与贪婪匹配和非贪婪匹配有关，在贪婪匹配下.*会匹配尽可能多的字符。 .*后面是\d+,也就是至少一个数字,并没有指定具体多少个数字，因此.*就尽可能匹配
多的字符，这里就把123456匹配了，给\d+留下了一个数字7最后得到的内容就只有数字7了，这时候会带来很大的不便，匹配结果会莫名奇妙少一部分,这时可以使用
非贪婪匹配 .*? 多了一个?,非贪婪匹配即尽可能匹配少的字符
'''

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('Hello .*?(\d+).*Demo$',content)
print(result)
print(result.group(1))
'''
此时就可以成功获取1234567了,原因贪婪匹配是尽可能匹配多的字符，非贪婪匹配是尽可能匹配少的字符
当 .*? 匹配到hello后面的空白符时,再往后的字符就是数字了,而\d+恰好可以匹配,那么这里 .*?就不再进行
匹配，交给\d+去匹配后面的数字,所以这样.*?匹配了尽可能少的字符,\d+的结果就是1234567
'''

#所以在做匹配的时候,字符串中间,尽量使用非贪婪匹配也就是用 .*? 来代替 .*以免出现匹配结果缺失的情况
#但是需要注意的是如果匹配结果在字符串结尾.*?就有可能匹配不到任何内容了,因为它会匹配尽可能少的字符
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)',content)
result2 = re.match('http.*?comment/(.*)',content)
print('result1',result1.group(1))
print('result2',result2.group(1))
#可以观察到,  .*?没有匹配到任何结果，而.*则尽量匹配多的内容，成功得到了匹配结果

#修饰符
#正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志
content = '''Hello 1234567 World_This' 
          is a Regex Demo'''
result = re.match('Hello.*?(\d+).*Demo$',content)
print(result)
#print(result.group(1))
#和上面的例子相仿，我们在字符串中加入了换行符,正则表达式还是一样的,用来匹配其中的数字

#运行直接报错,也就是说正则表达式没有匹配到这个字符串，返回结果为None,而我们又调用了group()方法导致AttributeError
'''
为什么加了一个换行符，就匹配不到了，这是因为.匹配的是除换行符之外的任意字符，当遇到换行符时, .*?就不能匹配了，所以导致匹配失败，
这里只需加一个修饰符re.S,就可以解决错误
'''
result = re.match('Hello.*?(\d+).*Demo$',content,re.S)
print(result)
print(result.group(1))
#这个修饰符的作用是使 .(点) 匹配包括换行符在内的所有字符
#re.S在网页匹配中经常用到。因为HTML节点经常会有换行,加上它就可以匹配节点与节点之间的换行了
'''
修饰符
re.I  使匹配对大小写不敏感
re.S  使.匹配包括换行在内的所有字符

re.M  多行匹配,影响^和$
re.L  做本地化识别(local-aware)匹配
re.X  这个标志通过给予你更灵活的格式以便你将正则表达式写的更容易理解
re.U  根据Unicode字符集解析字符。这个标志影响\w,\W,\b和\B
'''
#在网页匹配中常用的是re.I和re.S

#转义匹配
#我们知道正则表达式定义了许多匹配模式,如.匹配除换行符以外的任意字符，但是如果目标字符串里包含.该怎么办？
#这时就要用到转义匹配，当遇到正则匹配模式的特殊字符时,再前面加\（反斜线）转义一下即可。例如用\.来匹配.
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com',content)
print(result.group())


#3.  search()
#前面提到的match()方法是从字符串的开头开始匹配的，一旦开头不匹配那么整个匹配就失败了
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo',content)
print(result)
#这里的字符串以Extra开头，但是正则表达式以hello开头，整个正则表达式匹配的是字符串的一部分，但是这样匹配是失败的
#因为match()方法再使用时需要考虑开头的内容，它更适合用来做检测某个字符串是否符合某个正则表达式的规则

#search()方法，匹配时会扫描整个字符串，返回第一个成功匹配的结果，正则表达式可以是字符串的一部分，search()找到第一个符合规则的字符串，然后
#返回匹配内容，搜索完整个字符串，如果没有找到结果，就返回None
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo',content)
print(result)


#这里有一段待带匹配的html文本，接下来写正则表达式实现相应信息的获取
html = '''<div id="songs-list">
<h2 class = "title">经典老歌</h2>
<p class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mps" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>
'''
#可以观察到ul节点里面有许多li节点，其中li节点中有的包含a节点，有的不包含a节点，a节点还有一些相应的属性-超连接和歌手名
#首先，我们尝试class为active的li节点内部的超链接包含的歌手名和歌名，此时需要提取第3个li节点下a节点的singer属性和文本
#此时正则表达式以li开头,然后寻找一个  '标志符active' ,中间的部分可以用.*?来匹配，接下来要提取singer这个属性值，需要写入
#singer="(.*?)",这里需要提取的部分用小括号括起来，以便用group()的方法提取出来，它的两侧边界是双引号,然后还需要匹配a节点的文本其中它的左边界是>
#右边界是</a>。然后目标内容依然用(.*？)来获取所以最后的正则表达式是<li.*?active.*?singer="(.*?)>(.*？)</a>"

#然后使用search()方法，它会搜索整个文本，因为代码有换行，所以第三个参数需要传入re.S
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S) #用单引号包含正则表达式字符串，换行修饰符re.S
print(result.group(1),result.group(2))
#如果正则表达式不加active，active是标志符,匹配结果是什么?
result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))
#由于search()方法会返回第一个符合条件的匹配目标,这里的结果就变了:
#把active标签去掉后,从字符串开头开始搜索,此时符合条件的节点就变成了第二个li节点,后面的就不再匹配所以运行结果就变成了第二个li节点里面的内容

#注意,在上面的两次匹配中,search方法的第三个参数都加了re.S，这使得.*?可以匹配换行所以含有换行的li节点被匹配到了，如果去掉会怎样?
result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html)
print(result.group(1),result.group(2))
#结果变成了第四个节点中的内容,这是因为第二个和第三个li节点都包含了换行符,去掉re.S后 .*?已经不能匹配到换行符所以正则表达式不会匹配第二和第三个节点
#然而第四个节点内不包含换行符，所以就被匹配到了，由于绝大多数的html文本都包含换行符，所以尽量都加上re.S修饰符,以免出现匹配不到的问题


#findall()方法返回符合正则表达式的所有内容，将search()方法换成findall()方法，该方法会搜索整个字符串，然后返回正则表达式的所有内容
#如果有返回结果的话就是列表类型，列表中的元素是以元组的方式存放的，所以需要遍历来输出每组的内容,再索引出元组中的内容
#在上面的html文本中，如果想获取所有a节点的超链接，歌手和歌名可以将search()方法换成findall()方法
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0],result[1],result[2])
#如果是获取第一个内容可以使用search()方法，如果是要获取多个内容可以使用findall()方法

#sub()
#除了使用正则表达式提取信息外，有时还需借助它来修改文本。比如想要把一串文本中的所有数字都去掉如果只用字符串的replace()方法那就态繁琐，
#这时可以借助sub()方法,举个栗子
content = '23jhdsk8wjflwk'
content = re.sub('\d+','',content)
print(content)

#这里只需第一个参数传入\d+来匹配所有数字，第二个参数为替换掉的字符串（如果去掉该参数可以赋值为空），第三个参数为原字符串

#在上述的html文本中如果想获取所有li节点的歌名，直接用正则表达式来提取可能比较繁琐，例如
results = re.findall('<li.*?>.*?(<a.*?>)?(\w+)(</a>)?.*?</li>',html,re.S)   #\w可以用来匹配汉字
for result in results:
    print(result[1])
#这样写正则表达式坑比较复杂，此时借助sub()方法将a节点去掉,只留下文本然后再利用findall()提取就好了
html = re.sub('<a.*?>|</a>','',html)
print(html)
results = re.findall('<li.*?>(.*?)</li>',html,re.S)
for result in results:
    print(result.strip())   #当提取值只有一组时，返回值是列表，元素是字符串和多个换行符，用strip()函数将多余的换行符去掉
print(results)
#可以看到,a节点经过sub方法处理后就没有了,然后通过findall()方法直接提取即可，可以看到再适当的时候借助sub()方法可以起到事半功倍的效果

#compile()
#前面所讲的方法都是用来处理字符串的方法,compile()方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')#compile()函数可以传入修饰符，例如re.S
#pattern = '\d{2}:\d{2}'   #这样将字符串赋值给变量也行，不能传入修饰符
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
print(result1,result2,result3)
#这里有3个日期我们分别将3个日期中的时间去掉，可以使用sub()方法，该方法的第一个参数是正则表达式，这里没有必要将正则表达式重复写3遍，此时可以使用
#compile()函数将正则表达式编译成一个正则表达式对象以便复用

#另外compile()函数可以传入修饰符，例如re.S等修饰符，这样在search(),findall()方法里面就不需要额外传了，所以compile()方法可以说是给正则表达式做了一层
#封装，以便更好的复用





