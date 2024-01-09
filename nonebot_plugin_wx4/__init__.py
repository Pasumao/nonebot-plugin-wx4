from nonebot import on_command
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Message,PrivateMessageEvent
from nonebot.params import CommandArg
from .ConversationStorage import ConversationStorage

from nonebot.plugin import PluginMetadata

from .config import MyPluginConfig

__plugin_meta__ = PluginMetadata(
    name="文心一言4适配",
    description="文心一言4适配的连续对话",
    usage="《文心 内容》向文心提出问题，《失忆术》忘掉以往对话",

    type="application",

    homepage="https://github.com/Pasumao/nonebot-plugin-wx4",

    config=MyPluginConfig,

    supported_adapters={"~onebot.v11",},
)
Config=MyPluginConfig.Config

wx=on_command("文心",block=True, priority=1)
clear_wx = on_command("失忆术", block=True, priority=1)
  
wxbot=ConversationStorage(Config.DBNAME)

@wx.handle()
async def wx_handle(foo:Event,cmd: Message = CommandArg()):
    #指定的群聊或者私聊
    if grouplim(user_id,group_id) or isinstance(foo, PrivateMessageEvent):
        pass
    else:
        return
    user_id,group_id=get_id(foo)
    content = cmd.extract_plain_text()
    await wx.send('请稍等')
    res=wxbot.send_message(user_id,group_id,content)
    await wx.finish(res)

@clear_wx.handle()
async def clear_wx_func(foo:Event):
    user_id,group_id=get_id(foo)
    wxbot.clear(user_id,group_id)
    await clear_wx.finish("失忆了")

def get_id(foo):
    try:
        dt=foo.get_session_id().split('_')
        group_id=str(dt[1])
        user_id=str(dt[2])
    except:
        dt=foo.get_user_id()
        user_id=str(dt[1])
        group_id=""
    return user_id,group_id

def grouplim(user_id,group_id):
    if user_id in Config.SUPER_ID:
        return True

    if group_id=="":
        return False

    if group_id in Config.GROUP_LIST:
        return True
    else:
        return False