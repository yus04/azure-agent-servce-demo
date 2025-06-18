import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

project_endpoint = os.environ.get("PROJECT_ENDPOINT")
agent_id = os.environ.get("AGENT_ID")

# 認証には Azure Default Credential を使用
credential = DefaultAzureCredential()

# AIProjectClient インスタンスを作成
project_client = AIProjectClient(
    endpoint = project_endpoint,
    credential = credential
)

# エージェントを取得
agent = project_client.agents.get_agent(
    agent_id = agent_id,
)
print(f"Created agent, Name: {agent.name}")

# 新規のスレッドを作成
thread = project_client.agents.threads.create()
print(f"Created thread, ID: {thread.id}")

while True:
    content = input("ユーザー入力をどうぞ（終了するには 'exit' と入力）：")
    if content.lower() == 'exit':
        print("終了します。")
        break

    # スレッドにメッセージを追加
    message = project_client.agents.messages.create(
        thread_id = thread.id,
        role = "user",
        content = content,
    )
    print(f"Created message, ID: {message['id']}")

    # エージェントを実行
    run = project_client.agents.runs.create_and_process(thread_id = thread.id, agent_id = agent.id)
    print(f"Run finished with status: {run.status}")

    # 実行結果を確認
    if run.status == "failed":
        print(f"Run failed: {run.last_error}")

    # すべてのメッセージを取得
    messages = project_client.agents.messages.list(thread_id = thread.id)

    # 最後のメッセージを表示
    messages_list = list(messages)
    message = messages_list[0]
    print(message.content[0].text.value)
