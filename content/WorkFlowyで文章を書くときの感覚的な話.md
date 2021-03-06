---
title: WorkFlowyで文章を書くときの感覚的な話
author: choiyaki
type: post
date: 2016-08-31T09:00:02+00:00
url: /p151
views:
  - 1393
categories:
  - 雑記
tags: ["アウトライナー","ブログ","書くこと"]
---
WorkFlowyを使って文章を書くのは、「ブログの書き始め」がほとんどです。  
どんなことを書こうかなぁとぼんやりと考え、何か思いついたことについてだぁーと書き出す。いわゆるフリーライティングをおこなうとき。  
また、書き出した文章はそのままでは他の人が読んでも、というか、時間がたってから自分が読んでもおそらくなんのこっちゃわからないので、ちゃんと他の人が読んでもわかるように整理し、組み立てていくとき。  
FireFoxをWorkFlowyのための「[執筆専用ブラウザ][1]」として使って、書き始めから整理し、組み立てるまでをおこなっています。  
で、そこから先は他のエディタに書いたものを移し、あるいはそれまでの書いたものを見ながら他のエディタで文章を仕上げていく、というのがいつものぼくのパターンです。

## プレーンテキストに階層化が加わったもの

途中まではWorkFlowyを使って文章を書いていくわけですが、ブログほどの文章であればとくに階層化せず、文章たちの順番を移動させたり、改行を多く入れることで文章の塊を見えやすくしたりするくらいで仕上げまで持っていけることが少なくありません。  
ブログを書くときには、階層化する必然性はそんなにない、ということです。せいぜい2階層くらいまで扱うことができればいいんではないか、と思っていました。  
とはいえ、必要であればいつでも階層化できるという安心感は、かなり重要であるとも思うので、文章を書き始め、整理し、組み立てていくときにはWorkFlowyが安心なわけです。

WorkFlowyで文章を書く、となれば、階層化も利用しつつ文章を組み立てていきます。  
階層によって組み立てたあとは、文章をブログのエントリとして仕上げる際には、階層を「見出し」という形に変換し、整えていきます  
でも、ぼくはその方法が、見出しを文章を階層化することによって表現するのがしっくりきませんでした。  
WorkFlowyを使い始める以前からずっとマークダウン記法によってブログ記事を仕上げてきたから、なのでしょう。見出しは、マークダウン記法のように、「ここを見出しにしますよ」ってしるしを入れることで表現したいってどうしても思ってしまうんです。  
マークダウン記法に慣れているので、多くの文章が連なっている中で、ある文章を見出しにしたければ、その文章に「##」をつければいい。やめたければ「##」を消せばいい。  
なので、文章をWorkFlowyで書くときには、プレーンテキストに階層化が加わったもの、くらいに考えておくのがしっくりきているようだと気付きました。

## 見出しをつけたり消したりで、、、

見出しを階層化で表現するためには、見出しにしたい文章の後に続く文章たちをまるごとごっそり見出し文章の階層の下に入れなくちゃいけない。がために、なんだか一度見出しを定めてしまうと、ちょっと動かしにくさが出てしまう。気がする。  
文章たちの流動性が下がってしまう、気がする。

  * 見出しにあたる文章 
      * そこに続いていく文章
      * さらにそこに続いていく文章

よりも

\## 見出しにあたる文章  
そこに続いていく文章  
さらにそこに続いていく文章

のほうが、各々の自由度が高い、気がする。  
マークダウンによる表現のほうが、手軽に感じるんです。手軽に感じるので、文章の流動性を高いままに保つことができる、気がする。  
文章を書くときには、文章たちをリストっぽくは扱いたくないのかもしれません。「・」がいらないな、と感じるのも、「・」があったらどうしてもリストっぽくみえてしまうから、なのかも。

すべてフィーリングの話なので、もしかしたらぼくに限った話なのかもしれませんが。

なので、大きな構造を必要としないブログの文章では、「見出しですよ」を意味する「##」をつけたり消したりしながら、整理し、組み立てていくことになります。  
ある文章に「##」をつけてそれより下に連なる文章をグルーピングしたり、見出しを新たに書き加えたり。  
書き進めるうちに「ん？」となり、「##」を取り除いて一度フラットに戻したり。  
気付きました。ぼくは「##」をつけたり消したりして「シェイク」をおこなってるんやな、と。

## おわりに

ってなことを考えていると、だんだん「最後までWorkFlowyで完結させたい」と思うようになってきました。  
というのも、iMacとWindowsPCのeeebookとiPhoneと、というように、3つのデバイスでテキストを扱い、ブログを書いています。  
WorkFlowyで完結できれば、書く作業も、文章を管理する場所にもなってくれることになります。こんな快適なことはない。  
その際にほしいのが、マークダウン記法をシンタックスハイライトする機能。これがないために、仕上げの段階をほかのエディタにまかせている、と言えそうなので。  
というわけで、そこからハイライトをなんとか実装できないものか、といろいろとあがくことになりました。  
続きます。

では、お読みいただきありがとうございました。

 [1]: https://choiyaki.com/?p=106