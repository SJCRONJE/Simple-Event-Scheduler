from event import Event
from datetime import datetime

#Event Scheduler
class EventScheduler:
    def __init__(self):
        self.events = []

    def add_event(self, title, description, date, time):
        if not self._validate_date(date):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        formatted_date = self._format_date(date)

        if not self._validate_time(time):
            raise ValueError("Invalid time format. Please use HH:MM.")
        formatted_time = self._format_time(time)

        # Create a new event instance and append it to the events list
        new_event = Event(title, description, formatted_date, formatted_time)
        self.events.append(new_event)

    def list_events(self):
        sorted_events = sorted(self.events, key=lambda x: (x.date, x.time))
        for event in sorted_events:
            print(f"Title: {event.title}\nDescription: {event.description}\nDate: {event.date}\nTime: {event.time}\n")

    def delete_event(self, title):
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                print(f"Event '{title}' deleted successfully.")
                return
            print(f"Event '{title}' not founf.")

    def search_event(self, keyword):
        found_events =[event for event in self.events if keyword in event.title or keyword in event.description]
        if found_events:
            print("Found Events: ")
            for event in found_events:
                print(f"Title: {event.title}\nDescription: {event.description}\nDate: {event.date}\nTime: {event.time}\n")
        else:
            print("No events found matching search.")

    def edit_event(self, title, new_title=None, new_description=None, new_date=None, new_time=None):
        # Edit existing event
        for event in self.events:
            if event.title == title:
                if new_title:
                    event.title = new_title
                if new_description:
                    event.description = new_description
                if new_date:
                    event.date = new_date
                if new_time:
                    event.time = new_time
                print(f"Event '{title}' updated successfully.")
                return
        print(f"Event '{title}' not found.")

    def _validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def _validate_time(self, time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

    def _format_date(self, date_str):
        parts = date_str.split('-')
        if len(parts) == 3:
            formatted_date = "-".join(parts)
        else:
            formatted_date = f"{parts[0]}-{parts[1]}-{parts[2]}"
        return formatted_date

    def _format_time(self, time_str):
        parts = time_str.split(':')
        if len(parts) == 2:
            formatted_time = ":".join(parts)
        else:
            formatted_time = f"{parts[0]}:{parts[1]}"
        return formatted_time


#User Interface

def main():
    event_scheduler = EventScheduler()
    while True:
        print("\nEvent Scheduler Menu:")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Search Event")
        print("5. Edit Event")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            try:
                event_scheduler.add_event(title, description, date, time)
            except ValueError as e:
                print(str(e))
        elif choice == '2':
            event_scheduler.list_events()
        elif choice == '3':
            title = input("Enter the title of the event you want to delete: ")
            event_scheduler.delete_event(title)
        elif choice == '4':
            keyword = input("Enter a keyword to search for events: ")
            event_scheduler.search_event(keyword)
        elif choice == '5':
            title = input("Enter the title of the event you want to edit: ")
            new_title = input("Enter new title (leave blank to keep current): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            new_date = input("Enter new date (YYYY-MM-DD) (leave blank to keep current): ")
            new_time = input("Enter new time (HH:MM) (leave blank to keep current): ")
            try:
                event_scheduler.edit_event(title, new_title, new_description, new_date, new_time)
            except ValueError as e:
                print(str(e))
        elif choice == '6':
            print("Exiting Event Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
