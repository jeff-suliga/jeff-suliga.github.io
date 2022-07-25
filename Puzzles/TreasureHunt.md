---
layout: puzzle
puzzle-title: Treasure Hunt
flavortext: This perplexing map seems to have been made such that no average treasure hunter would stumble upon its bounty.<br><br>Each of the cryptic phrases reference two different hidden keywords. Decode each of these pairs and <em>cross-reference</em> them to claim its hidden prize, X marks the spot!
puzzle-folder: TreasureHunt
img-height: 700
answer: TORUS
answer-type: a single word
---

<p align="center">
    {% if page.img-path %}
    <img src="{{ site.imgurl }}/{{ page.puzzle-folder }}/{{ page.img-path }}" alt="{{ page.puzzle-title }}" style="width:100%;height:{{page.img-height}}px;object-fit:contain;">
    {% else %}
    <img src="{{ site.imgurl }}/{{ page.puzzle-folder }}/{{ page.puzzle-folder }}.jpg" alt="{{ page.puzzle-title }}" style="width:100%;height:{{page.img-height}}px;object-fit:contain;">
    {% endif %}
</p>
