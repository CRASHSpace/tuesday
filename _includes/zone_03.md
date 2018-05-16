{% assign itemstoshow = (site.sweep | where: "zone" , "permission" | sort: 'list_order') %}
{% for item in itemstoshow %}
* {{ item.weekly_todo_text }} [(more)]({{ item.url | relative_url }})
{% endfor %}
