---
layout: default
title: Learn More
navexclude: true
---

{% for item in site.learn %}
{% unless item.navexclude == true %}
  <h2>{{ item.title }}</h2>
  <p>{{ item.description }}</p>
{% endunless %}
{% endfor %}
