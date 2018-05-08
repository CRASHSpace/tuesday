---
collection: sweep
layout: page
name: zone_0_weekly_basics.md
title: Zone 0 - Weekly Basics
showonindexas: full
---

I'm here!

{% assign itemstoshow = (site.sweep | where: "zone" , 0) %}
{% for item in itemstoshow %}
* {{ item.weekly_todo_text }}[more]({{ item.url | relative_url }})
{% endfor %}
