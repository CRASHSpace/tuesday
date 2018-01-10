---
layout: default
title: Engage
navexclude: true
---

{% for item in site.engage %}
{% unless item.navexclude == true %}
  <h2><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h2>
  <p>{{ item.description }}</p>
{% endunless %}
{% endfor %}
