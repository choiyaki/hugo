# hugo

ブログ https://choiyaki.com のビルダー。**記事はこのリポジトリには無い。**

## 構成

| | |
|---|---|
| `blogbuild.py` | 記事（Markdown）を Hugo の `content/` 用に変換する前処理。ここが実質の本体 |
| `build.sh` | Netlify から呼ばれるビルド本体。豆論文を clone → `blogbuild.py` → `hugo --gc --minify` |
| `config.toml` | Hugo 設定。`markup.goldmark.renderer.unsafe = true`（生 HTML を通す） |
| `static/` | サイトから直接配信されるファイル。`static/x.png` → `https://choiyaki.com/x.png` |
| `themes/` `layouts/` `resources/` | 見た目 |

## ビルドの流れ

Netlify サイトは **記事リポジトリ [choiyaki/blogposts](https://github.com/choiyaki/blogposts) に接続されている。**

```
blogposts に push
  → Netlify が起動
  → blogposts の *.md を __posts/ へ退避
  → このリポジトリ(hugo)を __hugo/ に clone      ← ここで最新の hugo が取得される
  → build.sh
      → choiyaki/Published を __published/ に clone（豆論文リンクの解決に使う）
      → blogbuild.py __posts __published content/
      → hugo --gc --minify → public/
```

**このリポジトリに push しただけではサイトは再ビルドされない。** blogposts が push
されて初めて反映される。逆に言うと、ビルダーを直したいときは先にこちらを push して
おけば、次の記事更新のタイミングで安全に切り替わる。

## blogbuild.py がやること

- `[[📄タイトル]]` → `[タイトル](/pNNNN)`（ブログ内リンク）
- `[[豆論文のタイトル]]` → `[…](https://thst.choiyaki.com/docs/…/)`
- `[[X|表示テキスト]]` → 別名をリンク文字列に使う
- どちらにも解決しない `[[X]]` → 素のテキストにして、ビルドログに警告を出す
- `[[category:X]]` / `[[tag:Y]]` → frontmatter の `categories` / `tags` へ移し、本文から消す
- `<!-- ... -->` → 本文から除去する
- frontmatter に `url` が無ければ `date` から `/pYYYYMMDD` を採番する

---

## 触るときに知っておいてほしいこと（判断済み）

2026-08-29 に blogposts と合わせて棚卸しした。以下は「調べたうえで、あえてこの形にしている」もの。

### `MARK` / `MARKS` — 記事ファイル名の接頭辞

```python
MARK  = "📄"
MARKS = ("📄", "【Blog】")
```

記事のファイル名は `📄タイトル.md`。表示時にこの接頭辞を落とす。

- `MARKS` に旧接頭辞 `【Blog】` を残してあるのは移行期間のため。**記事側とビルダー側の
  どちらが先に反映されても表示が壊れないようにする安全装置。** couchNotes の同期が
  一巡して落ち着いたら外してよい。
- 接頭辞は記事の名前空間として機能している。**外す提案をしないこと。** 外すと
  Published のページ名と10件が衝突し、`url_of` を `published` より先に見る仕様のため、
  豆論文を指すはずのリンク13本がブログ記事に吸われる（警告も出ない）。
- 絵文字は単一コードポイントのものを使う。異体字セレクタ付き（`🗺️` = U+1F5FA U+FE0F）は
  同名判定が壊れやすい。実際 Published には `🗺️` と `🗺️️` が混在してしまっている。

### `strip_comments()` — HTML コメントの除去

`config.toml` が `unsafe = true` なので、記事の `<!-- -->` は放っておくと HTML に出る。
記事には執筆前の構想メモや Discord からの引用が15箇所あり、**これは記事側に残す方針**なので、
ビルダー側で確実に落としている。

- `hugo --minify` も結果的にコメントを消すが、**minify に依存しない。** `build.sh` から
  `--minify` を外しても漏れないようにするのが `strip_comments()` の役目。
- コードブロック／コードスパンの中の `<!-- -->` は残す（記述例の可能性があるため）。

### `link()` の別名対応

`[[X|表示]]` の別名を表示テキストに使う。これが無いと、文中に埋め込むリンク
（「前回」「先日紹介した」など）を wikilink で書けず、記事の文章が壊れる。
**`inner.split("|")[0]` に戻さないこと。**

### 解決順は `url_of` → `published`

ブログ記事を先に見る。同名のページが両方にある場合、ブログ記事が勝つ。
現状 blogposts と Published に同名のファイルは無いが、`📄` 接頭辞がそれを担保している。

### `static/` に置いている画像

| | |
|---|---|
| `static/img/math/*.png`（12枚） | 三角比の記事の図版。元は Scrapbox 配信だったが、302 →有効期限300秒の署名付き URL という経路で表示されない環境があったため取り込んだ |
| `static/wp-content/uploads/…` | WordPress 時代の画像 |
| `static/_redirects` | 旧 WordPress の `?p=ID` 形式を `/pID` に飛ばす |

記事側からは `https://choiyaki.com/img/math/...` と**絶対 URL で**参照している。
ルート相対にすると Obsidian でプレビューできなくなるため。

### ビルドログの警告について

`解決しなかった [[リンク]] N 件` は異常ではない。2026-08-29 時点で2件あり、どちらも
`[[「操作」に関しては紙にはかなわないので、デジタルでは、scrapboxのリンクによる
つながりでカバーする]]`。couchNotes にはあるが Published に未公開のため解決しない。
publish すれば自動的に thst へのリンクになる。

### 記事側の方針

リンクの張り方（単語をリンクにしない、キーワードはタグで、ページどうしだけリンクする）は
blogposts の README に書いてある。ビルダーを触る前にそちらも読むこと。
