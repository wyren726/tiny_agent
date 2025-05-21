import os, json
import requests
import os

from dotenv import load_dotenv
load_dotenv()  # 加载.env文件
api_key = os.getenv('API_KEY')

"""
工具函数

- 首先要在 tools 中添加工具的描述信息
- 然后在 tools 中添加工具的具体实现

- https://serper.dev/dashboard
"""

class Tools:
    def __init__(self) -> None:
        self.toolConfig = self._tools()
    
    def _tools(self):
        tools = [
            {
                'name_for_human': '谷歌搜索',
                'name_for_model': 'google_search',
                'description_for_model': '谷歌搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。',
                'parameters': [
                    {
                        'name': 'search_query',
                        'description': '搜索关键词或短语',
                        'required': True,
                        'schema': {'type': 'string'},
                    }
                ],
            }
        ]
        return tools

    def google_search(self, search_query: str):
        if not api_key:
            raise ValueError("API_KEY 环境变量未设置")
        url = "https://google.serper.dev/search"

        payload = json.dumps({"q": search_query})
        headers = {
            # 'X-API-KEY': '修改为你自己的key',
            'X-API-KEY': api_key,
            # api_key
            # 'X-API-KEY': '75edaf59839fa25dc62481b551d0096b61c37930',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()

        return response['organic'][0]['snippet']
