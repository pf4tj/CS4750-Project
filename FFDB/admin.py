from django.contrib import admin

from FFDB.models import League
from FFDB.models import Division
from FFDB.models import Team
from FFDB.models import Player
from FFDB.models import Week
from FFDB.models import Matchup
from FFDB.models import Playerprojection
from FFDB.models import Tradingblock
from FFDB.models import Our_User

class DivisionInLine(admin.TabularInline):
    model = Division
    extra = 0

class TeamInLine(admin.TabularInline):
    model = Team
    extra = 0
    
class PlayerInLine(admin.TabularInline):
    model = Player
    extra = 0

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['league_id', 'name', 'current_week']
    inlines = [DivisionInLine, ]
    
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['division_id', 'name', 'league']
    inlines = [TeamInLine, ]
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'division']
    inlines = [PlayerInLine, ]
    
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
    
@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ['week_number', 'league']
    
@admin.register(Our_User)
class Our_UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'owns_team']


# Register your models here.
