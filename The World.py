# -*- coding: utf-8 -*-
import time
from mcdreforged.api.decorator import new_thread
from mcdreforged.api.types import ServerInterface, Info

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

Prefix= '!!Theworld'
HelpMessage='''
§7{0} help §6显示此帮助界面
§7{0} §6激活时间停止，并且持续5秒
'''.strip().format(Prefix)

@new_thread('StopTime')
def stop_time(server: ServerInterface, info: Info)
    server.execute('title @a title "{}暂停了时间"'.format(info.player))
    server.execute("effect give @a[name=!{}] minecraft:slowness 1000 255".format(info.player))
    server.execute("effect give @a[name=!{}] minecraft:blindness 1000 255".format(info.player))
    server.execute("effect give @a[name=!{}] minecraft:jump_boost 1000 128".format(info.player))
    server.execute("tick freeze")
    time.sleep( 5 )
    server.execute("tick freeze")
    server.execute("effect clear @a")
    
def on_load(server: ServerInterface, old):
    server.logger.info(data)
        server.register_help_message(HelpMessage)
            server.register_command(
                Literal('!!Theworld help').
                    requires(lambda src: src.has_permission(PERMISSIONS['help'])).
                    then(
                    src.reply(info,HelpMessage)
                ).
                Literal('!!Theworld').
                    requires(lambda src: src.has_permission(PERMISSIONS['stop time'])).
                    then(
                        stop_time(server,info)
                    )
