#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""blogposts の .md を Hugo の content/ 用に変換する。

  - [[category:X]] / [[tag:Y]]  → frontmatter の categories/tags に移し、本文から消す
  - [[【Blog】T]]               → /pNNNN         （ブログ内リンク）
  - [[T]]（豆論文）             → https://thst.choiyaki.com/docs/T/
  - どちらでもない [[X]]        → リンクにせず素通し（警告を出す）
  - author / type を注入。url が無ければ date から /pYYYYMMDD を採番
"""
import os, re, sys, json, unicodedata, datetime
import urllib.parse as up

POSTS, PUBLISHED, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
THST = "https://thst.choiyaki.com/docs/"
MARK = "【Blog】"

def norm(s): return unicodedata.normalize("NFC", s).strip().lower()

FM = re.compile(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.S)
def split_fm(t):
    m = FM.match(t)
    return (m.group(1), t[m.end():]) if m else ("", t)

def fm_get(fm, key):
    m = re.search(rf'^{key}:[ \t]*(.+?)[ \t]*$', fm, re.M)
    return m.group(1).strip().strip('"\'') if m else None

def fm_lines(fm, drop):
    """drop に含まれないキーの行（複数行の値も含めて）を残す。"""
    out, skip = [], False
    for line in fm.split("\n"):
        if re.match(r'^[ \t]*-[ \t]', line) or (skip and line.startswith((" ", "\t"))):
            if not skip: out.append(line)
            continue
        m = re.match(r'^([A-Za-z_][\w-]*)[ \t]*:', line)
        skip = bool(m and m.group(1) in drop)
        if not skip: out.append(line)
    return [l for l in out if l.strip()]

# ---- 索引 -------------------------------------------------------------
published = {norm(f[:-3]): f[:-3] for f in os.listdir(PUBLISHED) if f.endswith(".md")}
posts = sorted(f for f in os.listdir(POSTS) if f.endswith(".md"))

url_of, meta = {}, {}
used_urls, dated = set(), []
for f in posts:
    raw = open(os.path.join(POSTS, f), encoding="utf-8", errors="replace").read()
    fm, body = split_fm(raw)
    stem = f[:-3]
    title = fm_get(fm, "title") or (stem[len(MARK):] if stem.startswith(MARK) else stem)
    date = fm_get(fm, "date")
    if not date:
        c = fm_get(fm, "created")
        if c and c.isdigit():
            date = datetime.datetime.fromtimestamp(int(c), datetime.timezone.utc).isoformat()
    u = fm_get(fm, "url")
    meta[f] = dict(fm=fm, body=body, title=title, date=date, url=u, stem=stem)
    if u: used_urls.add(u.strip("/"))
    else: dated.append(f)

# url が無い記事に /pYYYYMMDD を決定論的に採番（同日は -2, -3 …）
for f in dated:
    d = (meta[f]["date"] or "")[:10].replace("-", "")
    base = "p" + (d if len(d) == 8 else "00000000")
    cand, i = base, 1
    while cand in used_urls:
        i += 1; cand = f"{base}-{i}"
    used_urls.add(cand); meta[f]["url"] = "/" + cand

for f in posts:
    url_of[norm(meta[f]["stem"])] = meta[f]["url"]

# ---- 変換 -------------------------------------------------------------
CAT = re.compile(r'\[\[category:([^\]\n]+)\]\]')
TAG = re.compile(r'\[\[tag:([^\]\n]+)\]\]')
WL  = re.compile(r'\[\[([^\]\n]+)\]\]')
warn = []

def convert(f):
    m = meta[f]
    body = m["body"]
    cats = [x.strip() for x in CAT.findall(body)]
    tags = [x.strip() for x in TAG.findall(body)]
    body = TAG.sub("", CAT.sub("", body))
    body = re.sub(r'\n[ \t]*\n[ \t]*\n+', "\n\n", body).rstrip() + "\n"

    def link(mo):
        inner = mo.group(1).split("|")[0].split("#")[0].strip()
        if not inner: return mo.group(0)
        k = norm(inner)
        if k in url_of:                       # ブログ内の記事
            return f"[{inner[len(MARK):] if inner.startswith(MARK) else inner}]({url_of[k]})"
        if k in published:                    # 豆論文
            return f"[{inner}]({THST}{up.quote(published[k])}/)"
        warn.append((f, inner))
        return inner                          # 解決しないものは素のテキスト
    body = WL.sub(link, body)

    keep = fm_lines(m["fm"], {"categories", "tags", "tag", "author", "type",
                              "created", "updated", "url", "title", "date", "views"})
    out = ["---", f'title: "{m["title"]}"']
    if m["date"]: out.append(f'date: {m["date"]}')
    out.append(f'url: {m["url"]}')
    out += ["author: choiyaki", "type: post"]
    if cats: out += ["categories:"] + [f"  - {c}" for c in cats]
    if tags: out += ["tags:"] + [f"  - {t}" for t in dict.fromkeys(tags)]
    out += keep + ["---"]
    return "\n".join(out) + "\n" + body

os.makedirs(OUT, exist_ok=True)
n = 0
for f in posts:
    stem = meta[f]["stem"]
    name = (stem[len(MARK):] if stem.startswith(MARK) else stem).replace("/", "／")
    if len(name.encode()) > 200: name = name.encode()[:200].decode("utf-8", "ignore")
    dst = os.path.join(OUT, name + ".md")
    i = 1
    while os.path.exists(dst):
        i += 1; dst = os.path.join(OUT, f"{name}-{i}.md")
    open(dst, "w", encoding="utf-8").write(convert(f)); n += 1

print(f"[blogbuild] {n} 本を content/ に生成")
if warn:
    print(f"[blogbuild] 解決しなかった [[リンク]] {len(warn)} 件（素のテキストにしました）:")
    for f, w in warn[:40]: print(f"    {w}   ← {f}")
