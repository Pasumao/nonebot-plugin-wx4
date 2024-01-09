from pydantic import BaseModel  
  
class MyPluginConfig(BaseModel):  
    # 在这里定义你的配置项  
    DBNAME: str  
    SUPER_ID: list[str]  
    GROUP_LIST: list[str]  
    API_KEY: str
    SECRET_KEY: str
    MAX_MESSAGES: int

  
    class Config:  
        #指定群聊，群号
        #指定群所有人都可以调用文心
        GROUP_LIST=[]
        #超级ID，QQ号
        #超级ID可以在任意群调用文心
        SUPER_ID=[]

        #数据库名字
        DBNAME="wxbot.db"

        API_KEY = "" 
        SECRET_KEY = ""   

        #最大对话记忆
        MAX_MESSAGES = 5  