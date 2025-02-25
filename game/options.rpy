﻿## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("Welcome to KMUST")


## 决定上面给出的标题是否显示在主界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = True


## 游戏版本号。

define config.version = "Alpha-0.5.2(NewEden)"


## 放置在游戏“关于”屏幕的文本。将文本放在三个引号之间，并在段落之间留一个空行。
define gui.about = _p("""
{size=16}{color=#bbbbbb99}这是{a=https://www.wjghj.cn/wiki/机智的小鱼君}机智的小鱼君{/a}制作的第一个视觉小说，也就是实验作，用于测试RenPy的运作{/color}{/size}

{size=28}{color=#33acff}版本说明\n{/color}{/size}

▪ 升级了RenPy引擎的版本

▪ 修改背景音乐（都是随便拖的歌，嫌吵可以在设置里关掉）

{size=18}参见：{a=https://www.wjghj.cn/wiki/Game:欢迎来到KMUST#更新日志}更新日志{/a}▪{a=https://wjghj.cn/wiki/Game:欢迎来到KMUST#下载游戏}最新版本{/a}{/size}

{size=28}{color=#33acff}CAST\n{/color}{/size}

{color=#60df44}制作人{/color}

机智的小鱼君

{color=#60df44}脚本、美术、动画、交互、程序、推广{/color}

机智的小鱼君

{color=#60df44}特别鸣谢{/color}

让我接触视觉小说制作的{i}Beed~极暗幻想~{/i}社团团长{b}阿卡姆{/b}，以及我的好友{b}成XX{/b}

最后，我还要感谢下载并游玩本游戏的——{b}你{/b}

{size=28}{color=#33acff}免责声明\n{/color}{/size}

▪ {b}KMUST{/b}是一所真实存在的高校，但我们不保证游戏展示的画面与现实一致

▪ 所有角色均为虚构，{b}如有雷同纯属巧合{/b}

{size=28}{color=#33acff}版权声明\n{/color}{/size}

▪ 字体“思源黑体”，为谷歌公司的开源字体

▪ 本游戏程序所有文字内容、立绘，部分背景图片均按CC BY-NC-ND 4.0协议发布，具体的法律信息参考{a=https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh}这里{/a}

▪ 部分图片素材以及音乐来自互联网，仅作非商业合理使用，如果您认为某媒体文件侵犯了您的合法权利，请通过下面的联系方式联系我

若有任何疑问，请{a=mailto:dragon-fish@qq.com}点击这里{/a}给作者发送电子邮件

{size=28}{color=#33acff}RenPy信息\n{/color}{/size}
""")


## 在生成的发布版中，可执行文件和目录所使用的短名称。此处必须是仅 ASCII 字符，并
## 且不得包含空格、冒号和分号。

define build.name = "WelcometoKMUST"


## 音效和音乐 #######################################################################

## 这三个变量控制默认显示给用户的混音器。任一设置为 False 将隐藏对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 允许用户在音效或语音轨道上播放测试音频文件，将以下语句取消注释并设置样音就可
## 以使用。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置主界面播放的背景音乐文件。此文件将在整个游戏中持
## 续播放，直至音乐停止或其他文件开始播放。

# define config.main_menu_music = "music 明天会更好.mp3"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = None


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 声明。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。如果是“show”，对话框将永远显示。如果是“hide”，
## 仅在存在对话时显示。如果是“auto”，对话框会在 scene 声明前隐藏，并在有新对话时
## 重新显示。
##
## 在游戏开始后，此变量可通过“window show”、“window hide”和“window auto”声明来改
## 变。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 是瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 25


## 默认的自动前进延迟。越大的数字会产生越长的等待，有效范围为 0 - 30。

default preferences.afm_time = 10


## 存档目录 ########################################################################
##
## 控制 Ren'Py 为此游戏放置存档的，基于平台的特定目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该命令一般不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "WelcometoKUST-1582182969"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 生成配置 ########################################################################
##
## 这部分控制 Ren'Py 如何将您的工程转变为发行版文件。

init python:

    ## 以下功能为指定文件模式。文件模式大小写不敏感，且匹配基础目录相关的路径，
    ## 包括或不包括 /。如果多个文件模式匹配，将执行第一个。
    ##
    ## 在一个文件模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中所有的 txt 文件，“game/**.ogg”匹配所有的游戏目
    ## 录或子目录中的 ogg 文件，“**.psd”匹配工程中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从已生成的分发版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 若要打包文件，需将其列为“archive”。

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 匹配为文档模式的文件，将在 Mac 应用的生成中复制，因此它们同时存在于 app
    ## 和 zip 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 需要一个 Google Play 授权密钥来下载扩展文件并执行应用内购。授权密钥可以在
## Google Play 开发者控制台的“服务和 API”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 工程关联的用户名和工程名，以斜杠分隔。

# define build.itch_project = "renpytom/test-project"
