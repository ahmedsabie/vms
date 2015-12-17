<<<<<<< HEAD
from django.core.validators import RegexValidator
from django.db import models

class Organization(models.Model):
    name = models.CharField(
        unique=True,            
        max_length=75,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\-)|(:)|(\')]+$',
            ),
        ],
    )
=======
from django.core.validators import RegexValidator
from django.db import models

class Organization(models.Model):
    name = models.CharField(
        unique=True,            
        max_length=75,
        validators=[
            RegexValidator(
                r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\-)|(:)|(\')]+$',
            ),
        ],
    )
>>>>>>> 0852fdebbc3dcc259d16802e7949d56c55db1144
