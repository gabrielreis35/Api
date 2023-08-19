import hashlib, random, datetime
from django.db import models
from Produto.models import Produto

class Estoque(models.Model):
    Id = models.CharField(primary_key = True, max_length = 40),
    Quantidade = models.IntegerField(null = True, blank = False),
    QtdSeparacao = models.IntegerField(null = True, blank = False),
    DataCriacao = models.DateTimeField()
    Ativo = models.BooleanField(default = True)
    Produto = models.ForeignKey(Produto, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.Id
    
    def save(self, *args, **kwargs):
        if not self.Id:
            self.Id = hashlib.sha1(str(random.random())).hexdigest()
            self.CreatedDate = datetime.datetime.now() 
                
    class Meta:
        db_table = "Estoque"