django-smart-truncate
=====================

# Django Template Smart Truncate
## I dont like to cut words with the normal truncate from django so I created a smart one.
You shoud pass 2 arguments, the min and de max chars.
The template tag will truncate the text on the last space

```
{% load smarttruncate %}

<div> 
    My description is {{ description|smartcut:"50:70" }}
</div
```

This is specially usefull when you don't have controll over the meta titles,descriptions...etc. 
And you can still respect the max lenght. 


```
<meta property="og:title" content="{{ description|smartcut:"50:60" }}">
<meta property="og:description" content="{{ meta.description|smartcut:"120:158" }}">
```
