import django_filters
from .models import CpdScoreBoard, DevScoreBoard, Feed, Event, Voting


class CpdScoreBoardFilter(django_filters.FilterSet):
    class Meta:
        model = CpdScoreBoard
        fields = {
            'score_board_date': ['day', 'day__gt', 'day__lt', ],
            'score_board_date': ['day', 'month', 'year',],
            'week': ['exact', 'gt', 'lt', ],
        }

class DevScoreBoardFilter(django_filters.FilterSet):
    class Meta:
        model = DevScoreBoard
        fields = {
            'score_board_date': ['day', 'day__gt', 'day__lt', ],
            'score_board_date': ['day','month', 'year',],
            'week': ['exact', 'gt', 'lt', ],
            

        }
    
