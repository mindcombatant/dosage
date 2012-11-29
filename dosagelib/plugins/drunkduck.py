# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..helpers import bounceStarter
from ..util import tagre

# note: adding the compile() functions inside add() is a major performance hog
_imageSearch =  compile(tagre("img", "src", r'(http://media\.drunkduck\.com\.s3\.amazonaws\.com:80/[^"]+)', before="page-image"))
_linkSearch = tagre("a", "href", r'(/[^"]+/\d+/)')
_prevSearch = compile(_linkSearch + tagre("img", "class", "arrow_prev"))
_nextSearch = compile(_linkSearch + tagre("img", "class", "arrow_next"))

def add(name):
    classname = 'DrunkDuck_%s' % name
    url = 'http://www.drunkduck.com/%s/' % name

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').split('/')[-1])
        ext = imageUrl.rsplit('.')[-1]
        return '%d.%s' % (index, ext)

    globals()[classname] = make_scraper(classname,
        name = 'DrunkDuck/' + name,
        starter = bounceStarter(url, _nextSearch),
        stripUrl = url + '%s/',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help = 'Index format: n (unpadded)',
        namer = namer,
    )

# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
add('12_Men_Died_Making_This_Strip')
add('1337_Joe_and_Fellow_Seth')
add('20_Galaxies')
add('2Masters')
add('2_Bitter_4_Words')
add('2s_a_company')
add('3D_Glasses')
add('3rd_Party_Fantasy')
add('4_Humor')
add('70_Seas')
add('AD_1997')
add('AGENCY')
add('AKA_Limzee')
add('ALTER')
add('ANGELOU_____Las_aventuras_de_Nikole')
add('ANIME_WARS')
add('AWES0ME')
add('AWESOME_HIGH_FIVE_EDITION')
add('A_Burden')
add('A_Call_to_Destiny_Reloaded')
add('A_Call_to_Destiny__NC_17')
add('A_Day_in_the_Life_for_Erik')
add('A_Deviant_Mind')
add('A_Different_Perspective')
add('A_Dim_View')
add('A_Fairly_Twisted_Reality')
add('A_Few_Brain_Cells_Short_of_Normal')
add('A_Jagged_Mind')
add('A_Loonatics_Tale')
add('A_Note_On_My_Life')
add('A_Paige_Comic')
add('A_PoKeMoN_comic_that_everyone_will_ignore_even_though_the_author_puts_way_more_work_into_it_than_some_other_very_popular_PoKeMoN_comics_that_get_over_nine_thousand_views_on_days_they_DONT_update_What_the_hell')
add('A_Roll_of_the_Dice')
add('A_Step_Out_of_Phase')
add('A_Tale_of_Two_Sprites')
add('A_Way_to_the_Stars')
add('A_Word_Of_Wisdom')
add('A_town_called_Alandale')
add('Acrobat')
add('Across_the_Way')
add('Acting_Out')
add('Adam_and_Darcys_Shenanigans')
add('Adsecula_The_Seventh_Serpent')
add('Adventures_Guild')
add('Adventures_in_StuffedAnimalLand')
add('Adventures_of_Lucrezia')
add('Adventures_of_Martin')
add('Adventures_of_Wristance')
add('Aerians')
add('Air_Raid_Robertson')
add('Akniatt')
add('Al_De_Baran')
add('Al_and_Scout')
add('Alien_Circus')
add('Alien_Concepts')
add('Aliens_Anonymous')
add('All_Saints')
add('Allan')
add('Altimatium')
add('Amazing_Superteam')
add('America_Jr')
add('Amya')
add('An_Act_of_Aggression')
add('Anachronism')
add('Anarchy_2090')
add('Anathema')
add('Anecdote')
add('Angel_Guardian')
add('Angelfish_A_COV_comic')
add('Angry_D_Monkey')
add('Animania')
add('Anime_Remix')
add('Animosity_Sonata')
add('Anomic_v2')
add('Another_Articifial_Time')
add('Answers')
add('Antcomics')
add('Anything_could_happen')
add('Apartment_408_Full_Size')
add('Apathy_cigarettes_and_valentines')
add('Apple_Valley')
add('Apt_408_Minis')
add('Ar_Oh_Ef_El')
add('Arachnid_Goddess')
add('Ardra')
add('Arrowflight_Chronicles')
add('Art_Captions')
add('Art_and_sketches')
add('Art_table_of_Duck')
add('Artist_Adventure')
add('Artwork____The_Mirror_of_Life')
add('As_the_Galaxy_Turns')
add('Assassin_Assassin')
add('Asshole')
add('Asteroid_of_Doom')
add('Atavism')
add('Atlantis_Rising')
add('Attack_of_the_Robofemoids')
add('Augustos')
add('Avatar_of_Fire')
add('Aw_Nuts_2')
add('Awakenings_Online')
add('Awesomataz')
add('Ax_Crazy')
add('AyaTakeo')
add('BALLMAN')
add('BASO')
add('BFF')
add('BIBLE_BELT')
add('BK_Shadow_Nemesis')
add('BK_Shattered_Hate')
add('BLADE_OF_THE_FREAK')
add('BLANK_LIFE_insert_player_rokulily')
add('BRINK')
add('Ba_Ba')
add('Bacon_Strips')
add('BadBlood')
add('Bad_Guy_High')
add('Badly_Drawn_Penguins')
add('Badly_Drawn_Webcomic')
add('Banango')
add('Baroque_Viceroyalty')
add('Barry_Reviews_Webcomics')
add('Bass_Rebirth_of_Amp')
add('Battle_of_the_Robofemoids')
add('Bear_Versus_Zombies')
add('Bearly_Abel')
add('Beautiful_Skies')
add('Beauty_Into_Beast')
add('Because_of_Ivan')
add('Been_Better')
add('Beer_Noodles')
add('Beluga_Weekly')
add('Benders_and_Brawlers')
add('Beta')
add('Better_Luck_Next_Time')
add('Betting_On_Love')
add('Between_Worlds')
add('BffSatan')
add('Bhaddland')
add('Billy_Learns_To_Rock')
add('Binary_Souls_Other_Dimensions')
add('Bird_and_Worm')
add('Birdman')
add('Bitter_Sweet_Melancholy')
add('Blade_of_Toshubi')
add('Blitz')
add('Blood_Bound')
add('Blood_Nation')
add('Bloodlust_Eternal_Conflict')
add('Blue_Comics')
add('Blue_Strawberry')
add('Blues_Rhapsody')
add('Bobby_Monos_Crappy_Comics')
add('Bobby_the_fetus')
add('Bombshell')
add('Bombshell_Fights_For_America')
add('Boobs_Ahoy')
add('Boogey_Dancing')
add('Bored_by_the_Bus_Stop')
add('Bouncing_Orbs_of_Beauty')
add('Bounty')
add('Bowsers_Plan_B')
add('Brainfuzz')
add('Brathalla')
add('Breaking_the_Ice')
add('Bricktown')
add('Brinkerhoff')
add('Broken_Wings')
add('Brymstone')
add('Bulletproof')
add('Busty_Solar')
add('CATS_AND_ICECREAM')
add('CDA')
add('COMPANY_MAN')
add('CRAZED')
add('CROSS_WORLDS_NEXXUS')
add('Caggage')
add('Camera_Obscura')
add('Camp_Calomine')
add('Canadian_Gamers')
add('Captain_Communism')
add('Carbon_and_Space')
add('Carnivore_Carnival')
add('Carrot_and_Roper')
add('Case_1048_Blind_and_Blue')
add('Cashcow')
add('Cataclysm')
add('Catboy_at_th_Con')
add('Celebrity_Stalker')
add('Cerintha')
add('Chad_the_Fat_Kid')
add('Chain_of_Stuff')
add('Changes')
add('Changes_Redux')
add('Changing_Worlds')
add('Chaos_Punks')
add('Chaos_Reigns')
add('Character_Development')
add('Charby_the_Vampirate')
add('Chester_and_Ferdie')
add('Children_at_Play')
add('Children_of_the_Tiger')
add('Chimera')
add('Chomp')
add('Christopher')
add('Chrono_Redux')
add('Chu_and_Kenny')
add('Circle_Arcadia')
add('City_of_Dream')
add('Civil_Servitude')
add('ClashDown')
add('Clockwork_Atrium')
add('Cloud_Eagle')
add('Coalition_of_the_Reluctant')
add('Cockroach_Theater')
add('Coffee_Time')
add('Coga_Suro')
add('Coga_Suro_2')
add('Collision')
add('Comic_Pie')
add('Comic_Remix')
add('Comicarotica')
add('Coming_Soon')
add('Conventional_Wisdom')
add('Cooks_Assistant')
add('Corporate_Life')
add('CorruptHardware')
add('Covalence')
add('Coveinant_Journey')
add('Cowboys_and_Aliens_II')
add('Crack')
add('Crack_Bird_and_Company')
add('Crackwalker')
add('Cramberries')
add('Crap_on_a_Stick')
add('CrayonS')
add('Crazy_Duck')
add('Creepy_Girl_and_Her_Zombie_Dog')
add('Crickets_Creature')
add('Crimson_Dark')
add('Crossover')
add('Crossover_High')
add('Crossoverkill')
add('Crossoverlord')
add('Crossoville')
add('Cru_The_DwarF')
add('Ctownstrips')
add('Culture_Shock')
add('Cumic_relief')
add('CuoreVoodoo')
add('Curse_of_The_Black_Terror')
add('Cute_N_Spicy')
add('Cuttley_Bear')
add('Cwens_Quest')
add('CyBoar')
add('Cyberspace')
add('Cybertech')
add('DD24hour_2010')
add('DD24hour_2011')
add('DDSR')
add('DHF_Jam')
add('DIAMOND_English_version')
add('DIS')
add('DR_Valume_1')
add('D_U_E')
add('Danielle_Dark')
add('Dansk_Folly')
add('Daqueran')
add('DarkKyos_Short')
add('Dark_Sisters')
add('Darken')
add('Darkling_Visions_of_a_Madmans_Soul')
add('Daryl_and_Susie')
add('Dasien')
add('Day_in_the_Life_of_a_Cosplayer')
add('DeadFingers')
add('Dead_Men')
add('Dead_Strangers')
add('Death_Brigade')
add('Death_P0rn')
add('Decimated_Eden')
add('DeepHurting')
add('Demon_Eater')
add('Demon_Fist')
add('Demon_Slayers')
add('Demonics')
add('Denizens__Attention')
add('Depths_of_My_Empty_Soul')
add('Desperate_Angels')
add('Despotize')
add('Destroying_The_Illusion')
add('Deviant_Prophets')
add('Diamond')
add('Din_Krakatau')
add('Dirtheads')
add('Distant_Embrace')
add('Divine_Engine_Experimental_Prototype')
add('Divine_Grace')
add('Divine_Leap')
add('Dobutsu_no_Tamashii')
add('Doctor_Death_vs_The_Zombie_')
add('Dog_the_Spot')
add('Dogs_Eye_View')
add('Don_Josh')
add('Dont_Eat_the_Bread')
add('Doodlerama')
add('Dot_Dot_Dot')
add('Dot_TXT')
add('Double_Coupons')
add('Dragon_City')
add('Dragon_Kingdoms')
add('Dragonaur')
add('Dragonaur_Mini')
add('Dragonballz__Smash_Tournament')
add('Dragonet')
add('Dragons_Quest___Crystals_of_the_Elder')
add('Drawn_to_you')
add('Dread_Sisterhood_of_Randomnessossity')
add('Dreadnought_Invasion_Six')
add('DreamCatcher')
add('Dream_Chronicles')
add('Dreams_in_Synergy')
add('Dribble_For_Kids')
add('DrunkDuck_Poop')
add('Drunk_Duck_Awards_2011')
add('Drunk_Duck_Awards_2012')
add('Drunk_Duck_Beauty_Contest')
add('Drunk_Duck_Gift_Exchanges')
add('Drunk_Duck_Zombies')
add('Duck_and_Quail')
add('Ducks_of_Doom')
add('Due_East')
add('Dungeon_Hordes')
add('Dying_to_Live')
add('ELEMENT')
add('ELO')
add('Edepth_Angel')
add('Edge_of_December')
add('Educomix')
add('Elastik_Dreamz')
add('Electronic_Revolutions_The_Burnhams')
add('Elemental_Animarus')
add('Elements_CYOA')
add('Elf_N_Hood')
add('Elijah_and_Azuu')
add('Elijah_and_Azuu_Classic')
add('Elsewhere')
add('Elves_With_Mecha')
add('Em_oi')
add('Emerald_Winter')
add('Emma')
add('Endstone')
add('Energize')
add('Engine')
add('Enter_the_Duck_2')
add('Enter_the_Duck_3')
add('Ephemeral')
add('Epic_Brundala')
add('Epic_adventures')
add('Erth')
add('Essay_Bee_Comics_Presents_Fusion')
add('Estatic_Gods')
add('Eternal_Flame')
add('EternityComplex')
add('Eternity_Comic')
add('Eternity_Complex')
add('Ethereal')
add('Evan_Yeti')
add('Even_For_a_Lunch_Meat')
add('Evergreen_Comics')
add('Everybody_Loves_Zero')
add('Everybody_hates_Herb')
add('Eves_Apple')
add('Evil_Dawn')
add('Evil_Empire_Moratorium')
add('Evil_Inc')
add('Evil_Plan')
add('Evilish')
add('Explorers_Of_the_Unknown')
add('Extra_stuff_of_the_other_comics')
add('FIGHT')
add('FIGHT_2')
add('FRANKENSTEIN__Her_Majestys_Secret_Service')
add('Fahei_Volume_1__Firefly')
add('Fainting_Spells')
add('FanDanGo')
add('FantastiTeam')
add('Far_Out_There')
add('Fated_Feather')
add('Faults')
add('Faust')
add('Feeling_Rushed')
add('Fifth_Dimension')
add('Fighter_House')
add('Fightsplosion_Legends')
add('Figured_It_Out')
add('Final_Blasphemy')
add('Fizz')
add('Flame_of_Earth')
add('Flaming_Codfish')
add('Flaming_Fuzzy_People')
add('Floyd_and_Mike')
add('Flying_Under_the_Influence')
add('For_Your_Eyes_Only')
add('Forsaken_Valor')
add('Fortress_Avalon')
add('Found_Art')
add('Four_Bats')
add('Frame_by_Frame')
add('Frank_and_Steinway')
add('Frank_and_Vinny')
add('Fred_Peterson_The_Mighty_Warlord_Book_1')
add('Frobert_the_Demon')
add('Frog_Skin_Boots')
add('Frontier__2170')
add('Fun_Times')
add('Function_Over_Fashion')
add('Funday_Morning')
add('Fuse')
add('Fusion')
add('GAAK')
add('GIF_Showcase')
add('GNight_Shade')
add('GRIND')
add('Gambit_as_Bishounen')
add('Gamers_Anonymous')
add('Gametard')
add('Gary_the_Alchemist')
add('Gello_Apocalypse')
add('Gelotology')
add('Geminni')
add('Geminni_LEVEL_UP')
add('Gemutations__Plague')
add('George_the_Dragon')
add('Get_Up_and_Go')
add('Getting_Into_The_MiddleGround')
add('Ghost_Hunters_Online_Manga')
add('Ghosting')
add('Gift')
add('Gifted')
add('Ginger_and_Shadow')
add('Give_Me_The_Sky')
add('Glass_Hearts')
add('Gnoph')
add('Go_A_Viking_The_Sword_of_Kings')
add('Go_For_it')
add('Goblin_Hollow')
add('God_Complex')
add('God_Damn_It')
add('God_of_Destruction')
add('Godlings')
add('Godot')
add('Gods_Playing_Poker')
add('Golden_Gamers')
add('Goo_From_Another_Dimension')
add('Goober_Nice_To_Meep_You')
add('Good_Guy')
add('Good_Sir_Cat')
add('Good_Taste')
add('Goosetown_and_Lunch_Break')
add('Graphical_Deviants')
add('Grayling')
add('Grim')
add('Grog')
add('Grounded_Angel')
add('Growth')
add('Guardian_of_Twilight')
add('Guinea_Something_Good')
add('Gundula_un_de_Stuventiger')
add('HASBEN_AND_HASH')
add('HSW_Remix')
add('HUSS')
add('H_A_R_D')
add('H_I_K_A_R_I')
add('Hakkum_Town')
add('Hand_Drawn')
add('Happyface_Comics')
add('Harkovast')
add('Head_over_Heart')
add('Headless_Cross')
add('Heart_of_a_Dragon')
add('Hearts_and_Nails')
add('Heavy_Mech')
add('Hellbent')
add('Hellscream')
add('Hephaestus')
add('Here_Comes_the_Chavalry_and_other_random_things_we_decided_to_draw')
add('Hero_Force')
add('Heroes_Alliance')
add('Heroes_Unite')
add('Hexagon_Death_Squad')
add('Hi_Res_Heroes')
add('Hikari_The_Demon_Swordsman')
add('Hit_and_Miss')
add('Holon')
add('Horribleville')
add('Hospitality_Included')
add('HotelSoul')
add('House_of_the_Muses_1')
add('How_I_Killed_The_Gods')
add('How_Unfortunate')
add('Hurrocks_Fardel')
add('Hyper_Death_Babies')
add('Hyperactive_Comics')
add('IF_I_GET_LOCKED_UP_TONITE')
add('IRC')
add('I_Come_From_Mars')
add('I_Drew_150_Pokemon')
add('I_Fell_Down_The_Stairs')
add('I_Was_Kidnapped_By_Lesbian_Pirates_From_Outer_Space')
add('I_got_it_in_my_mouth')
add('Illusional_Beauty')
add('ImaginaryFriends')
add('Imaginary_Daughter_Bonus')
add('Imaginary_Tactics')
add('Inappropriate_Irving')
add('Inchoatica')
add('Incorporated_Hate')
add('Indigo_Bunting__Vampire')
add('Infinity_Burger')
add('Inhuman')
add('Insanity_Untamed')
add('Insanity_of_Xade')
add('Inside_OuT')
add('Insomnia_The_Comic')
add('Insomniart')
add('Intergalactic_Continental_Dimension_Travelers')
add('Internet_Superbuddies')
add('Iornhart')
add('Iron_Wolf')
add('Irrumator')
add('Ishi_Alliance')
add('Island_Of_Submission')
add('Its_A_Boy_Thing')
add('Its_Ninja_Time')
add('ItzWrAiTh')
add('JRs_Minutemen')
add('JUNK_a_story')
add('Jac_Strips_for_You')
add('Jack')
add('Jake_the_Evil_Hare')
add('Jays_Internet_Fight_Club')
add('Jeriah')
add('Jericho')
add('Jerk_Wadz')
add('Jet_and_Joe')
add('Jhulene_the_Paladin')
add('Jix')
add('Joe_Bivins_Man_Genius')
add('Joe_Pop')
add('John')
add('Jonkos_Picture_Diary')
add('Journey_to_Raifina')
add('Jump')
add('Junk_Food')
add('Jurbas')
add('JustAnotherDay')
add('Just_Call_Me_Freedom')
add('Just_Liam')
add('Just_My_Luck')
add('KAKA_PENCIL_magical_pen')
add('KALA_dan')
add('KAMs_Fanart')
add('KISS_4K_the_webcomic')
add('Karabear_Comics_Unlimited')
add('Karen_the_Marilith')
add('Kat_and_Dogg')
add('Kawaii_Daigakusei')
add('Kazei_5_Rebirth')
add('Keeping_Up_with_Thursday')
add('Kemono_Densetsu')
add('Kenji_Nin')
add('Kevin_Wards_A_Frickin_Ninja_Story')
add('Keyguard_Active')
add('Kids_With_Gas_Eat_Free')
add('Killer_Kittenz')
add('Kimeral')
add('King_Me')
add('Kirby_Komiks')
add('Kitty_Litter')
add('Knights_Requiem')
add('Knock_on_Wood')
add('Kokuahiru_comics')
add('Kroniki_Black_Dragons')
add('Kung_Fu_Komix')
add('Kurenai_Mashin')
add('Kuro_Shouri')
add('LASTFantasy')
add('LA_ESPADA_DEL_ANORMAL')
add('LOE_Plus')
add('Lacerated_Veil')
add('Laggoo_and_the_Kings_Trident')
add('Lancaster_the_Ghost_Detective')
add('Last_Chance_The_Beast_Hunter')
add('Last_Of_The_Wilds')
add('Last_Place_Comics')
add('Last_War')
add('Last_words')
add('Latchkey')
add('Laurentinas_Improv_Studio_The_Comic_Art')
add('Lavender_Legend')
add('Led_by_a_Mad_Man')
add('LeeEXE')
add('Legacy_of_Blaze')
add('Legacy_of_Kain_Laugh_Reaver')
add('Legend_of_Link')
add('Legend_of_Setar')
add('Legend_of_Zelda__Ocarina_of_Tim')
add('Legends_of_Idiocy')
add('Leggo_my_Ego')
add('Lego_Space')
add('Lena')
add('Leo')
add('Lexcore')
add('Life_Blowz')
add('Life_and_Death')
add('Life_and_Maybe_Death_of_Ed')
add('Life_as_an_8bit')
add('Life_with_Dragons')
add('Lifeblood')
add('Like_Fish_in_Water')
add('Lil_Hero_Artists_Manga_Edition')
add('Link_Skywalker')
add('Linnyanie')
add('Liquid_Lunch')
add('Lite_bites')
add('Little_Bat_Koku')
add('Little_Black_Dress')
add('Little_Digital_People')
add('Little_Terrors')
add('Live_to_tell')
add('Livin_On_The_Edge')
add('Living_With_Insanity')
add('Lizzy')
add('Locoma')
add('Lola')
add('London_Underworld')
add('Long_Conversations_About_Nothing')
add('Loose_Lips')
add('Lost')
add('Lost_Chapters_of_Megaman')
add('Lost_Invisible')
add('Lost_Tribe_of_Pen_GUin')
add('Lost_in_Transition')
add('Louder_Than_Bombs')
add('Lovarian_Adventures')
add('Love_And_Chaos')
add('Love_Story')
add('Lovecraft_Yaoi')
add('Lucidfairy')
add('Lucky_Dawg')
add('Lugnor_Riders')
add('MAG_ISA')
add('MAYA_____The_legend_of_Wolf')
add('MAYA_la_leyenda_del_lobo')
add('MIKYAGU')
add('MISFIT_ASSASSINS')
add('MKIA_The_Sprite_Comic')
add('MMM_BooGrrs')
add('MMZ_After_Zero')
add('MOSAIC')
add('MS_Pain')
add('M_Organ_Art')
add('Mad_World')
add('Madness_to_my_Method')
add('Mafital')
add('Mage')
add('Magellan')
add('Maggot_Boy')
add('Magical_Misfits')
add('Magicians_Quest')
add('Magiversity')
add('Maidens_Monsters_and_Madmen_the_Tim_Tyler_sketchbook')
add('Malefic')
add('Malefic_Tales')
add('ManBoys')
add('Mario_and_Luigi_Misadventures')
add('Mario_in_Johto')
add('Marios_Day_Job')
add('Marital_Bliss')
add('Mary_Sue_Academy')
add('Mask_of_the_Aryans')
add('Master')
add('Master_the_Tiger')
add('Mastermind_BTRN')
add('Mastorism')
add('Matthews_crazy_adventure')
add('Max_Zing')
add('Mayhem_the_Comic')
add('Mech_Academy')
add('MegaNonsense')
add('Mega_Child_Xtreme')
add('Mega_Maiden_and_the_Chop_Chop_Princess')
add('Megaman_EXE')
add('Megaman_Neo_Adventures')
add('Megaman_The_Megamissions')
add('Megaman_Zero')
add('Megaman_battle_network_continues')
add('Melody_and_Macabre')
add('Memories_from_Requiem')
add('Mental_Meltdown')
add('Mercs')
add('Messenger')
add('Metal_Breakdown')
add('Metroid_Vengeance')
add('Mildly_mundane')
add('Milo_and_John')
add('Mind_Under_Matter')
add('Mindmistress_at_Drunk_Duck')
add('Minion')
add('Misadventures_of_Classic_MegaMan')
add('Misfire_Reactional')
add('Misfits_of_Fandom')
add('Mishap_Mania')
add('Miss_Grey')
add('Mixed_Bag_Comics')
add('Mob_Ties')
add('Modern_Day_Witchdoctor')
add('Modest_Medusa')
add('Monkey_Pot')
add('Monster_Lover')
add('Monster_Lover_Destinys_Path')
add('Monster_Soup')
add('Moon_Reflected_in_Water')
add('Moonlight_Doll')
add('Moose_Shoe')
add('Morning_Squirtz')
add('Morning_Squirtz_lite')
add('Morph_Man_Heir')
add('Morphic')
add('MrRiot_Theater')
add('Much_the_Millers_Son')
add('Murder_in_the_Mushroom_Kingdom')
add('Muse_of_a_Knight')
add('Musical_Farm')
add('My_Angel_and_My_Devil')
add('My_Imaginary_Life')
add('My_Parents_are_Nobodies')
add('My_Pet_Demon')
add('My_Shining_Knight')
add('My_Sister_The_Demon')
add('My_Sister_The_Goddess')
add('My_Sister_prequel_Eclipse')
add('My_Sister_the_Awakening')
add('My_Sister_the_Damned')
add('My_Sister_the_Witch_0')
add('My_TV_is_Evil')
add('My_Thingie')
add('Myo_Min_Myo')
add('Mystery_World')
add('Myths_And_Legends')
add('NEC')
add('NPC')
add('NUTS')
add('N_N_Sp')
add('Nahim')
add('Namco_Wars')
add('Naruto_Blood_Inheritance')
add('Naruto_The_Comic')
add('Necromancer_Troubadour')
add('Nectar_of_the_Gods')
add('Negate_Never')
add('Negligence')
add('Neil_And_Ryan')
add('Nemution_Jewel')
add('Nemution_Redux')
add('Nerdcore')
add('NewGirl')
add('New_America')
add('New_Challenger_Approaches')
add('New_Jerusalem')
add('New_Pages')
add('Newton_the_Newt')
add('Niego')
add('Nightmistress')
add('Ninja_Shizatch')
add('Ninjoy')
add('Nintendo_Super_Squad')
add('Nintendo_randomness')
add('Nintendos_Untold_Legends')
add('No_Capes')
add('No_Need_for_Bushido')
add('No_Parking')
add('No_Talent')
add('Nocturne_21')
add('Normalcy_is_for_Wimps')
add('Not_Faust')
add('Nothing_Really_Serious')
add('Novusgenesis_Hype')
add('OTENBA_Files')
add('O_deer')
add('Obiit')
add('Oblivion')
add('Obnoxious_High')
add('Odd_Days')
add('Off_Hours')
add('Off_White')
add('Oh_Brother_Qlippoth')
add('Okonomi_Yaki')
add('Old_Batman_Comics')
add('Old_Comic')
add('Old_Pond')
add('Omikami')
add('One_Piece_Grand_Line_3_point_5')
add('One_Question')
add('One_Sixth_Sense')
add('One_Third_Of_Your_Life_Is_Spent_Sleeping_One_Third_Of_Your_Life_Is_Spent_Working_And_Half_Of_One_Third_Is_Spent_Waiting_The_Question_Is_It_Really_Your_Life')
add('One_last_breath')
add('Opey_the_Warhead')
add('Our_Amazing_Adventures')
add('Out_of_Curiosity')
add('Outer_Space_Alien_Nazis_From_Outer_Space')
add('Outlawed')
add('Overshadow')
add('Oyer')
add('POKETTO_MONSUTAA_SPECIAL_SUPER_EX_ADVENTURE_XXXVX_THE_CHRONICLES_OF_RED_BLUE_GREEN_AND_A_BUNCH_OF_OTHER_KIDS_WITH_COLORS_FOR_NAMES')
add('PSI')
add('PUTRID_MEAT')
add('Pagan_Zoetrope')
add('Paint_Heroes')
add('Panacea')
add('Panda_panda')
add('Pandemonium')
add('Paper_Cuts')
add('Paranoia_and_Denial')
add('Paranormal_Activity')
add('Parker_Lot')
add('Parody_Paridise')
add('Pegwarmers')
add('Per_Ardua')
add('Peregrination_of_the_Deliverer')
add('Perpendicular_Universe')
add('Persona_3_FTW')
add('Persona_4TW')
add('Persona_Won')
add('Perspectives')
add('Peter_And_The_Wolf')
add('Phayrh')
add('Philly')
add('Phineus_Magician_for_Hire')
add('Phobophobia')
add('PiLLI__ADVENTURE')
add('Pinkerton')
add('Pinky_TA')
add('Pinnacle_of_Evolution')
add('Pixel_Plumbers')
add('Pizza_Project')
add('Planet_B')
add('Planet_Chaser')
add('Plastic_Bullets')
add('Plumber_Switch_a_rio')
add('PoKeMoN_HEROES')
add('Poharex_issues_1_to_11')
add('Pokemon_Contest_Challenge')
add('Pokemon_Edge_2009')
add('Pokemon_Granite')
add('Pokemon_Haven')
add('Pokemon_Jade')
add('Pokemon_Light_and_Dark')
add('Pokemon_Mystery_Dungeon_Strikedown_Chronicles')
add('Pokemon_Random_Kanto')
add('Pokemon_Shroom_Version')
add('Pokemon_Silver_State_Version')
add('Pokemon_Sinnoh_Surfer')
add('Pokemon_Warpers')
add('Pokemon_World_Trainers')
add('Pokemon_Yellow_Comics')
add('Politics_The_Tankers_Way')
add('Ponzi')
add('Potpourri_of_Lascivious_Whimsy')
add('Powell_and_Derry_Product_')
add('PowerTrip')
add('Powerjeff')
add('Powerup_Adventure')
add('Powerup_Comics')
add('Pr0nCrest')
add('Prelude')
add('Present_Day')
add('Princess_Natsumi')
add('Professor_Dolphin_presents_Pokemon')
add('Project_217')
add('Project_Darklight')
add('Project_GTH')
add('Proto_Culture_Comics')
add('Proyecto_GTH')
add('Pugnuggle_Tales')
add('Pulp_Fantasy')
add('Pulse_Comics')
add('Punk_Pink')
add('Puppetry')
add('Puppets_and_Strings')
add('QUANTUM_Rock_of_Ages')
add('Quickening')
add('REAL_Men_Wear_Lipstick')
add('RIDDICK_Q_LOSS_TALES')
add('RIOT_and_FadeOut_From_the_Top')
add('Radio_Active_Rainbows')
add('Raiders_of_The_Lost_Mind')
add('Raidou_Kuzunoha_the_19th')
add('Rain_Of_Gods')
add('Rainbow_Carousel')
add('Rainbow_Connection_2')
add('Rakina')
add('Randi')
add('Random_Ramblings')
add('Random_Sonic_Stories')
add('Random_Street_Theater')
add('Rangetsu')
add('Rasvaar')
add('Ravenwood')
add('Raw_Fish')
add('Razor_Candy')
add('Rebound')
add('Reckless_Youth')
add('Red_Dog_Venue')
add('Red_Moon')
add('Red_String')
add('Redemption_of_Heroes')
add('Redneck_Comics')
add('Remote_Angel')
add('Requiem_for_Innocents')
add('Requiems_Gate')
add('Retake')
add('RiTH')
add('Riggs_Hell')
add('Rileys_notebook')
add('Rival_Angels')
add('Robomeks')
add('Robot_Chuck')
add('Robot_Friday')
add('Robot_Wars')
add('Robukkagenerator')
add('Rock_Paper_Cynic')
add('Rocketship_A_GoGo')
add('Rococo_Eternal')
add('Rogue_Agent_Axl')
add('Rogues_of_Clwyd_Rhan')
add('Roll_Call')
add('Roll_For_Intelligence')
add('Romeo')
add('Room_Mates')
add('Row_and_Bee')
add('Roy_Barley')
add('Royal_Icing')
add('Ruby')
add('Ruby_And_Pipers_World_Of_Magical_Pink_Fearie_Unicorns')
add('Rule_of_Three')
add('Rules_of_Make_Believe')
add('Rune')
add('Runway')
add('Ryosaki_Uzumaki_1')
add('SECKS')
add('SFA')
add('SHELL')
add('SOPHIA_Awakening')
add('SPOON')
add('STARSEARCHERS')
add('STICKFODDER')
add('Safety_Man')
add('Sailor_Soldiers_of_Justice')
add('Saint_Remy')
add('Salvation_Of_Morrowind')
add('Satans_Evil_Square')
add('Saturday_Morning_')
add('Saviours_X')
add('ScareCrow_Lullaby')
add('Schadenfreude')
add('Schizophrenia_Bloom')
add('School_Spirit')
add('School_of__Rumble')
add('Scorch')
add('Screwball_Islands')
add('Seedy_Comics')
add('Senretsu_Gaiden')
add('Senshi_Vs_Sentai')
add('Serai')
add('Seth_the_Hippo')
add('Shades')
add('Shades_of_Gray')
add('Shades_of_Illusion')
add('Shadow_Root')
add('Shadow_Sprinters')
add('Shaman_Quest')
add('Shelter_of_Wings')
add('Shiny_Things')
add('Shiro_Karasu')
add('Short_Bus')
add('Silver_Vein')
add('Sinful')
add('Sire')
add('Sketchy')
add('Skewed_Reality_Origins')
add('Skooland')
add('Slice_of_Life')
add('Slugs_of_Mystery')
add('Small_Wonder')
add('Smash_Bros_Royale')
add('Smoke_Manmuscle_PI')
add('So_Fantastic_Pork_Show_9oCLOCK')
add('SoapOperaGoneWrong')
add('Soapbox_Hill')
add('Solar_Salvage')
add('Some_Notes')
add('Something_Else_Anime_Theater')
add('Something_Like_Life')
add('Something_To_Do')
add('Somewhere_in_San_Fransisco_Half_Way_Beyond_The_Bridge_and_The_Tower_Lies_A_Place_Where_Nothing_is_Ever_What_It_Seems_On_A_Day_to_Day_Basis_Because_That_Is_What_Happens_in_This_Kinda_Place')
add('Songs_of_An_Angel')
add('Sonic_A_Heroes_Tail')
add('Sonic_Advance_The_Real_Story')
add('Sonic_Advanced_Online')
add('Sonic_Adventurz')
add('Sonic_Bluff')
add('Sonic_College')
add('Sonic_Destination_Chaos')
add('Sonic_Meets_Megaman')
add('Sonic_Overdose')
add('Sonic_Unreal')
add('Sonic_and_tails_corner')
add('Sonic_plus_a_castle')
add('Sonic_the_Hedgehog_in_the_Comic')
add('Soul_Less')
add('Soul_Palisade')
add('Soul_Symphony')
add('South_Of_Sanity')
add('Spellmon')
add('Spitfire')
add('Splash_Damage')
add('Splices_of_Life')
add('Sprite_Happy_Comic')
add('Sprite_Life___Nineteen_Eternal')
add('Spritely')
add('St_Dyphnia_Academy')
add('Stafettserien')
add('Star_Crossed_Destiny')
add('Starcrossed')
add('Starfox__Declassified')
add('Startoons_Super_Force')
add('Starving_Artists')
add('Status_Update')
add('Stellar_Arcana')
add('Stellar_Arcana_Spanish')
add('Step_It_Up')
add('Stick_Figure_Comics')
add('Stickman_and_Cube')
add('Stories_of_Strangeness')
add('Story_of_My_Life')
add('Story_of_a_Robot')
add('Strange_Attractors')
add('Stranger_Things_have_Happened')
add('Strangers_and_Friends')
add('Strawberry_Death_Cake')
add('Stupidity_in_Magic')
add('SubStandard_Comics')
add('Such_A_Simple_Life')
add('Such_Is_Life')
add('SunSpots')
add('Sun_Fish_Moon_Fish')
add('Sune')
add('Sunset_Grill')
add('Super_Mario_super_comic')
add('Super_Smash_Bros_Grand_Tour')
add('Super_Smash_Bros_Royale')
add('Super_Temps')
add('Superior_Day')
add('Supermassive_Black_Hole_A_Star')
add('Surviving_Older_Schools')
add('Sword_in_Hand')
add('Sword_of_Heaven')
add('Syndicate')
add('Synthea')
add('TCCPC')
add('THE_RANCAT')
add('THRUD_Goddess_Of_Thunder')
add('TRUBBLE')
add('Taint_of_Exile')
add('Taking_Stock')
add('Tales_of_Kenah')
add('Tales_of_Magid')
add('Tales_of_Schlock')
add('Tales_of_The_Sly_Ditt_Inn')
add('Team_Kim_Possible')
add('Tears_will_Shatter_Steel')
add('Ted_The_Terrible_Superhero')
add('TeenTeam')
add('Teenage_Wasteland')
add('Tennisball_Man')
add('Tera_Forming')
add('Tern_and_Zebra')
add('Terra_online_comic')
add('Terror_Of_The_Undead')
add('That_Which_Is_Summoned')
add('Thats_Comical')
add('The_3rd')
add('The_600')
add('The_Adventure_of_the_Goat_Chin_Pirates')
add('The_Adventures_Of_Vindibudd_Superhero_In_Training')
add('The_Adventures_of_Chad_Cleanly')
add('The_Apocalypse')
add('The_Art_of_Joe_Jarin')
add('The_Asim_Stone')
add('The_Auragon_Base')
add('The_Author')
add('The_Authors_Corner')
add('The_Beast_Legion')
add('The_Begining_of_an_End')
add('The_Bend')
add('The_Black_Dragons_Chronicles')
add('The_Bluenoser')
add('The_Cafe_d_Alizee')
add('The_Chelation_Kid')
add('The_Chronicles_of_Drew')
add('The_Chronicles_of_Gaddick')
add('The_Chronicles_of_Wyrden')
add('The_Compozerz')
add('The_Continentals')
add('The_Crossroads')
add('The_Dashing_Rogue')
add('The_Death_Pact')
add('The_Deed')
add('The_Demonic_Adventures_of_Angel_Witch_Pita')
add('The_Devils_Horn')
add('The_Devon_Legacy_Prologue')
add('The_Dragon_Doctors')
add('The_Dragon_Fists_of_Smorty_Smythe')
add('The_Dragon_and_the_Lemur')
add('The_Drunk_Duck_Mafia')
add('The_ECS_Strips')
add('The_Emerald_City')
add('The_Errant_Apprentice')
add('The_Escapists')
add('The_Essyane_Warriors')
add('The_Fabled_Travelers')
add('The_Faction')
add('The_Fifty_Peso_Ninja')
add('The_Fighting_Stranger')
add('The_Final_Zone')
add('The_Garden')
add('The_Gimblians')
add('The_Girl_Next_Door')
add('The_Goblin_Apprentice')
add('The_Gods_of_ArrKelaan')
add('The_Greening_Wars')
add('The_Hero_Factor')
add('The_Horribles')
add('The_KAMics')
add('The_Lamp')
add('The_Last_Element')
add('The_Loserz')
add('The_Manual')
add('The_Many_Misfortunes_of_Lady_Luck')
add('The_MatFkkinRix')
add('The_Mephit_Plot')
add('The_Mercs')
add('The_Mighty_Omega')
add('The_Misadventures_of_Everyone')
add('The_Muffinman')
add('The_NEW_Life_Of_TimmY')
add('The_Necropolis_Chronicles')
add('The_Nineteenth_Century_Industrialist')
add('The_Nonstandard_Assembly')
add('The_Omega_Key')
add('The_Onett_Suite')
add('The_Only_Half_Saga')
add('The_Order_vol_1')
add('The_Path')
add('The_People_That_Melt_in_The_Rain')
add('The_Pirate_Balthasar')
add('The_Planet_Closest_To_Heaven')
add('The_Portland_Express')
add('The_Princess')
add('The_Princess_and_the_Giant')
add('The_Pure_Soul')
add('The_Realms_of_Aegis')
add('The_Reborn')
add('The_Repository_of_Dangerous_Things')
add('The_Rift')
add('The_Rose_Killer')
add('The_Rube_Goldberg_Machine')
add('The_SMW_Chronicles')
add('The_SSA')
add('The_Shape_of_the_Heart')
add('The_Silver_Eye')
add('The_Sok_Comic')
add('The_SuperFogeys')
add('The_Surreal_Adventures_of_Edgar_Allan_Poo')
add('The_Symmetrical_Breadpazoid')
add('The_Tainted')
add('The_Temple_of_a_Thousand_Tears')
add('The_Tonberry_Spritedom')
add('The_Truth_About_Corey_Strode')
add('The_Uncanny_Uper_Dave')
add('The_Unthinkable_Hybrid')
add('The_Vanguard')
add('The_WAVAM_Project')
add('The_World_Robot_Competition')
add('The_World_of_Higal')
add('The_Young_Defenders')
add('The__Flea')
add('The__Porch')
add('The_idiotic_odyssey')
add('The_lost_boys_of_hometown')
add('The_story_of_Quark')
add('The_world_of_Aeria')
add('They_Are_Night_Zombies_They_Are_Neighbors_They_Have_Come_Back_From_The_Dead_Ahhhhh')
add('This_Ego_of_Mine')
add('This_Is_What_I_Do')
add('This_is_a_random_comic')
add('Thog_Infinitron')
add('Thunder_Roarer')
add('Timed_chaos')
add('Times_Like_This')
add('Tony_The_Hedgehog')
add('Too_Many_Authors')
add('Total_Immersion')
add('Total_Insanity')
add('Toy_Story_X')
add('Tozzer')
add('Trail_Mix')
add('TransUMan')
add('Trapped_in_a_Comic')
add('Tri_Noble')
add('Trinity_Legends_of_Zevera')
add('Triple_Torture')
add('Troop_37')
add('TrueNuff')
add('True_North')
add('True_Power')
add('Try_Everything_Once')
add('Twenty_Eight')
add('Twisted_Chronicles')
add('Twisted_Mind_of_Stranger')
add('Twisted_Mirrors')
add('TwoMoons')
add('Two_Rooks')
add('Two_Weeks_Notice')
add('Typical_Strange')
add('UNA_Frontiers_Commentary')
add('USB')
add('U_Chuu_No_Hoshi_Hotoshi_Tsuko')
add('Ultimate_X')
add('Ultimate_tourny_of_ultimate_fighting')
add('Ultranimu')
add('Un_Re_Stop_Comics')
add('Underscore')
add('Unfunny_comics')
add('Unlife_is_Unfair')
add('Unsound_of_Mind')
add('Unsung_Heroes_Of_Subtlety')
add('Unwanted_Eyes')
add('Used_Books')
add('Utterly_Rucked')
add('Valentines_Dei')
add('Vampire_Chronicles__Dark_Lust')
add('Vampire_Phantasm_X')
add('VampyrFetal')
add('Vanguard')
add('Version_2_Fantasy')
add('Vi_is_Manor')
add('Vic_and_Edwards')
add('Vice_and_Virtue')
add('Viera_Dimension')
add('Vigil_1to_4')
add('Vile_Withering')
add('Villian_Next_Door')
add('Virtual_reality')
add('Vita_Di_Vetro')
add('Voodoo_Walrus')
add('Vreakerz')
add('WACOT')
add('WIRES_2')
add('WTF_Renewed')
add('WWE_The_Comic')
add('Wakon_Yosai')
add('Wanted_Dead_or_dead')
add('WarMage')
add('WarriorBorn')
add('Warriors_of_the_night')
add('Waste_Of_Time')
add('Wasted_Potential')
add('Watashi_No_Ame')
add('Weave')
add('WeirdStar')
add('Weirdlings')
add('Welcome_To_Border_City')
add('What_I_Learned_Today')
add('What_The_Fucking_Shit_Fuck_Ass_Fuck_Is_Mario_Gonna_Do_Now')
add('What_You_Dont_See')
add('When_Video_Games_Collided')
add('White_Noise')
add('Will_And_Tokyo')
add('Wintergreen')
add('Witchthorn')
add('With_Friends_like_these')
add('Within_Shadows')
add('Woah_Roscoe')
add('Wolf')
add('Working_Stiffs')
add('World_of_Orenda')
add('Worlds_Apart')
add('Wren')
add('Wyyrd_Vintage')
add('XAZ_A_Megaman_X_Fancomic')
add('XTIN__The_Dragons_Dream_World')
add('XYZ_Identity')
add('X_UP')
add('Xenogenesis')
add('Xolta')
add('YO_Comix')
add('Yamase')
add('Yamete_Kudasai')
add('Yami_No_Tainai')
add('Yaoi_Seth')
add('Yeah_wait_what')
add('Yoshi_Saga')
add('Zandars_Saga')
add('Zodiac_Battle')
add('Zombie_Mojo')
add('Zombies_Are_People_Too')
add('Zorphbert_and_Fred')
add('Zos_Kias')
add('Zuber_Zakari')
add('action')
add('amoebaville')
add('and_Id')
add('atxs')
add('blackheart')
add('breeding_ground')
add('brick')
add('cowtoon')
add('dairyaire')
add('dead_ducks')
add('dot_EXE_Saga')
add('drag_them_down')
add('eliada')
add('featuring_Talking_Guinea_Pigs')
add('ffff')
add('girl_robot')
add('greys_journey')
add('grin_n_spirit')
add('hanged_doll')
add('hiro')
add('jenffers_show')
add('just_random')
add('kirby_supah_star')
add('light_within_shadow')
add('magick')
add('metroid_primed')
add('nicola_and_belmondo')
add('operation_blakck_sun')
add('patent_pending')
add('project_kokiro')
add('public_humiliation')
add('punished_girls')
add('pyroicon')
add('random_anime_fanart_comics')
add('roastytoasty')
add('rubber_girls')
add('signifikat')
add('simply_sarah')
add('story_irc')
add('stupid_machine_comics')
add('supahnariobros')
add('super_smash_bros_omega')
add('the_Many_Deaths_of_Mario')
add('the_hedgehogs')
add('the_random_archives_of_TJ')
add('vnd')
add('what_comes_first')
add('what_errant_beast')
add('whensdays')
add('xAll_Things_Consideredx')
