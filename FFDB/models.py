from django.db import models
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
    ( 'Dallas Cowboys','Dallas Cowboys')
    # Denver BroncosDenver Broncos
    # Detroit LionsDetroit Lions
    # Green Bay PackersGreen Bay Packers
    # Houston TexansHouston Texans
    # Indianapolis ColtsIndianapolis Colts
    # Jacksonville JaguarsJacksonville Jaguars
    # Kansas City ChiefsKansas City Chiefs
    # Miami DolphinsMiami Dolphins
    # Minnesota VikingsMinnesota Vikings
    # New England PatriotsNew England Patriots
    # New Orleans SaintsNew Orleans Saints
    # New York GiantsNew York Giants
    # New York JetsNew York Jets
    # Oakland RaidersOakland Raiders
    # Philadelphia EaglesPhiladelphia Eagles
    # Pittsburgh SteelersPittsburgh Steelers
    # St. Louis RamsSt. Louis Rams
    # San Diego ChargersSan Diego Chargers
    # San Francisco 49ersSan Francisco 49ers
    # Seattle SeahawksSeattle Seahawks
    # Tampa Bay BuccaneersTampa Bay Buccaneers
    # Tennessee TitansTennessee Titans
    # Washington RedskinsWashington Redskins
)

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
    owner = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, default = "No Team Name", unique=True)
    wins = models.IntegerField(default = 0)
    loses = models.IntegerField(default = 0)
    ties = models.IntegerField(default = 0)
    current_points = models.IntegerField(default = 0)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name + " " + self.owner

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default = "")
    position = models.CharField(max_length=2,choices=POSITION_CHOICES,default='NA')
    starter = models.BooleanField()
    current_points = models.IntegerField(default = 0)
    NFL_team = models.CharField(choices=NFL_TEAMS,default=None, max_length=100)
    league_team = models.ForeignKey(Team, on_delete = models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.name


class Week(models.Model):
    week_number = models.IntegerField(primary_key=True)
    league = models.ForeignKey(League, on_delete = models.CASCADE)

class Matchup(models.Model):
    matchup_id = models.AutoField(primary_key=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='home_team')
    home_team_points = models.IntegerField(default = 0)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='away_team')
    away_team_points = models.IntegerField(default = 0)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)

    def __str__(self):
        return self.home_team.name + " vs. " + self.away_team.name + " Week(" + week.week_number + ")"

class Playerprojection(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    pass_yards = models.IntegerField(default=0)
    rush_yards = models.IntegerField(default=0)
    receptions = models.IntegerField(default=0)
    receiving_yards = models.IntegerField(default=0)
    touchdowns = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.player.name + "'s Projected Points: " + self.points

class Tradingblock(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, primary_key=True)
    team_needs = models.CharField(max_length=2,choices=POSITION_CHOICES,default='NA')
    team_availables = models.CharField(max_length=2,choices=POSITION_CHOICES,default='NA')
    interested_in = models.ForeignKey(Player, on_delete=models.SET_DEFAULT, default=None)
