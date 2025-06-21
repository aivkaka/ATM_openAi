from openai import OpenAI
from openai.types.chat import ChatCompletion

BASE_URL: str = "https://api.chatfire.cn/v1"
API_KEY: str = "sk-zO8exlBicZh7nJeZn5GuC5X9SPuVrZzXoGyOW0i9BFvN62ON"

client: OpenAI = OpenAI(base_url=BASE_URL, api_key=API_KEY)
completion: ChatCompletion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a software requirements analyst."},
        {"role": "user", "content": """
            请根据以下指令生成一个 ATM 自动取款机系统的需求模型：

            1. 包含主要功能模块，例如登录、余额查询、取款、存款、转账、修改密码等。
            2. 列出涉及的用户角色，比如普通用户和管理员。
            3. 每个功能模块需要有简要的业务流程描述。
            4. 使用 JSON 格式输出，不要使用任何 Markdown 或注释。
            5. 输出内容应简洁明了，适合后续开发人员理解和实现。

            示例输出格式如下：
            {
              "system_name": "ATM System",
              "roles": ["Customer", "Admin"],
              "modules": [
                {
                  "name": "Login",
                  "description": "User authentication using card and PIN.",
                  "flow": [
                    "Insert card",
                    "Enter PIN",
                    "Validate credentials",
                    "Grant access or deny"
                  ]
                }
              ]
            }
        """},
    ]
)
print(completion.choices[0].message)
