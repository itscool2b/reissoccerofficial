from django.contrib import admin
from .models import DashboardStats, Player, StatsPerGame, PlayerGameStats

# Optionally create custom admin classes to customize the admin interface
class DashboardStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'games_played', 'wins', 'losses', 'total_goals')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_goals', 'total_assists')

class StatsPerGameAdmin(admin.ModelAdmin):
    list_display = ('vs', 'date', 'wl', 'user')

class PlayerGameStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'game', 'goals', 'assists')

# Register your models here
admin.site.register(DashboardStats, DashboardStatsAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(StatsPerGame, StatsPerGameAdmin)
admin.site.register(PlayerGameStats, PlayerGameStatsAdmin)