
from django.db import models
from clients.models import ClientModel
from stock.models import StockProduct


class Chat(models.Model):
    user = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    client_question = models.ForeignKey(ClientModel, on_delete=models.DO_NOTHING, related_name="client_question")
    client_seller = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name="client_seller")
    

class MessageConsumer(models.Model):
    question = models.TextField()
    

class MessageSeller(models.Model):
    answer = models.TextField(blank=True, default="")
    @property
    def is_answer(self):
        return bool(self.answer)
