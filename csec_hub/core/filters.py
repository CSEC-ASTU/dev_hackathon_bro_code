import django_filters
from .models import ScoreBoard, Feed, Event, Voting


class ScoreBoardFilter(django_filters.FilterSet):
    class Meta:
        model = ScoreBoard
        fields = {
            'scoreboard_date': ['day', 'day__gt', 'day__lt', ],
            'scoreboard_date': ['day', 'month', 'year',],
            'week': ['exact', 'gt', 'lt', ],
        }

