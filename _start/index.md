---
layout: default
title: Start Here
navexclude: true
---

Welcome. This site is meant to help folks organize their own Tuesday Sweep. Fork it, update it, make suggestions.

What's a Tuesday Sweep? Well, maintaining your own privacy and security online works like housework, it's important but typically boring stuff that just needs to be done. So just pick a day and a time and do it. We've picked Tuesdays.

If you haven’t been following along, it’s okay. You’re not behind, you’re just where you are. Never forget that. If you miss a week, shake it off and just pick up where you are.

Privacy and security has become quite the trendy topic. There are lots of getting started guide on the internet. We'll list them as we find them, but most of them don't give you the tools on how to stay organized about the process itself. That's where the Tuesday Sweep fits in with its own first steps. 

{% for item in site.start %}
{% unless item.navexclude == true %}
  <h2>{{ item.title }}</h2>
  <p>{{ item.description }}</p>
  <p><a href="{{ item.url }}">{{ item.title }}</a></p>
{% endunless %}
{% endfor %}
