django-smart-truncate
=====================

# Django Template Smart Truncate
## I dont like to cut words with the normal truncate from django so i created a smart one.
### You shoud pass 2 arguments, the min and de max chars.
### The template tag will truncate the text on the last space

```
{% load smarttruncate %}

<div> 
    My description is {{ description|smartcut:"50:70" }}
</div
```
