from django.db import models

from django.db import models

class Test(models.Model):
    id = None
    No_2 = models.CharField(max_length=50)
    Description = models.TextField()
    
    class Meta:
        #db_table = 'db_test.dbo.tab_test'
        db_table = 'db_test.dbo.tab_test'
        db_tablespace = 'secondary'
        managed = False