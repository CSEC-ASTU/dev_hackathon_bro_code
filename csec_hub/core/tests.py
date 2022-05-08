from django.test import TestCase
from .models import ScoreBoard, Feed, Event, Voting
# Test the views
class TestViews(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        
    def test_feed_page_status_code(self):
        response = self.client.get('/feed/')
        self.assertEquals(response.status_code, 200)
    
    def test_event_page_status_code(self):
        response = self.client.get('/event/')
        self.assertEquals(response.status_code, 200)
    
    def test_score_board_page_status_code(self):
        response = self.client.get('/cpd_score_board/')
        self.assertEquals(response.status_code, 200)

    def test_voting_page_status_code(self):
        response = self.client.get('/voting/')
        self.assertEquals(response.status_code, 200)

    def test_feed_detail_page_status_code(self):
        response = self.client.get('/feed/1/')
        self.assertEquals(response.status_code, 200)
    
    def test_event_detail_page_status_code(self):
        response = self.client.get('/event/1/')
        self.assertEquals(response.status_code, 200)
    
    def test_score_board_detail_page_status_code(self):
        response = self.client.get('/score_board/1/')
        self.assertEquals(response.status_code, 200)
    
    def test_voting_detail_page_status_code(self):
        response = self.client.get('/voting/1/')
        self.assertEquals(response.status_code, 200)
    
    def test_feed_detail_page_status_code(self):
        response = self.client.get('/feed/1/')
        self.assertEquals(response.status_code, 200)

#test the models
class TestModels(TestCase):
    def test_feed_model(self):
        feed = Feed(title='test', content='test')
        feed.save()
        self.assertEqual(feed.title, 'test')
        self.assertEqual(feed.content, 'test')
        self.assertEqual(feed.is_active, True)
        self.assertEqual(feed.created_at, feed.updated_at)
        self.assertEqual(feed.created_by, feed.updated_by)
        self.assertEqual(feed.created_by, None)
        self.assertEqual(feed.updated_by, None)
        self.assertEqual(feed.created_at, None)
        self.assertEqual(feed.updated_at, None)
        self.assertEqual(feed.__str__(), 'test')
        self.assertEqual(feed.__repr__(), 'test')
        self.assertEqual(feed.__unicode__(), 'test')

    def test_event_model(self):
        event = Event(title='test', content='test')
        event.save()
        self.assertEqual(event.title, 'test')
        self.assertEqual(event.content, 'test')
        self.assertEqual(event.is_active, True)
        self.assertEqual(event.created_at, event.updated_at)
        self.assertEqual(event.created_by, event.updated_by)
        self.assertEqual(event.created_by, None)
        self.assertEqual(event.updated_by, None)
        self.assertEqual(event.created_at, None)
        self.assertEqual(event.updated_at, None)
        self.assertEqual(event.__str__(), 'test')
        self.assertEqual(event.__repr__(), 'test')
        self.assertEqual(event.__unicode__(), 'test')

    def test_score_board_model(self):
        score_board = ScoreBoard(title='test', content='test')
        score_board.save()
        self.assertEqual(score_board.title, 'test')
        self.assertEqual(score_board.content, 'test')
        self.assertEqual(score_board.is_active, True)
        self.assertEqual(score_board.created_at, score_board.updated_at)
        self.assertEqual(score_board.created_by, score_board.updated_by)
        self.assertEqual(score_board.created_by, None)
        self.assertEqual(score_board.updated_by, None)
        self.assertEqual(score_board.created_at, None)
        self.assertEqual(score_board.updated_at, None)
        self.assertEqual(score_board.__str__(), 'test')
        self.assertEqual(score_board.__repr__(), 'test')
        self.assertEqual(score_board.__unicode__(), 'test')
    
    def test_voting_model(self):
        voting = Voting(title='test', content='test')
        voting.save()
        self.assertEqual(voting.title, 'test')
        self.assertEqual(voting.content, 'test')
        self.assertEqual(voting.is_active, True)
        self.assertEqual(voting.created_at, voting.updated_at)
        self.assertEqual(voting.created_by, voting.updated_by)
        self.assertEqual(voting.created_by, None)
        self.assertEqual(voting.updated_by, None)
        self.assertEqual(voting.created_at, None)
        self.assertEqual(voting.updated_at, None)
        self.assertEqual(voting.__str__(), 'test')
        self.assertEqual(voting.__repr__(), 'test')
        self.assertEqual(voting.__unicode__(), 'test')
    
