from pydantic import BaseModel
from typing import Callable, Dict, List

class Event(BaseModel):
    """Event base class."""
    
    class Config:
        protected_namespaces = ()

class ModelLoadedEvent(Event):
    """Event triggered when a model is loaded."""
    model_name: str

class PluginLoadedEvent(Event):
    """Event triggered when a plugin is loaded."""
    plugin_name: str

class EventManager:
    """Manages event subscriptions and emissions."""

    def __init__(self):
        self.listeners: Dict[str, List[Callable[[Event], None]]] = {}

    def subscribe(self, event_type: str, listener: Callable[[Event], None]) -> None:
        """Subscribe a listener to an event type."""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def emit(self, event: Event) -> None:
        """Emit an event to all subscribed listeners."""
        event_type = event.__class__.__name__
        for listener in self.listeners.get(event_type, []):
            listener(event)
