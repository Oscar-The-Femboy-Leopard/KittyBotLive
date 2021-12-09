import discord
import time

from mainconfig import Owner_ID, Owner_Name, PREFIX, TOKEN, INVITE, imgflipuser, imgflippass, paypal1, paypal2, password

_PREFIX = "beast "
_prefix = "beast"

TOKEN = TOKEN

Owner_Name = Owner_Name

_password = password

start_time = time.time()

_blnk_value = "_ _"

INVITE = INVITE

Blacklist_IDs = []
Blacklist_Channels = []

Whitelist_IDs = []
Whitelist_Channels = []

cog_extentions = [
    'fun._8ball',
    # 'fun.AResponder',  # TODO Look into the code to make it respond to the person ID
    # 'fun.coinflip', # TODO Throws a List dir error saying it can't find the file
    # 'fun.diceroll', TODO Make the dice roll
    'fun.fact',
    # 'fun.idiot',  # TODO Make this into a command that works, not with it just calling the client an idiot
    'fun.insult',
    'fun.kill',
    # 'fun.numguess', # TODO Make the game work
    # 'fun.OwOviolation',  # TODO Make the video play within the embed
    'fun.quote',
    # 'fun.QuoteOfTheDay',  # TODO Make this appear every time at Midnight GMT 0
    'fun.rps',
    'fun.ship',  # TODO It runs rather well, just need to make it ship 2 different people - Need to make it split
    # 'fun.flip', # TODO Remember what this command is for and then investigate the errors
    # 'imgflip_meme_creation.bf',
    'imgflip_meme_creation.brace',
    'imgflip_meme_creation.cardboard_sign',
    'imgflip_meme_creation.change_my_mind',
    'imgflip_meme_creation.first_world_problem',
    # 'imgflip_meme_creation.gru', # TODO Set up the 4 variables but need to get them to split properly
    'imgflip_meme_creation.lie_detector',
    'imgflip_meme_creation.nut_button',
    'imgflip_meme_creation.option',
    'imgflip_meme_creation.put_it_somewhere_else',
    'imgflip_meme_creation.say_that_again',
    # 'imgflip_meme_creation.seagull', # TODO Need to set up the 4 variables
    'imgflip_meme_creation.skeleton',
    'imgflip_meme_creation.Spongebob_heads_out',
    'imgflip_meme_creation.spongebob_imagination',
    'imgflip_meme_creation.think',
    'imgflip_meme_creation.this_is_fine',
    'imgflip_meme_creation.too_high',
    'imgflip_meme_creation.trump',
    'imgflip_meme_creation.uno',
    'listener.noU',
    # 'moderation.antispam', # TODO Activate this before letting the client go live
    # 'moderation.ban',
    # 'moderation.clear',
    # 'moderation.kick',
    # 'moderation.unban', #  TODO Make it unban
    # 'moderation.m_index',
    # 'moderation.m_config',
    'owner.booster',
    'owner.bot_inv',
    'owner.cmessage',
    'owner.current_verified_artist',
    # 'owner.custom_statuses',
    # 'owner.directory',
    'owner.dm_',
    # 'owner.emoji',
    # 'owner.leave',
    'owner.load_cog',
    'owner.partner',
    'owner.paypal',
    # 'owner.qotd',
    'owner.reload_cog',
    'owner.rules',
    'owner.rules_staff',
    'owner.staff_application_form',
    'owner.staff_intro',
    'owner.sudo',
    'owner.unload_cog',
    'owner.verify_artist',
    'Utility.announcement',
    'Utility.bot_info',
    'Utility.error_handlers',
    'Utility.error_report',
    # 'Utility.helpcommand', # TODO Help command running in main.py .... May investigate into improving the code
    # 'Utility.modmail',
    'Utility.personinfo',
    'Utility.pfp',
    'Utility.ping',
    # 'Utility.report', #  TODO Make it report into beta testing server
    'Utility.timer',
    'Utility.uptime',
    # 'Utility.vc_role_give',
    'Utility.verification',
    'Wynter_Integration.boop',
    'Wynter_Integration.doggo',
    'Wynter_Integration.hug',
    'Wynter_Integration.lick',

]

_commands = ["BotInfo",
             "8 ball",
             "Quote"]

unfair_message = f"If you think this is unfair, please DM my dev, <@{Owner_ID}>, and she will look into it. If you can't message her, please DM one of the Staff"

