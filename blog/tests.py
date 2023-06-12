from django.test import TestCase
from blog.models import *

p = Post.objects.all()

print(p)
