from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Extends the default Django User with gamification data.
    A profile is automatically created for every new User via a signal.
    """
    STATUS_CHOICES = [
        ('🚀', 'Coding'),
        ('📚', 'Studying'),
        ('🏆', 'Competing'),
        ('💡', 'Building'),
        ('💤', 'AFK'),
    ]

    user           = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    code_points    = models.IntegerField(default=0)
    stars_earned   = models.IntegerField(default=0)
    challenges_solved = models.IntegerField(default=0)
    bio            = models.CharField(max_length=120, blank=True, default='', help_text='Short bio (max 120 chars)')
    status_emoji   = models.CharField(max_length=4, blank=True, default='🚀', choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} — {self.code_points} pts"

    @property
    def global_rank(self):
        """Returns the user's rank on the leaderboard (by code_points, descending)."""
        return UserProfile.objects.filter(code_points__gt=self.code_points).count() + 1

    @property
    def total_users(self):
        """Total number of users for rank percentage calculation."""
        return UserProfile.objects.count()

    @property
    def rank_percentile(self):
        """Returns what top percentage the user is in."""
        total = self.total_users
        if total <= 1:
            return 100
        rank = self.global_rank
        return max(1, int((rank / total) * 100))


# ── Signal: auto-create a UserProfile whenever a new User is registered ──────
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    UserProfile.objects.get_or_create(user=instance)
