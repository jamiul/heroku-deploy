from django.db import models

# Create your models here.

class quoteCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)  

    quote_category = models.ForeignKey(
        'quoteCategory',
        on_delete = models.CASCADE
    )  

    def __str__(self):
        if len(self.quote) > 60:
            return self.quote[:60] + "....."

        return self.quote   