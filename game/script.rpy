# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define df = Character("[dfname]", color="#1f6dff")
define teacher = Character("老师", color="#a0a0a0")
define mei = Character("[meiname]", color="#fa1a84")


## 游戏在此开始 ##

label start:

    scene bg library up
    play music "music PattyTheme.mp3"
    
    "终于，我来到了梦寐以求的顶级大学"

    "KMUST"

    "我将在这里……进行4年的学习，并生活在这座陌生的城市"
    
    python:
        dfname = renpy.input("我的名字叫：\n{size=12}(为主角起一个名字，请在输入完成后按下Enter键。可以随便填，但之后的游戏过程中将不能更改。{s}另外求求你们不要起奇怪的名字！{/s}){/size}",default="小鱼")
        dfname = dfname.strip()

        if not dfname:
            dfname = "你"

    scene bg library
    show df standing default

    df  "好大的太阳啊"

    df "这大概就是这座城市的特色吧"

    df "该去参加开学典礼了……"

    scene bg hall
    show df standing default

    teacher "blah blah blah"

    show df standing doubt
    
    df "卧槽真无聊"
    
    show df standing surprised
    
    "?" "那是肯定的"
    
    "?" "毕竟我们刚刚步入高校的生活，哪能理解老师所讲的那些道理呢"
    
    "?" "也许在实际体验以后，自然会慢慢明白吧"
    
    show df standing doubt
    
    df "……"
    
    df "话是这么说啦……{w}\n咦，你是？"
    
    show df standing surprised at right
    show mei standing happy at left
    "?" "诶嘿嘿，[dfname]{w}\n我们刚才在火车站碰到过呢"
    show mei standing default at left
    
    show df standing doubt at right
    "对，我想起来了，我帮她搬过行李……\n她好像还和我是一个专业的呢"
    
    "好像是叫……"
    
    python:
        meiname = renpy.input("女孩的名字叫？\n{size=12}(为女孩起一个名字，请在输入完成后按下Enter键。可以随便填，但之后的游戏过程中将不能更改。{s}另外求求你们不要起奇怪的名字！{/s}){/size}",default="小美")
        meiname = meiname.strip()

        if not meiname:
            meiname = "小美"
    
    show df standing surprised at right
    df "啊，原来是[meiname]吗"
    
    show mei standing happy at left
    mei "诶嘿嘿，对啦"
    
    show mei standing default at left
    mei "诶嘿嘿，对啦{fast}\n我还以为你不记得我了呢"
    
    show df standing default at right
    df "怎么会啦，只是入学手续有点多，忙不过来了"

    show mei standing happy at left
    mei "哈哈，我也忙的要死呢"
    show mei standing default at left
    
    df "看看，下了火车，一路把行李拖到学校……"
    
    mei "还好高铁车站离这里很近"
    
    show df standing doubt at right
    df "关键是我们这一届学生"
    
    show mei standing doubt at left
    "[dfname] & [meiname]" "(异口同声)宿舍居然在顶楼！{fast}"

    show df standing default at right
    show mei standing default at left
    df "啊哈，其实多爬几次也习惯了"
    
    df "主要是接下来的各种申请{w}，入学登记啦{w}、寝室登记啦{w}、学院报到啦{w}、缴费啦……{w}关键是不在一个地方！"
    
    mei "嗯，确实烦死了{w}，从这里跑过去，又从那里跑回来"
    
    df "……"
    
    teacher "希望大家在这四年里，过得精彩！"
    
    "哗啦啦啦啦啦（掌声）"
    
    show mei standing happy at left
    mei "喔喔喔，看来开学典礼结束了"
    
    df "嗯，终于……{w}\n我们一起去吃点东西吧"
    
    mei "好啊，据说KMUST的食堂可棒了"
    
    scene bg canteen
    "……"
    show df standing default at right
    show mei standing default at left
    mei "(突然停住)"
    
    mei "哇！{w}这也！！{w}太棒了吧！！！"
    
    df "别站着了，我们进去快点餐吧"
    
    show df standing surprised at right
    df "喔！{w}\n这是！！！"
    show mei standing happy at left
    mei "为什么啊，这居然是食堂吗~"
    
    df "这里是食堂吗？太棒了吧，居然还有特色小吃？我以为食堂只是卖盒饭的耶！？"
    
    mei "真是刷新了世界观呢~~~"
    
    scene bg food casserole
    show df standing default at right
    show mei standing happy at left
    mei "你点了一份砂锅啊"
    
    show mei standing default at left
    df "吸溜吸溜……是啊，怎么了吗？{w}\n因为，看起来肉相当的多"
    
    show mei standing happy at left
    mei "(笑)是呢，还真是个吃货哦"
    
    show mei standing default at left
    df "话说回来，你吃的是什么呢"
    
    scene food ricenoodle
    show df standing default at right
    show mei standing happy at left
    mei "啊~这是米线哦"
    
    df "我好像听说过……{w}\n啊，就是过桥米线的那个米线吗？"
    
    mei "对啊，就是那个米线哦~这可是本地的特色小吃呢~"
    
    show mei standing default at left
    mei "米线顾名思义，就是由米制成的。事实上在南方各地都有米线的身影，只不过我们一般把它叫做“米粉”~"
    
    df "哦，就是米粉的正统原型啊"
    
    mei "也算不上什么原型啦，只是各个地方的叫法不一样，只不过这里的最有名啦"
    
    df "就像肉夹馍和汉堡包么"
    
    show mei standing happy at left
    mei "(笑)真是有趣的形容啊"
    
    jump toBeContinue

