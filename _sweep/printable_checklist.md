---
collection: sweep
layout: checklist
name: checklist.md
title: Basic Checklist
navexclude: true
---
<text x="0" y="0">{{page.title}} for  {{ "now" | date: "%Y-%m-%d" }}</text>
<g id="list" transform="translate(0, 150)">
{% assign todolist_count = '' %}
{% for item in site.data.basic_weekly_checklist.bwc %}
  <rect x="30" y="{{ todolist_count.size | times: 150.0 | minus: 65}}" width="75" height="75" style="fill:rgb(255,255,255);stroke:rgb(153,153,153);stroke-width:2" />
  <text x="150" y="{{ todolist_count.size | times: 150.0 }}">{{ item.title }}</text>
  {% assign todolist_count = todolist_count | append: 'x' %}
{% endfor %}
</g>
