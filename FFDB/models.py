from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator
# Create your models here.

POSITION_CHOICES= (
	('QB','QB'),
	('RB','RB'),
	('WR','WR'),
    ('TE','TE'),
    ('NA','NA'),
)

NFL_TEAMS= (
    ('Arizona Cardinals', 'Arizona Cardinals'),
    ('Atlanta Falcons', 'Atlanta Falcons'),
    ('Baltimore Ravens', 'Baltimore Ravens'),
    ('Buffalo Bills','Buffalo Bills'),
    ('Carolina Panthers', 'Carolina Panthers'),
    ('Chicago Bears','Chicago Bears'),
    ('Cincinnati Bengals','Cincinnati Bengals'),
    ('Cleveland Browns','Cleveland Browns'),
    ('Dallas Cowboys', 'Dallas Cowboys'),
	('Denver Broncos','Denver Broncos'),
	('Detroit Lions','Detroit Lions'),
	('Green Bay Packers','Green Bay Packers'),
	('Houston Texans','Houston Texans'),
	('Indianapolis Colts','Indianapolis Colts'),
	('Jacksonville Jaguars','Jacksonville Jaguars'),
	('Kansas City Chiefs','Kansas City Chiefs'),
	('Miami Dolphins','Miami Dolphins'),
	('Minnesota Vikings','Minnesota Vikings'),
	('New England Patriots','New England Patriots'),
	('New Orleans Saints','New Orleans Saints'),
	('New York Giants','New York Giants'),
	('New York Jets','New York Jets'),
	('Oakland Raiders','Oakland Raiders'),
	('Philadelphia Eagles','Philadelphia Eagles'),
	('Pittsburgh Steelers','Pittsburgh Steelers'),
	('Los Angeles Rams', 'Los Angeles Rams'),
	('Los Angeles Chargers','Los Angeles Chargers'),
	('San Francisco 49ers','San Francisco 49ers'),
	('Seattle Seahawks','Seattle Seahawks'),
	('Tampa Bay Buccaneers','Tampa Bay Buccaneers'),
	('Tennessee Titans','Tennessee Titans'),
	('Washington Redskins','Washington Redskins'),
)

class Our_User(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	owns_team = models.BooleanField(default = False)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Our_User.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.our_user.save()

	def __str__(self):
		return self.user.username

class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default = "No League Name", unique=True)
    current_week = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default = "No Division Name", unique=True)
    league = models.ForeignKey(League, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Our_User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default = "No Team Name", unique=True)
    wins = models.IntegerField(default = 0)
    loses = models.IntegerField(default = 0)
    ties = models.IntegerField(default = 0)
    current_points = models.IntegerField(default = 0)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default = "")
    position = models.CharField(max_length=2,choices=POSITION_CHOICES,default='NA')
    starter = models.BooleanField()
    current_points = models.IntegerField(default = 0)
    NFL_team = models.CharField(choices=NFL_TEAMS,default=None, max_length=100)
    league_team = models.ForeignKey(Team, on_delete = models.SET_DEFAULT, default=None, null=True, blank=True, )

    def __str__(self):
        return self.name + '(' + self.position + ')'


class Week(models.Model):
    week_number = models.IntegerField(primary_key=True)
    league = models.ForeignKey(League, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.week_number)

class Matchup(models.Model):
    matchup_id = models.AutoField(primary_key=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='home_team')
    home_team_points = models.IntegerField(default = 0)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='away_team')
    away_team_points = models.IntegerField(default = 0)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    concluded = models.BooleanField()

    def __str__(self):
        return self.home_team.name + " vs. " + self.away_team.name + " Week(" + str(self.week.week_number) + ")"

class Playerprojection(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    pass_yards = models.IntegerField(default=0)
    rush_yards = models.IntegerField(default=0)
    receptions = models.IntegerField(default=0)
    receiving_yards = models.IntegerField(default=0)
    touchdowns = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.player.name + "'s Projected Points: " + str(self.points)

class Tradingblock(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, primary_key=True)
    team_needs = models.CharField(max_length=2,choices=POSITION_CHOICES,default='NA')
    team_availables = models.CharField(max_length=2,choices=POSITION_CHOICES,default='NA')
    interested_in = models.ForeignKey(Player, on_delete=models.SET_DEFAULT, default=None)
