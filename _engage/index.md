---
layout: default
title: Engage
navexclude: true
---

{% for item in site.engage %}
{% unless item.navexclude == true %}
  <h2>{{ item.title }}</h2>
  <p>{{ item.description }}</p>
  <p><a href="{{ item.url | relative_url }}">{{ item.title }}</a></p>
{% endunless %}
{% endfor %}
