# Generated by Django 2.1.1 on 2018-11-29 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('division_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='No Division Name', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('league_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='No League Name', max_length=100, unique=True)),
                ('current_week', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('matchup_id', models.AutoField(primary_key=True, serialize=False)),
                ('home_team_points', models.IntegerField(default=0)),
                ('away_team_points', models.IntegerField(default=0)),
                ('concluded', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Our_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owns_team', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('position', models.CharField(choices=[('QB', 'QB'), ('RB', 'RB'), ('WR', 'WR'), ('TE', 'TE'), ('NA', 'NA')], default='NA', max_length=2)),
                ('starter', models.BooleanField()),
                ('current_points', models.IntegerField(default=0)),
                ('NFL_team', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Carolina Panthers', 'Carolina Panthers'), ('Chicago Bears', 'Chicago Bears'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonville Jaguars'), ('Kansas City', 'Kansas City'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New England Patriots', 'New England Patriots'), ('New Orleans Saints', 'New Orleans Saints'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Oakland Raiders', 'Oakland Raiders'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('St. Louis Rams', 'St. Louis Rams'), ('San Diego Chargers', 'San Diego Chargers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seattle Seahawks', 'Seattle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Redskins', 'Washington Redskins')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='No Team Name', max_length=100, unique=True)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('ties', models.IntegerField(default=0)),
                ('current_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('week_number', models.IntegerField(primary_key=True, serialize=False)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FFDB.League')),
            ],
        ),
        migrations.CreateModel(
            name='Playerprojection',
            fields=[
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='FFDB.Player')),
                ('pass_yards', models.IntegerField(default=0)),
                ('rush_yards', models.IntegerField(default=0)),
                ('receptions', models.IntegerField(default=0)),
                ('receiving_yards', models.IntegerField(default=0)),
                ('touchdowns', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tradingblock',
            fields=[
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='FFDB.Team')),
                ('team_needs', models.CharField(choices=[('QB', 'QB'), ('RB', 'RB'), ('WR', 'WR'), ('TE', 'TE'), ('NA', 'NA')], default='NA', max_length=2)),
                ('team_availables', models.CharField(choices=[('QB', 'QB'), ('RB', 'RB'), ('WR', 'WR'), ('TE', 'TE'), ('NA', 'NA')], default='NA', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='division',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='FFDB.Division'),
        ),
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='FFDB.Our_User'),
        ),
        migrations.AddField(
            model_name='player',
            name='league_team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='FFDB.Team'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='away_team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='FFDB.Team'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='home_team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='FFDB.Team'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FFDB.Week'),
        ),
        migrations.AddField(
            model_name='division',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FFDB.League'),
        ),
        migrations.AddField(
            model_name='tradingblock',
            name='interested_in',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='FFDB.Player'),
        ),
    ]
