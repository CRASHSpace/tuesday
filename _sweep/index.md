---
layout: default
title: Sweep
showonindexas: none
---

Ping?

{% include weekly_basics.md %}

## Other Checklists

{% assign itemstolink = (site.sweep | where: "showonindexas" , "link") %}
{% for item in itemstolink %}
<h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
<p>{{ item.description }}</p>
{% endfor %}
