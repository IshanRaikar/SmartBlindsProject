from django.db import models

# Create your models here.
class Room(models.Model):
        roomId = models.AutoField(primary_key = True)
        roomName = models.CharField(max_length=50, unique=True)
        def __str__(self):
                return f"Room {self.roomId}: {self.roomName}"

class Window(models.Model):
        DIRECTIONS = [
                ('N', 'North'), ('NE', 'Northeast'), ('E', 'East'), ('SE', 'Southeast'),
                ('S', 'South'), ('SW', 'Southwest'), ('W', 'West'), ('NW', 'Northwest')
        ]

        windowId = models.AutoField(primary_key=True)
        facing = models.CharField(max_length=2, choices=DIRECTIONS, null=False, blank=False)
        room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='windows')

        def __str__(self):
                return f"Window {self.windowId} facing {self.facing} in Room {self.room.roomName}"