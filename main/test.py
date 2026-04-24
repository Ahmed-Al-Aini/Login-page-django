from main.models import Tolist

t=Tolist(name="Ahmed Alaini")
t.save()

print(Tolist.objects.all())