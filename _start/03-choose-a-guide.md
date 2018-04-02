---
collection: start
layout: page
name: 03-choose-a-guide.md
title: Choose a guide
---

Everyone will have different priorities, so pick a guide or set of tips that reflects what's important to you.

Judge a guide by the same standards used for all primary resources, with a couple of additions.

* Who wrote it
* Who's their audience
* When was it written?
* Where did they get their information?
* What's their benefit if you believe them?
* What's the plan to keep it up to date?

## General Guides

These guides provide and overview of loads of topics and provide mountains of things to do. Pick one guide, and then do one thing from it a week.

{% for item in site.data.content.privacy_security_guides.gsg %}
<p><a class="page-link" href="{{ item.url | relative_url }}" alt="{{ item.title }}">{{ item.title }}</a><br>{{ item.description }}</p>
{% endfor %}
