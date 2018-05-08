---
layout: default
title: Relative Links Test
showonindexas: none
---

{% for item in site.data.content.relative_link_test.links %}
[{{ item.title }}]({{site.baseurl}}{{ item.support_file }})
{% endfor %}

* [Same dir](sweep_basic_checklist.md)
* [File in learn dir with dots](../_learn/01-news.md)
* [File in learn dir, abs]({{site.baseurl}}/_learn/01-news.md)
* [File in subfolder](subfolder/does_it_find_me.md)
* [File in File in subfolder, underscore](_othersubfolder/does_it_find_me_too.md)
* baseurl, FYI: {{ site.baseurl }}