My_Paypal = paypal1  # Paypal sent to peeps that don't know my irl name
My_Paypal_2 = paypal2  # Paypal sent to peeps that know my irl name

# Club Fur Staff Roles
Role_Mod_Trainee = '752631938560295012'  # Trainee
Role_Helper = '752631938560295013'  # Helper
Role_Mod = '752631938560295014'  # Moderator
Role_Admin = '752631938560295015'  # Administrator
Role_Owner = '752631938560295016'  # Owner
Staff_Roles_Group_Import = [Role_Mod_Trainee,
                            Role_Helper,
                            Role_Mod,
                            Role_Admin,
                            Role_Owner]

random_color = [discord.Color.blurple(),
                discord.Color.blue(),
                discord.Color.dark_blue(),
                discord.Color.red(),
                discord.Color.dark_red(),
                discord.Color.green(),
                discord.Color.dark_purple(),
                discord.Color.purple(),
                discord.Color.gold(),
                discord.Color.dark_gold()]

bad_list = ["fuck",
            "Fuck",
            "bitch",
            "Bitch",
            "cunt",
            "Cunt",
            "slut",
            "Slut",
            "dick",
            "ass",
            "dike",
            "cunt",
            "pussy",
            "nigger",
            "kkk",
            "negro",
            "cracka",
            "jew",
            "honkie",
            "furfag",
            "furry faggot"]
blist_responses = ["I hope you didn't kiss your mother with that mouth....",
                   ".....some people these days..... need to good switch to the [REDACTED]",
                   "Who taught you to use such filthy language?!?",
                   "You're choice in words is reassuring. I know that you will never be anything now.",
                   "FUCK! Another one slipped through! GRAB THE RAID!",
                   "SHIT! SHIT! WE GOT ONE! WE FINALLY GOT ONE! GET THE HAMMER!",
                   "Something I was told by my programmer was that swearing shows a low IQ... I believe her",
                   "Get silenced! OOOOOOOHHHHHHH!!!",
                   "I just don't care about your foul mouth. The jerk store called, they're running out of you. I would love to insult you but I'm afraid I wouldn't do as well as nature did. You're the reason nobody likes you so you have to use bad language."
                   "Less of the language. This is a christian minecraft server.... Well... Keep this to the minimum!",
                   "Please stop the language. - Staff",
                   ".....Oop.... I should tell your mom....."]

_8ball_responses = ['As I see it, yes.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Don’t count on it.',
                    'It is certain.',
                    'It is decidedly so.',
                    'Most likely.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Outlook good.',
                    'Reply hazy, try again.',
                    'Signs point to yes.',
                    'Very doubtful.',
                    'Without a doubt.',
                    'Yes.',
                    'Yes – definitely.',
                    'You may rely on it.']

idiot_responses = ["Yes, I am an idiot... Just wish I could accept it. However, my programmer isn't! Please show "
                   "her some love :heart: :heart:",
                   "No U",
                   "You're the idiot, not me",
                   "I know you are, you said you are, but what am I?"]

Playing_Bot_Status = [discord.Activity(name=f'my fav games|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'Chinese Whispers with my dev|{PREFIX}help',
                                       type=discord.ActivityType.playing),
                      discord.Activity(name=f'crane games for cool stuff|{PREFIX}help',
                                       type=discord.ActivityType.playing),
                      discord.Activity(name=f'with my friends|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with leopards!|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with foxes!|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with bunnies!|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with wolves|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with lynxes|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with paws|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with my RAM|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'on Overclocking my CPU|{PREFIX}help', type=discord.ActivityType.playing),
                      # discord.Activity(name=f'on my dedicated server!|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with you cool furs|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with my Dev|{PREFIX}help', type=discord.ActivityType.playing),
                      discord.Activity(name=f'with my Prefix|{PREFIX}help', type=discord.ActivityType.playing),
                      ]
Watching_Bot_Status = [discord.Activity(name=f'the sever for my Dev|{PREFIX}help', type=discord.ActivityType.watching),
                       discord.Activity(name=f'some cool things with my Dev|{PREFIX}help',
                                        type=discord.ActivityType.watching),
                       discord.Activity(name=f'something lame... Why is my dev boring?|{PREFIX}help',
                                        type=discord.ActivityType.watching)]
Load_Status = [Playing_Bot_Status, Watching_Bot_Status]

# Wynter_API_Connection = 'http.client.HTTPSConnection("api.furrycentr.al")'

imgflip_username = imgflipuser
imgflip_password = imgflippass
