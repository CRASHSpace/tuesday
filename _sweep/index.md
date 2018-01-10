---
layout: default
title: Start Here
navexclude: true
---

{% for item in site.sweep %}
{% unless item.navexclude == true %}
  <h2><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h2>
  <p>{{ item.description }}</p>
  {{  item.content  }}
{% endunless %}
{% endfor %}
