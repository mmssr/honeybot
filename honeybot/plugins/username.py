# -*- coding: utf-8 -*-
"""
[username.py]
Username Generator Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
generates random usernames, used for inspiration

[Commands]
>>> .uname
returns generated username
"""
import random


class Plugin:
    def __init__(self):
        pass
    
    def gen_uname(self):
        """Return a string containing a randomly-generated username based on an adjectives list 
        (p1) and a noun list (p2)"""
        p1 = ['hopeful', 'young', 'sloppy', 'magic', 'intelligent', 'uncommon', 'cute', 'dangerous'
        'innocent', 'spooky', 'crazy', 'young', 'desperate', 'epic', 'anonymous', 'acceptable', 'achievable', 
        'active', 'active', 'active', 'additional', 'adjustable', 'admirable', 'advisable', 'massive', 
        'amazing', 'amusing', 'annoying', 'approachable', 'attentive', 'attractive', 'avoidable', 'believable', 
        'black', 'bloody', 'boring', 'bothering', 'breathing', 'buried', 'careful', 'challenging', 'chasing', 
        'cheerful', 'chosen', 'clear', 'collective', 'comfortable', 'complex', 'confused', 'considerable', 
        'consoled', 'continuous', 'crazy', 'creative', 'creditable', 'curable', 'cursed', 'damaged', 'deaf',
        'decisive', 'decorative', 'delightful', 'demanding', 'derivative', 'deserving', 'destructive', 
        'developing', 'dead', 'different', 'disturbing', 'dusty', 'educative', 'embarrassing', 'powerful', 
        'empty', 'circular', 'courageous', 'dangerous', 'enthusiastic', 'numerable', 'envious', 'evaporating', 
        'expected', 'explainable', 'exploring', 'fascinating', '', 'firm', 'flying', 'forceful', 'glorious', 
        'growing', 'harmful', 'hateful', 'healthy', 'hopeful', 'indentified', 'indentifying', 'imitative', 
        'impressive', 'inclusive', 'indicative', 'informative', 'inhabitant', 'injurious', 'inquiring', 
        'instructive', 'insulting', 'intentional', 'interfering', 'introductory', 'inventive', 'irritating', 
        'leading', 'lively', 'alive', 'lively', 'lost', 'mad', 'migrating', 'modern', 'moistures', 'monotonous', 
        'movable', 'narrow', 'national', 'observatory', 'own', 'performing', 'permissible', 'persuasive', 
        'pleasant', 'popular', 'quick', 'red', 'sad', 'secured', 'scenic', 'seen', 'speedy', 'white', 'bad']
        p2 = ['star', 'tree', 'ant', 'spider', 'moon', 'bug', 'name', 'heisenberg', 'dragon'
        'snake', 'lion', 'rebel', 'patriot', 'flower', 'popsicle', 'sun', 'failure','apple', 'arm', 'banana', 
        'bike', 'bird', 'book', 'chin', 'clam', 'class', 'clover', 'club', 'corn', 'crayon', 'crow', 'crown',
        'crowd', 'crib', 'desk', 'dime', 'dirt', 'dress', 'fang', 'field', 'flag', 'flower', 'fog', 'game', 
        'heat', 'hill', 'home', 'horn', 'hose', 'joke', 'juice', 'kite', 'lake', 'maid', 'mask', 'mice', 'milk',
        'mint', 'meal', 'meat', 'moon', 'mother', 'morning', 'name', 'nest', 'nose', 'pear', 'pen', 'pencil',
        'plant', 'rain', 'river', 'road', 'rock', 'room', 'rose', 'seed', 'shape', 'shoe', 'shop', 'show', 
        'sink', 'snail', 'snake', 'snow', 'soda', 'sofa', 'star', 'step', 'stew', 'stove', 'straw', 'string',
        'summer', 'swing', 'table', 'tank', 'team', 'tent', 'test', 'toes', 'tree', 'vest', 'water', 'wing',
        'winter', 'woman', 'women']
        return '{}{}'.format(random.choice(p1), random.choice(p2))

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.uname':
                methods['send'](info['address'], Plugin.gen_uname(self))
        except Exception as e:
            print('woops plug', e)
