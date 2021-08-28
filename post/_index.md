---
title: "Recent Post"
date: 2021-03-10T23:37:42+09:00
---
<div class="widget-recent widget">
	<h4 class="widget__title">{{ T "recent_title" }}</h4>
	<div class="widget__content">
		<ul class="widget__list">
  			{{ range first 5 .Site.RegularPages.ByDate.Reverse }}
    		<li class="widget__item"><a href="{{.RelPermalink}}">{{.Title}}</a><time>{{.Date.Format "2006-01-02"}}</time></li>
  			{{ end }}
		</ul>
	</div>
</div>