import logging
import subprocess
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
logger=logging.getLogger(__name__)
class FendExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent,Listen())
class Listen(EventListener):
    def on_event(self,event:KeywordQueryEvent,_):
        args=event.get_argument()
        out=subprocess.run(['fend',args],capture_output=True).stdout.decode()
        return [ExtensionResultItem(
            name=out,
            on_enter=True,
        )]
if __name__=='__main__':
    FendExtension().run()
