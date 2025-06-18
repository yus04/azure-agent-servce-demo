# azure-agent-servce-demo
Azure AI Foundry Agent Service のデモ用のサンプルリポジトリです。
agent.yaml ディレクトリ配下に Connected Agents でマルチエージェントを構築しているエージェント定義ファイルが配置されています。

## プログラム利用手順
src 配下に移動する。
```bash
cd src
```

必要なライブラリをインストールする。
```bash
pip install -r requirements.txt
```

Azure にログインする。Azure CLI がインストールされていない場合はインストールする。
```bash
az login
```

エージェント実行
```bash
python agent.py
```

## 留意点
- Visual Studio Code で Agent Service 開発をするためには AI Foundry Agent の拡張機能が必要です
- Visual Studio Code の拡張機能に一部サポートされていないツールがある場合がございます。その場合は Azure ポータルでの開発を行ってください。

> Tool: "bing_custom_search" currently not supported in the VS Code extension, please use Azure AI Foundry web portal instead.

> Tool: "connected_agent" currently not supported in the VS Code extension, please use Azure AI Foundry web portal instead.

## 参考ドキュメント
- Microsoft Learn 「クイック スタート: 新しいエージェントを作成する」
https://learn.microsoft.com/ja-jp/azure/ai-services/agents/quickstart?pivots=programming-language-python-azure
