from django.db import models
from apps.log_reg.models import User

class Tarot(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    suit = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    meaning_up = models.CharField(max_length=300)
    meaning_rev = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __repr__(self):
        return f"ID:{self.id}, Name:{self.name}, Image URL:{self.image}, Category:{self.category}, Suit:{self.suit}, Description:{self.description}, Meaning:{self.meaning_up}, Reversed Meaning:{self.meaning_rev}"

class ThreeCardReading(models.Model):
    past = models.ForeignKey(Tarot, related_name="past_cards")
    present = models.ForeignKey(Tarot, related_name="present_cards")
    future = models.ForeignKey(Tarot, related_name="future_cards")
    user = models.ForeignKey(User, related_name="three_card_readings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"ID:{self.id}, Reading Name:{self.name}, Reading Description:{self.description}"


class FourCardReading(models.Model):
    name = models.CharField(max_length=50)
    you = models.ForeignKey(Tarot, related_name="you_cards")
    unknown = models.ForeignKey(Tarot, related_name="unknown_cards")
    known = models.ForeignKey(Tarot, related_name="known_cards")
    action = models.ForeignKey(Tarot, related_name="action_cards")
    user = models.ForeignKey(User, related_name="four_card_readings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"ID:{self.id}, Reading Name:{self.name}, Reading Description:{self.description}"