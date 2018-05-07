---
layout: default
title: Sweep
showonindexas: none
---

{% assign itemstoshow = (site.sweep | where: "showonindexas" , "full") %}
{% for item in itemstoshow %}
<h2><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h2>
<p>{{ item.description }}</p>
{{ item.content }}
{% endfor %}

## Other Checklists

{% assign itemstolink = (site.sweep | where: "showonindexas" , "link") %}
{% for item in itemstolink %}
<h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
<p>{{ item.description }}</p>
{% endfor %}
