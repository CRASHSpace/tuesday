---
layout: default
title: Start Here
---

{% for start in site.start %}


<a href="{{ start.url | prepend: site.baseurl }}">
        <h2>{{ start.title }}</h2>
</a>

<p class="post-excerpt">{{ start.description | truncate: 160 }}</p>

{% endfor %}
