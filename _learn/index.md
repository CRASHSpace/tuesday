---
layout: default
title: Learn More
navexclude: true
---

TEST!!!

{% for item in site.learn %}
{% unless item.navexclude == true %}
  <h2><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h2>
  <p>{{ item.description }}</p>
{% endunless %}
{% endfor %}
