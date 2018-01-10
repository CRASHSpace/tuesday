---
layout: default
title: Sweep
navexclude: true
---

{% for item in site.sweep %}
{% unless item.navexclude == true %}
  <h2>{{ item.title }}</h2>
  <p>{{ item.description }}</p>
  <p><a href="{{ item.url | relative_url }}">{{ item.title }}</a></p>
  {{ item.content }}
{% endunless %}
{% endfor %}
