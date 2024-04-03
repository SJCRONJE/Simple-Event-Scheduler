import unittest
from event_scheduler import EventScheduler


class TestEventScheduler(unittest.TestCase):
    def setUp(self):
        self.event_scheduler = EventScheduler()

    def test_add_event(self):
        self.event_scheduler.add_event("Meeting", "Team meeting", "2024-04-01", "10:00")
        self.assertEqual(len(self.event_scheduler.events), 1)

    def test_delete_event(self):
        self.event_scheduler.add_event("Meeting", "Team meeting", "2024-04-01", "10:00")
        self.event_scheduler.delete_event("Meeting")
        self.assertEqual(len(self.event_scheduler.events), 0)

    # Add more test cases for other functions

if __name__ == '__main__':
    unittest.main()
