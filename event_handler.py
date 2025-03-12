from event import Event
from typing import Callable

class EventHandler:
    subscribers = {}

    @staticmethod
    def subscribe(event: Event, handler: Callable):
        """Adds a subscriber to the list"""
        if event not in EventHandler.subscribers:
            EventHandler.subscribers[event] = []
        EventHandler.subscribers[event].append(handler)


    @staticmethod
    def publish(event: Event, data: str):
        """publishes data to all handlers subscribed to that event"""
        if event in EventHandler.subscribers:
            for handler in EventHandler.subscribers.get(event, []):
                handler(data)
        else:
            print(f"No subscribers for event: {event}")