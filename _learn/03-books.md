---
collection: learn
layout: page
name: 03-books.md
title: Books
description: A small collection of books on helpful topics. The most up to date technical information tends to be online, which is why you won't see any books like that here.
---


{% for item in site.data.books.books %}
<p>{{ item.title }}
<br>{{ item.author }}, {{ item.year_published }}
<br><a class="page-link" href="{{ item.publisher_url }}">Publisher's Link</a> | <a class="page-link" href="{{ item.amz_affiliate_url }}">Amazon Affliate Link</a>
</p>
{% endfor %}
