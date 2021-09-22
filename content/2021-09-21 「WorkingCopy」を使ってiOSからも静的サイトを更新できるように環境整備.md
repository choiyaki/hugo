---
title: 「WorkingCopy」を使ってiOSからも静的サイトを更新できるように環境整備
date: 2021-09-22T22:00:00+09:00
type: post
author: choiyaki
url: /p20210919
categories:
  - ブログ
tags:
  - github
  - iPhone
  - iPad
  - ブログ

---

ブログを静的サイトに移行しました。  
静的サイトによるブログ更新の仕組みは、gitへpushしたら更新される、というもの。gitに更新内容をpushすると、netlifyとhugoという奴らがなんか良きに計らってくれて無事ブログが更新される、というものみたいです。ようわかってませんが。

で、gitへのpushには、Macのターミナルが必要になります。ターミナルにてgitへあげるフォルダを指定し、内容をpushする、というコマンドを入力していくことでposhし、ブログを更新するわけです。
となると、Macからしか更新が出来ない、ということになります。これをなんとかしたかった。

そこで、iPhoneやiPadのiOSからでもgitにpushできるものがあればいいな、と散策。無事見つけました。「WorkingCopy」というアプリを。

<span class="appIcon"><img class="appIconImg" height="60" src="https://is2-ssl.mzstatic.com/image/thumb/Purple125/v4/4e/36/9d/4e369dbb-8f53-9db2-4358-83fd846a1cbc/source/60x60bb.jpg" style="float:left;margin: 0px 15px 15px 5px;"></span><span class="appName"><strong><a href="https://apps.apple.com/jp/app/working-copy-git-client/id896694807?uo=4" target="itunes_store">Working Copy - Git client</a></strong></span><br><span class="appCategory">カテゴリ: 開発ツール, 仕事効率化</span><br><span class="badgeS" style="display:inline-block; margin:6px"><a href="https://apps.apple.com/jp/app/working-copy-git-client/id896694807?uo=4" target="itunes_store" style="display:inline-block;overflow:hidden;background:url(http://linkmaker.itunes.apple.com/htmlResources/assets//images/web/linkmaker/badge_appstore-sm.png) no-repeat;width:61px;height:15px;"></a></span><br style="clear:both;">

というか、以前iPadでウェブアプリを開発できないものかと思った際に、一度利用したことのあるアプリです。これを使えばいけそう、ということで、早速有料契約に。有料じゃないとpushができないからです。
そして、WorkingCopyにてブログ用のフォルダを開き、gitにpushできる環境を作ればiOSからでもブログの更新ができるようになる。でもすんなりとはいきません。
WorkingCopyにてブログ用のフォルダを開くときにエラーが出てだめでした。

原因は、あんまりちゃんとわかっていないのですが、多分iCloudのようなクラウドストレージ上のフォルダをgitとつなげることはできませんと、という趣旨だと理解しています。
そうなんです。ブログ用のデータの入ったフォルダは、iCloud上に保管しているんです。もちろん、いろんなデバイスでObsidianを使うため、です。
Obsidianでは、iCloudを介してでデータの同期をおこないます。ブログの記事もObsidianで書いているので、ブログ用のフォルダを丸っと全てObsidian内に置いておくと、MacでもiPhoneでもiPadでも扱うことができ、何かと便利なわけです。
ただ、ここで僕は気づきます。ブログ用のフォルダをObsidian内に置いておく必要はないじゃないか、と。

各デバイスで同期しておきたいのは、あくまでも記事のページだけで、ブログを構成するデータたちは別に同期しておく必要はありません。記事を保管してあるフォルダさえ同期できればいい。それは、Obsidian上に置いておこう。他のページとも、ダブルブラケットの利用でリンクさせておくこともできる。
ただし、ブログを更新するためには、記事のフォルダだけではだめで、他のブログを構築するためのデータが入っているフォルダたちが必要になってきます。これらは、iCloudを介すことなく、各デバイス間で同期させる必要がある。
いやいやそのためのgitですやん、ということに気づいたのです。

- Obsidian上には記事を保管するフォルダを置いておく。
- その他のブログのデータは、他のところ（各デバイスのローカル環境）においておく。
- Obsidian上で、必要であれば他のページともリンクさせつつ、記事を書く。
- 記事が書けたら、そのページをブログ用のフォルダ内にコピーする。で、push。めでたく更新。

つまり、ブログ用の記事以外の諸々のデータも入っているフォルダと、Obsidianで同期しながら使うブログの記事が入っているフォルダを分ける、ということです。

![](https://i.gyazo.com/c3e6f4a3d2b31fb32ff97bbe4c101245.jpg)

こうすることで、

- ブログの記事フォルダだけObsidianに置けばよく、Obsidian上には必要ないデータを置かなくて済む。
- WorkingCopyを使って、pushができるようになる。

という一石二鳥で万々歳な環境になることに気づきました。ようやく、気づきました。
実際、この記事がちゃんとブログにアップされていたら、ひとまずは成功したということになります。
gitのことは正直全然理解できていないのですが、これならいけそうなので、今後はこの環境で、MacからでもiPadからでもiPhoneからでもブログを更新していくことができれば、と考えています。
今後も、iPhoneと本と数学となんやかんやとをよろしくお願いします。

<!--
- Obsidianの内部では、二重ブラケットによりページごとが繋がるけど、ブログとして更新する場合はそのままではよろしくなく、書き換える必要がある。
	- 書き換えてしまうと、Obsidian内でリンクしなくなっちゃう。
	- でも、ブログとして更新するためには、リンクは書き換えないといけない。
	- リンクでつながっていて欲しいのに、ブログの記事として公開する際にはリンクが途切れてしまう。
- で、解決策は、
	- ブログの記事はObsidian内で書く。
	- Obsidian外のフォルダにコピーし、公開用に加工する。
	- ブログの様々なデータもObsidian外におく。
- Obsidian外に置いているフォルダを、ブログ用とするということ。Macにも、iPadにも、iPhoneにも各々ブログ公開用のフォルダをクローンする。で、Obsidianで書き上げた記事を、ブログ公開用フォルダにコピーし、公開用に修正してgitにプッシュする。
- まず、プルしてgit上のデータとiPad上のデータを同じにして、記事を放り込み、プッシュ。
- そう、Obsidian上に全てのファイルを置いておく必要はなかったのよね。必要なものだけ置いといて、別個にブログ公開フォルダを作成しておけば。
- gitで管理されてるので、デバイスが違ってもデータの同期はできるわけやし。万事解決ですね。
-->