---
layout: default
title: Sweep
navexclude: true
---

{% for item in site.sweep %}
{% unless item.navexclude == true %}
  ## [{{ item.title }}]({{ item.url | relative_url }})

  {{ item.description }}

  {{ item.content }}
{% endunless %}
{% endfor %}
