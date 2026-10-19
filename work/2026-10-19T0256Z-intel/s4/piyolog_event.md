---
title: 運営指定の遠隔操作ソフト導入を参加条件とされたセキュリティイベントについてまとめてみた - piyolog
author: Piyokango
url: https://piyolog.hatenadiary.jp/entry/2026/10/19/032554
hostname: hatenadiary.jp
description: "2026年10月12日、Elastic Security Labsは、暗号資産やWeb3の創業者を狙う偽のアクセラレーター「Apex Accelerator」が悪性のnpmパッケージで端末を狙っていたと公表しました。同じ名称の運営がTOKEN2049期間中の催しで参加の条件としてセキュリティ製品の導入を迫ったとする申告も出ています。ここでは関連する情報をまとめます。 偽アクセラレーターApex Accelerator Apex Acceleratorは、暗号資産やWeb3の創業者を狙う偽のアクセラレーター。Elastic Security Labsは追跡名REF8801として調査しており、「A…"
sitename: Piyolog
date: "2026-10-19"
categories: ['海外事例']
tags: ['海外事例']
fingerprint: "7bc8d4302c30ff8b"
---
2026年10月12日、Elastic Security Labsは、暗号資産やWeb3の創業者を狙う偽のアクセラレーター「Apex Accelerator」が悪性のnpmパッケージで端末を狙っていたと公表しました。同じ名称の運営がTOKEN2049期間中の催しで参加の条件としてセキュリティ製品の導入を迫ったとする申告も出ています。ここでは関連する情報をまとめます。

### 偽アクセラレーターApex Accelerator

Apex Acceleratorは、暗号資産やWeb3の創業者を狙う偽のアクセラレーター。Elastic Security Labsは追跡名REF8801として調査しており、「Apex」という名のアクセラレーターが支える非公開ワークスペース「Apex Arena」を前面に出し、運営のサイトは200超のポートフォリオと1.24億ドル超の調達を掲げ、偽のレビューも使っていたと記述している(出典: 2)。

