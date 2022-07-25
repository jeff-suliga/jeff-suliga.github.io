---
layout: puzzle
puzzle-title: Spotlight
flavortext:
puzzle-folder: Spotlight
img-height: 500
answer: SNOOP
answer-type: a single word
---

<p align="center">
    {% if page.img-path %}
    <img src="{{ site.imgurl }}/{{ page.puzzle-folder }}/{{ page.img-path }}" alt="{{ page.puzzle-title }}" style="width:100%;height:{{page.img-height}}px;object-fit:contain;">
    {% else %}
    <img src="{{ site.imgurl }}/{{ page.puzzle-folder }}/{{ page.puzzle-folder }}.jpg" alt="{{ page.puzzle-title }}" style="width:100%;height:{{page.img-height}}px;object-fit:contain;">
    {% endif %}
</p>