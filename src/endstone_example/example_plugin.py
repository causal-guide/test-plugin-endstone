from endstone import ColorFormat
from endstone.event import event_handler, PlayerJoinEvent
from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version = "0.4"
    def on_enable(self) -> None:
        self.logger.info("on_enable is called!")
        self.register_events(self) # register the event listener

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent, player : Player):
        player.send_message(ColorFormat.YELLOW + f"{event.player.name} has joined the server")
