from aiogram import Dispatcher, filters
from aiogram.types import ContentTypes
from handlers.user import start, menu, grammar_level_A1, tests_A1_to_be_1, tests_A1_arkt_2, tests_A1_there_is_3, \
    tests_A1_4, tests_A1_5, tests_A1_6, tests_A1_7, tests_A1_8, tests_A1_9, tests_A1_10, tests_A1_11, tests_A1_12, \
    tests_A1_13, tests_A1_14, tests_A1_15, support, commands_bot, reading, games_word
from states.tests_A1 import Test_A1
from states.games import Game
from states.support import Support

ADMIN = [994115172]


def setup(dp: Dispatcher):
    dp.register_message_handler(start.start_bot, filters.CommandStart())
    dp.register_callback_query_handler(menu.lang_func, text="lang")
    dp.register_callback_query_handler(menu.call_start, text="grammar")
    dp.register_callback_query_handler(grammar_level_A1.gramm1, text="a1")
    # A1 Тема 1
    dp.register_callback_query_handler(tests_A1_to_be_1.start_test_a1_1, text="to_be")
    dp.register_callback_query_handler(tests_A1_to_be_1.questions_to_user_1, text="start_test")
    dp.register_message_handler(tests_A1_to_be_1.next_message_1, state=Test_A1.stage_1)
    # A1 Тема 2
    dp.register_callback_query_handler(tests_A1_arkt_2.start_test_a1_2, text="arkt")
    dp.register_callback_query_handler(tests_A1_arkt_2.questions_to_user_2, text="start_test2")
    dp.register_message_handler(tests_A1_arkt_2.next_message_2, state=Test_A1.stage_2)
    # A1 Тема 3
    dp.register_callback_query_handler(tests_A1_there_is_3.start_test_a1_3, text="there")
    dp.register_callback_query_handler(tests_A1_there_is_3.questions_to_user_3, text="start_test3")
    dp.register_message_handler(tests_A1_there_is_3.next_message_3, state=Test_A1.stage_3)
    # A1 Тема 4
    dp.register_callback_query_handler(tests_A1_4.start_test_a1_4, text="question")
    dp.register_callback_query_handler(tests_A1_4.questions_to_user_4, text="start_test4")
    dp.register_message_handler(tests_A1_4.next_message_4, state=Test_A1.stage_4)
    # A1 Тема 5
    dp.register_callback_query_handler(tests_A1_5.start_test_a1_5, text="nums")
    dp.register_callback_query_handler(tests_A1_5.questions_to_user_5, text="start_test5")
    dp.register_message_handler(tests_A1_5.next_message_5, state=Test_A1.stage_5)
    # A1 Тема 6
    dp.register_callback_query_handler(tests_A1_6.start_test_a1_6, text="modal")
    dp.register_callback_query_handler(tests_A1_6.questions_to_user_6, text="start_test6")
    dp.register_message_handler(tests_A1_6.next_message_6, state=Test_A1.stage_6)
    # A1 Тема 7
    dp.register_callback_query_handler(tests_A1_7.start_test_a1_7, text="pron")
    dp.register_callback_query_handler(tests_A1_7.questions_to_user_7, text="start_test7")
    dp.register_message_handler(tests_A1_7.next_message_7, state=Test_A1.stage_7)
    # A1 Тема 8
    dp.register_callback_query_handler(tests_A1_8.start_test_a1_8, text="noun_pron")
    dp.register_callback_query_handler(tests_A1_8.questions_to_user_8, text="start_test8")
    dp.register_message_handler(tests_A1_8.next_message_8, state=Test_A1.stage_8)
    # A1 Тема 9
    dp.register_callback_query_handler(tests_A1_9.start_test_a1_9, text="ukaz_pron")
    dp.register_callback_query_handler(tests_A1_9.questions_to_user_9, text="start_test9")
    dp.register_message_handler(tests_A1_9.next_message_9, state=Test_A1.stage_9)
    # A1 Тема 10
    dp.register_callback_query_handler(tests_A1_10.start_test_a1_10, text="prit_pron")
    dp.register_callback_query_handler(tests_A1_10.questions_to_user_10, text="start_test10")
    dp.register_message_handler(tests_A1_10.next_message_10, state=Test_A1.stage_10)
    # A1 Тема 11
    dp.register_callback_query_handler(tests_A1_11.start_test_a1_11, text="nar")
    dp.register_callback_query_handler(tests_A1_11.questions_to_user_11, text="start_test11")
    dp.register_message_handler(tests_A1_11.next_message_11, state=Test_A1.stage_11)
    # A1 Тема 12
    dp.register_callback_query_handler(tests_A1_12.start_test_a1_12, text="pr_s")
    dp.register_callback_query_handler(tests_A1_12.questions_to_user_12, text="start_test12")
    dp.register_message_handler(tests_A1_12.next_message_12, state=Test_A1.stage_12)
    # A1 Тема 13
    dp.register_callback_query_handler(tests_A1_13.start_test_a1_13, text="ps_s")
    dp.register_callback_query_handler(tests_A1_13.questions_to_user_13, text="start_test13")
    dp.register_message_handler(tests_A1_13.next_message_13, state=Test_A1.stage_13)
    # A1 Тема 14
    dp.register_callback_query_handler(tests_A1_14.start_test_a1_14, text="fut_s")
    dp.register_callback_query_handler(tests_A1_14.questions_to_user_14, text="start_test14")
    dp.register_message_handler(tests_A1_14.next_message_14, state=Test_A1.stage_14)
    # A1 Тема 15
    dp.register_callback_query_handler(tests_A1_15.start_test_a1_15, text="pr_c")
    dp.register_callback_query_handler(tests_A1_15.questions_to_user_15, text="start_test15")
    dp.register_message_handler(tests_A1_15.next_message_15, state=Test_A1.stage_15)
    # Другое
    dp.register_message_handler(commands_bot.message_reset_commands, commands='reset_commands')
    dp.register_callback_query_handler(reading.read, text="read")
    # dp.register_message_handler(games_word.start_game, commands="/start_game")
    #dp.register_message_handler(games_word.check_answer)


    dp.register_message_handler(support.support_users, lambda message: message.chat.id not in ADMIN,
                                commands='support'),
    dp.register_message_handler(support.send_message_to_admin, content_types=ContentTypes.ANY, state=Support().stage_1),
    dp.register_message_handler(support.send_message_to_user, lambda message: message.chat.id in ADMIN)