from discord.ext import commands

import requests, json
import argparse, inspect

class Koran(commands.Cog):
    def __init__(self) -> None:
        super().__init__()

        self.create_parser()

    @commands.command()
    def koran(self, ctx, argument):
            kwargs = self.parser.parse_args(argument.split())
            if not kwargs.subkoran:
                
                return
            pass

    def ctftime(self, ctx, **kwargs):
        pass

    def whatsapp(self, ctx, **kwargs):
        pass

    def nhentai(self, ctx, **kwargs):
        pass

    def create_parser(self):
        self.parser = parser = argparse.ArgumentParser()
        parser.add_argument("subkoran", type=str, help="pilihan langganan", choices=self.methods)
        parser.add_argument("-d", "--delay", type=int, help="delay between request(for request based)")

    def get_self_methods(self):
        self.methods = mtds = [t[0] for t in inspect.getmembers(self, predicate=inspect.ismethod)]
        mtds.remove("create_parser")
        mtds.remove("koran")
        mtds.remove("get_self_methods")

def request_ctftime():
    r = requests.get("https://ctftime.org/api/v1/events/?limit=1", headers = {"User-Agent": 'browser palsu'})
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        return False