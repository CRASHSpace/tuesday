---
collection: sweep
layout: page
name: zone_0_weekly_basics.md
title: Zone 0 - Weekly Basics
showonindexas: full
---

Basic tasks that prevent the bulk of the most common problems.

{% assign itemstoshow = (site.sweep | where: "zone" , "basics" | sort: 'list_order') %}
{% for item in itemstoshow %}
* {{ item.weekly_todo_text }} [(more)]({{ item.url | relative_url }})
{% endfor %}
