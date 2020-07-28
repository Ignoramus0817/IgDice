from nonebot import on_command, CommandSession
import random


@on_command('roll', aliases=('dice', 'random'))
async def roll(session: CommandSession):
    n_dices = session.get('n_dices', prompt='请指定骰子个数')
    n_faces = session.get('n_faces', prompt='请指定骰子种类')

    res = []
    for i in range(n_dices):
        res.append(random.randint(1, n_faces))

    await session.send(res)


@roll.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    splited = [0, 0]

    if stripped_arg:
        splited = stripped_arg.lower().split(str='d')

        if splited[0] != 0 and splited[1] != 0:
            session.state['n_dices'] = int(splited[0])
            session.state['n_faces'] = int(splited[1])
            return
        elif splited[0] == 0 and splited[1] != 0:
            session.pause('请指定骰子个数')
        else:
            session.pause('请指定骰子种类')

    if not stripped_arg:
        session.pause('请输入骰点参数')
