---
title: カレンダーとの連携【Pro】〜checkvistの使い方5〜
author: choiyaki
type: post
date: 2020-04-18T13:57:15+00:00
url: /p1040
views:
  - 738
categories:
  - checkvist
tags:
  - checkvist
  - たすくま
  - タスク管理

---
[checkvist][1]のProアカウントでは、「dd」によって実行日を設定したタスクを、カレンダーに表示することができます。具体的には、Macの標準アプリのカレンダーか、[Googleカレンダー][2]との連携が可能となっています。  
この連携はあくまでも「表示できるようになる」だけで、カレンダーに表示されているタスクを選択して編集、はできません。あくまでも、表示できるようになるだけ。基本的にcheckvist上でタスクを扱うのであれば、表示できるだけでも十分ではないかな、と思います。

### 連携の方法

では、連携方法について。ここからは、まずはProアカウントにしてから、の話になります。  
まず、選択モード中に「gd」とキーを押すか、ページ上部の「Due」と書かれている部分をクリックします。すると、日付を設定したタスクたちがずらっと日付順に並ぶページに移動します。そのページ上部には、「SendCalendar」というボタンがあるので、それをポチッと押します。  
[![Image][3]][4]

するとカレンダーのリンクをコピーするポップアップが表示されます。  
[![Image][5]][6]

これの「iCalendar link」と書かれている部分がカレンダーを表示させるための照会リンクとなります。そのリンクの下に、4つのチェック項目があるので、自分が必要だと思うものにチェックを入れた後、リンクをコピーします。  
今回はGoogleカレンダーに表示させる方法を書きますと、[GoogleカレンダーのWEBページ][7]にいき、ページ左側の「他のカレンダー」と書かれている横に表示されている「＋」ボタンを押します。  
[![Image][8]][9]

押した後、「URLで追加」を選択し、コピーしておいたリンクを入力→「カレンダーを追加」で、無事checkvist上で日付を設定したリストが、カレンダー上の、設定した日付の部分に表示されるようになります。ちなみに、ちょっとタイムラグがあるので、しばらく待つ必要があるかも、です。  
これにて無事に、checkvistをカレンダーに連携することができたと思います。  
iPhoneを使っていて、この照会したカレンダーがiPhoneでは表示されない場合は、[同期するカレンダーを選択するページ][10]に行き、照会したカレンダーにチェックを入れれば、iPhoneでもちゃんと表示されるようになると思います。もちろん、「たすくま」に取り込むことも可能です。  
これによって、[アウトライナー][11]でタスクを扱い、[タスク管理][12]をし、[デイリータスクリスト][13]である[たすくま][14]に受け渡す、という流れが非常にスムーズになりました。いい感じです。

  * [カレンダーとの連携【Pro】〜checkvistの使い方5〜 &#8211; book scrapbook][15]

 [1]: https://scrapbox.io/choiyaki-hondana/checkvist
 [2]: https://scrapbox.io/choiyaki-hondana/Google%E3%82%AB%E3%83%AC%E3%83%B3%E3%83%80%E3%83%BC
 [3]: https://gyazo.com/1ee33cc1766c9b537077de6ba1d8ffe0/thumb/1000
 [4]: https://gyazo.com/1ee33cc1766c9b537077de6ba1d8ffe0
 [5]: https://gyazo.com/7ee6cf74f4efd8ced66012251b4c717d/thumb/1000
 [6]: https://gyazo.com/7ee6cf74f4efd8ced66012251b4c717d
 [7]: https://calendar.google.com/
 [8]: https://gyazo.com/84882fcb298b559f79968b80af172580/thumb/1000
 [9]: https://gyazo.com/84882fcb298b559f79968b80af172580
 [10]: https://calendar.google.com/calendar/iphoneselect
 [11]: https://scrapbox.io/choiyaki-hondana/%E3%82%A2%E3%82%A6%E3%83%88%E3%83%A9%E3%82%A4%E3%83%8A%E3%83%BC
 [12]: https://scrapbox.io/choiyaki-hondana/%E3%82%BF%E3%82%B9%E3%82%AF%E7%AE%A1%E7%90%86
 [13]: https://scrapbox.io/choiyaki-hondana/%E3%83%87%E3%82%A4%E3%83%AA%E3%83%BC%E3%82%BF%E3%82%B9%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%88
 [14]: https://scrapbox.io/choiyaki-hondana/%E3%81%9F%E3%81%99%E3%81%8F%E3%81%BE
 [15]: https://scrapbox.io/choiyaki-hondana/%E3%82%AB%E3%83%AC%E3%83%B3%E3%83%80%E3%83%BC%E3%81%A8%E3%81%AE%E9%80%A3%E6%90%BA%E3%80%90Pro%E3%80%91%E3%80%9Ccheckvist%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B95%E3%80%9C