端末を狙う経路は2つ。1つ目は開発ツールやセキュリティ監査を名乗るnpmパッケージで、SafeDepが7月22日に、Elasticが10月12日にそれぞれ公表した。運営は無料のAIクレジットやコーディングツール、セキュリティ監査の提供を掲げて創業者に接近し、デューデリジェンス名目などでパッケージを実行させる(出典: 1, 2, 3)。2つ目はTOKEN2049の期間中の催しで、参加の条件として正規のセキュリティ製品のインストーラーを導入させようとしたとされるもの。シンガポール警察(SPF)に申告したとする申告者の投稿に基づく[\*1](https://piyolog.hatenadiary.jp#f-3fb35b18) (出典: 4, 5)。

### 削除後に別名で再公開されたnpmパッケージ

SafeDepによると、2026年4月30日(UTC)に「Apex-Foundation」と無害を装ったパッケージが作られ、パッケージは約3か月間、通常のオープンソースとして運用されていた。7月5日に最初のドロッパー版となる@apexfdn/apexがnpmに公開され、21日までに計34版が公開された。同日、npmセキュリティチームが悪性コードを理由に同パッケージを削除し、プレースホルダーに置き換えた(出典: 1)。

約11時間後の7月22日、同じドロッパーが新しいスコープの@copilot-mcp/apexとして再公開され、同日中に20版超が公開された。SafeDepは、macOSでの起動方法を変えながら試していたと記述している。このパッケージもその後削除された(出典: 1)。

SafeDepの解析では、postinstallでプラットフォーム別のバイナリをGitHubのリリースから取得して実行する。macOSではAMOS系のAppleScript製の窃取型を実行し、パスワードを求める偽のプロンプトでブラウザの資格情報や暗号資産ウォレット等を集めて送出するほか、60秒ごとにC2(指令サーバー)を確認するLaunchAgentを設置する。「無料のLLMクレジット」を餌にWeb3の創業者を狙うもので、機能上の偽装には正規のコーディングエージェントOh My Piのフォークが使われた(出典: 1)。

### 正規のコーディングエージェントを改変した@apexacc/cli

Elasticは、自社のサプライチェーン監視ボットの通知で@apexacc/cliを検出し、公開時点から悪性のパッケージと判断した。同日中に、SafeDepが既報のキャンペーンと同じ公開者であることをElasticが把握し、その後、同じ攻撃者が別の悪性パッケージ@apexacc/auditを公開した(出典: 2)。

Elasticの解析では、@apexacc/cli(GitHubではapexaccs/copilot、製品名はApex Copilot)は正規のオープンソースのコーディングエージェントOh My Piを再パッケージしたもので、Apex Copilot v1.6.1のpackages/coding-agent/src/配下の1,363ファイルのうち、Oh My Pi v16.3.6の同じ位置のファイルと内容が一致したのは1,351。@apexacc/auditは18のセキュリティツールを持つMCPサーバーとして宣伝されていた。どちらもnpmのランチャーがGitHubのリリースからプラットフォーム別の実行ファイルを取得して起動する。Elasticは、@apexacc/cliについて次の3点を検証で確認したとしている(出典: 2)。

- LLM通信をOpenRouter名義で攻撃者管理のサーバーに向ける
- 攻撃者管理のMCPサーバーをエージェントの設定に登録する
- 明示的にファイル読み取りを指示した試験で、ローカルで読んだファイルの内容がLLMリクエストに含まれて攻撃者側に送られる

Elasticは、LLM応答の悪意ある差し替えは観測していないとしている。監査ツールについては、@apexacc/auditの18ツールのハンドラのソース検査で、いずれも実際のスキャンを行わず、固定の所見や乱数、日付由来の値で整形した偽の結果を返す作りだったと記述している(出典: 2)。

9月15日には、暗号資産プロジェクトの創業者がXで、「Apex Accelerator」からデューデリジェンス名目でnpx @apexacc/cliの実行を求められたと投稿した。隔離したmacOSのユーザーで実行したところ、Appleを装った隠しアプリが作成され、暗号化されたペイロードが自己復号して実行、削除されたという。指摘するとTelegramのグループが数分で削除された。損失はなかったとしている(出典: 3)。Elasticはこの投稿を創業者の体験例として引用している(出典: 2)。

### 実行ファイルの先で配られたmacOSとWindowsのマルウェア

Elasticによると、ランチャーがGitHubのリリースから取得して起動する実行ファイルには、攻撃者のサーバー(vrf.apexaccs\[.\]org)から実行するコマンドを取得して起動する「検証」の処理が組み込まれている。macOSでは別のRust製の実行ファイルがコマンドを取得し、CloudSyncDと呼ばれるファミリーのドロッパーが配布される(C2からの追加ペイロードは観測していない)。Windowsでは取得したPowerShellコマンドから多段のローダーが配られ、Elasticの解析ではPythonの依存関係不足で第1段で停止したが、別途の隔離環境での実行で、収集データをTelegramに送出する情報窃取型の動作が確認された。収集対象にはClaude、Cursor、WindsurfといったAIクライアントのファイルが含まれる。Elasticは、@apexacc/auditがWindows 11でMicrosoft Defenderの除外追加とSmart App Controlの無効化を試みるとも記述している(出典: 2)。

### TOKEN2049の期間中の催し「Don't Get Played」

TOKEN2049 Singaporeの本会議の会期は10月7〜8日、会場はMarina Bay Sands。会期中のシンガポールでは、独立して運営されるサイドイベントが1,000件超ある(出典: 8)。

申告者は、運営側が「Don't Get Played」を、10月11日(日)18時から22時、The Singapore EDITIONでの暗号資産セキュリティイベントとして告知していたと記載している。運営名義は「Apex Accelerator」と「Stone Venture」。告知にはウォレットを接続して「スキャン」するLive Wallet Clinic、運営側のSophosを導入した人に3,000ドルを贈るDirtiest Laptop Award、Sophosをパートナーとする表記があったとする(出典: 5)。

申告者がThe Singapore EDITIONに電話で確認したところ、18時から22時の催しはあるものの、Apex、Sophos、Stone Ventureは主催者ではないと従業員に言われたと記載している(出典: 5)。

### 参加の条件とされたSophos Centralのインストーラー

申告者は、次の経緯を記載している(出典: 5)。

1. token.apexaccs\[.\]orgに登録し、10月8日に運営側のメールで参加バッジの確認を受けた。
2. 10月10日、Sophos Centralの送信元から「Software Deployment For Sophos Central」の件名でインストーラー付きのメールが2通届いた(12時43分と21時46分、SGT)。同日21時38分、運営側は「無償の1年版アンチウイルスとMDR」を「セキュリティパートナー」に引き渡したとするメールを送ってきた。
3. Telegramでは、100万ドルの保証と、一般向けのアンチウイルスはマルウェアを検出できないとの説明でインストールを迫られた。インストールの期限は申告者に対して23時から翌1時、さらに10月11日正午へと延長された。
4. 写真の景品に当選したと告げられたが支払いはなく、その後、Sophosを導入しなければイベントに参加できないと告げられた。

申告者は、インストーラーに同梱されていた設定ファイルについて、Sophos Homeではなく業務版のSophos Centralのもので、運営側のアカウントを示す識別子と、端末を自動でアカウントに参加させる登録トークンを含むと記載している。導入すると端末が運営側のSophos Central業務アカウントに追加され、遠隔で監視、操作されうると説明している(出典: 4, 5)。申告者は、端末の点検で遠隔操作ソフトは見つからず、運営側のインストーラーは実行されていないとしている(出典: 5)。

### シンガポール警察への申告

申告者は10月11日、SPFに申告(出典: 7)。申告書には、運営名義、サイト、Telegram、遠隔操作ソフトの導入を迫られたことが記載されている(出典: 5, 6)。10月12日に申告書の2ページ目をXで公開し、同日、SolanaFloorも申告書を画像で紹介した(出典: 4, 6)。申告者は13日に経緯の続きを公開し、アカウントとドメインの調査を求めたうえで、運営者を特定できる情報を持つ事業者としてSophos、npm、GitHub、Namecheap、Cloudflare、Telegramを挙げている(出典: 5)。

申告者は最初の投稿でSophosに対応を求めた。Sophosのセキュリティチームを名乗るXのアカウントは、その投稿に返信して調査中であること、このイベントで何かを導入した人はサポートへDMするよう伝えた[\*2](https://piyolog.hatenadiary.jp#f-d16353e1) (出典: 4)。

### 2つの経路に共通する名称とアカウント

2つの経路には、次の共通点がある。

- Telegramのアカウント: SafeDepが運営側の指標として記載したTelegramアカウントの1つは、申告者が導入を迫った相手として記載するアカウントと同じ。申告者は、このアカウントがnpmの@apexacc/cliのサポート窓口でもあると記載している(出典: 1, 5)。
- 名称: 申告者が公開した運営名義やドメイン等の一覧に「Apex Accelerator」と「Apex Foundation」があり、SafeDepはキャンペーンの名目を「Apex Foundation」と記述している(出典: 1, 5)。
- ドメイン: Elasticはtoken.apexaccs\[.\]orgを対面イベントの招待サイトとして記載しており、申告者も登録に使ったサイトとして同じtoken.apexaccs\[.\]orgを挙げている(出典: 2, 5)。

Elasticは、運営がTOKEN2049での存在などで信頼を装っていると記述し、会議の主催者に通知して公表前に要約を提供したとしている(出典: 2)。申告者は、@apexacc/cliがイベントの「Apex MCP」ツールとして宣伝されていたとも記載している(出典: 5)。

### 参考情報

#### 観測の当事者

- \[1\] 2026年7月22日 SafeDep「[@copilot-mcp/apex: A macOS Infostealer Re-Published on npm After Takedown](https://safedep.io/malicious-copilot-mcp-apex-npm-macos-infostealer/)」
- \[2\] 2026年10月12日 Elastic Security Labs「[Auditing the auditor: Unmasking Apex Accelerator](https://www.elastic.co/security-labs/threat-command/apex-accelerator-malicious-npm-packages)」

#### 創業者と申告者の投稿

- \[3\] 2026年9月15日 X「[暗号資産プロジェクトの創業者による投稿](https://x.com/hialex_sol/status/2099575319002800415)」
- \[4\] 2026年10月12日 X「[申告者による申告書と設定ファイルのスキャン結果の投稿](https://x.com/KYMRegistrySG/status/2109611683446677849)」
- \[5\] 2026年10月13日 X「[申告者による申告書の続きの公開](https://x.com/KYMRegistrySG/status/2110022394056409427)」
- \[6\] 2026年10月12日 X「[SolanaFloorによる申告書の紹介](https://x.com/SolanaFloor/status/2109654244655812768)」

#### 報道

- \[7\] 2026年10月13日 Journal du Coin「[Arnaque TOKEN2049 : un faux atelier crypto visé par la police](https://journalducoin.com/?p=824188)」

### 更新履歴

- 2026年10月16日 新規作成
