label toBeContinue:
    scene black

    "未完待续……"
    
    "只是试验作啦，所以会很粗糙{w}\n而且基本是在测试游戏引擎的各个功能{w}\n所以请原谅谜一般的立绘"
    
    scene black
    menu:

        "请期待我的更新吧~"

        "催更 催更！":
        
            jump cuiGeng

        "好的，我期待着哟~":
        
            jump endGame

label cuiGeng:
    menu:
    
      "{a=https://wjghj.cn/wiki/Game:欢迎来到KMUST}检查更新{/a}":
        jump cuiGeng
      
      "{a=mailto:dragon-fish@qq.com}捶死作者{/a}":
        jump cuiGeng
        
      "结束":
        jump endGame

label endGame:
    
    return
