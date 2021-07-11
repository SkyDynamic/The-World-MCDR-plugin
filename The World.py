# -*- coding: utf-8 -*-
import time
from mcdreforged.plugin.server_interface import *
from mcdreforged.api.decorator import *
from mcdreforged.api.command import *

PERMISSIONS = {
    'help': 1,
    'stop time': 2,
}

PLUGIN_METADATA = {
    'id': 'theworld',
    'version': '0.0.1',
    'name': 'The World',
    'description': 'Allows you to use the 「The World」 in Minecraft',
    'author': 'Sky_Dynamic',
    'link': 'https://github.com/SkyDynamic/The-World-MCDR-plugin'
}

Prefix= '!!TW'
HelpMessage='''
§7{0} help §6显示此帮助界面
§7{0} §6激活时间停止，并且持续5秒
'''.strip().format(Prefix)

@new_thread
def stop_time(src: CommandSource):
    server=src.get_server()
    server.execute(f'title @a title "§4{src.player}§7暂停了时间"')
    server.execute(f"effect give @a[name=!{src.player}] minecraft:slowness 1000 255")
    server.execute(f"effect give @a[name=!{src.player}] minecraft:blindness 1000 255")
    server.execute(f"effect give @a[name=!{src.player}] minecraft:jump_boost 1000 128")
    server.execute(f"tick freeze")
    time.sleep( 5 )
    server.execute(f"tick freeze")
    server.execute(f"effect clear @a")

def on_load(server: ServerInterface, old):
    server.register_help_message('!!TW help', '显示The World插件帮助')

    server.register_command(
        Literal(Prefix).
            requires(lambda src: src.has_permission(PERMISSIONS['help'])).
            then(
            Literal('help').runs(lambda src: src.reply(HelpMessage))
        ).
            then(
                Literal('on').
                    requires(lambda src: src.has_permission(PERMISSIONS['stop time'])).runs(stop_time)
        )
    )
