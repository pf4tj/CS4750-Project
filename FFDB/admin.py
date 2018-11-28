from django.contrib import admin

from FFDB.models import League
from FFDB.models import Division
from FFDB.models import Team
from FFDB.models import Player
from FFDB.models import Week
from FFDB.models import Matchup
from FFDB.models import Playerprojection
from FFDB.models import Tradingblock

class DivisionInLine(admin.TabularInline):
    model = Division

class TeamInLine(admin.TabularInline):
    model = Team
    
class PlayerInLine(admin.TabularInline):
    model = Player

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['league_id', 'name', 'current_week']
    #inlines = [DivisionInLine, ]
    
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['division_id', 'name', 'league']
    #inlines = [TeamInLine, ]
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'division']
    #inlines = [PlayerInLine, ]
    
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_id', 'name', 'position', 'NFL_team', 'league_team']
    
@admin.register(Matchup)
class MatchupAdmin(admin.ModelAdmin):
    list_display = ['matchup_id', 'home_team', 'away_team', 'week']
    
@admin.register(Playerprojection)
class PlayerprojectionAdmin(admin.ModelAdmin):
    list_display = ['player']
    
@admin.register(Tradingblock)
class Tradingblock(admin.ModelAdmin):
    list_display = ['team', 'team_needs', 'team_availables', 'interested_in']


# Register your models here.
