from djongo import models

class Conversation(models.Model):
    _id=models.ObjectIdField()
    user_input=models.TextField()
    response=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input