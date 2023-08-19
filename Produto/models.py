import hashlib, random, datetime
from django.db import models

class Produto(models.Model):
    Id = models.CharField(primary_key = True, max_length = 40)
    Nome = models.CharField(max_length = 150, null = False, blank = False)
    Descricao = models.TextField()
    Marca = models.CharField(max_length = 100, null = False, blank = False)
    Modelo = models.CharField(max_length = 100, null = False, blank = False)
    Sku = models.CharField(max_length = 10, null = False, blank = False)
    Ncm = models.CharField(max_length = 8, null = False, blank = False)
    Ean = models.CharField(max_length = 13, null = False, blank = False)
    Unidade = models.CharField(max_length = 5, null = False, blank = False)
    Preco = models.DecimalField(decimal_places = 2, max_digits = 5, default = 0.0)
    DataCriacao = models.DateTimeField()
    Ativo = models.BooleanField(default = True)
    
    def __str__(self):
        return self.Id
    
    def save(self, *args, **kwargs):
        if not self.Id:
            self.Id = hashlib.sha1(str(random.random())).hexdigest()
            self.CreatedDate = datetime.datetime.now() 
                
    class Meta:
        db_table = "Produto"