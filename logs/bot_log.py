2025-04-24 11:58:51,320 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 11:58:51,322 - __main__ - INFO - Starting MovieMawaBot...
2025-04-24 11:58:52,829 - __main__ - INFO - Bot polling started...
2025-04-24 11:58:52,829 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 11:58:53,940 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getMe "HTTP/1.1 200 OK"
2025-04-24 11:58:53,941 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7013259213}
2025-04-24 11:58:53,941 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 11:58:53,941 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 11:58:53,942 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 11:58:53,942 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 11:58:53,942 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 11:58:53,943 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 11:58:54,128 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 11:58:54,129 - telegram._bot - DEBUG - True
2025-04-24 11:58:54,130 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 11:58:54,130 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 11:58:54,130 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 11:58:54,130 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 11:58:54,130 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 11:58:54,130 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:58:54,132 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 11:58:54,132 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 11:58:54,132 - telegram.ext._application - INFO - Application started
2025-04-24 11:58:54,134 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 11:58:54,134 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 11:59:04,798 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 11:59:04,799 - telegram._bot - DEBUG - No new updates found.
2025-04-24 11:59:04,799 - telegram._bot - DEBUG - []
2025-04-24 11:59:04,799 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 11:59:04,800 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:59:14,115 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 11:59:14,116 - telegram._bot - DEBUG - Getting updates: [826430998]
2025-04-24 11:59:14,117 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000020C0BA51A80>]
2025-04-24 11:59:14,118 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 11:59:14,118 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:59:14,119 - telegram.ext._application - DEBUG - Processing update {'update_id': 826430998, 'message': {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': '/Start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 256, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476154, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'username': 'Neemohammanda', 'first_name': 'N.e.v.e.r', 'id': 861691679, 'language_code': 'en'}}}
2025-04-24 11:59:14,121 - __main__ - INFO - Received /start command
2025-04-24 11:59:14,121 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:14,892 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:14,894 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': "Rey mawa, welcome to MovieMawaBot! Movies, series, PDFs—em adigina search chesi pampistha. Ex: 'inception', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 145}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 257, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476155, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:14,897 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:24,353 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 11:59:24,355 - telegram._bot - DEBUG - No new updates found.
2025-04-24 11:59:24,356 - telegram._bot - DEBUG - []
2025-04-24 11:59:24,356 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 11:59:24,356 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:59:30,581 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 11:59:30,582 - telegram._bot - DEBUG - Getting updates: [826430999]
2025-04-24 11:59:30,584 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000020C0BA50280>]
2025-04-24 11:59:30,584 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 11:59:30,584 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:59:30,586 - telegram.ext._application - DEBUG - Processing update {'update_id': 826430999, 'message': {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Robbins pathology', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 258, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476171, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'username': 'Neemohammanda', 'first_name': 'N.e.v.e.r', 'id': 861691679, 'language_code': 'en'}}}
2025-04-24 11:59:30,587 - __main__ - INFO - Received message: robbins pathology
2025-04-24 11:59:30,588 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:31,384 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:31,386 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:robbins pathology', 'text': 'Movie'}, {'callback_data': 'series:robbins pathology', 'text': 'Series'}, {'callback_data': 'pdf:robbins pathology', 'text': 'PDF'}]]}, 'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': "Is 'robbins pathology' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 259, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476172, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:31,386 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:32,611 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 11:59:32,612 - telegram._bot - DEBUG - Getting updates: [826431000]
2025-04-24 11:59:32,614 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000020C0BA52C80>]
2025-04-24 11:59:32,614 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 11:59:32,615 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:59:32,616 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:robbins pathology', 'text': 'Movie'}, {'callback_data': 'series:robbins pathology', 'text': 'Series'}, {'callback_data': 'pdf:robbins pathology', 'text': 'PDF'}]]}, 'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': "Is 'robbins pathology' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 259, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476172, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}, 'chat_instance': '7359689328061020838', 'id': '3700937584822563426', 'data': 'pdf:robbins pathology', 'from': {'is_bot': False, 'username': 'Neemohammanda', 'first_name': 'N.e.v.e.r', 'id': 861691679, 'language_code': 'en'}}, 'update_id': 826431000}
2025-04-24 11:59:32,617 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 11:59:33,057 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 11:59:33,058 - telegram._bot - DEBUG - True
2025-04-24 11:59:33,059 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 11:59:33,060 - __main__ - INFO - Searching pdf: robbins pathology
2025-04-24 11:59:33,060 - __main__ - INFO - Discovering groups...
2025-04-24 11:59:33,060 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 11:59:33,061 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 11:59:33,062 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 11:59:33,260 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 11:59:33,261 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 11:59:33,262 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 11:59:33,262 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 11:59:33,271 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:33,271 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763080066803368 to InvokeWithLayerRequest (20c0bb72270)
2025-04-24 11:59:33,272 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 11:59:33,273 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:33,273 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:33,274 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:33,570 - telethon.network.mtprotostate - DEBUG - Updated time offset (old offset 0, bad 7496763081262487800, good 7496763084951808001, new 1)
2025-04-24 11:59:33,570 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496763080066803368
2025-04-24 11:59:33,572 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 11:59:33,572 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:33,573 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763085571320568 to InvokeWithLayerRequest (20c0bb72270)
2025-04-24 11:59:33,574 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 11:59:33,577 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:33,578 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:33,578 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763085591370616 to MsgsAck (20c0bb72420)
2025-04-24 11:59:33,579 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:33,580 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:33,580 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:33,861 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 11:59:33,862 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 11:59:33,863 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496763085571320568]
2025-04-24 11:59:33,863 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:33,868 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763085571320568
2025-04-24 11:59:33,869 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:33,869 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763086753733668 to GetUsersRequest (20c0bb71d90)
2025-04-24 11:59:33,870 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 11:59:33,871 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:33,872 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:33,872 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763086766260180 to MsgsAck (20c0b7bac00)
2025-04-24 11:59:33,873 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 11:59:33,875 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:33,875 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:34,080 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763086753733668
2025-04-24 11:59:34,080 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:34,081 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763087899696984 to MsgsAck (20c0bb71b50)
2025-04-24 11:59:34,081 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:34,083 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:34,083 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:34,084 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763087909846940 to MsgsAck (20c0bb71ac0)
2025-04-24 11:59:34,084 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:34,086 - __main__ - INFO - Client connected successfully
2025-04-24 11:59:34,086 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:34,088 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:34,088 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:34,459 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:34,460 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 260, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476175, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:34,461 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:34,462 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763089419835724 to SearchRequest (20c0bb70c50)
2025-04-24 11:59:34,462 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 11:59:34,463 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:34,463 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:34,660 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763089419835724
2025-04-24 11:59:34,662 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:34,664 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763090228710808 to MsgsAck (20c0a30a930)
2025-04-24 11:59:34,664 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:34,665 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:34,666 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:34,667 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763090236788428 to MsgsAck (20c0bb70d40)
2025-04-24 11:59:34,667 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:34,668 - __main__ - ERROR - Error discovering groups: The key is not registered in the system (caused by SearchRequest)
2025-04-24 11:59:34,668 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:34,670 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:34,671 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:35,082 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:35,083 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Error ra: The key is not registered in the system (caused by SearchRequest)', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 261, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476175, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:35,084 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:35,084 - __main__ - INFO - Searching files for query: robbins pathology, types: ['.pdf']
2025-04-24 11:59:35,084 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:35,616 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:35,617 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Files lo chusthunna: robbins pathology...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 262, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476176, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:35,618 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:35,620 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763094348433772 to ResolveUsernameRequest (20c0bb89070)
2025-04-24 11:59:35,620 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 11:59:35,622 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:35,622 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:35,814 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763094348433772
2025-04-24 11:59:35,815 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:35,816 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763095134711544 to MsgsAck (20c0bb71e80)
2025-04-24 11:59:35,817 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:35,818 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:35,819 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:35,820 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763095150465288 to MsgsAck (20c0bb70530)
2025-04-24 11:59:35,820 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:35,821 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 11:59:35,824 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:35,825 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:35,826 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763095170205392 to ResolveUsernameRequest (20c0bb70650)
2025-04-24 11:59:35,826 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 11:59:35,827 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:35,828 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:36,024 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763095170205392
2025-04-24 11:59:36,025 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:36,026 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763096267391128 to MsgsAck (20c0bb89310)
2025-04-24 11:59:36,027 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:36,027 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:36,027 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:36,028 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763096276152532 to MsgsAck (20c0bb89220)
2025-04-24 11:59:36,028 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:36,029 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 11:59:36,029 - __main__ - INFO - Searching files for query: robbins pathology pdf, types: ['.pdf']
2025-04-24 11:59:36,030 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:36,034 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:36,035 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:36,456 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:36,458 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Files lo chusthunna: robbins pathology pdf...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 263, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476177, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:36,459 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:36,460 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763098003432196 to ResolveUsernameRequest (20c0bb704a0)
2025-04-24 11:59:36,460 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 11:59:36,462 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:36,462 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:36,678 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763098003432196
2025-04-24 11:59:36,679 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:36,681 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763098887236516 to MsgsAck (20c0bb70ad0)
2025-04-24 11:59:36,681 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:36,682 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:36,682 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:36,683 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763098895235936 to MsgsAck (20c0bb701d0)
2025-04-24 11:59:36,683 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:36,684 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 11:59:36,685 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:36,686 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:36,686 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763098907248420 to ResolveUsernameRequest (20c0bb70aa0)
2025-04-24 11:59:36,686 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 11:59:36,688 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:36,688 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:36,874 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763098907248420
2025-04-24 11:59:36,874 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:36,875 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763099665704648 to MsgsAck (20c0bb70410)
2025-04-24 11:59:36,877 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:36,877 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:36,878 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:36,878 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763099674248616 to MsgsAck (20c0bb70fb0)
2025-04-24 11:59:36,878 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:36,879 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 11:59:36,880 - __main__ - INFO - Searching files for query: robbins pathology pdf, types: ['.pdf']
2025-04-24 11:59:36,880 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:36,881 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:36,881 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:37,257 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:37,259 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Files lo chusthunna: robbins pathology pdf...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 264, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476178, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:37,260 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:37,261 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763101504239604 to ResolveUsernameRequest (20c0bb71d30)
2025-04-24 11:59:37,261 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 11:59:37,262 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:37,262 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:37,542 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763101504239604
2025-04-24 11:59:37,542 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:37,545 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763102638333840 to MsgsAck (20c0bb70890)
2025-04-24 11:59:37,545 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:37,546 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:37,546 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:37,546 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763102642388864 to MsgsAck (20c0bb704d0)
2025-04-24 11:59:37,547 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:37,547 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 11:59:37,549 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:37,550 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:37,550 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763102657213732 to ResolveUsernameRequest (20c0bb709e0)
2025-04-24 11:59:37,550 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 11:59:37,551 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:37,551 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:37,766 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763102657213732
2025-04-24 11:59:37,767 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:37,769 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763103536889596 to MsgsAck (20c0bb73a40)
2025-04-24 11:59:37,770 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:37,771 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:37,772 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:37,772 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763103547117752 to MsgsAck (20c0bb72630)
2025-04-24 11:59:37,773 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:37,774 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 11:59:37,774 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:37,776 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:37,777 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:38,219 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:38,221 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': "Files em levu for 'robbins pathology' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 265, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476179, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:38,222 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:38,222 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:38,687 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:38,689 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': '**Book: robbins pathology**\nLink: https://free.usa1lib.is/book/123457/robbins\nNote: Free PDF\nVideo: Robbins Pathology Basics (YouTube)', 'group_chat_created': False, 'entities': [{'length': 43, 'type': <MessageEntityType.URL>, 'offset': 34}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 266, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476179, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:38,691 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:42,989 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 11:59:42,991 - telegram._bot - DEBUG - No new updates found.
2025-04-24 11:59:42,991 - telegram._bot - DEBUG - []
2025-04-24 11:59:42,992 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 11:59:42,992 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:59:50,727 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 11:59:50,728 - telegram._bot - DEBUG - Getting updates: [826431001]
2025-04-24 11:59:50,730 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000020C0BA53F40>]
2025-04-24 11:59:50,730 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 11:59:50,730 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:59:50,731 - telegram.ext._application - DEBUG - Processing update {'update_id': 826431001, 'message': {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Breaking bad', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 267, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476191, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'username': 'Neemohammanda', 'first_name': 'N.e.v.e.r', 'id': 861691679, 'language_code': 'en'}}}
2025-04-24 11:59:50,732 - __main__ - INFO - Received message: breaking bad
2025-04-24 11:59:50,733 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:51,659 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:51,661 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:breaking bad', 'text': 'Movie'}, {'callback_data': 'series:breaking bad', 'text': 'Series'}, {'callback_data': 'pdf:breaking bad', 'text': 'PDF'}]]}, 'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': "Is 'breaking bad' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 268, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476192, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:51,662 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:53,742 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 11:59:53,743 - telegram._bot - DEBUG - Getting updates: [826431002]
2025-04-24 11:59:53,744 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000020C0BA52B00>]
2025-04-24 11:59:53,744 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 11:59:53,744 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 11:59:53,746 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:breaking bad', 'text': 'Movie'}, {'callback_data': 'series:breaking bad', 'text': 'Series'}, {'callback_data': 'pdf:breaking bad', 'text': 'PDF'}]]}, 'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': "Is 'breaking bad' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 268, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476192, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}, 'chat_instance': '7359689328061020838', 'id': '3700937581662913599', 'data': 'series:breaking bad', 'from': {'is_bot': False, 'username': 'Neemohammanda', 'first_name': 'N.e.v.e.r', 'id': 861691679, 'language_code': 'en'}}, 'update_id': 826431002}
2025-04-24 11:59:53,746 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 11:59:54,124 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 11:59:54,126 - telegram._bot - DEBUG - True
2025-04-24 11:59:54,127 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 11:59:54,127 - __main__ - INFO - Searching series: breaking bad
2025-04-24 11:59:54,128 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/tv?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=breaking+bad&page=1&include_adult=false
2025-04-24 11:59:54,130 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 11:59:54,663 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/tv?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=breaking+bad&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 11:59:54,664 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 11:59:54,665 - __main__ - INFO - TMDB found 1 results for breaking+bad
2025-04-24 11:59:54,667 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 11:59:55,446 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=breaking%20bad+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 11:59:55,449 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 11:59:55,809 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/series/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 404 None
2025-04-24 11:59:56,480 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 11:59:58,220 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 11:59:58,344 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 11:59:58,344 - __main__ - INFO - Discovering groups...
2025-04-24 11:59:58,344 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:58,721 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:58,722 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 270, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476199, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:58,724 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:58,724 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763193549503060 to SearchRequest (20c0baff110)
2025-04-24 11:59:58,724 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 11:59:58,725 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:58,725 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:58,962 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763193549503060
2025-04-24 11:59:58,963 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 11:59:58,964 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763194509150240 to MsgsAck (20c0a30a930)
2025-04-24 11:59:58,964 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:58,964 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:58,965 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:58,965 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763194514288636 to MsgsAck (20c0bb72b10)
2025-04-24 11:59:58,965 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 11:59:58,966 - __main__ - ERROR - Error discovering groups: The key is not registered in the system (caused by SearchRequest)
2025-04-24 11:59:58,966 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 11:59:58,967 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 11:59:58,967 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 11:59:59,883 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 11:59:59,884 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Error ra: The key is not registered in the system (caused by SearchRequest)', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 271, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476200, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 11:59:59,885 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 11:59:59,885 - __main__ - INFO - Searching files for query: breaking bad, types: ['.mp4', '.mkv']
2025-04-24 11:59:59,885 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 12:00:00,252 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 12:00:00,252 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Files lo chusthunna: breaking bad...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 272, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476201, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 12:00:00,253 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 12:00:00,254 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763200256216024 to ResolveUsernameRequest (20c0bb8b6b0)
2025-04-24 12:00:00,254 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 12:00:00,255 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:00,255 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:00,566 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763200256216024
2025-04-24 12:00:00,566 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:00:00,567 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763201509356476 to MsgsAck (20c0bb72f60)
2025-04-24 12:00:00,567 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:00,568 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:00,568 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:00,569 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763201517345404 to MsgsAck (20c0bb70080)
2025-04-24 12:00:00,569 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:00,569 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 12:00:00,570 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:00,570 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:00,571 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763201525347688 to ResolveUsernameRequest (20c0bb71a00)
2025-04-24 12:00:00,571 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 12:00:00,572 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:00,574 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:00,909 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763201525347688
2025-04-24 12:00:00,910 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:00:00,911 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763202886504148 to MsgsAck (20c0bb71610)
2025-04-24 12:00:00,912 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:00,912 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:00,912 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:00,913 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763202896223044 to MsgsAck (20c0bb71160)
2025-04-24 12:00:00,913 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:00,914 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 12:00:00,914 - __main__ - INFO - Searching files for query: breaking bad series, types: ['.mp4', '.mkv']
2025-04-24 12:00:00,915 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 12:00:00,917 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:00,917 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:01,299 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 12:00:01,300 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Files lo chusthunna: breaking bad series...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 273, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476202, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 12:00:01,301 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 12:00:01,302 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763204747113804 to ResolveUsernameRequest (20c0bb8a180)
2025-04-24 12:00:01,303 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 12:00:01,303 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:01,304 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:01,502 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763204747113804
2025-04-24 12:00:01,504 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:00:01,505 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763205556566812 to MsgsAck (20c0bb88ad0)
2025-04-24 12:00:01,505 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:01,505 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:01,505 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:01,506 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763205562034228 to MsgsAck (20c0bb8a0c0)
2025-04-24 12:00:01,506 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:01,506 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 12:00:01,507 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:01,507 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:01,507 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763205567938424 to ResolveUsernameRequest (20c0bb89fa0)
2025-04-24 12:00:01,507 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 12:00:01,509 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:01,509 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:01,703 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763205567938424
2025-04-24 12:00:01,704 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:00:01,705 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763206356807328 to MsgsAck (20c0bb72f60)
2025-04-24 12:00:01,705 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:01,706 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:01,706 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:01,706 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763206362032512 to MsgsAck (20c0bb88170)
2025-04-24 12:00:01,706 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:01,707 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 12:00:01,707 - __main__ - INFO - Searching files for query: breaking bad mp4, types: ['.mp4', '.mkv']
2025-04-24 12:00:01,707 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 12:00:01,708 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:01,708 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:02,119 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 12:00:02,120 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Files lo chusthunna: breaking bad mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 274, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476202, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 12:00:02,121 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 12:00:02,121 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763208316546660 to ResolveUsernameRequest (20c0bb882f0)
2025-04-24 12:00:02,121 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 12:00:02,122 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:02,122 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:02,345 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763208316546660
2025-04-24 12:00:02,346 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:00:02,346 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763209215874892 to MsgsAck (20c0bb89970)
2025-04-24 12:00:02,347 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:02,347 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:02,347 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:02,347 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763209219859344 to MsgsAck (20c0bb88d70)
2025-04-24 12:00:02,347 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:02,348 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 12:00:02,348 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:02,348 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:02,349 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763209229915840 to ResolveUsernameRequest (20c0bb89220)
2025-04-24 12:00:02,349 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 12:00:02,349 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:02,350 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:02,639 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496763209229915840
2025-04-24 12:00:02,639 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:00:02,640 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763210393781880 to MsgsAck (20c0bb88380)
2025-04-24 12:00:02,641 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:02,641 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:02,642 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:02,642 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763210401775580 to MsgsAck (20c0bb88f80)
2025-04-24 12:00:02,642 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:00:02,643 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 12:00:02,644 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 12:00:02,646 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:02,646 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:03,085 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 12:00:03,087 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': "Files em levu for 'breaking bad' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 275, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476203, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 12:00:03,087 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 12:00:03,982 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:00:03,983 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:00:03,985 - telegram._bot - DEBUG - []
2025-04-24 12:00:03,985 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:00:03,986 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:00:13,589 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:00:13,590 - telegram._bot - DEBUG - Getting updates: [826431003]
2025-04-24 12:00:13,592 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000020C0BA53640>]
2025-04-24 12:00:13,592 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:00:13,593 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:00:13,597 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 12:00:14,445 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 12:00:14,446 - telegram._bot - DEBUG - True
2025-04-24 12:00:14,447 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 12:00:14,447 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 12:00:15,041 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 12:00:15,042 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': "Fetching download links for 'Breaking Bad'...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 276, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476215, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 12:00:15,042 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 12:00:15,043 - web_scrappers.utils - DEBUG - Fetching Netnaija: https://www.thenetnaija.co/search?t=Breaking+Bad
2025-04-24 12:00:15,044 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.thenetnaija.co:443
2025-04-24 12:00:16,870 - urllib3.connectionpool - DEBUG - https://www.thenetnaija.co:443 "GET /search?t=Breaking+Bad HTTP/1.1" 301 None
2025-04-24 12:00:16,873 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.thenetnaija.com:443
2025-04-24 12:00:18,541 - urllib3.connectionpool - DEBUG - https://www.thenetnaija.com:443 "GET /search?t=Breaking+Bad HTTP/1.1" 200 None
2025-04-24 12:00:18,728 - web_scrappers.utils - DEBUG - Successful request to https://www.thenetnaija.co/search?t=Breaking+Bad
2025-04-24 12:00:18,776 - web_scrappers.utils - DEBUG - Found 18 elements for selector: article
2025-04-24 12:00:18,777 - web_scrappers.utils - INFO - Found 0 Netnaija links for Breaking Bad
2025-04-24 12:00:18,779 - __main__ - WARNING - No Netnaija links for Breaking Bad
2025-04-24 12:00:21,176 - telegram._bot - DEBUG - Entering: edit_message_text
2025-04-24 12:00:21,812 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/editMessageText "HTTP/1.1 400 Bad Request"
2025-04-24 12:00:21,813 - __main__ - ERROR - TFPDL scraper error: There is no text in the message to edit
2025-04-24 12:00:22,356 - __main__ - ERROR - Torrent1337x scraper error: Cannot connect to host www.1337xx.to:443 ssl:<ssl.SSLContext object at 0x0000020C0BE2EAD0> [The specified network name is no longer available]
2025-04-24 12:00:22,357 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 12:00:22,756 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/sendMessage "HTTP/1.1 200 OK"
2025-04-24 12:00:22,759 - telegram._bot - DEBUG - {'chat': {'id': 861691679, 'type': <ChatType.PRIVATE>, 'first_name': 'N.e.v.e.r', 'username': 'Neemohammanda'}, 'text': 'Links Not Found ra!', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 277, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745476223, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'MovieMawaBot', 'first_name': '@MovieMawaBot', 'id': 7013259213}}
2025-04-24 12:00:22,760 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 12:00:23,846 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:00:23,848 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:00:23,849 - telegram._bot - DEBUG - []
2025-04-24 12:00:23,849 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:00:23,850 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:00:34,062 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:00:34,062 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:00:34,063 - telegram._bot - DEBUG - []
2025-04-24 12:00:34,063 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:00:34,063 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:00:34,102 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763345676124864 to PingRequest (20c0bb713d0)
2025-04-24 12:00:34,102 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:00:34,104 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:00:34,104 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:00:34,293 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496763345676124864
2025-04-24 12:00:34,294 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:00:44,278 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:00:44,279 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:00:44,281 - telegram._bot - DEBUG - []
2025-04-24 12:00:44,281 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:00:44,281 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:00:54,566 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:00:54,567 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:00:54,568 - telegram._bot - DEBUG - []
2025-04-24 12:00:54,568 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:00:54,568 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:01:04,913 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:01:04,916 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:01:04,920 - telegram._bot - DEBUG - []
2025-04-24 12:01:04,924 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:01:04,929 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:01:15,199 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:01:15,201 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:01:15,202 - telegram._bot - DEBUG - []
2025-04-24 12:01:15,202 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:01:15,202 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:01:25,413 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:01:25,415 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:01:25,418 - telegram._bot - DEBUG - []
2025-04-24 12:01:25,419 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:01:25,419 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:01:34,118 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763603443265864 to PingRequest (20c0bb71a30)
2025-04-24 12:01:34,118 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:01:34,123 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:01:34,124 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:01:34,125 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763603469679784 to MsgsAck (20c0be0d1c0)
2025-04-24 12:01:34,125 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:01:34,126 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:01:34,127 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:01:34,401 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496763603443265864
2025-04-24 12:01:34,402 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:01:35,730 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:01:35,732 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:01:35,733 - telegram._bot - DEBUG - []
2025-04-24 12:01:35,733 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:01:35,734 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:01:46,072 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:01:46,074 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:01:46,076 - telegram._bot - DEBUG - []
2025-04-24 12:01:46,076 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:01:46,076 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:01:56,314 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:01:56,315 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:01:56,317 - telegram._bot - DEBUG - []
2025-04-24 12:01:56,318 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:01:56,318 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:02:07,034 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:02:07,036 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:02:07,038 - telegram._bot - DEBUG - []
2025-04-24 12:02:07,038 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:02:07,039 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:02:17,306 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:02:17,307 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:02:17,309 - telegram._bot - DEBUG - []
2025-04-24 12:02:17,309 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:02:17,310 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:02:27,520 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:02:27,521 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:02:27,523 - telegram._bot - DEBUG - []
2025-04-24 12:02:27,523 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:02:27,523 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:02:34,145 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763861243306724 to PingRequest (20c0be0d160)
2025-04-24 12:02:34,146 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:02:34,147 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:02:34,147 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:02:34,147 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496763861256978600 to MsgsAck (20c0bdd83e0)
2025-04-24 12:02:34,148 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:02:34,150 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:02:34,150 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:02:34,346 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496763861243306724
2025-04-24 12:02:34,347 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:02:37,713 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:02:37,714 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:02:37,715 - telegram._bot - DEBUG - []
2025-04-24 12:02:37,716 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:02:37,716 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:02:47,910 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:02:47,911 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:02:47,912 - telegram._bot - DEBUG - []
2025-04-24 12:02:47,913 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:02:47,914 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:02:58,117 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:02:58,118 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:02:58,122 - telegram._bot - DEBUG - []
2025-04-24 12:02:58,122 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:02:58,123 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:03:08,338 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:03:08,360 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:03:08,370 - telegram._bot - DEBUG - []
2025-04-24 12:03:08,371 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:03:08,372 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:03:18,570 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:03:18,577 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:03:18,579 - telegram._bot - DEBUG - []
2025-04-24 12:03:18,583 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:03:18,589 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:03:28,799 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:03:28,805 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:03:28,808 - telegram._bot - DEBUG - []
2025-04-24 12:03:28,809 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:03:28,811 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:03:34,164 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496764119021669608 to PingRequest (20c0bdf4770)
2025-04-24 12:03:34,167 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:03:34,171 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:03:34,172 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:03:34,172 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496764119055739624 to MsgsAck (20c0bdf5550)
2025-04-24 12:03:34,173 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:03:34,174 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:03:34,174 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:03:34,369 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496764119021669608
2025-04-24 12:03:34,374 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:03:39,015 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:03:39,031 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:03:39,033 - telegram._bot - DEBUG - []
2025-04-24 12:03:39,033 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:03:39,034 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:03:49,323 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:03:49,324 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:03:49,325 - telegram._bot - DEBUG - []
2025-04-24 12:03:49,326 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:03:49,326 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:03:59,528 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:03:59,529 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:03:59,530 - telegram._bot - DEBUG - []
2025-04-24 12:03:59,530 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:03:59,531 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:04:09,779 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:04:09,780 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:04:09,780 - telegram._bot - DEBUG - []
2025-04-24 12:04:09,781 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:04:09,781 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:04:19,968 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:04:19,969 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:04:19,970 - telegram._bot - DEBUG - []
2025-04-24 12:04:19,970 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:04:19,971 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:04:30,157 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:04:30,158 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:04:30,159 - telegram._bot - DEBUG - []
2025-04-24 12:04:30,159 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:04:30,159 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:04:34,190 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496764376824205280 to PingRequest (20c0bdf5f70)
2025-04-24 12:04:34,190 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:04:34,193 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:04:34,196 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:04:34,197 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496764376850279688 to MsgsAck (20c0be0e3f0)
2025-04-24 12:04:34,198 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:04:34,205 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:04:34,206 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:04:34,388 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496764376824205280
2025-04-24 12:04:34,389 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:04:40,356 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:04:40,357 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:04:40,358 - telegram._bot - DEBUG - []
2025-04-24 12:04:40,358 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:04:40,358 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:04:50,552 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:04:50,555 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:04:50,558 - telegram._bot - DEBUG - []
2025-04-24 12:04:50,559 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:04:50,560 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:05:00,748 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:05:00,752 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:05:00,752 - telegram._bot - DEBUG - []
2025-04-24 12:05:00,752 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:05:00,752 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:05:10,953 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:05:10,953 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:05:10,954 - telegram._bot - DEBUG - []
2025-04-24 12:05:10,955 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:05:10,955 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:05:21,316 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:05:21,318 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:05:21,319 - telegram._bot - DEBUG - []
2025-04-24 12:05:21,319 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:05:21,319 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:05:31,571 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:05:31,573 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:05:31,575 - telegram._bot - DEBUG - []
2025-04-24 12:05:31,575 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:05:31,575 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:05:34,209 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496764634597792164 to PingRequest (20c0bdf5fd0)
2025-04-24 12:05:34,210 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:05:34,213 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:05:34,213 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:05:34,216 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496764634626556888 to MsgsAck (20c0be1b0e0)
2025-04-24 12:05:34,217 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:05:34,219 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:05:34,220 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:05:34,621 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496764634597792164
2025-04-24 12:05:34,622 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:05:41,769 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:05:41,770 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:05:41,771 - telegram._bot - DEBUG - []
2025-04-24 12:05:41,771 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:05:41,772 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:05:52,035 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:05:52,036 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:05:52,038 - telegram._bot - DEBUG - []
2025-04-24 12:05:52,039 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:05:52,040 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:06:02,275 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:06:02,277 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:06:02,280 - telegram._bot - DEBUG - []
2025-04-24 12:06:02,280 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:06:02,281 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:06:12,515 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:06:12,519 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:06:12,521 - telegram._bot - DEBUG - []
2025-04-24 12:06:12,521 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:06:12,522 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:06:22,729 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:06:22,730 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:06:22,731 - telegram._bot - DEBUG - []
2025-04-24 12:06:22,732 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:06:22,732 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:06:33,098 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:06:33,099 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:06:33,100 - telegram._bot - DEBUG - []
2025-04-24 12:06:33,100 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:06:33,100 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:06:34,231 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496764892381982000 to PingRequest (20c0be0de50)
2025-04-24 12:06:34,231 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:06:34,236 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:06:34,237 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:06:34,238 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496764892411688956 to MsgsAck (20c0bddbce0)
2025-04-24 12:06:34,238 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:06:34,240 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:06:34,240 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:06:34,427 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496764892381982000
2025-04-24 12:06:34,428 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:06:43,290 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:06:43,291 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:06:43,293 - telegram._bot - DEBUG - []
2025-04-24 12:06:43,293 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:06:43,294 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:06:53,577 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:06:53,579 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:06:53,583 - telegram._bot - DEBUG - []
2025-04-24 12:06:53,585 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:06:53,586 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:07:03,788 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:07:03,791 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:07:03,793 - telegram._bot - DEBUG - []
2025-04-24 12:07:03,794 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:07:03,794 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:07:13,986 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:07:13,987 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:07:13,988 - telegram._bot - DEBUG - []
2025-04-24 12:07:13,988 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:07:13,988 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:07:24,183 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:07:24,187 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:07:24,190 - telegram._bot - DEBUG - []
2025-04-24 12:07:24,191 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:07:24,191 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:07:34,252 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496765150168115428 to PingRequest (20c0be1b0b0)
2025-04-24 12:07:34,255 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:07:34,261 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:07:34,263 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:07:34,266 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496765150220557024 to MsgsAck (20c0bba1e80)
2025-04-24 12:07:34,266 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:07:34,269 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:07:34,269 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:07:34,392 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:07:34,393 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:07:34,393 - telegram._bot - DEBUG - []
2025-04-24 12:07:34,394 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:07:34,394 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:07:34,467 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496765150168115428
2025-04-24 12:07:34,468 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:07:44,589 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:07:44,591 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:07:44,591 - telegram._bot - DEBUG - []
2025-04-24 12:07:44,593 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:07:44,593 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:07:54,783 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:07:54,784 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:07:54,786 - telegram._bot - DEBUG - []
2025-04-24 12:07:54,787 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:07:54,787 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:08:05,052 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:08:05,053 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:08:05,055 - telegram._bot - DEBUG - []
2025-04-24 12:08:05,055 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:08:05,057 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:08:15,394 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:08:15,395 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:08:15,397 - telegram._bot - DEBUG - []
2025-04-24 12:08:15,398 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:08:15,398 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:08:25,633 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:08:25,636 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:08:25,637 - telegram._bot - DEBUG - []
2025-04-24 12:08:25,637 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:08:25,638 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:08:34,280 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496765407978167004 to PingRequest (20c0bba1550)
2025-04-24 12:08:34,282 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:08:34,285 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:08:34,285 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:08:34,285 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496765407997384496 to MsgsAck (20c0be0d670)
2025-04-24 12:08:34,287 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:08:34,289 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:08:34,289 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:08:34,508 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496765407978167004
2025-04-24 12:08:34,509 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:08:35,825 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:08:35,826 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:08:35,828 - telegram._bot - DEBUG - []
2025-04-24 12:08:35,830 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:08:35,830 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:08:46,024 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:08:46,025 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:08:46,026 - telegram._bot - DEBUG - []
2025-04-24 12:08:46,026 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:08:46,026 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:08:56,252 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:08:56,253 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:08:56,254 - telegram._bot - DEBUG - []
2025-04-24 12:08:56,254 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:08:56,255 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:09:06,572 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:09:06,574 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:09:06,579 - telegram._bot - DEBUG - []
2025-04-24 12:09:06,580 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:09:06,580 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:09:16,784 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:09:16,785 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:09:16,787 - telegram._bot - DEBUG - []
2025-04-24 12:09:16,787 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:09:16,788 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:09:27,051 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:09:27,052 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:09:27,053 - telegram._bot - DEBUG - []
2025-04-24 12:09:27,054 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:09:27,054 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:09:34,302 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496765665762666784 to PingRequest (20c0bba1670)
2025-04-24 12:09:34,303 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:09:34,305 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:09:34,306 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:09:34,307 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496765665781117520 to MsgsAck (20c0bdd9ee0)
2025-04-24 12:09:34,307 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:09:34,308 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:09:34,309 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:09:34,505 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496765665762666784
2025-04-24 12:09:34,505 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:09:37,323 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:09:37,324 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:09:37,325 - telegram._bot - DEBUG - []
2025-04-24 12:09:37,325 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:09:37,325 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:09:47,663 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:09:47,667 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:09:47,669 - telegram._bot - DEBUG - []
2025-04-24 12:09:47,670 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:09:47,670 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:09:57,896 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:09:57,897 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:09:57,898 - telegram._bot - DEBUG - []
2025-04-24 12:09:57,898 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:09:57,899 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:10:08,136 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:10:08,138 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:10:08,139 - telegram._bot - DEBUG - []
2025-04-24 12:10:08,139 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:10:08,140 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:10:18,341 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:10:18,343 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:10:18,344 - telegram._bot - DEBUG - []
2025-04-24 12:10:18,344 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:10:18,344 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:10:28,606 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:10:28,608 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:10:28,608 - telegram._bot - DEBUG - []
2025-04-24 12:10:28,608 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:10:28,608 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:10:34,318 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496765923526520472 to PingRequest (20c0be0fd70)
2025-04-24 12:10:34,319 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:10:34,322 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:10:34,322 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:10:34,322 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496765923542486884 to MsgsAck (20c0bdf7d10)
2025-04-24 12:10:34,324 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:10:34,326 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:10:34,326 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:10:34,522 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496765923526520472
2025-04-24 12:10:34,522 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:10:38,855 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:10:38,857 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:10:38,858 - telegram._bot - DEBUG - []
2025-04-24 12:10:38,858 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:10:38,859 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:10:49,075 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:10:49,163 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:10:49,164 - telegram._bot - DEBUG - []
2025-04-24 12:10:49,165 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:10:49,166 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:10:59,541 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:10:59,542 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:10:59,544 - telegram._bot - DEBUG - []
2025-04-24 12:10:59,544 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:10:59,545 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:11:09,742 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:11:09,743 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:11:09,744 - telegram._bot - DEBUG - []
2025-04-24 12:11:09,744 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:11:09,744 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:11:19,940 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:11:19,942 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:11:19,943 - telegram._bot - DEBUG - []
2025-04-24 12:11:19,945 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:11:19,946 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:11:30,143 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:11:30,144 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:11:30,145 - telegram._bot - DEBUG - []
2025-04-24 12:11:30,147 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:11:30,147 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:11:34,329 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496766181268209812 to PingRequest (20c0bdf7980)
2025-04-24 12:11:34,329 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:11:34,332 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:11:34,332 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:11:34,332 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496766181280503628 to MsgsAck (20c0bdf5100)
2025-04-24 12:11:34,333 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:11:34,334 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:11:34,335 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:11:34,562 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496766181268209812
2025-04-24 12:11:34,563 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:11:40,344 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:11:40,345 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:11:40,346 - telegram._bot - DEBUG - []
2025-04-24 12:11:40,347 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:11:40,347 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:05,650 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:37:05,690 - telethon.client.updates - DEBUG - Timeout waiting for updates expired
2025-04-24 12:37:05,696 - telethon.network.connection.connection - WARNING - Server closed the connection: [WinError 1236] The network connection was aborted by the local system
2025-04-24 12:37:08,923 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496772772124096640 to PingRequest (20c0bdf5250)
2025-04-24 12:37:08,991 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:37:09,065 - telethon.network.mtprotosender - INFO - Connection closed while sending data
2025-04-24 12:37:09,092 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:37:09,249 - telegram._bot - DEBUG - []
2025-04-24 12:37:09,273 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:37:09,287 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:09,295 - telethon.network.mtprotosender - INFO - Connection closed while receiving data: [WinError 1236] The network connection was aborted by the local system
2025-04-24 12:37:09,330 - telethon.network.mtprotosender - INFO - Closing current connection to begin reconnect...
2025-04-24 12:37:09,402 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 12:37:09,424 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 12:37:09,429 - telethon.network.mtprotosender - WARNING - Attempt 1 at connecting failed: OSError: [WinError 1231] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 12:37:09,431 - telethon.network.connection.connection - INFO - <class 'ConnectionAbortedError'> during disconnect: [WinError 1236] The network connection was aborted by the local system
2025-04-24 12:37:09,436 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:09,436 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:10,542 - telethon.network.mtprotosender - DEBUG - Connection attempt 2...
2025-04-24 12:37:10,681 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:10,759 - telethon.network.mtprotosender - WARNING - Attempt 2 at connecting failed: OSError: [WinError 1231] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 12:37:10,914 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:10,941 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:11,814 - telethon.network.mtprotosender - DEBUG - Connection attempt 3...
2025-04-24 12:37:11,816 - telethon.network.mtprotosender - WARNING - Attempt 3 at connecting failed: OSError: [WinError 1231] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 12:37:12,451 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:12,455 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:12,456 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:12,822 - telethon.network.mtprotosender - DEBUG - Connection attempt 4...
2025-04-24 12:37:12,823 - telethon.network.mtprotosender - WARNING - Attempt 4 at connecting failed: OSError: [WinError 1231] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 12:37:13,832 - telethon.network.mtprotosender - DEBUG - Connection attempt 5...
2025-04-24 12:37:13,835 - telethon.network.mtprotosender - WARNING - Attempt 5 at connecting failed: OSError: [WinError 1231] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 12:37:14,719 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:14,724 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:14,724 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:14,843 - telethon.network.mtprotosender - DEBUG - Connection attempt 6...
2025-04-24 12:37:14,846 - telethon.network.mtprotosender - WARNING - Attempt 6 at connecting failed: OSError: [WinError 1231] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 12:37:15,856 - telethon.network.mtprotosender - INFO - Failed reconnection attempt 1 with ConnectionError
2025-04-24 12:37:16,870 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 12:37:16,870 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 12:37:16,873 - telethon.network.mtprotosender - WARNING - Attempt 1 at connecting failed: OSError: [WinError 1231] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 12:37:17,879 - telethon.network.mtprotosender - DEBUG - Connection attempt 2...
2025-04-24 12:37:17,886 - telethon.network.mtprotosender - WARNING - Attempt 2 at connecting failed: OSError: [WinError 1231] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 12:37:18,116 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:18,191 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:18,215 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 12:37:18,891 - telethon.network.mtprotosender - DEBUG - Connection attempt 3...
2025-04-24 12:37:20,104 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 12:37:20,104 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 12:37:20,412 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 12:37:20,412 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 12:37:20,413 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:37:20,413 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496772821621049200 to PingRequest (20c0bdf5250)
2025-04-24 12:37:20,413 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496772821621049204 to MsgsAck (20c0a1d8f80)
2025-04-24 12:37:20,413 - telethon.network.mtprotosender - DEBUG - Encrypting 2 message(s) in 88 bytes for sending
2025-04-24 12:37:20,414 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:37:20,415 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:37:20,415 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:37:20,416 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496772821633067404 to GetUsersRequest (20c0bdf5ee0)
2025-04-24 12:37:20,417 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 12:37:20,418 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:37:20,418 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:37:20,620 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 12:37:20,620 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 12:37:20,622 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496772821621049200
2025-04-24 12:37:20,622 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:37:20,639 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496772821633067404
2025-04-24 12:37:20,639 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:37:20,640 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496772822529280936 to MsgsAck (20c0b9f1250)
2025-04-24 12:37:20,640 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:37:20,641 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:37:20,642 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:37:20,644 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496772822545278820 to MsgsAck (20c0bdf5340)
2025-04-24 12:37:20,644 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 12:37:20,646 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:37:20,646 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:37:23,274 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:34,104 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:37:34,106 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:37:34,107 - telegram._bot - DEBUG - []
2025-04-24 12:37:34,107 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:37:34,109 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:44,306 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:37:44,308 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:37:44,309 - telegram._bot - DEBUG - []
2025-04-24 12:37:44,310 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:37:44,311 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:37:54,502 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:37:54,503 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:37:54,503 - telegram._bot - DEBUG - []
2025-04-24 12:37:54,504 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:37:54,504 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:38:04,693 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:38:04,694 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:38:04,695 - telegram._bot - DEBUG - []
2025-04-24 12:38:04,695 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:38:04,696 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:38:05,714 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496773016099435344 to PingRequest (20c0bdf4680)
2025-04-24 12:38:05,715 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:38:05,717 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:38:05,718 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:38:05,949 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496773016099435344
2025-04-24 12:38:05,949 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:38:14,891 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:38:14,892 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:38:14,894 - telegram._bot - DEBUG - []
2025-04-24 12:38:14,894 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:38:14,895 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:38:25,092 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:38:25,093 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:38:25,094 - telegram._bot - DEBUG - []
2025-04-24 12:38:25,094 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:38:25,095 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:38:35,328 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:38:35,329 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:38:35,330 - telegram._bot - DEBUG - []
2025-04-24 12:38:35,331 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:38:35,331 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:38:45,508 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:38:45,509 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:38:45,511 - telegram._bot - DEBUG - []
2025-04-24 12:38:45,512 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:38:45,513 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:38:55,716 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:38:55,717 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:38:55,717 - telegram._bot - DEBUG - []
2025-04-24 12:38:55,717 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:38:55,718 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:39:05,718 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496773273813171540 to PingRequest (20c0bdf4890)
2025-04-24 12:39:05,719 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:39:05,722 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:39:05,722 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:39:05,723 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496773273833175812 to MsgsAck (20c0bdd8aa0)
2025-04-24 12:39:05,723 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:39:05,725 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:39:05,725 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:39:05,956 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:39:05,958 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:39:05,958 - telegram._bot - DEBUG - []
2025-04-24 12:39:05,959 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:39:05,959 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:39:05,961 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496773273813171540
2025-04-24 12:39:05,961 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:39:16,132 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:39:16,135 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:39:16,136 - telegram._bot - DEBUG - []
2025-04-24 12:39:16,136 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:39:16,137 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:39:26,333 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:39:26,334 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:39:26,335 - telegram._bot - DEBUG - []
2025-04-24 12:39:26,336 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:39:26,336 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:39:36,573 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:39:36,574 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:39:36,575 - telegram._bot - DEBUG - []
2025-04-24 12:39:36,575 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:39:36,576 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:39:46,771 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:39:46,773 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:39:46,774 - telegram._bot - DEBUG - []
2025-04-24 12:39:46,775 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:39:46,775 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:39:56,961 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:39:56,963 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:39:56,963 - telegram._bot - DEBUG - []
2025-04-24 12:39:56,964 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:39:56,964 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:40:05,743 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496773531610234072 to PingRequest (20c0bdd8d70)
2025-04-24 12:40:05,743 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 12:40:05,747 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:40:05,747 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:40:05,748 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496773531629042436 to MsgsAck (20c0be0c980)
2025-04-24 12:40:05,748 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 12:40:05,750 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 12:40:05,751 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 12:40:05,962 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496773531610234072
2025-04-24 12:40:05,962 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 12:40:07,293 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:40:07,294 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:40:07,295 - telegram._bot - DEBUG - []
2025-04-24 12:40:07,296 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:40:07,296 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 12:40:17,533 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 12:40:17,535 - telegram._bot - DEBUG - No new updates found.
2025-04-24 12:40:17,535 - telegram._bot - DEBUG - []
2025-04-24 12:40:17,536 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 12:40:17,537 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 13:26:17,188 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 13:26:17,378 - telethon.client.updates - DEBUG - Timeout waiting for updates expired
2025-04-24 13:26:17,439 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785436039044260 to PingRequest (20c0be0f740)
2025-04-24 13:26:17,470 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 13:26:17,521 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:26:17,574 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:17,648 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785436879809260 to MsgsAck (20c0be0e450)
2025-04-24 13:26:18,162 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 13:26:18,333 - telegram._bot - DEBUG - No new updates found.
2025-04-24 13:26:18,405 - telegram._bot - DEBUG - []
2025-04-24 13:26:18,523 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 13:26:18,652 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 13:26:18,837 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:26:18,870 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:19,248 - telethon.network.connection.connection - INFO - The server closed the connection while sending
2025-04-24 13:26:19,270 - telethon.network.connection.connection - WARNING - Server closed the connection: [WinError 10054] An existing connection was forcibly closed by the remote host
2025-04-24 13:26:19,972 - telethon.network.connection.connection - INFO - <class 'ConnectionResetError'> during disconnect: [WinError 10054] An existing connection was forcibly closed by the remote host
2025-04-24 13:26:19,984 - telethon.network.mtprotosender - INFO - Connection closed while receiving data: [WinError 10054] An existing connection was forcibly closed by the remote host
2025-04-24 13:26:20,028 - telethon.network.mtprotosender - INFO - Closing current connection to begin reconnect...
2025-04-24 13:26:20,068 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 13:26:20,127 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 13:26:20,178 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: 
2025-04-24 13:26:20,244 - __main__ - ERROR - Update None caused error: httpx HTTPError: 
2025-04-24 13:26:20,490 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 13:26:20,510 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 13:26:20,522 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 13:26:20,995 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 13:26:21,116 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:21,832 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785454793942816 to PingRequest (20c0be0f740)
2025-04-24 13:26:21,835 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 13:26:21,836 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:26:21,836 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:21,841 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:26:21,843 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785454839222320 to GetUsersRequest (20c0be0cc50)
2025-04-24 13:26:21,872 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 13:26:22,027 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:26:22,273 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:22,504 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 13:26:22,562 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496785454793942816
2025-04-24 13:26:22,570 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 13:26:22,674 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:26:22,719 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785458638716708 to PingRequest (20c0be0f740)
2025-04-24 13:26:22,854 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 13:26:22,867 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:26:22,885 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:22,908 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785459393836984 to MsgsAck (20c0be0e0c0)
2025-04-24 13:26:22,944 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 13:26:23,037 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:26:23,054 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:23,071 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496785454839222320
2025-04-24 13:26:23,567 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 13:26:23,572 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:26:23,586 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785462402692448 to GetUsersRequest (20c0be0cc50)
2025-04-24 13:26:23,594 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 13:26:23,635 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:26:23,730 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:23,756 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785463083595884 to MsgsAck (20c0be0eae0)
2025-04-24 13:26:23,765 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 13:26:23,777 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:26:23,901 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:26:23,951 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 13:26:24,053 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 13:26:24,091 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496785458638716708
2025-04-24 13:26:24,122 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:27:06,024 - telethon.network.connection.connection - INFO - The server closed the connection while sending
2025-04-24 13:27:06,141 - telethon.network.connection.connection - WARNING - Server closed the connection: [WinError 10054] An existing connection was forcibly closed by the remote host
2025-04-24 13:27:06,170 - telethon.network.connection.connection - INFO - <class 'ConnectionResetError'> during disconnect: [WinError 10054] An existing connection was forcibly closed by the remote host
2025-04-24 13:27:06,229 - telethon.network.mtprotosender - INFO - Connection closed while receiving data: [WinError 10054] An existing connection was forcibly closed by the remote host
2025-04-24 13:27:06,383 - telegram.ext._updater - DEBUG - Timed out getting Updates: Timed out
2025-04-24 13:27:06,394 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 13:27:06,433 - telethon.network.mtprotosender - INFO - Closing current connection to begin reconnect...
2025-04-24 13:27:06,444 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 13:27:06,448 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 13:27:07,689 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 13:27:07,711 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 13:27:07,712 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 13:27:07,713 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 13:27:07,713 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:27:07,714 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785651893578760 to GetUsersRequest (20c0be0cc50)
2025-04-24 13:27:07,714 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785651893578764 to MsgsAck (20c0be0fbf0)
2025-04-24 13:27:07,714 - telethon.network.mtprotosender - DEBUG - Encrypting 2 message(s) in 108 bytes for sending
2025-04-24 13:27:07,715 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:27:07,762 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:27:07,767 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:27:07,780 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785652156045188 to GetUsersRequest (20c0be0fb90)
2025-04-24 13:27:07,781 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 13:27:07,783 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:27:07,784 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:27:12,262 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 13:27:12,277 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 13:27:12,311 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496785651893578760]
2025-04-24 13:27:12,378 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:27:12,403 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 13:27:12,406 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496785651893578760
2025-04-24 13:27:12,407 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496785652156045188]
2025-04-24 13:27:12,410 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:27:12,411 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785672154352548 to MsgsAck (20c0bdf75f0)
2025-04-24 13:27:12,412 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 13:27:12,413 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:27:12,413 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:27:12,413 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785672162392024 to MsgsAck (20c0bdf7e90)
2025-04-24 13:27:12,414 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 13:27:12,417 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496785652156045188
2025-04-24 13:27:12,417 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:27:12,418 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:27:12,418 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:27:12,419 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785672186416988 to MsgsAck (20c0bb33f80)
2025-04-24 13:27:12,419 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785672186416992 to MsgsAck (20c0bdf79e0)
2025-04-24 13:27:12,420 - telethon.network.mtprotosender - DEBUG - Encrypting 2 message(s) in 96 bytes for sending
2025-04-24 13:27:12,422 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:27:12,422 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:27:17,118 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 13:27:17,119 - telegram._bot - DEBUG - No new updates found.
2025-04-24 13:27:17,120 - telegram._bot - DEBUG - []
2025-04-24 13:27:17,120 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 13:27:17,120 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 13:27:17,404 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496785693602928652 to PingRequest (20c0be0e840)
2025-04-24 13:27:17,416 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 13:27:17,429 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 13:27:17,480 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 13:27:17,723 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496785693602928652
2025-04-24 13:27:17,828 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 13:27:27,305 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 13:27:27,308 - telegram._bot - DEBUG - No new updates found.
2025-04-24 13:27:27,309 - telegram._bot - DEBUG - []
2025-04-24 13:27:27,310 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 13:27:27,311 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 13:27:37,504 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 13:27:37,506 - telegram._bot - DEBUG - No new updates found.
2025-04-24 13:27:37,507 - telegram._bot - DEBUG - []
2025-04-24 13:27:37,507 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 13:27:37,507 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 13:27:47,687 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 13:27:47,690 - telegram._bot - DEBUG - No new updates found.
2025-04-24 13:27:47,691 - telegram._bot - DEBUG - []
2025-04-24 13:27:47,691 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 13:27:47,693 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 13:27:57,951 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getUpdates "HTTP/1.1 200 OK"
2025-04-24 13:27:57,951 - telegram._bot - DEBUG - No new updates found.
2025-04-24 13:27:57,952 - telegram._bot - DEBUG - []
2025-04-24 13:27:57,952 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 13:27:57,952 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:03:46,617 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 14:03:46,624 - __main__ - INFO - Starting MovieMawaBot...
2025-04-24 14:03:49,786 - __main__ - INFO - Bot polling started...
2025-04-24 14:03:49,792 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 14:03:52,385 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs/getMe "HTTP/1.1 401 Unauthorized"
2025-04-24 14:03:52,387 - telegram.ext._application - DEBUG - This Application is already shut down. Returning.
2025-04-24 14:03:52,388 - __main__ - ERROR - General error: The token `7013259213:AAHXieC41Bxe2xOeFlIx1yYeodaV46U8WDs` was rejected by the server.
2025-04-24 14:05:06,183 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 14:05:06,185 - __main__ - INFO - Starting MovieMawaBot...
2025-04-24 14:05:07,115 - __main__ - INFO - Bot polling started...
2025-04-24 14:05:07,116 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 14:05:11,706 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 14:05:11,707 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 14:05:11,707 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 14:05:11,707 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 14:05:11,708 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 14:05:11,708 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 14:05:11,709 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 14:05:11,709 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 14:05:12,011 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 14:05:12,013 - telegram._bot - DEBUG - True
2025-04-24 14:05:12,014 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 14:05:12,014 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 14:05:12,015 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 14:05:12,015 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 14:05:12,016 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 14:05:12,017 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:05:12,019 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 14:05:12,019 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 14:05:12,020 - telegram.ext._application - INFO - Application started
2025-04-24 14:05:12,020 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 14:05:12,021 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 14:05:22,897 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:05:22,900 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:05:22,900 - telegram._bot - DEBUG - []
2025-04-24 14:05:22,900 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:05:22,901 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:05:33,105 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:05:33,106 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:05:33,107 - telegram._bot - DEBUG - []
2025-04-24 14:05:33,108 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:05:33,108 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:05:43,301 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:05:43,303 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:05:43,303 - telegram._bot - DEBUG - []
2025-04-24 14:05:43,304 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:05:43,304 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:05:53,500 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:05:53,502 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:05:53,502 - telegram._bot - DEBUG - []
2025-04-24 14:05:53,503 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:05:53,503 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:03,853 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:06:03,854 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:06:03,854 - telegram._bot - DEBUG - []
2025-04-24 14:06:03,855 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:06:03,855 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:14,083 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:06:14,084 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:06:14,085 - telegram._bot - DEBUG - []
2025-04-24 14:06:14,085 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:06:14,086 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:24,304 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:06:24,313 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:06:24,313 - telegram._bot - DEBUG - []
2025-04-24 14:06:24,314 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:06:24,314 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:29,742 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:06:29,743 - telegram._bot - DEBUG - Getting updates: [954247015]
2025-04-24 14:06:29,743 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A7280>]
2025-04-24 14:06:29,744 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:06:29,744 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:29,746 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247015, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 1, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483790, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:06:29,746 - __main__ - INFO - Received /start command
2025-04-24 14:06:29,746 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:30,516 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:30,524 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to MovieMawaBot! Movies, series, PDFs—em adigina search chesi pampistha. Ex: 'inception', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 145}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 2, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483791, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:30,530 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:38,691 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:06:38,692 - telegram._bot - DEBUG - Getting updates: [954247016]
2025-04-24 14:06:38,693 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A6E00>]
2025-04-24 14:06:38,694 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:06:38,694 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:38,695 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247016, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 3, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483799, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:06:38,696 - __main__ - INFO - Received /start command
2025-04-24 14:06:38,696 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:39,467 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:39,470 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to MovieMawaBot! Movies, series, PDFs—em adigina search chesi pampistha. Ex: 'inception', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 145}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 4, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483800, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:39,471 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:47,307 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:06:47,308 - telegram._bot - DEBUG - Getting updates: [954247017]
2025-04-24 14:06:47,308 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A5900>]
2025-04-24 14:06:47,309 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:06:47,309 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:47,310 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247017, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Devara', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 5, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483808, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:06:47,311 - __main__ - INFO - Received message: devara
2025-04-24 14:06:47,312 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:48,105 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:48,105 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 6, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483809, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:48,106 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:49,743 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:06:49,744 - telegram._bot - DEBUG - Getting updates: [954247018]
2025-04-24 14:06:49,745 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A7100>]
2025-04-24 14:06:49,746 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:06:49,746 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:49,747 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 6, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483809, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488946312115109', 'data': 'movie:devara', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247018}
2025-04-24 14:06:49,748 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:06:50,123 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:06:50,125 - telegram._bot - DEBUG - True
2025-04-24 14:06:50,125 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:06:50,126 - __main__ - INFO - Searching movie: devara
2025-04-24 14:06:50,126 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false
2025-04-24 14:06:50,129 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:06:50,679 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:06:50,683 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:06:50,685 - __main__ - INFO - TMDB found 12 results for devara
2025-04-24 14:06:50,687 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 14:06:51,385 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=devara+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 14:06:51,388 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:06:51,855 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 14:06:52,553 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 14:06:54,182 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 14:06:54,362 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 14:06:54,362 - __main__ - INFO - Discovering groups...
2025-04-24 14:06:54,363 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 14:06:54,363 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 14:06:54,364 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 14:06:54,366 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:06:54,372 - telegram._bot - DEBUG - Getting updates: [954247019]
2025-04-24 14:06:54,375 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A59C0>]
2025-04-24 14:06:54,376 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:06:54,380 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:06:54,544 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 14:06:54,559 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 14:06:54,581 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 14:06:54,582 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 14:06:54,623 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:54,641 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795899394655368 to InvokeWithLayerRequest (257c763d430)
2025-04-24 14:06:54,649 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 14:06:54,661 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:54,664 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:54,665 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:55,052 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496795899394655368
2025-04-24 14:06:55,053 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 14:06:55,053 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:55,053 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795901336966300 to InvokeWithLayerRequest (257c763d430)
2025-04-24 14:06:55,055 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 14:06:55,056 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:55,057 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:55,057 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795901350400708 to MsgsAck (257c761d760)
2025-04-24 14:06:55,058 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:55,059 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:55,059 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:55,335 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 14:06:55,336 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 14:06:55,336 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496795901336966300]
2025-04-24 14:06:55,336 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:55,339 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795901336966300
2025-04-24 14:06:55,340 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:55,341 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795902488900924 to GetUsersRequest (257c763d340)
2025-04-24 14:06:55,341 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:06:55,342 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:55,342 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:55,343 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795902497415328 to MsgsAck (257c725acc0)
2025-04-24 14:06:55,343 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 14:06:55,345 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:55,345 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:55,641 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795902488900924
2025-04-24 14:06:55,642 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:55,642 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795903692195676 to MsgsAck (257c763cfb0)
2025-04-24 14:06:55,643 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:55,644 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:55,644 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:55,645 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795903705087448 to MsgsAck (257c763cf80)
2025-04-24 14:06:55,645 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:55,646 - __main__ - INFO - Client connected successfully
2025-04-24 14:06:55,647 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:55,648 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:55,649 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:56,046 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:56,047 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 8, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483816, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:56,048 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:56,048 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795905611198808 to SearchRequest (257c763eae0)
2025-04-24 14:06:56,049 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:06:56,050 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:56,051 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:56,332 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795905611198808
2025-04-24 14:06:56,337 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:56,338 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795906770631220 to MsgsAck (257c7292000)
2025-04-24 14:06:56,339 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:56,342 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:56,342 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:56,342 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795906786630060 to MsgsAck (257c763cc20)
2025-04-24 14:06:56,342 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:56,343 - __main__ - ERROR - Error discovering groups: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:06:56,343 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:56,344 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:56,346 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:56,720 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:56,722 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Error ra: The key is not registered in the system (caused by SearchRequest)', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 9, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483817, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:56,723 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:56,723 - __main__ - INFO - Searching files for query: devara, types: ['.mp4', '.mkv']
2025-04-24 14:06:56,724 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:57,094 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:57,095 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: devara...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 10, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483818, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:57,096 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:57,097 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795910103749304 to SearchRequest (257c763f7d0)
2025-04-24 14:06:57,099 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 14:06:57,101 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:57,101 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:57,296 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795910103749304
2025-04-24 14:06:57,297 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:57,297 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795910903060940 to MsgsAck (257c763e9f0)
2025-04-24 14:06:57,297 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:57,298 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:57,299 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:57,299 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795910909312276 to MsgsAck (257c763f0b0)
2025-04-24 14:06:57,299 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:57,301 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:06:57,302 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:57,302 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:57,302 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795910922536876 to SearchRequest (257c763e9f0)
2025-04-24 14:06:57,303 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 14:06:57,304 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:57,305 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:57,500 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795910922536876
2025-04-24 14:06:57,500 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:57,501 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795911718445804 to MsgsAck (257c763e930)
2025-04-24 14:06:57,502 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:57,503 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:57,503 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:57,503 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795911727290180 to MsgsAck (257c763eae0)
2025-04-24 14:06:57,503 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:57,505 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:06:57,506 - __main__ - INFO - Searching files for query: devara movie, types: ['.mp4', '.mkv']
2025-04-24 14:06:57,506 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:57,508 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:57,508 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:57,892 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:57,893 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: devara movie...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 11, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483818, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:57,894 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:57,895 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795913292548208 to SearchRequest (257c763e030)
2025-04-24 14:06:57,896 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:06:57,897 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:57,898 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,088 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795913292548208
2025-04-24 14:06:58,088 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:58,088 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795914361723572 to MsgsAck (257c763f4a0)
2025-04-24 14:06:58,089 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:58,090 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,091 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,091 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795914374178560 to MsgsAck (257c763f3e0)
2025-04-24 14:06:58,092 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:58,093 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:06:58,094 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,094 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,095 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795914389784484 to SearchRequest (257c763f4a0)
2025-04-24 14:06:58,095 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:06:58,096 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,097 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,295 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795914389784484
2025-04-24 14:06:58,296 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:58,296 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795915194865852 to MsgsAck (257c763ef00)
2025-04-24 14:06:58,297 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:58,298 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,299 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,300 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795915208549172 to MsgsAck (257c759c680)
2025-04-24 14:06:58,300 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:58,302 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:06:58,302 - __main__ - INFO - Searching files for query: devara mp4, types: ['.mp4', '.mkv']
2025-04-24 14:06:58,303 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:58,304 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,305 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,678 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:58,681 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: devara mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 12, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483819, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:58,690 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:58,690 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795916770936640 to SearchRequest (257c763e390)
2025-04-24 14:06:58,691 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:06:58,695 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,695 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,887 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795916770936640
2025-04-24 14:06:58,888 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:58,889 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795917566035896 to MsgsAck (257c763f290)
2025-04-24 14:06:58,889 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:58,890 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,890 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,891 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795917574520736 to MsgsAck (257c763ec90)
2025-04-24 14:06:58,891 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:58,892 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:06:58,893 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,893 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:58,894 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795917586259516 to SearchRequest (257c763f290)
2025-04-24 14:06:58,894 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:06:58,896 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:58,896 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:59,080 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795917586259516
2025-04-24 14:06:59,081 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:06:59,081 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795918627568516 to MsgsAck (257c761d910)
2025-04-24 14:06:59,081 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:59,083 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:59,083 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:59,084 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795918640548024 to MsgsAck (257c761d970)
2025-04-24 14:06:59,085 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:06:59,085 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:06:59,085 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:06:59,088 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:06:59,088 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:06:59,468 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:06:59,469 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'devara' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 13, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483820, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:06:59,474 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:06:59,477 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 6, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483809, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488947638205647', 'data': 'movie:devara', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247019}
2025-04-24 14:06:59,478 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:06:59,839 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:06:59,840 - telegram._bot - DEBUG - True
2025-04-24 14:06:59,840 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:06:59,840 - __main__ - INFO - Searching movie: devara
2025-04-24 14:06:59,840 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false
2025-04-24 14:06:59,842 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:07:00,045 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:07:00,069 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:07:00,070 - __main__ - INFO - TMDB found 12 results for devara
2025-04-24 14:07:00,100 - __main__ - DEBUG - Returning cached trailer for devara
2025-04-24 14:07:00,110 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:07:00,201 - __main__ - WARNING - Genre fetch failed, retrying 1...
2025-04-24 14:07:02,268 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:07:02,451 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 14:07:02,824 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 14:07:03,224 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 14:07:03,232 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 14:07:03,233 - __main__ - INFO - Discovering groups...
2025-04-24 14:07:03,233 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:03,627 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:03,628 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 15, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483824, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:03,629 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:03,629 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795938001577180 to SearchRequest (257c765b8c0)
2025-04-24 14:07:03,630 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:07:03,631 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:03,631 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:03,870 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795938001577180
2025-04-24 14:07:03,871 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:03,871 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795938967209620 to MsgsAck (257c761f320)
2025-04-24 14:07:03,871 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:03,872 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:03,872 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:03,873 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795938976513664 to MsgsAck (257c761fb90)
2025-04-24 14:07:03,873 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:03,873 - __main__ - ERROR - Error discovering groups: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:03,875 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:03,879 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:03,880 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:04,276 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:04,278 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Error ra: The key is not registered in the system (caused by SearchRequest)', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 16, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483825, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:04,279 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:04,280 - __main__ - INFO - Searching files for query: devara, types: ['.mp4', '.mkv']
2025-04-24 14:07:04,280 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:04,580 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:04,581 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:07:04,582 - telegram._bot - DEBUG - []
2025-04-24 14:07:04,585 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:04,586 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:04,646 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:04,648 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: devara...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 17, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483825, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:04,648 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:04,652 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795942385725424 to SearchRequest (257c7658aa0)
2025-04-24 14:07:04,653 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 14:07:04,655 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:04,656 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:05,058 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795942385725424
2025-04-24 14:07:05,062 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:05,062 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795944322261856 to MsgsAck (257c7659ac0)
2025-04-24 14:07:05,062 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:05,063 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:05,063 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:05,063 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795944326545760 to MsgsAck (257c765b350)
2025-04-24 14:07:05,064 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:05,064 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:05,064 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:05,066 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:05,066 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795944336149260 to SearchRequest (257c7659ac0)
2025-04-24 14:07:05,066 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 14:07:05,070 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:05,070 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:05,401 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795944336149260
2025-04-24 14:07:05,404 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:05,406 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795945698054360 to MsgsAck (257c7659d30)
2025-04-24 14:07:05,408 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:05,413 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:05,415 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:05,417 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795945742056892 to MsgsAck (257c765a060)
2025-04-24 14:07:05,418 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:05,423 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:05,426 - __main__ - INFO - Searching files for query: devara movie, types: ['.mp4', '.mkv']
2025-04-24 14:07:05,433 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:05,440 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:05,454 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:05,874 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:05,875 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: devara movie...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 18, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483826, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:05,876 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:05,877 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795947581786200 to SearchRequest (257c7659250)
2025-04-24 14:07:05,877 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:07:05,878 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:05,879 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,073 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795947581786200
2025-04-24 14:07:06,074 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:06,074 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795948665691068 to MsgsAck (257c7659760)
2025-04-24 14:07:06,075 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:06,076 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,078 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,078 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795948679281880 to MsgsAck (257c765a930)
2025-04-24 14:07:06,079 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:06,080 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:06,081 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,081 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,081 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795948691352536 to SearchRequest (257c7659760)
2025-04-24 14:07:06,082 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:07:06,084 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,085 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,267 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795948691352536
2025-04-24 14:07:06,267 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:06,269 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795949443258928 to MsgsAck (257c7658e90)
2025-04-24 14:07:06,270 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:06,270 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,272 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,272 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795949455402064 to MsgsAck (257c7658b90)
2025-04-24 14:07:06,273 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:06,274 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:06,275 - __main__ - INFO - Searching files for query: devara mp4, types: ['.mp4', '.mkv']
2025-04-24 14:07:06,275 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:06,277 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,277 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,653 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:06,657 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: devara mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 19, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483827, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:06,658 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:06,659 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795951004249264 to SearchRequest (257c7658a10)
2025-04-24 14:07:06,660 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:07:06,661 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,661 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,856 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795951004249264
2025-04-24 14:07:06,857 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:06,857 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795951798032452 to MsgsAck (257c7658a40)
2025-04-24 14:07:06,859 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:06,860 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,860 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,861 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795951811335256 to MsgsAck (257c76581d0)
2025-04-24 14:07:06,861 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:06,862 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:06,863 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,863 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:06,863 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795951819946932 to SearchRequest (257c763cc20)
2025-04-24 14:07:06,864 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:07:06,865 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:06,865 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:07,057 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496795951819946932
2025-04-24 14:07:07,058 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:07,059 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795952900383284 to MsgsAck (257c763c560)
2025-04-24 14:07:07,060 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:07,061 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:07,062 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:07,062 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496795952910023024 to MsgsAck (257c763c4a0)
2025-04-24 14:07:07,063 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:07,064 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:07,064 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:07,066 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:07,068 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:07,452 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:07,454 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'devara' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 20, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483828, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:07,455 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:14,786 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:14,787 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:07:14,787 - telegram._bot - DEBUG - []
2025-04-24 14:07:14,787 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:14,789 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:24,987 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:24,989 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:07:24,990 - telegram._bot - DEBUG - []
2025-04-24 14:07:24,990 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:24,990 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:29,027 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:29,028 - telegram._bot - DEBUG - Getting updates: [954247020]
2025-04-24 14:07:29,029 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A7340>]
2025-04-24 14:07:29,029 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:29,030 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:29,030 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247020, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Neet pg 2024 question paper', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 21, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483849, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:07:29,031 - __main__ - INFO - Received message: neet pg 2024 question paper
2025-04-24 14:07:29,032 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:30,113 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:30,115 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:neet pg 2024 question paper', 'text': 'Movie'}, {'callback_data': 'series:neet pg 2024 question paper', 'text': 'Series'}, {'callback_data': 'pdf:neet pg 2024 question paper', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'neet pg 2024 question paper' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 22, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483851, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:30,116 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:31,995 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:31,997 - telegram._bot - DEBUG - Getting updates: [954247021]
2025-04-24 14:07:31,997 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A7700>]
2025-04-24 14:07:31,997 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:31,999 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:32,000 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:neet pg 2024 question paper', 'text': 'Movie'}, {'callback_data': 'series:neet pg 2024 question paper', 'text': 'Series'}, {'callback_data': 'pdf:neet pg 2024 question paper', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'neet pg 2024 question paper' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 22, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483851, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488946699162416', 'data': 'pdf:neet pg 2024 question paper', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247021}
2025-04-24 14:07:32,001 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:07:32,365 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:07:32,366 - telegram._bot - DEBUG - True
2025-04-24 14:07:32,366 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:07:32,367 - __main__ - INFO - Searching pdf: neet pg 2024 question paper
2025-04-24 14:07:32,367 - __main__ - INFO - Discovering groups...
2025-04-24 14:07:32,368 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:32,771 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:32,772 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 23, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483853, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:32,773 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:32,774 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796063134467112 to SearchRequest (257c782f6b0)
2025-04-24 14:07:32,774 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:07:32,775 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:32,776 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:33,018 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796063134467112
2025-04-24 14:07:33,020 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:33,020 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796064411733260 to MsgsAck (257c763daf0)
2025-04-24 14:07:33,020 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:33,021 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:33,022 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:33,023 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796064423593152 to MsgsAck (257c763c620)
2025-04-24 14:07:33,023 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:33,024 - __main__ - ERROR - Error discovering groups: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:33,025 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:33,026 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:33,027 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:33,433 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:33,435 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Error ra: The key is not registered in the system (caused by SearchRequest)', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 24, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483854, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:33,435 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:33,436 - __main__ - INFO - Searching files for query: neet pg 2024 question paper, types: ['.pdf']
2025-04-24 14:07:33,437 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:33,925 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:33,926 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: neet pg 2024 question paper...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 25, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483854, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:33,927 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:33,929 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796068048107732 to SearchRequest (257c7824e60)
2025-04-24 14:07:33,929 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 104 bytes for sending
2025-04-24 14:07:33,931 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:33,931 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,123 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796068048107732
2025-04-24 14:07:34,124 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:34,125 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796069130002252 to MsgsAck (257c782f5c0)
2025-04-24 14:07:34,127 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:34,127 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,127 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,127 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796069137507668 to MsgsAck (257c782faa0)
2025-04-24 14:07:34,127 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:34,129 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:34,130 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,130 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,130 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796069147400132 to SearchRequest (257c782f5c0)
2025-04-24 14:07:34,130 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 104 bytes for sending
2025-04-24 14:07:34,132 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,132 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,316 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796069147400132
2025-04-24 14:07:34,317 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:34,317 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796069897681468 to MsgsAck (257c7824c50)
2025-04-24 14:07:34,319 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:34,319 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,320 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,320 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796069906459084 to MsgsAck (257c7824200)
2025-04-24 14:07:34,321 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:34,322 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:34,322 - __main__ - INFO - Searching files for query: neet pg 2024 question paper pdf, types: ['.pdf']
2025-04-24 14:07:34,323 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:34,325 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,325 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,697 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:34,700 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: neet pg 2024 question paper pdf...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 26, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483855, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:34,701 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:34,703 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796071438135376 to SearchRequest (257c5da46e0)
2025-04-24 14:07:34,704 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 108 bytes for sending
2025-04-24 14:07:34,705 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,706 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,892 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796071438135376
2025-04-24 14:07:34,894 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:34,894 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796072202527276 to MsgsAck (257c725acc0)
2025-04-24 14:07:34,895 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:34,896 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,897 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,897 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796072216790428 to MsgsAck (257c74f6a80)
2025-04-24 14:07:34,898 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:34,899 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:34,900 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,900 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:34,901 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796072231325380 to SearchRequest (257c725acc0)
2025-04-24 14:07:34,901 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 108 bytes for sending
2025-04-24 14:07:34,903 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:34,903 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:35,098 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796072231325380
2025-04-24 14:07:35,099 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:35,099 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796073318774100 to MsgsAck (257c757b560)
2025-04-24 14:07:35,100 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:35,102 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:35,103 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:35,103 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796073333733432 to MsgsAck (257c75e4c20)
2025-04-24 14:07:35,104 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:35,105 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:35,105 - __main__ - INFO - Searching files for query: neet pg 2024 question paper pdf, types: ['.pdf']
2025-04-24 14:07:35,106 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:35,107 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:35,108 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:35,512 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:35,514 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: neet pg 2024 question paper pdf...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 27, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483856, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:35,515 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:35,516 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796074987410420 to SearchRequest (257c763d580)
2025-04-24 14:07:35,517 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 108 bytes for sending
2025-04-24 14:07:35,518 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:35,520 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:35,724 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796074987410420
2025-04-24 14:07:35,725 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:35,725 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796075821723812 to MsgsAck (257c763f890)
2025-04-24 14:07:35,726 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:35,727 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:35,727 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:35,727 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796075832990520 to MsgsAck (257c763de80)
2025-04-24 14:07:35,729 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:35,729 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:35,730 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:35,731 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:35,731 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796075845056408 to SearchRequest (257c763f890)
2025-04-24 14:07:35,732 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 108 bytes for sending
2025-04-24 14:07:35,733 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:35,735 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:35,938 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796075845056408
2025-04-24 14:07:35,939 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:35,940 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796076681468840 to MsgsAck (257c763ec30)
2025-04-24 14:07:35,940 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:35,941 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:35,942 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:35,942 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796076689472072 to MsgsAck (257c763c350)
2025-04-24 14:07:35,943 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:35,944 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:35,945 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:35,946 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:35,946 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:36,392 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:36,394 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'neet pg 2024 question paper' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 28, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483857, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:36,394 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:42,200 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:42,201 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:07:42,202 - telegram._bot - DEBUG - []
2025-04-24 14:07:42,202 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:42,203 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:45,218 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:45,219 - telegram._bot - DEBUG - Getting updates: [954247022]
2025-04-24 14:07:45,220 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A7940>]
2025-04-24 14:07:45,221 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:45,222 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:45,223 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247022, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Inception', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 29, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483866, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:07:45,223 - __main__ - INFO - Received message: inception
2025-04-24 14:07:45,225 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:46,025 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:46,026 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:inception', 'text': 'Movie'}, {'callback_data': 'series:inception', 'text': 'Series'}, {'callback_data': 'pdf:inception', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'inception' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 30, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483866, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:46,027 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:47,683 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:47,686 - telegram._bot - DEBUG - Getting updates: [954247023]
2025-04-24 14:07:47,686 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A77C0>]
2025-04-24 14:07:47,687 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:47,687 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:47,687 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:inception', 'text': 'Movie'}, {'callback_data': 'series:inception', 'text': 'Series'}, {'callback_data': 'pdf:inception', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'inception' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 30, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483866, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488946523695971', 'data': 'movie:inception', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247023}
2025-04-24 14:07:47,689 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:07:48,145 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:07:48,146 - telegram._bot - DEBUG - True
2025-04-24 14:07:48,147 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:07:48,147 - __main__ - INFO - Searching movie: inception
2025-04-24 14:07:48,150 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=inception&page=1&include_adult=false
2025-04-24 14:07:48,152 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:07:48,356 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=inception&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:07:48,358 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:07:48,359 - __main__ - INFO - TMDB found 2 results for inception
2025-04-24 14:07:48,362 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 14:07:49,132 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=inception+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 14:07:49,137 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:07:49,220 - __main__ - WARNING - Genre fetch failed, retrying 1...
2025-04-24 14:07:51,225 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:07:51,379 - __main__ - WARNING - Genre fetch failed, retrying 2...
2025-04-24 14:07:52,725 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:07:52,725 - telegram._bot - DEBUG - Getting updates: [954247024]
2025-04-24 14:07:52,727 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000257C74A6740>]
2025-04-24 14:07:52,727 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:07:52,727 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:07:53,396 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:07:53,558 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 14:07:54,019 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 14:07:55,671 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796161506929796 to PingRequest (257c761f080)
2025-04-24 14:07:55,675 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:07:55,676 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:55,676 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:55,944 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496796161506929796
2025-04-24 14:07:55,945 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:56,069 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 14:07:56,076 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 14:07:56,076 - __main__ - INFO - Discovering groups...
2025-04-24 14:07:56,078 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:56,461 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:56,463 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 32, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483877, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:56,463 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:56,464 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796164973041576 to SearchRequest (257c7658bf0)
2025-04-24 14:07:56,465 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:07:56,467 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:56,467 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:56,467 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796164986650508 to MsgsAck (257c757b560)
2025-04-24 14:07:56,469 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:56,470 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:56,470 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:56,662 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796164973041576
2025-04-24 14:07:56,663 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:56,663 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796165767622036 to MsgsAck (257c761f080)
2025-04-24 14:07:56,663 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:56,665 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:56,666 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:56,666 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796165781010668 to MsgsAck (257c765a450)
2025-04-24 14:07:56,666 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:56,667 - __main__ - ERROR - Error discovering groups: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:56,668 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:56,669 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:56,669 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:57,062 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:57,064 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Error ra: The key is not registered in the system (caused by SearchRequest)', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 33, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483878, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:57,065 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:57,065 - __main__ - INFO - Searching files for query: inception, types: ['.mp4', '.mkv']
2025-04-24 14:07:57,066 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:57,448 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:57,450 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: inception...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 34, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483878, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:57,451 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:57,452 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796169219320936 to SearchRequest (257c763c110)
2025-04-24 14:07:57,452 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:07:57,453 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:57,455 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:57,691 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796169219320936
2025-04-24 14:07:57,691 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:57,691 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796170177061720 to MsgsAck (257c765b950)
2025-04-24 14:07:57,691 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:57,692 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:57,693 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:57,693 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796170186063452 to MsgsAck (257c765baa0)
2025-04-24 14:07:57,694 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:57,695 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:57,696 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:57,696 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:57,697 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796170194478676 to SearchRequest (257c763dee0)
2025-04-24 14:07:57,697 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:07:57,698 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:57,699 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:57,891 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796170194478676
2025-04-24 14:07:57,891 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:57,892 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796170980006860 to MsgsAck (257c763c200)
2025-04-24 14:07:57,893 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:57,893 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:57,893 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:57,893 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796170985986396 to MsgsAck (257c763df40)
2025-04-24 14:07:57,893 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:57,895 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:57,895 - __main__ - INFO - Searching files for query: inception movie, types: ['.mp4', '.mkv']
2025-04-24 14:07:57,895 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:57,896 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:57,897 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:58,286 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:58,288 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: inception movie...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 35, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483879, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:58,289 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:58,290 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796172868974972 to SearchRequest (257c763c800)
2025-04-24 14:07:58,291 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:07:58,292 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:58,292 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:58,519 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796172868974972
2025-04-24 14:07:58,520 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:58,521 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796173787330912 to MsgsAck (257c763ffb0)
2025-04-24 14:07:58,523 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:58,524 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:58,525 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:58,525 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796173805749224 to MsgsAck (257c763e630)
2025-04-24 14:07:58,526 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:58,527 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:58,527 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:58,528 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:58,528 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796173819356248 to SearchRequest (257c763ffb0)
2025-04-24 14:07:58,529 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:07:58,531 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:58,531 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:58,745 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796173819356248
2025-04-24 14:07:58,745 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:58,746 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796174690915392 to MsgsAck (257c763d5b0)
2025-04-24 14:07:58,746 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:58,747 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:58,747 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:58,748 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796174698566720 to MsgsAck (257c763c0e0)
2025-04-24 14:07:58,748 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:58,749 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:58,749 - __main__ - INFO - Searching files for query: inception mp4, types: ['.mp4', '.mkv']
2025-04-24 14:07:58,751 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:58,752 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:58,752 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:59,393 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:07:59,410 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: inception mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 36, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483880, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:07:59,422 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:07:59,423 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796177695988584 to SearchRequest (257c763f5f0)
2025-04-24 14:07:59,429 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:07:59,431 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:59,439 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:59,665 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796177695988584
2025-04-24 14:07:59,666 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:59,668 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796178675531316 to MsgsAck (257c75e4b30)
2025-04-24 14:07:59,668 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:59,669 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:59,671 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:59,672 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796178687530448 to MsgsAck (257c75e4a40)
2025-04-24 14:07:59,672 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:59,674 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:59,675 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:59,675 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:59,676 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796178707550932 to SearchRequest (257c75e4b30)
2025-04-24 14:07:59,676 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:07:59,678 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:59,678 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:59,868 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796178707550932
2025-04-24 14:07:59,868 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:07:59,868 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796179474541592 to MsgsAck (257c7342780)
2025-04-24 14:07:59,869 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:59,870 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:59,870 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:07:59,870 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796179482594420 to MsgsAck (257c763d850)
2025-04-24 14:07:59,870 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:07:59,871 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:07:59,872 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:07:59,873 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:07:59,874 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:00,262 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:08:00,264 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'inception' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 37, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483881, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:08:00,265 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:08:00,265 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:inception', 'text': 'Movie'}, {'callback_data': 'series:inception', 'text': 'Series'}, {'callback_data': 'pdf:inception', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'inception' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 30, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483866, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488945689926857', 'data': 'movie:inception', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247024}
2025-04-24 14:08:00,267 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:08:00,639 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:08:00,640 - telegram._bot - DEBUG - True
2025-04-24 14:08:00,641 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:08:00,641 - __main__ - INFO - Searching movie: inception
2025-04-24 14:08:00,643 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=inception&page=1&include_adult=false
2025-04-24 14:08:00,644 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:08:00,772 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=inception&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:08:00,773 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:08:00,774 - __main__ - INFO - TMDB found 2 results for inception
2025-04-24 14:08:00,775 - __main__ - DEBUG - Returning cached trailer for inception
2025-04-24 14:08:00,777 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:08:00,941 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 14:08:01,334 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 14:08:01,746 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 14:08:01,758 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 14:08:01,758 - __main__ - INFO - Discovering groups...
2025-04-24 14:08:01,758 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:08:02,135 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:08:02,137 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 39, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483883, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:08:02,138 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:08:02,138 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796189438703356 to SearchRequest (257c5e26e70)
2025-04-24 14:08:02,139 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:08:02,140 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:02,141 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:02,325 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796189438703356
2025-04-24 14:08:02,326 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:08:02,326 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796190190069016 to MsgsAck (257c74b1910)
2025-04-24 14:08:02,326 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:02,327 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:02,327 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:02,327 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796190196923072 to MsgsAck (257c763d550)
2025-04-24 14:08:02,327 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:02,329 - __main__ - ERROR - Error discovering groups: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:08:02,329 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:08:02,329 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:02,330 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:02,712 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:08:02,714 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Error ra: The key is not registered in the system (caused by SearchRequest)', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 40, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483883, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:08:02,714 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:08:02,715 - __main__ - INFO - Searching files for query: inception, types: ['.mp4', '.mkv']
2025-04-24 14:08:02,715 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:08:02,917 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:08:02,918 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:08:02,919 - telegram._bot - DEBUG - []
2025-04-24 14:08:02,919 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:08:02,919 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:08:03,174 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:08:03,175 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: inception...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 41, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483884, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:08:03,175 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:08:03,176 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796193887686192 to SearchRequest (257c763fd70)
2025-04-24 14:08:03,177 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:08:03,178 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:03,178 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:03,379 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796193887686192
2025-04-24 14:08:03,380 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:08:03,381 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796194707745012 to MsgsAck (257c763d1c0)
2025-04-24 14:08:03,383 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:03,385 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:03,386 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:03,386 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796194727561412 to MsgsAck (257c763cf20)
2025-04-24 14:08:03,386 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:03,388 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:08:03,389 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:03,389 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:03,391 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796194747047840 to SearchRequest (257c763caa0)
2025-04-24 14:08:03,392 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:08:03,393 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:03,393 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:03,595 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796194747047840
2025-04-24 14:08:03,596 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:08:03,597 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796195572033344 to MsgsAck (257c763d8b0)
2025-04-24 14:08:03,597 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:03,599 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:03,600 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:03,600 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796195584027704 to MsgsAck (257c763f410)
2025-04-24 14:08:03,602 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:03,603 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:08:03,603 - __main__ - INFO - Searching files for query: inception movie, types: ['.mp4', '.mkv']
2025-04-24 14:08:03,604 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:08:03,605 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:03,606 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:03,985 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:08:03,987 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: inception movie...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 42, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483884, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:08:03,988 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:08:03,988 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796197134046972 to SearchRequest (257c7658d10)
2025-04-24 14:08:03,989 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:08:03,991 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:03,992 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:04,307 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796197134046972
2025-04-24 14:08:04,309 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:08:04,309 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796198714150488 to MsgsAck (257c763e7b0)
2025-04-24 14:08:04,310 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:04,312 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:04,312 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:04,312 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796198724502624 to MsgsAck (257c763ec30)
2025-04-24 14:08:04,313 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:04,313 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:08:04,315 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:04,317 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:04,318 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796198748614372 to SearchRequest (257c763e7b0)
2025-04-24 14:08:04,319 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:08:04,320 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:04,320 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:04,531 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796198748614372
2025-04-24 14:08:04,533 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:08:04,534 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796199610717832 to MsgsAck (257c76582f0)
2025-04-24 14:08:04,535 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:04,536 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:04,537 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:04,537 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796199626766264 to MsgsAck (257c7658e30)
2025-04-24 14:08:04,538 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:04,538 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:08:04,539 - __main__ - INFO - Searching files for query: inception mp4, types: ['.mp4', '.mkv']
2025-04-24 14:08:04,539 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:08:04,540 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:04,540 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:04,943 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:08:04,945 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: inception mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 43, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483885, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:08:04,950 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:08:04,953 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796201287254392 to SearchRequest (257c76593a0)
2025-04-24 14:08:04,954 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:08:04,956 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:04,956 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:05,194 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796201287254392
2025-04-24 14:08:05,197 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:08:05,199 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796202568136872 to MsgsAck (257c76592e0)
2025-04-24 14:08:05,199 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:05,200 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:05,202 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:05,202 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796202578046504 to MsgsAck (257c765a3c0)
2025-04-24 14:08:05,203 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:05,204 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:08:05,205 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:05,205 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:05,205 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796202590825740 to SearchRequest (257c76592e0)
2025-04-24 14:08:05,205 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:08:05,207 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:05,208 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:05,512 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796202590825740
2025-04-24 14:08:05,513 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:08:05,514 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796203826036156 to MsgsAck (257c7659eb0)
2025-04-24 14:08:05,514 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:05,515 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:05,516 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:05,517 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796203838041964 to MsgsAck (257c76582f0)
2025-04-24 14:08:05,517 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:08:05,518 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:08:05,519 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:08:05,521 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:05,523 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:05,919 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:08:05,921 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'inception' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 44, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745483886, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:08:05,921 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:08:13,135 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:08:13,136 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:08:13,137 - telegram._bot - DEBUG - []
2025-04-24 14:08:13,137 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:08:13,138 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:08:23,335 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:08:23,337 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:08:23,338 - telegram._bot - DEBUG - []
2025-04-24 14:08:23,338 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:08:23,339 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:08:33,544 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:08:33,545 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:08:33,546 - telegram._bot - DEBUG - []
2025-04-24 14:08:33,546 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:08:33,547 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:08:43,749 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:08:43,750 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:08:43,751 - telegram._bot - DEBUG - []
2025-04-24 14:08:43,751 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:08:43,751 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:08:54,079 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:08:54,080 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:08:54,080 - telegram._bot - DEBUG - []
2025-04-24 14:08:54,080 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:08:54,081 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:08:55,685 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796419261335428 to PingRequest (257c763e180)
2025-04-24 14:08:55,685 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:08:55,687 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:08:55,687 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:08:55,936 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496796419261335428
2025-04-24 14:08:55,937 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:09:04,288 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:09:04,290 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:09:04,290 - telegram._bot - DEBUG - []
2025-04-24 14:09:04,291 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:09:04,292 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:09:05,888 - telethon.network.connection.connection - WARNING - Server closed the connection: [WinError 1236] The network connection was aborted by the local system
2025-04-24 14:09:05,903 - telethon.network.mtprotosender - INFO - Connection closed while receiving data: [WinError 1236] The network connection was aborted by the local system
2025-04-24 14:09:05,909 - telethon.network.mtprotosender - INFO - Closing current connection to begin reconnect...
2025-04-24 14:09:05,913 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: 
2025-04-24 14:09:05,920 - telethon.network.connection.connection - INFO - <class 'ConnectionAbortedError'> during disconnect: [WinError 1236] The network connection was aborted by the local system
2025-04-24 14:09:05,927 - __main__ - ERROR - Update None caused error: httpx HTTPError: 
2025-04-24 14:09:05,931 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 14:09:05,945 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 14:09:06,311 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 14:09:06,311 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 14:09:06,311 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 14:09:06,312 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 14:09:06,312 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:09:06,312 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796465013787232 to MsgsAck (257c75e49e0)
2025-04-24 14:09:06,313 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:09:06,313 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:09:06,314 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:09:06,314 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:09:06,315 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796465025804480 to GetUsersRequest (257c761f080)
2025-04-24 14:09:06,315 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:09:06,315 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:09:06,316 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:09:06,680 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 14:09:06,683 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:09:06,685 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496796465025804480
2025-04-24 14:09:06,685 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:09:06,685 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796466504732092 to MsgsAck (257c782e8d0)
2025-04-24 14:09:06,686 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:09:06,686 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:09:06,686 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:09:06,686 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796466510724984 to MsgsAck (257c4e09d90)
2025-04-24 14:09:06,686 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 44 bytes for sending
2025-04-24 14:09:06,688 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:09:06,688 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:09:06,922 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:09:17,460 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:09:17,462 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:09:17,463 - telegram._bot - DEBUG - []
2025-04-24 14:09:17,463 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:09:17,464 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:09:27,627 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:09:27,629 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:09:27,630 - telegram._bot - DEBUG - []
2025-04-24 14:09:27,631 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:09:27,631 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:09:37,810 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:09:37,811 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:09:37,811 - telegram._bot - DEBUG - []
2025-04-24 14:09:37,812 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:09:37,812 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:09:47,985 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:09:47,986 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:09:47,986 - telegram._bot - DEBUG - []
2025-04-24 14:09:47,987 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:09:47,987 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:09:55,703 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796677029995632 to PingRequest (257c7659100)
2025-04-24 14:09:55,704 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:09:55,706 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:09:55,706 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:09:55,862 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496796677029995632
2025-04-24 14:09:55,862 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:09:58,170 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:09:58,171 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:09:58,172 - telegram._bot - DEBUG - []
2025-04-24 14:09:58,172 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:09:58,172 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:10:08,335 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:10:08,336 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:10:08,337 - telegram._bot - DEBUG - []
2025-04-24 14:10:08,338 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:10:08,338 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:10:18,507 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:10:18,508 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:10:18,508 - telegram._bot - DEBUG - []
2025-04-24 14:10:18,509 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:10:18,509 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:10:28,683 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:10:28,684 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:10:28,685 - telegram._bot - DEBUG - []
2025-04-24 14:10:28,685 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:10:28,686 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:10:38,870 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:10:38,871 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:10:38,871 - telegram._bot - DEBUG - []
2025-04-24 14:10:38,872 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:10:38,872 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:10:49,259 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:10:49,260 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:10:49,261 - telegram._bot - DEBUG - []
2025-04-24 14:10:49,261 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:10:49,262 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:10:55,723 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796934808644624 to PingRequest (257c7658290)
2025-04-24 14:10:55,723 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:10:55,725 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:10:55,726 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:10:55,726 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496796934820894568 to MsgsAck (257c7659100)
2025-04-24 14:10:55,727 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:10:55,729 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:10:55,729 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:10:55,899 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496796934808644624
2025-04-24 14:10:55,900 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:10:59,431 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:10:59,434 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:10:59,434 - telegram._bot - DEBUG - []
2025-04-24 14:10:59,435 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:10:59,435 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:11:09,656 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:11:09,657 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:11:09,657 - telegram._bot - DEBUG - []
2025-04-24 14:11:09,657 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:11:09,657 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:11:19,829 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:11:19,830 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:11:19,831 - telegram._bot - DEBUG - []
2025-04-24 14:11:19,831 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:11:19,831 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:11:29,994 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:11:29,996 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:11:29,997 - telegram._bot - DEBUG - []
2025-04-24 14:11:29,997 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:11:29,998 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:11:40,171 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:11:40,172 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:11:40,172 - telegram._bot - DEBUG - []
2025-04-24 14:11:40,172 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:11:40,173 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:11:50,354 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:11:50,355 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:11:50,356 - telegram._bot - DEBUG - []
2025-04-24 14:11:50,356 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:11:50,357 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:11:55,745 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496797192594841944 to PingRequest (257c763d370)
2025-04-24 14:11:55,746 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:11:55,747 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:11:55,747 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:11:55,748 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496797192606537804 to MsgsAck (257c7826ff0)
2025-04-24 14:11:55,748 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:11:55,750 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:11:55,751 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:11:55,900 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496797192594841944
2025-04-24 14:11:55,901 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:12:00,530 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:12:00,532 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:12:00,535 - telegram._bot - DEBUG - []
2025-04-24 14:12:00,539 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:12:00,541 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:12:10,712 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:12:10,713 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:12:10,714 - telegram._bot - DEBUG - []
2025-04-24 14:12:10,714 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:12:10,714 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:12:20,898 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:12:20,899 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:12:20,899 - telegram._bot - DEBUG - []
2025-04-24 14:12:20,900 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:12:20,900 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:12:31,069 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:12:31,070 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:12:31,070 - telegram._bot - DEBUG - []
2025-04-24 14:12:31,072 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:12:31,072 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:12:41,240 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:12:41,247 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:12:41,248 - telegram._bot - DEBUG - []
2025-04-24 14:12:41,249 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:12:41,249 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:12:51,412 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:12:51,413 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:12:51,413 - telegram._bot - DEBUG - []
2025-04-24 14:12:51,413 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:12:51,414 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:12:55,754 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496797450329215648 to PingRequest (257c7826e70)
2025-04-24 14:12:55,754 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:12:55,755 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:12:55,756 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:12:55,756 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496797450337028148 to MsgsAck (257c784ecf0)
2025-04-24 14:12:55,756 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:12:55,758 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:12:55,758 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:12:55,918 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496797450329215648
2025-04-24 14:12:55,918 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:13:01,585 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:13:01,586 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:13:01,586 - telegram._bot - DEBUG - []
2025-04-24 14:13:01,587 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:13:01,587 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:13:11,774 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:13:11,774 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:13:11,775 - telegram._bot - DEBUG - []
2025-04-24 14:13:11,775 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:13:11,776 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:13:21,946 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:13:21,946 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:13:21,947 - telegram._bot - DEBUG - []
2025-04-24 14:13:21,947 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:13:21,947 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:13:32,120 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:13:32,121 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:13:32,121 - telegram._bot - DEBUG - []
2025-04-24 14:13:32,121 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:13:32,121 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:13:42,288 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:13:42,288 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:13:42,288 - telegram._bot - DEBUG - []
2025-04-24 14:13:42,289 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:13:42,289 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:13:52,467 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:13:52,471 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:13:52,471 - telegram._bot - DEBUG - []
2025-04-24 14:13:52,472 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:13:52,472 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:13:55,765 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496797708072078964 to PingRequest (257c782f080)
2025-04-24 14:13:55,768 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:13:55,770 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:13:55,771 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:13:55,771 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496797708094702980 to MsgsAck (257c74b2510)
2025-04-24 14:13:55,772 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:13:55,773 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:13:55,773 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:13:55,945 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496797708072078964
2025-04-24 14:13:55,946 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:14:02,651 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:14:02,652 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:14:02,652 - telegram._bot - DEBUG - []
2025-04-24 14:14:02,652 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:14:02,652 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:14:12,815 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:14:12,815 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:14:12,816 - telegram._bot - DEBUG - []
2025-04-24 14:14:12,816 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:14:12,816 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:14:23,007 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:14:23,008 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:14:23,008 - telegram._bot - DEBUG - []
2025-04-24 14:14:23,008 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:14:23,008 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:14:33,186 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:14:33,187 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:14:33,187 - telegram._bot - DEBUG - []
2025-04-24 14:14:33,187 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:14:33,188 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:14:43,398 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:14:43,399 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:14:43,400 - telegram._bot - DEBUG - []
2025-04-24 14:14:43,400 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:14:43,400 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:14:53,573 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:14:53,574 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:14:53,574 - telegram._bot - DEBUG - []
2025-04-24 14:14:53,575 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:14:53,575 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:14:55,799 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496797965903546248 to PingRequest (257c782f0b0)
2025-04-24 14:14:55,800 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:14:55,800 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:14:55,801 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:14:55,802 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496797965915539656 to MsgsAck (257c7824260)
2025-04-24 14:14:55,802 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:14:55,804 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:14:55,804 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:14:55,977 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496797965903546248
2025-04-24 14:14:55,977 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:15:03,748 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:15:03,748 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:15:03,749 - telegram._bot - DEBUG - []
2025-04-24 14:15:03,749 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:15:03,749 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:25:05,248 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 14:25:05,251 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 14:25:06,329 - __main__ - INFO - Bot polling started...
2025-04-24 14:25:06,330 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 14:25:07,046 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/botyour_new_bot_token/getMe "HTTP/1.1 404 Not Found"
2025-04-24 14:25:07,048 - telegram.ext._application - DEBUG - This Application is already shut down. Returning.
2025-04-24 14:25:07,049 - __main__ - ERROR - General error: The token `your_new_bot_token` was rejected by the server.
2025-04-24 14:26:30,261 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 14:26:30,262 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 14:26:31,185 - __main__ - INFO - Bot polling started...
2025-04-24 14:26:31,185 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 14:26:31,974 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 14:26:31,976 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 14:26:31,977 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 14:26:31,977 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 14:26:31,978 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 14:26:31,978 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 14:26:31,979 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 14:26:31,979 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 14:26:32,176 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 14:26:32,178 - telegram._bot - DEBUG - True
2025-04-24 14:26:32,178 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 14:26:32,179 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 14:26:32,179 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 14:26:32,179 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 14:26:32,180 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 14:26:32,180 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:26:32,182 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 14:26:32,183 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 14:26:32,183 - telegram.ext._application - INFO - Application started
2025-04-24 14:26:32,183 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 14:26:32,184 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 14:26:42,751 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:26:42,752 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:26:42,752 - telegram._bot - DEBUG - []
2025-04-24 14:26:42,753 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:26:42,753 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:26:52,945 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:26:52,948 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:26:52,948 - telegram._bot - DEBUG - []
2025-04-24 14:26:52,948 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:26:52,950 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:26:53,145 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:26:53,147 - telegram._bot - DEBUG - Getting updates: [954247025]
2025-04-24 14:26:53,148 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000021EABF31C00>]
2025-04-24 14:26:53,148 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:26:53,148 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:26:53,149 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247025, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 45, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485013, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:26:53,150 - __main__ - INFO - Received /start command
2025-04-24 14:26:53,151 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:26:53,873 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:26:53,877 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—em adigina search chesi pampistha. Ex: 'inception', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 144}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 46, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485014, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:26:53,878 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:03,349 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:03,349 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:27:03,351 - telegram._bot - DEBUG - []
2025-04-24 14:27:03,352 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:03,352 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:03,547 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:03,548 - telegram._bot - DEBUG - Getting updates: [954247026]
2025-04-24 14:27:03,548 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000021EABF31F00>]
2025-04-24 14:27:03,550 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:03,550 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:03,551 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247026, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Dunkrik', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 47, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485024, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:27:03,552 - __main__ - INFO - Received message: dunkrik
2025-04-24 14:27:03,553 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:04,307 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:04,310 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:dunkrik', 'text': 'Movie'}, {'callback_data': 'series:dunkrik', 'text': 'Series'}, {'callback_data': 'pdf:dunkrik', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'dunkrik' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 48, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485025, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:04,311 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:06,871 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:06,872 - telegram._bot - DEBUG - Getting updates: [954247027]
2025-04-24 14:27:06,872 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000021EABF32740>]
2025-04-24 14:27:06,873 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:06,873 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:06,874 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:dunkrik', 'text': 'Movie'}, {'callback_data': 'series:dunkrik', 'text': 'Series'}, {'callback_data': 'pdf:dunkrik', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'dunkrik' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 48, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485025, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488947443867993', 'data': 'movie:dunkrik', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247027}
2025-04-24 14:27:06,876 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:27:07,246 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:27:07,247 - telegram._bot - DEBUG - True
2025-04-24 14:27:07,248 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:27:07,248 - __main__ - INFO - Searching movie: dunkrik
2025-04-24 14:27:07,248 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=dunkrik&page=1&include_adult=false
2025-04-24 14:27:07,252 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:07,726 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=dunkrik&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:27:07,728 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:27:07,728 - __main__ - WARNING - No TMDB results for query: dunkrik, category: movie
2025-04-24 14:27:07,746 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:08,110 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:08,112 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "No results for 'dunkrik' ra, check your internet or try again!", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 49, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485029, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:08,113 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:08,113 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:08,488 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:08,489 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:dunkrik', 'text': 'Retry'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Click to retry:', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 50, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485029, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:08,490 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:15,271 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:15,272 - telegram._bot - DEBUG - Getting updates: [954247028]
2025-04-24 14:27:15,273 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000021EABF33AC0>]
2025-04-24 14:27:15,273 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:15,273 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:15,274 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:dunkrik', 'text': 'Retry'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Click to retry:', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 50, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485029, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488949484886979', 'data': 'movie:dunkrik', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247028}
2025-04-24 14:27:15,275 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:27:16,054 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:27:16,054 - telegram._bot - DEBUG - True
2025-04-24 14:27:16,055 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:27:16,057 - __main__ - INFO - Searching movie: dunkrik
2025-04-24 14:27:16,059 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=dunkrik&page=1&include_adult=false
2025-04-24 14:27:16,061 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:16,203 - __main__ - ERROR - TMDB request error on attempt 1: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2025-04-24 14:27:17,218 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:17,491 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=dunkrik&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:27:17,493 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:27:17,494 - __main__ - WARNING - No TMDB results for query: dunkrik, category: movie
2025-04-24 14:27:17,495 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:17,872 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:17,873 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "No results for 'dunkrik' ra, check your internet or try again!", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 51, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485038, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:17,875 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:17,876 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:18,294 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:18,295 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:dunkrik', 'text': 'Retry'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Click to retry:', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 52, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485039, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:18,295 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:25,463 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:25,464 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:27:25,464 - telegram._bot - DEBUG - []
2025-04-24 14:27:25,466 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:25,466 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:25,642 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:25,643 - telegram._bot - DEBUG - Getting updates: [954247029]
2025-04-24 14:27:25,645 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000021EABF33D00>]
2025-04-24 14:27:25,645 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:25,645 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:25,646 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247029, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Batman', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 53, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485046, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:27:25,647 - __main__ - INFO - Received message: batman
2025-04-24 14:27:25,648 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:26,380 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:26,382 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:batman', 'text': 'Movie'}, {'callback_data': 'series:batman', 'text': 'Series'}, {'callback_data': 'pdf:batman', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'batman' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 54, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485047, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:26,382 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:27,931 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:27,936 - telegram._bot - DEBUG - Getting updates: [954247030]
2025-04-24 14:27:27,936 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000021EABF331C0>]
2025-04-24 14:27:27,937 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:27,937 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:27,938 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:batman', 'text': 'Movie'}, {'callback_data': 'series:batman', 'text': 'Series'}, {'callback_data': 'pdf:batman', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'batman' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 54, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485047, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488945612073585', 'data': 'movie:batman', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247030}
2025-04-24 14:27:27,938 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:27:28,290 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:27:28,293 - telegram._bot - DEBUG - True
2025-04-24 14:27:28,294 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:27:28,294 - __main__ - INFO - Searching movie: batman
2025-04-24 14:27:28,294 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=batman&page=1&include_adult=false
2025-04-24 14:27:28,295 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:28,690 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=batman&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:27:28,691 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:27:28,692 - __main__ - INFO - TMDB found 3 results for batman
2025-04-24 14:27:28,694 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 14:27:29,465 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=batman+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 14:27:29,469 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:29,771 - __main__ - WARNING - Genre fetch failed, retrying 1...
2025-04-24 14:27:31,783 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:31,888 - __main__ - WARNING - Genre fetch failed, retrying 2...
2025-04-24 14:27:33,896 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:34,099 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 14:27:34,654 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 14:27:36,615 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 14:27:36,633 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 14:27:36,634 - __main__ - INFO - Discovering groups...
2025-04-24 14:27:36,634 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 14:27:36,634 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 14:27:36,635 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 14:27:36,830 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 14:27:36,830 - telethon.network.mtprotosender - DEBUG - New auth_key attempt 1...
2025-04-24 14:27:38,125 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:38,125 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:27:38,126 - telegram._bot - DEBUG - []
2025-04-24 14:27:38,127 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:38,127 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:38,697 - telethon.network.mtprotosender - DEBUG - auth_key generation success!
2025-04-24 14:27:38,701 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 14:27:38,701 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 14:27:38,701 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 14:27:38,709 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:38,710 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801246904877876 to InvokeWithLayerRequest (21eac078740)
2025-04-24 14:27:38,711 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 14:27:38,712 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:38,712 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:38,712 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:38,911 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496801246904877876
2025-04-24 14:27:38,912 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 14:27:38,912 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:38,913 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801247709899160 to InvokeWithLayerRequest (21eac078740)
2025-04-24 14:27:38,913 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 14:27:38,915 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:38,915 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:38,916 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801247726358628 to MsgsAck (21eac078b30)
2025-04-24 14:27:38,917 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:38,918 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:38,918 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:39,732 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 14:27:39,733 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 14:27:39,734 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496801247709899160]
2025-04-24 14:27:39,734 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:39,738 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801247709899160
2025-04-24 14:27:39,739 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:39,739 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801251316059924 to GetUsersRequest (21eac078740)
2025-04-24 14:27:39,741 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:27:39,742 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:39,742 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:39,743 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801251332403996 to MsgsAck (21eabf8e750)
2025-04-24 14:27:39,743 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 14:27:39,744 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:39,745 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:39,942 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801251316059924
2025-04-24 14:27:39,943 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:39,944 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801252133284428 to MsgsAck (21eabf8c680)
2025-04-24 14:27:39,945 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:39,946 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:39,946 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:39,947 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801252145356036 to MsgsAck (21eabeeed20)
2025-04-24 14:27:39,947 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:39,948 - __main__ - INFO - Client connected successfully
2025-04-24 14:27:39,949 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:39,951 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:39,951 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:40,326 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:40,328 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 56, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485061, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:40,329 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:40,331 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801253976047020 to SearchRequest (21eac052750)
2025-04-24 14:27:40,332 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:27:40,333 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:40,333 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:40,544 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801253976047020
2025-04-24 14:27:40,545 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:40,545 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801254835437276 to MsgsAck (21eac052ab0)
2025-04-24 14:27:40,546 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:40,547 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:40,549 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:40,549 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801254848391988 to MsgsAck (21eac052060)
2025-04-24 14:27:40,550 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:40,551 - __main__ - ERROR - Telethon search error: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:27:40,552 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:40,553 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:40,554 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:40,920 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:40,920 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Group search failed, using default groups...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 57, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485061, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:40,921 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:40,923 - __main__ - INFO - Searching files for query: batman, types: ['.mp4', '.mkv']
2025-04-24 14:27:40,923 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:41,301 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:41,303 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: batman...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 58, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485062, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:41,303 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:41,304 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801258163184268 to ResolveUsernameRequest (21eac094380)
2025-04-24 14:27:41,305 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 14:27:41,306 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:41,306 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:41,496 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801258163184268
2025-04-24 14:27:41,496 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:41,497 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801258936850648 to MsgsAck (21eac07a8a0)
2025-04-24 14:27:41,497 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:41,499 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:41,500 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:41,502 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801258954874140 to MsgsAck (21eac078170)
2025-04-24 14:27:41,502 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:41,503 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:27:41,503 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:41,503 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:41,503 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801258960929972 to ResolveUsernameRequest (21eac078230)
2025-04-24 14:27:41,503 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:27:41,504 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:41,504 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:41,701 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801258960929972
2025-04-24 14:27:41,701 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:41,702 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801259756946664 to MsgsAck (21eac094260)
2025-04-24 14:27:41,702 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:41,703 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:41,703 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:41,703 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801259761370760 to MsgsAck (21eac0951c0)
2025-04-24 14:27:41,703 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:41,705 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:27:41,706 - __main__ - INFO - Searching files for query: batman movie, types: ['.mp4', '.mkv']
2025-04-24 14:27:41,706 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:41,708 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:41,709 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:42,110 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:42,112 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: batman movie...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 59, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485063, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:42,113 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:42,113 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801261695197804 to ResolveUsernameRequest (21eac0968a0)
2025-04-24 14:27:42,114 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 14:27:42,114 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:42,114 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:42,317 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801261695197804
2025-04-24 14:27:42,318 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:42,318 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801262516269428 to MsgsAck (21eac094cb0)
2025-04-24 14:27:42,321 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:42,322 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:42,322 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:42,322 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801262532041296 to MsgsAck (21eac094b60)
2025-04-24 14:27:42,323 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:42,324 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:27:42,326 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:42,327 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:42,327 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801262552428944 to ResolveUsernameRequest (21eac094c80)
2025-04-24 14:27:42,327 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:27:42,329 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:42,329 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:42,540 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801262552428944
2025-04-24 14:27:42,542 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:42,542 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801263411489232 to MsgsAck (21eac097050)
2025-04-24 14:27:42,542 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:42,543 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:42,543 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:42,544 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801263421231016 to MsgsAck (21eac096960)
2025-04-24 14:27:42,544 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:42,545 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:27:42,545 - __main__ - INFO - Searching files for query: batman mp4, types: ['.mp4', '.mkv']
2025-04-24 14:27:42,546 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:42,547 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:42,547 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:42,913 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:42,915 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: batman mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 60, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485063, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:42,915 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:42,916 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801264908976300 to ResolveUsernameRequest (21eac0975c0)
2025-04-24 14:27:42,917 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 14:27:42,918 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:42,918 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:43,123 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801264908976300
2025-04-24 14:27:43,124 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:43,125 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801266039162980 to MsgsAck (21eac096e10)
2025-04-24 14:27:43,126 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:43,127 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:43,127 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:43,128 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801266051156388 to MsgsAck (21eac096fc0)
2025-04-24 14:27:43,128 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:43,129 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:27:43,130 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:43,131 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:43,131 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801266063161240 to ResolveUsernameRequest (21eac096ff0)
2025-04-24 14:27:43,132 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:27:43,133 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:43,133 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:43,347 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801266063161240
2025-04-24 14:27:43,347 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:27:43,348 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801266930177080 to MsgsAck (21eac0977a0)
2025-04-24 14:27:43,348 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:43,349 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:43,350 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:43,350 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801266938090668 to MsgsAck (21eac097d10)
2025-04-24 14:27:43,351 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:27:43,352 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:27:43,352 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:43,354 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:27:43,354 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:27:43,726 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:43,728 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'batman' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 61, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485064, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:43,729 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:48,315 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:48,316 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:27:48,318 - telegram._bot - DEBUG - []
2025-04-24 14:27:48,318 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:48,318 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:55,138 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:55,139 - telegram._bot - DEBUG - Getting updates: [954247031]
2025-04-24 14:27:55,140 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000021EABF33100>]
2025-04-24 14:27:55,140 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:55,142 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:55,143 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247031, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Hi nanna', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 62, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485076, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:27:55,143 - __main__ - INFO - Received message: hi nanna
2025-04-24 14:27:55,144 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:27:55,893 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:27:55,895 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:hi nanna', 'text': 'Movie'}, {'callback_data': 'series:hi nanna', 'text': 'Series'}, {'callback_data': 'pdf:hi nanna', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'hi nanna' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 63, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485076, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:27:55,895 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:27:57,571 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:27:57,572 - telegram._bot - DEBUG - Getting updates: [954247032]
2025-04-24 14:27:57,573 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000021EABF32980>]
2025-04-24 14:27:57,574 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:27:57,574 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:27:57,575 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:hi nanna', 'text': 'Movie'}, {'callback_data': 'series:hi nanna', 'text': 'Series'}, {'callback_data': 'pdf:hi nanna', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'hi nanna' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 63, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485076, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488946926421921', 'data': 'movie:hi nanna', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247032}
2025-04-24 14:27:57,577 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:27:57,926 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:27:57,927 - telegram._bot - DEBUG - True
2025-04-24 14:27:57,927 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:27:57,927 - __main__ - INFO - Searching movie: hi nanna
2025-04-24 14:27:57,928 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=hi+nanna&page=1&include_adult=false
2025-04-24 14:27:57,930 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:58,350 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=hi+nanna&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:27:58,365 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:27:58,385 - __main__ - INFO - TMDB found 1 results for hi+nanna
2025-04-24 14:27:58,405 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 14:27:59,325 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=hi%20nanna+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 14:27:59,333 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:27:59,448 - __main__ - WARNING - Genre fetch failed, retrying 1...
2025-04-24 14:28:01,459 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:28:01,638 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 14:28:02,066 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 14:28:03,373 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 14:28:03,379 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 14:28:03,379 - __main__ - INFO - Discovering groups...
2025-04-24 14:28:03,379 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:28:03,748 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:28:03,749 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Groups lo chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 65, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485084, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:28:03,750 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:28:03,750 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801354436640652 to SearchRequest (21eac26ce30)
2025-04-24 14:28:03,751 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:28:03,752 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:03,752 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:04,025 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801354436640652
2025-04-24 14:28:04,026 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:28:04,026 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801355838051352 to MsgsAck (21eac26cfe0)
2025-04-24 14:28:04,028 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:04,028 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:04,028 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:04,029 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801355850407156 to MsgsAck (21eac26cbc0)
2025-04-24 14:28:04,029 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:04,031 - __main__ - ERROR - Telethon search error: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:28:04,031 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:28:04,033 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:04,033 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:04,410 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:28:04,419 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Group search failed, using default groups...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 66, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485085, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:28:04,430 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:28:04,434 - __main__ - INFO - Searching files for query: hi nanna, types: ['.mp4', '.mkv']
2025-04-24 14:28:04,438 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:28:04,827 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:28:04,828 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: hi nanna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 67, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485085, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:28:04,829 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:28:04,830 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801359050913368 to ResolveUsernameRequest (21eac26c2f0)
2025-04-24 14:28:04,831 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 14:28:04,832 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:04,832 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,046 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801359050913368
2025-04-24 14:28:05,048 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:28:05,049 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801360217970048 to MsgsAck (21eac26c9e0)
2025-04-24 14:28:05,049 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:05,051 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,052 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,052 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801360234053768 to MsgsAck (21eac26c980)
2025-04-24 14:28:05,052 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:05,053 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:28:05,054 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,054 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,054 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801360242096104 to ResolveUsernameRequest (21eac26c9e0)
2025-04-24 14:28:05,054 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:28:05,055 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,056 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,274 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801360242096104
2025-04-24 14:28:05,274 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:28:05,275 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801361129275476 to MsgsAck (21eabf8e750)
2025-04-24 14:28:05,275 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:05,276 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,278 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,278 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801361138005412 to MsgsAck (21eac097770)
2025-04-24 14:28:05,279 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:05,280 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:28:05,280 - __main__ - INFO - Searching files for query: hi nanna movie, types: ['.mp4', '.mkv']
2025-04-24 14:28:05,280 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:28:05,281 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,283 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,645 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:28:05,646 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: hi nanna movie...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 68, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485086, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:28:05,647 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:28:05,648 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801362618583836 to ResolveUsernameRequest (21eac0973e0)
2025-04-24 14:28:05,649 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 14:28:05,650 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,650 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,838 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801362618583836
2025-04-24 14:28:05,839 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:28:05,839 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801363382388268 to MsgsAck (21eac097590)
2025-04-24 14:28:05,840 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:05,841 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,842 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,842 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801363396312868 to MsgsAck (21eac097230)
2025-04-24 14:28:05,842 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:05,843 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:28:05,846 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,846 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:05,847 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801363414005436 to ResolveUsernameRequest (21eac094320)
2025-04-24 14:28:05,847 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:28:05,849 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:05,849 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:06,053 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801363414005436
2025-04-24 14:28:06,054 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:28:06,054 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801364539096632 to MsgsAck (21eac0969f0)
2025-04-24 14:28:06,055 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:06,058 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:06,060 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:06,061 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801364565593520 to MsgsAck (21eac0967b0)
2025-04-24 14:28:06,061 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:06,062 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:28:06,062 - __main__ - INFO - Searching files for query: hi nanna mp4, types: ['.mp4', '.mkv']
2025-04-24 14:28:06,063 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:28:06,064 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:06,065 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:06,438 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:28:06,442 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: hi nanna mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 69, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485087, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:28:06,442 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:28:06,444 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801366099223892 to ResolveUsernameRequest (21eac094920)
2025-04-24 14:28:06,444 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 48 bytes for sending
2025-04-24 14:28:06,445 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:06,445 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:06,637 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801366099223892
2025-04-24 14:28:06,638 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:28:06,638 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801366875224868 to MsgsAck (21eac094d10)
2025-04-24 14:28:06,640 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:06,641 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:06,641 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:06,642 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801366891143600 to MsgsAck (21eac096570)
2025-04-24 14:28:06,643 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:06,644 - __main__ - ERROR - File search error in group @SOUTH_ALL_LATEST_MOVIE: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:28:06,645 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:06,645 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:06,646 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801366905829228 to ResolveUsernameRequest (21eac0951c0)
2025-04-24 14:28:06,646 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:28:06,648 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:06,648 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:06,848 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496801366905829228
2025-04-24 14:28:06,849 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:28:06,849 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801367718797484 to MsgsAck (21eac094c20)
2025-04-24 14:28:06,849 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:06,851 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:06,851 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:06,851 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801367727549352 to MsgsAck (21eac095340)
2025-04-24 14:28:06,852 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:28:06,853 - __main__ - ERROR - File search error in group @MedicalBooksPDF: The key is not registered in the system (caused by ResolveUsernameRequest)
2025-04-24 14:28:06,853 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:28:06,855 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:06,856 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:07,251 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:28:07,251 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'hi nanna' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 70, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485088, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:28:07,253 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:28:07,765 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:28:07,775 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:28:07,776 - telegram._bot - DEBUG - []
2025-04-24 14:28:07,777 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:28:07,786 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:28:17,982 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:28:17,983 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:28:17,984 - telegram._bot - DEBUG - []
2025-04-24 14:28:17,984 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:28:17,984 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:28:28,161 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:28:28,162 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:28:28,163 - telegram._bot - DEBUG - []
2025-04-24 14:28:28,163 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:28:28,164 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:28:38,339 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:28:38,340 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:28:38,341 - telegram._bot - DEBUG - []
2025-04-24 14:28:38,341 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:28:38,342 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:28:39,959 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801509893397800 to PingRequest (21eac011550)
2025-04-24 14:28:39,960 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:28:39,961 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:28:39,962 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:28:40,150 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496801509893397800
2025-04-24 14:28:40,151 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:28:48,527 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:28:48,528 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:28:48,528 - telegram._bot - DEBUG - []
2025-04-24 14:28:48,529 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:28:48,529 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:28:58,727 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:28:58,727 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:28:58,728 - telegram._bot - DEBUG - []
2025-04-24 14:28:58,728 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:28:58,728 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:29:08,925 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:29:08,926 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:29:08,927 - telegram._bot - DEBUG - []
2025-04-24 14:29:08,927 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:29:08,928 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:29:19,522 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:29:19,524 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:29:19,525 - telegram._bot - DEBUG - []
2025-04-24 14:29:19,525 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:29:19,525 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:29:29,743 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:29:29,747 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:29:29,748 - telegram._bot - DEBUG - []
2025-04-24 14:29:29,748 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:29:29,750 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:29:39,949 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:29:39,950 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:29:39,950 - telegram._bot - DEBUG - []
2025-04-24 14:29:39,950 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:29:39,950 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:29:39,962 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801767600749144 to PingRequest (21eac27c1d0)
2025-04-24 14:29:39,963 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:29:39,963 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:29:39,965 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:29:39,966 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496801767616673600 to MsgsAck (21eac011550)
2025-04-24 14:29:39,966 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:29:39,969 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:29:39,970 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:29:40,169 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496801767600749144
2025-04-24 14:29:40,169 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:29:50,160 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:29:50,161 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:29:50,161 - telegram._bot - DEBUG - []
2025-04-24 14:29:50,162 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:29:50,162 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:30:00,334 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:30:00,335 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:30:00,335 - telegram._bot - DEBUG - []
2025-04-24 14:30:00,336 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:30:00,336 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:30:10,511 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:30:10,512 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:30:10,513 - telegram._bot - DEBUG - []
2025-04-24 14:30:10,513 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:30:10,514 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:30:20,685 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:30:20,685 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:30:20,685 - telegram._bot - DEBUG - []
2025-04-24 14:30:20,685 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:30:20,686 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:30:30,860 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:30:30,861 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:30:30,861 - telegram._bot - DEBUG - []
2025-04-24 14:30:30,861 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:30:30,861 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:30:39,979 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496802025370232368 to PingRequest (21ea9816810)
2025-04-24 14:30:39,980 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:30:39,981 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:30:39,982 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:30:39,983 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496802025386181620 to MsgsAck (21eac096510)
2025-04-24 14:30:39,983 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:30:39,985 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:30:39,986 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:30:40,188 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496802025370232368
2025-04-24 14:30:40,189 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:30:41,033 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:30:41,034 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:30:41,037 - telegram._bot - DEBUG - []
2025-04-24 14:30:41,037 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:30:41,037 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:30:51,215 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:30:51,216 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:30:51,217 - telegram._bot - DEBUG - []
2025-04-24 14:30:51,217 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:30:51,217 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:31:01,403 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:31:01,404 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:31:01,404 - telegram._bot - DEBUG - []
2025-04-24 14:31:01,404 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:31:01,404 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:31:11,598 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:31:11,599 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:31:11,599 - telegram._bot - DEBUG - []
2025-04-24 14:31:11,600 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:31:11,600 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:31:21,773 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:31:21,774 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:31:21,774 - telegram._bot - DEBUG - []
2025-04-24 14:31:21,774 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:31:21,774 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:31:31,957 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:31:31,958 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:31:31,958 - telegram._bot - DEBUG - []
2025-04-24 14:31:31,958 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:31:31,958 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:31:40,000 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496802283446188016 to PingRequest (21eac096450)
2025-04-24 14:31:40,000 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:31:40,001 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:31:40,001 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:31:40,002 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496802283455595060 to MsgsAck (21eac27d250)
2025-04-24 14:31:40,002 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:31:40,004 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:31:40,004 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:31:40,190 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496802283446188016
2025-04-24 14:31:40,192 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:31:42,145 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:31:42,145 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:31:42,146 - telegram._bot - DEBUG - []
2025-04-24 14:31:42,146 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:31:42,146 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:31:52,337 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:31:52,338 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:31:52,338 - telegram._bot - DEBUG - []
2025-04-24 14:31:52,339 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:31:52,339 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:32:02,515 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:32:02,516 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:32:02,516 - telegram._bot - DEBUG - []
2025-04-24 14:32:02,516 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:32:02,517 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:32:12,717 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:32:12,717 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:32:12,718 - telegram._bot - DEBUG - []
2025-04-24 14:32:12,718 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:32:12,718 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:32:22,895 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:32:22,896 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:32:22,896 - telegram._bot - DEBUG - []
2025-04-24 14:32:22,896 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:32:22,897 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:32:33,080 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:32:33,081 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:32:33,081 - telegram._bot - DEBUG - []
2025-04-24 14:32:33,081 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:32:33,081 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:32:40,016 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496802541208087624 to PingRequest (21eac096780)
2025-04-24 14:32:40,017 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:32:40,018 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:32:40,018 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:32:40,019 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496802541219543160 to MsgsAck (21eac26e870)
2025-04-24 14:32:40,019 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:32:40,021 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:32:40,021 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:32:40,226 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496802541208087624
2025-04-24 14:32:40,226 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:32:43,278 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:32:43,279 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:32:43,279 - telegram._bot - DEBUG - []
2025-04-24 14:32:43,279 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:32:43,279 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:32:53,452 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:32:53,453 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:32:53,453 - telegram._bot - DEBUG - []
2025-04-24 14:32:53,454 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:32:53,454 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:33:03,636 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:33:03,638 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:33:03,638 - telegram._bot - DEBUG - []
2025-04-24 14:33:03,639 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:33:03,639 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:33:13,811 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:33:13,811 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:33:13,812 - telegram._bot - DEBUG - []
2025-04-24 14:33:13,812 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:33:13,812 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:33:24,011 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:33:24,013 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:33:24,013 - telegram._bot - DEBUG - []
2025-04-24 14:33:24,013 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:33:24,014 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:33:50,482 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 14:33:50,484 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 14:33:51,453 - __main__ - INFO - Bot polling started...
2025-04-24 14:33:51,453 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 14:33:52,323 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 14:33:52,324 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 14:33:52,324 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 14:33:52,325 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 14:33:52,325 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 14:33:52,325 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 14:33:52,325 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 14:33:52,325 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 14:33:52,506 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 14:33:52,507 - telegram._bot - DEBUG - True
2025-04-24 14:33:52,507 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 14:33:52,507 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 14:33:52,507 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 14:33:52,507 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 14:33:52,507 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 14:33:52,507 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:33:52,509 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 14:33:52,509 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 14:33:52,510 - telegram.ext._application - INFO - Application started
2025-04-24 14:33:52,510 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 14:33:52,510 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 14:34:03,115 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:34:03,117 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:34:03,117 - telegram._bot - DEBUG - []
2025-04-24 14:34:03,117 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:34:03,117 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:34:13,293 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:34:13,295 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:34:13,295 - telegram._bot - DEBUG - []
2025-04-24 14:34:13,295 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:34:13,296 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:34:23,477 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:34:23,478 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:34:23,478 - telegram._bot - DEBUG - []
2025-04-24 14:34:23,478 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:34:23,478 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:34:24,652 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:34:24,652 - telegram._bot - DEBUG - Getting updates: [954247033]
2025-04-24 14:34:24,653 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001AA6E690100>]
2025-04-24 14:34:24,653 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:34:24,654 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:34:24,655 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247033, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 71, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485465, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:34:24,656 - __main__ - INFO - Received /start command
2025-04-24 14:34:24,656 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:34:25,451 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:34:25,451 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—em adigina entire Telegram lo search chesi pampistha. Ex: 'hi nanna', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 162}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 72, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485466, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:34:25,452 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:34:32,962 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:34:32,963 - telegram._bot - DEBUG - Getting updates: [954247034]
2025-04-24 14:34:32,964 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001AA6E691900>]
2025-04-24 14:34:32,964 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:34:32,964 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:34:32,966 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247034, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Hi nanna', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 73, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485473, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:34:32,966 - __main__ - INFO - Received message: hi nanna
2025-04-24 14:34:32,967 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:34:33,699 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:34:33,700 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:hi nanna', 'text': 'Movie'}, {'callback_data': 'series:hi nanna', 'text': 'Series'}, {'callback_data': 'pdf:hi nanna', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'hi nanna' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 74, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485474, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:34:33,701 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:34:37,050 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:34:37,051 - telegram._bot - DEBUG - Getting updates: [954247035]
2025-04-24 14:34:37,052 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001AA6E692800>]
2025-04-24 14:34:37,052 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:34:37,053 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:34:37,054 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:hi nanna', 'text': 'Movie'}, {'callback_data': 'series:hi nanna', 'text': 'Series'}, {'callback_data': 'pdf:hi nanna', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'hi nanna' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 74, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485474, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488949528042380', 'data': 'movie:hi nanna', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247035}
2025-04-24 14:34:37,055 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:34:37,421 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:34:37,422 - telegram._bot - DEBUG - True
2025-04-24 14:34:37,422 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:34:37,422 - __main__ - INFO - Searching movie: hi nanna
2025-04-24 14:34:37,422 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=hi+nanna&page=1&include_adult=false
2025-04-24 14:34:37,424 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:34:37,604 - __main__ - ERROR - TMDB request error on attempt 1: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2025-04-24 14:34:38,617 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:34:38,738 - __main__ - ERROR - TMDB request error on attempt 2: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2025-04-24 14:34:40,752 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:34:41,139 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=hi+nanna&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:34:41,140 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:34:41,140 - __main__ - INFO - TMDB found 1 results for hi+nanna
2025-04-24 14:34:41,142 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 14:34:41,844 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=hi%20nanna+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 14:34:41,846 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:34:42,021 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 14:34:42,637 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 14:34:43,719 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 14:34:43,735 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 14:34:43,735 - __main__ - INFO - Discovering groups across Telegram...
2025-04-24 14:34:43,735 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 14:34:43,735 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 14:34:43,736 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 14:34:43,918 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 14:34:43,919 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 14:34:43,919 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 14:34:43,919 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 14:34:43,928 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:43,928 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803068843557576 to InvokeWithLayerRequest (1aa6e80de80)
2025-04-24 14:34:43,929 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 14:34:43,930 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:43,930 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:43,931 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:44,133 - telethon.network.mtprotostate - DEBUG - Updated time offset (old offset 0, bad 7496803069943696840, good 7496803074529439745, new 1)
2025-04-24 14:34:44,133 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496803068843557576
2025-04-24 14:34:44,133 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 14:34:44,133 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:44,134 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803074254159436 to InvokeWithLayerRequest (1aa6e80de80)
2025-04-24 14:34:44,134 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 14:34:44,135 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:44,135 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:44,136 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803074258158192 to MsgsAck (1aa6e6294c0)
2025-04-24 14:34:44,136 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:44,137 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:44,137 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:44,320 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 14:34:44,320 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 14:34:44,320 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496803074254159436]
2025-04-24 14:34:44,320 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:44,331 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803074254159436
2025-04-24 14:34:44,332 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:44,332 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803075046601756 to GetUsersRequest (1aa6e7e2fc0)
2025-04-24 14:34:44,333 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:34:44,333 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:44,333 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:44,334 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803075054579240 to MsgsAck (1aa6e6f6330)
2025-04-24 14:34:44,334 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 14:34:44,335 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:44,335 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:44,537 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803075046601756
2025-04-24 14:34:44,537 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:44,537 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803075869057164 to MsgsAck (1aa6e4aa7e0)
2025-04-24 14:34:44,537 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:44,538 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:44,538 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:44,538 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803075873034940 to MsgsAck (1aa6e667740)
2025-04-24 14:34:44,538 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:44,538 - __main__ - INFO - Client connected successfully
2025-04-24 14:34:44,538 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:34:44,539 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:44,539 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:44,909 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:34:44,910 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Entire Telegram lo groups chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 76, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485485, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:34:44,910 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:34:44,910 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803077360327228 to SearchRequest (1aa6e667770)
2025-04-24 14:34:44,910 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:34:44,911 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:44,911 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:45,108 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803077360327228
2025-04-24 14:34:45,109 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:45,109 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803078452154264 to MsgsAck (1aa6e6677d0)
2025-04-24 14:34:45,109 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:45,111 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:45,111 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:45,111 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803078457385168 to MsgsAck (1aa6e666c60)
2025-04-24 14:34:45,111 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:45,112 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:45,112 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:45,112 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:46,119 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803082786957492 to SearchRequest (1aa6e6f5df0)
2025-04-24 14:34:46,119 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:34:46,120 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:46,120 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:46,326 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803082786957492
2025-04-24 14:34:46,327 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:46,327 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803083619017352 to MsgsAck (1aa6e6676e0)
2025-04-24 14:34:46,327 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:46,328 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:46,328 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:46,328 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803083623048532 to MsgsAck (1aa6e6677d0)
2025-04-24 14:34:46,328 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:46,328 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:46,329 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:46,329 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:47,255 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:34:47,255 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:34:47,255 - telegram._bot - DEBUG - []
2025-04-24 14:34:47,255 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:34:47,255 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:34:48,337 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803092247033112 to SearchRequest (1aa6e80efc0)
2025-04-24 14:34:48,337 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:34:48,338 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:48,338 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:48,526 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803092247033112
2025-04-24 14:34:48,526 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:48,527 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803093002364152 to MsgsAck (1aa6e80d8e0)
2025-04-24 14:34:48,527 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:48,527 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:48,528 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:48,528 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803093010354036 to MsgsAck (1aa6e80e450)
2025-04-24 14:34:48,528 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:48,529 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:48,529 - __main__ - ERROR - Failed to search movies after 3 attempts
2025-04-24 14:34:48,529 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:48,529 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:48,529 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803093014380448 to SearchRequest (1aa6e80eab0)
2025-04-24 14:34:48,529 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:34:48,530 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:48,530 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:48,738 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803093014380448
2025-04-24 14:34:48,739 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:48,739 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803093856092444 to MsgsAck (1aa6e80f1a0)
2025-04-24 14:34:48,739 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:48,740 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:48,740 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:48,740 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803093860684388 to MsgsAck (1aa6e80fe60)
2025-04-24 14:34:48,740 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:48,741 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:48,741 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:48,741 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:49,754 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803098208009356 to SearchRequest (1aa6e80e6f0)
2025-04-24 14:34:49,754 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:34:49,754 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:49,755 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:50,343 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803098208009356
2025-04-24 14:34:50,344 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:50,344 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803100864220856 to MsgsAck (1aa6e80e330)
2025-04-24 14:34:50,344 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:50,344 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:50,344 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:50,344 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803100864220860 to MsgsAck (1aa6e80ef60)
2025-04-24 14:34:50,344 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:50,345 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:50,345 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:50,345 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:52,348 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803109471525672 to SearchRequest (1aa6e80e330)
2025-04-24 14:34:52,348 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:34:52,349 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:52,349 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:52,544 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803109471525672
2025-04-24 14:34:52,544 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:52,545 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803110261246208 to MsgsAck (1aa6e80f1a0)
2025-04-24 14:34:52,545 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:52,546 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:52,546 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:52,546 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803110264882568 to MsgsAck (1aa6e830290)
2025-04-24 14:34:52,546 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:52,546 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:52,547 - __main__ - ERROR - Failed to search series after 3 attempts
2025-04-24 14:34:52,547 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:52,547 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:52,547 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803110268849852 to SearchRequest (1aa6e80f1a0)
2025-04-24 14:34:52,547 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:34:52,548 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:52,548 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:52,748 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803110268849852
2025-04-24 14:34:52,749 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:52,749 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803111074104788 to MsgsAck (1aa6e80d8e0)
2025-04-24 14:34:52,749 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:52,749 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:52,749 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:52,749 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803111074104792 to MsgsAck (1aa6e8302f0)
2025-04-24 14:34:52,749 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:52,749 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:52,749 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:52,749 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:53,757 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803115401359680 to SearchRequest (1aa6e80d8e0)
2025-04-24 14:34:53,757 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:34:53,758 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:53,758 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:53,981 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803115401359680
2025-04-24 14:34:53,981 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:53,981 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803116298919800 to MsgsAck (1aa6e830920)
2025-04-24 14:34:53,981 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:53,982 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:53,982 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:53,982 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803116302917604 to MsgsAck (1aa6e830500)
2025-04-24 14:34:53,982 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:53,983 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:53,983 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:53,983 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:55,998 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803124954782852 to SearchRequest (1aa6e6294c0)
2025-04-24 14:34:55,998 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:34:55,999 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:56,000 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:56,258 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803124954782852
2025-04-24 14:34:56,258 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:56,259 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803126295037280 to MsgsAck (1aa6e830560)
2025-04-24 14:34:56,259 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:56,259 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:56,259 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:56,260 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803126295037284 to MsgsAck (1aa6e830620)
2025-04-24 14:34:56,260 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:56,260 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:56,260 - __main__ - ERROR - Failed to search pdf after 3 attempts
2025-04-24 14:34:56,261 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:56,261 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:56,261 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803126303028116 to SearchRequest (1aa6e5ddaf0)
2025-04-24 14:34:56,261 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:34:56,262 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:56,262 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:56,483 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803126303028116
2025-04-24 14:34:56,483 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:56,483 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803127191515932 to MsgsAck (1aa6e6675c0)
2025-04-24 14:34:56,483 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:56,484 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:56,484 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:56,485 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803127197862636 to MsgsAck (1aa6e8308c0)
2025-04-24 14:34:56,485 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:56,485 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:56,485 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:56,486 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:57,456 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:34:57,457 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:34:57,457 - telegram._bot - DEBUG - []
2025-04-24 14:34:57,457 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:34:57,457 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:34:57,503 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803131562616004 to SearchRequest (1aa6e830e30)
2025-04-24 14:34:57,503 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:34:57,504 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:57,504 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:57,698 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803131562616004
2025-04-24 14:34:57,699 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:34:57,699 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803132351050032 to MsgsAck (1aa6e830b90)
2025-04-24 14:34:57,699 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:57,701 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:57,701 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:57,701 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803132358665124 to MsgsAck (1aa6e830710)
2025-04-24 14:34:57,701 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:34:57,702 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:34:57,703 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:57,703 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:34:59,718 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803141017197508 to SearchRequest (1aa6e666c60)
2025-04-24 14:34:59,718 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:34:59,719 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:34:59,720 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:00,058 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803141017197508
2025-04-24 14:35:00,058 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:00,058 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803142671799204 to MsgsAck (1aa6e830ef0)
2025-04-24 14:35:00,058 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:00,059 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:00,059 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:00,060 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803142677750132 to MsgsAck (1aa6e830e90)
2025-04-24 14:35:00,060 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:00,060 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:00,060 - __main__ - ERROR - Failed to search telugu movies after 3 attempts
2025-04-24 14:35:00,061 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:00,061 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:00,061 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803142681787988 to SearchRequest (1aa6e6677d0)
2025-04-24 14:35:00,061 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:00,061 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:00,061 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:00,400 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803142681787988
2025-04-24 14:35:00,401 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:00,401 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803144041856308 to MsgsAck (1aa6e8314c0)
2025-04-24 14:35:00,401 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:00,402 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:00,403 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:00,403 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803144049860496 to MsgsAck (1aa6e830e00)
2025-04-24 14:35:00,403 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:00,404 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:00,404 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:00,405 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:01,420 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803148413521908 to SearchRequest (1aa6e80e450)
2025-04-24 14:35:01,421 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:01,422 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:01,423 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:01,640 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803148413521908
2025-04-24 14:35:01,640 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:01,640 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803149294634008 to MsgsAck (1aa6e831340)
2025-04-24 14:35:01,640 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:01,641 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:01,642 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:01,642 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803149302671576 to MsgsAck (1aa6e831370)
2025-04-24 14:35:01,642 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:01,643 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:01,643 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:01,644 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:03,667 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803157989444164 to SearchRequest (1aa6e80fe60)
2025-04-24 14:35:03,667 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:03,668 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:03,668 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:03,899 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803157989444164
2025-04-24 14:35:03,899 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:03,900 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803158925427820 to MsgsAck (1aa6e8312e0)
2025-04-24 14:35:03,900 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:03,901 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:03,901 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:03,901 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803158929409412 to MsgsAck (1aa6e8315e0)
2025-04-24 14:35:03,901 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:03,902 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:03,902 - __main__ - ERROR - Failed to search english movies after 3 attempts
2025-04-24 14:35:03,903 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:03,903 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:03,903 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803158937427904 to SearchRequest (1aa6e80ef60)
2025-04-24 14:35:03,903 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:03,904 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:03,904 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:04,112 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803158937427904
2025-04-24 14:35:04,112 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:04,112 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803160067214040 to MsgsAck (1aa6e831190)
2025-04-24 14:35:04,112 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:04,113 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:04,113 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:04,113 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803160071213752 to MsgsAck (1aa6e8313a0)
2025-04-24 14:35:04,113 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:04,114 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:04,114 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:04,114 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:05,129 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803164425863892 to SearchRequest (1aa6e830e60)
2025-04-24 14:35:05,129 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:05,130 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:05,130 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:05,312 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803164425863892
2025-04-24 14:35:05,313 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:05,313 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803165166493088 to MsgsAck (1aa6e830920)
2025-04-24 14:35:05,313 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:05,313 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:05,314 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:05,314 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803165170487076 to MsgsAck (1aa6e830ef0)
2025-04-24 14:35:05,314 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:05,314 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:05,315 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:05,315 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:07,316 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803173769591248 to SearchRequest (1aa6e831580)
2025-04-24 14:35:07,316 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:07,317 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:07,317 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:07,514 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803173769591248
2025-04-24 14:35:07,514 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:07,514 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803174559679900 to MsgsAck (1aa6e8311f0)
2025-04-24 14:35:07,514 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:07,515 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:07,515 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:07,515 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803174563687240 to MsgsAck (1aa6e830290)
2025-04-24 14:35:07,515 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:07,515 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:07,516 - __main__ - ERROR - Failed to search hindi movies after 3 attempts
2025-04-24 14:35:07,516 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:07,516 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:07,516 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803174569771684 to SearchRequest (1aa6e5ddc70)
2025-04-24 14:35:07,516 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:07,517 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:07,517 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:07,653 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:35:07,653 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:35:07,654 - telegram._bot - DEBUG - []
2025-04-24 14:35:07,654 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:35:07,654 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:35:07,750 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803174569771684
2025-04-24 14:35:07,751 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:07,751 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803175507051384 to MsgsAck (1aa6e830d10)
2025-04-24 14:35:07,751 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:07,752 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:07,752 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:07,752 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803175511025344 to MsgsAck (1aa6e831850)
2025-04-24 14:35:07,752 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:07,753 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:07,753 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:07,754 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:08,760 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803179839112796 to SearchRequest (1aa6e6f6330)
2025-04-24 14:35:08,760 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:08,762 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:08,762 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:09,497 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803179839112796
2025-04-24 14:35:09,498 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:09,498 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803183086265724 to MsgsAck (1aa6e831c70)
2025-04-24 14:35:09,498 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:09,498 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:09,498 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:09,499 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803183090262572 to MsgsAck (1aa6e831c40)
2025-04-24 14:35:09,499 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:09,499 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:09,499 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:09,500 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:11,505 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803191702586576 to SearchRequest (1aa6e6643b0)
2025-04-24 14:35:11,505 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:11,506 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:11,506 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:11,744 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803191702586576
2025-04-24 14:35:11,744 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:11,744 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803192658047124 to MsgsAck (1aa6e831b80)
2025-04-24 14:35:11,745 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:11,745 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:11,745 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:11,745 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803192662045880 to MsgsAck (1aa6e831fd0)
2025-04-24 14:35:11,746 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:11,746 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:11,747 - __main__ - ERROR - Failed to search tamil movies after 3 attempts
2025-04-24 14:35:11,747 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:11,747 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:11,747 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803192670054840 to SearchRequest (1aa6e664200)
2025-04-24 14:35:11,747 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:11,748 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:11,749 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:12,008 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803192670054840
2025-04-24 14:35:12,008 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:12,008 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803194011002588 to MsgsAck (1aa6e830410)
2025-04-24 14:35:12,008 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:12,009 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:12,010 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:12,010 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803194018583344 to MsgsAck (1aa6e832060)
2025-04-24 14:35:12,010 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:12,011 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:12,012 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:12,012 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:13,014 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803198327609708 to SearchRequest (1aa6e80e420)
2025-04-24 14:35:13,014 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:13,016 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:13,016 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:13,222 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803198327609708
2025-04-24 14:35:13,222 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:13,223 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803199166886020 to MsgsAck (1aa6e8322a0)
2025-04-24 14:35:13,223 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:13,224 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:13,224 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:13,224 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803199170884776 to MsgsAck (1aa6e832150)
2025-04-24 14:35:13,225 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:13,226 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:13,226 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:13,227 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:15,228 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803207775146420 to SearchRequest (1aa6e80eb10)
2025-04-24 14:35:15,228 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:15,229 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:15,229 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:15,439 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803207775146420
2025-04-24 14:35:15,440 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:15,440 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803208621940548 to MsgsAck (1aa6e8320f0)
2025-04-24 14:35:15,440 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:15,441 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:15,441 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:15,442 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803208632032328 to MsgsAck (1aa6e832360)
2025-04-24 14:35:15,442 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:15,443 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:15,443 - __main__ - ERROR - Failed to search web series after 3 attempts
2025-04-24 14:35:15,444 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:15,444 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:15,444 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803208640026980 to SearchRequest (1aa6e80e870)
2025-04-24 14:35:15,444 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:35:15,445 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:15,445 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:15,659 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803208640026980
2025-04-24 14:35:15,659 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:15,659 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803209497732096 to MsgsAck (1aa6e831ca0)
2025-04-24 14:35:15,659 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:15,659 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:15,659 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:15,659 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803209501615460 to MsgsAck (1aa6e831dc0)
2025-04-24 14:35:15,659 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:15,660 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:15,661 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:15,661 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:16,673 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803213850913580 to SearchRequest (1aa6e831fa0)
2025-04-24 14:35:16,673 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:35:16,674 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:16,674 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:17,048 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803213850913580
2025-04-24 14:35:17,048 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:17,048 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803215646155536 to MsgsAck (1aa6e832420)
2025-04-24 14:35:17,048 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:17,049 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:17,050 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:17,050 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803215654192148 to MsgsAck (1aa6e8323f0)
2025-04-24 14:35:17,050 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:17,051 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:17,051 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:17,051 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:17,822 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:35:17,823 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:35:17,823 - telegram._bot - DEBUG - []
2025-04-24 14:35:17,823 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:35:17,823 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:35:19,062 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803224291383212 to SearchRequest (1aa6e832990)
2025-04-24 14:35:19,062 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:35:19,063 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:19,063 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:19,582 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803224291383212
2025-04-24 14:35:19,582 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:19,583 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803226373128360 to MsgsAck (1aa6e8301d0)
2025-04-24 14:35:19,583 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:19,583 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:19,583 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:19,583 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803226377145236 to MsgsAck (1aa6e831f70)
2025-04-24 14:35:19,584 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:19,584 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:19,584 - __main__ - ERROR - Failed to search books after 3 attempts
2025-04-24 14:35:19,585 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:19,585 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:19,585 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803226385178988 to SearchRequest (1aa6e831f10)
2025-04-24 14:35:19,585 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:19,586 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:19,586 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:19,782 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803226385178988
2025-04-24 14:35:19,783 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:19,783 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803227177058640 to MsgsAck (1aa6e832870)
2025-04-24 14:35:19,783 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:19,784 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:19,784 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:19,784 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803227181053584 to MsgsAck (1aa6e8327e0)
2025-04-24 14:35:19,784 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:19,785 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:19,786 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:19,786 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:20,797 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803231527296132 to SearchRequest (1aa6e832b10)
2025-04-24 14:35:20,797 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:20,798 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:20,798 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:21,004 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803231527296132
2025-04-24 14:35:21,004 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:21,004 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803232650015540 to MsgsAck (1aa6e832f30)
2025-04-24 14:35:21,004 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:21,005 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:21,005 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:21,005 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803232653986640 to MsgsAck (1aa6e832db0)
2025-04-24 14:35:21,005 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:21,006 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:21,006 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:21,007 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:23,015 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803241282012892 to SearchRequest (1aa6e830ef0)
2025-04-24 14:35:23,015 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:23,016 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:23,016 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:23,228 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803241282012892
2025-04-24 14:35:23,229 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:23,229 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803242138324692 to MsgsAck (1aa6e832a80)
2025-04-24 14:35:23,229 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:23,229 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:23,230 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:23,230 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803242144618940 to MsgsAck (1aa6e832a50)
2025-04-24 14:35:23,230 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:23,231 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:23,231 - __main__ - ERROR - Failed to search medical books after 3 attempts
2025-04-24 14:35:23,231 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:23,232 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:23,232 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803242152629804 to SearchRequest (1aa6e8301d0)
2025-04-24 14:35:23,232 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:23,233 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:23,233 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:23,434 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803242152629804
2025-04-24 14:35:23,434 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:23,434 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803242960474920 to MsgsAck (1aa6e832de0)
2025-04-24 14:35:23,434 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:23,435 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:23,435 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:23,435 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803242964459372 to MsgsAck (1aa6e832f00)
2025-04-24 14:35:23,435 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:23,436 - __main__ - ERROR - Telethon search error for inception: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:23,436 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:23,436 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:24,448 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803247309389664 to SearchRequest (1aa6e832bd0)
2025-04-24 14:35:24,448 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:24,449 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:24,450 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:24,648 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803247309389664
2025-04-24 14:35:24,648 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:24,648 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803248110487536 to MsgsAck (1aa6e833020)
2025-04-24 14:35:24,648 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:24,649 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:24,649 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:24,649 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803248112606600 to MsgsAck (1aa6e833170)
2025-04-24 14:35:24,649 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:24,650 - __main__ - ERROR - Telethon search error for inception: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:24,650 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:24,651 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:26,657 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803256737058480 to SearchRequest (1aa6e8330e0)
2025-04-24 14:35:26,658 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:26,659 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:26,659 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:26,861 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803256737058480
2025-04-24 14:35:26,861 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:26,861 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803257552191576 to MsgsAck (1aa6e832ed0)
2025-04-24 14:35:26,861 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:26,862 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:26,862 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:26,862 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803257556023440 to MsgsAck (1aa6e832e10)
2025-04-24 14:35:26,863 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:26,863 - __main__ - ERROR - Telethon search error for inception: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:26,863 - __main__ - ERROR - Failed to search inception after 3 attempts
2025-04-24 14:35:26,864 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:26,864 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:26,864 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803257564009508 to SearchRequest (1aa6e832f90)
2025-04-24 14:35:26,864 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:26,865 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:26,865 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:27,062 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803257564009508
2025-04-24 14:35:27,062 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:27,062 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803258651072940 to MsgsAck (1aa6e833290)
2025-04-24 14:35:27,062 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:27,063 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:27,063 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:27,063 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803258654886684 to MsgsAck (1aa6e832870)
2025-04-24 14:35:27,063 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:27,063 - __main__ - ERROR - Telethon search error for breaking bad: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:27,063 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:27,063 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:28,012 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:35:28,013 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:35:28,013 - telegram._bot - DEBUG - []
2025-04-24 14:35:28,013 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:35:28,013 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:35:28,068 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803262971384132 to SearchRequest (1aa6e833770)
2025-04-24 14:35:28,069 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:28,070 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:28,071 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:28,263 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803262971384132
2025-04-24 14:35:28,263 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:28,263 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803263749296272 to MsgsAck (1aa6e832e70)
2025-04-24 14:35:28,263 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:28,264 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:28,264 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:28,264 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803263753337944 to MsgsAck (1aa6e832150)
2025-04-24 14:35:28,264 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:28,265 - __main__ - ERROR - Telethon search error for breaking bad: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:28,265 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:28,265 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:30,277 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803272396796552 to SearchRequest (1aa6e831eb0)
2025-04-24 14:35:30,278 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:30,279 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:30,279 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:30,508 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803272396796552
2025-04-24 14:35:30,509 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:30,509 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803273325653404 to MsgsAck (1aa6e833830)
2025-04-24 14:35:30,509 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:30,510 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:30,510 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:30,510 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803273329314560 to MsgsAck (1aa6e8337d0)
2025-04-24 14:35:30,510 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:30,511 - __main__ - ERROR - Telethon search error for breaking bad: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:30,512 - __main__ - ERROR - Failed to search breaking bad after 3 attempts
2025-04-24 14:35:30,512 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:30,512 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:30,512 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803273337310164 to SearchRequest (1aa6e833860)
2025-04-24 14:35:30,512 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 44 bytes for sending
2025-04-24 14:35:30,514 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:30,514 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:30,712 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803273337310164
2025-04-24 14:35:30,713 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:30,713 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803274139872876 to MsgsAck (1aa6e833bc0)
2025-04-24 14:35:30,713 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:30,714 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:30,714 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:30,714 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803274143931716 to MsgsAck (1aa6e833cb0)
2025-04-24 14:35:30,714 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:30,714 - __main__ - ERROR - Telethon search error for robbins pathology: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:30,715 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:30,715 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:31,719 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803278460016220 to SearchRequest (1aa6e833b60)
2025-04-24 14:35:31,719 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 44 bytes for sending
2025-04-24 14:35:31,720 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:31,721 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:31,929 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803278460016220
2025-04-24 14:35:31,929 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:31,929 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803279297291728 to MsgsAck (1aa6e833d70)
2025-04-24 14:35:31,929 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:31,930 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:31,930 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:31,930 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803279301291436 to MsgsAck (1aa6e8323f0)
2025-04-24 14:35:31,930 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:31,930 - __main__ - ERROR - Telethon search error for robbins pathology: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:31,930 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:31,930 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:33,942 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803287939419008 to SearchRequest (1aa6e833bf0)
2025-04-24 14:35:33,942 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 44 bytes for sending
2025-04-24 14:35:33,943 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:33,943 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:34,144 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803287939419008
2025-04-24 14:35:34,144 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:34,144 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803289042521336 to MsgsAck (1aa6e833a10)
2025-04-24 14:35:34,144 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:34,145 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:34,145 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:34,145 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803289046538212 to MsgsAck (1aa6e8339e0)
2025-04-24 14:35:34,145 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:34,145 - __main__ - ERROR - Telethon search error for robbins pathology: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:34,145 - __main__ - ERROR - Failed to search robbins pathology after 3 attempts
2025-04-24 14:35:34,145 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:34,145 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:34,146 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803289050510264 to SearchRequest (1aa6e833aa0)
2025-04-24 14:35:34,146 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:34,146 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:34,146 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:34,349 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803289050510264
2025-04-24 14:35:34,349 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:34,349 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803289864019252 to MsgsAck (1aa6e833980)
2025-04-24 14:35:34,349 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:34,351 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:34,351 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:34,351 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803289873283244 to MsgsAck (1aa6e8327e0)
2025-04-24 14:35:34,351 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:34,352 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:34,352 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:34,353 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:35,359 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803294198864440 to SearchRequest (1aa6e833740)
2025-04-24 14:35:35,360 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:35,361 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:35,361 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:35,584 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803294198864440
2025-04-24 14:35:35,584 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:35,585 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803295101641160 to MsgsAck (1aa6e37eab0)
2025-04-24 14:35:35,585 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:35,585 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:35,586 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:35,586 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803295105642776 to MsgsAck (1aa6e5ddaf0)
2025-04-24 14:35:35,586 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:35,586 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:35,587 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:35,587 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:37,590 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803303711971984 to SearchRequest (1aa6e37eab0)
2025-04-24 14:35:37,591 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:37,592 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:37,592 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:37,799 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803303711971984
2025-04-24 14:35:37,799 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:37,799 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803304549833044 to MsgsAck (1aa6e0c4470)
2025-04-24 14:35:37,799 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:37,800 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:37,800 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:37,800 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803304552417500 to MsgsAck (1aa6e6f6330)
2025-04-24 14:35:37,800 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:37,800 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:37,800 - __main__ - ERROR - Failed to search movie download after 3 attempts
2025-04-24 14:35:37,800 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:37,800 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:37,800 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803304554536564 to SearchRequest (1aa6e5ddc70)
2025-04-24 14:35:37,800 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:37,801 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:37,801 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:38,025 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803304554536564
2025-04-24 14:35:38,026 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:38,026 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803305750569688 to MsgsAck (1aa6e0c4470)
2025-04-24 14:35:38,026 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:38,027 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:38,027 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:38,027 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803305754124984 to MsgsAck (1aa6e667770)
2025-04-24 14:35:38,027 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:38,028 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:38,029 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:38,029 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:38,205 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:35:38,206 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:35:38,206 - telegram._bot - DEBUG - []
2025-04-24 14:35:38,206 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:35:38,206 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:35:39,034 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803310077210416 to SearchRequest (1aa6e80cef0)
2025-04-24 14:35:39,034 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:39,035 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:39,035 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:39,774 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803310077210416
2025-04-24 14:35:39,774 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:39,774 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803313037326800 to MsgsAck (1aa6e7e37a0)
2025-04-24 14:35:39,775 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:39,775 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:39,776 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:39,776 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803313045325268 to MsgsAck (1aa6e667800)
2025-04-24 14:35:39,776 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:39,777 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:39,777 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:39,777 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:41,782 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803321659232372 to SearchRequest (1aa6e7e37a0)
2025-04-24 14:35:41,783 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:35:41,784 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:41,785 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:41,993 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803321659232372
2025-04-24 14:35:41,993 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:41,993 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803322503135912 to MsgsAck (1aa6e664200)
2025-04-24 14:35:41,993 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:41,993 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:41,993 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:41,993 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803322506757016 to MsgsAck (1aa6e6642f0)
2025-04-24 14:35:41,993 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:41,994 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:41,994 - __main__ - ERROR - Failed to search series download after 3 attempts
2025-04-24 14:35:41,994 - __main__ - INFO - Total groups: 2
2025-04-24 14:35:41,995 - __main__ - INFO - Searching files for query: hi nanna, types: ['.mp4', '.mkv'], groups: 2
2025-04-24 14:35:41,995 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:35:41,997 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:41,997 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:42,718 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:35:42,719 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: hi nanna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 77, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485543, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:35:42,720 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:35:42,721 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803325710316536 to SearchRequest (1aa6e80e150)
2025-04-24 14:35:42,721 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:35:42,723 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:42,723 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:43,020 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803325710316536
2025-04-24 14:35:43,021 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:43,021 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803327208005428 to MsgsAck (1aa6e80d340)
2025-04-24 14:35:43,021 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:43,021 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:43,021 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:43,021 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803327208005432 to MsgsAck (1aa6e80d790)
2025-04-24 14:35:43,021 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:43,022 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:43,022 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:43,023 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:43,023 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803327216009616 to SearchRequest (1aa6e80d340)
2025-04-24 14:35:43,023 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:35:43,024 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:43,024 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:43,315 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803327216009616
2025-04-24 14:35:43,315 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:43,316 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803328386767864 to MsgsAck (1aa6e80ed20)
2025-04-24 14:35:43,316 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:43,316 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:43,317 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:43,317 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803328390786644 to MsgsAck (1aa6e8335f0)
2025-04-24 14:35:43,317 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:43,318 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:43,318 - __main__ - INFO - Searching files for query: hi nanna movie, types: ['.mp4', '.mkv'], groups: 2
2025-04-24 14:35:43,319 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:35:43,321 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:43,321 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:43,695 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:35:43,695 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: hi nanna movie...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 78, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485544, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:35:43,696 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:35:43,696 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803329906526088 to SearchRequest (1aa6e8323c0)
2025-04-24 14:35:43,697 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:35:43,698 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:43,698 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:43,999 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803329906526088
2025-04-24 14:35:44,000 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:44,000 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803331417156340 to MsgsAck (1aa6e8337d0)
2025-04-24 14:35:44,000 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:44,000 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,000 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,001 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803331421172260 to MsgsAck (1aa6e833440)
2025-04-24 14:35:44,001 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:44,001 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:44,002 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,002 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,002 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803331425123336 to SearchRequest (1aa6e8337d0)
2025-04-24 14:35:44,002 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:35:44,003 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,003 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,335 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803331425123336
2025-04-24 14:35:44,335 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:44,336 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803332760525824 to MsgsAck (1aa6e8321b0)
2025-04-24 14:35:44,336 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:44,336 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,336 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,336 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803332763027312 to MsgsAck (1aa6e833620)
2025-04-24 14:35:44,336 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:44,336 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:44,338 - __main__ - INFO - Searching files for query: hi nanna mp4, types: ['.mp4', '.mkv'], groups: 2
2025-04-24 14:35:44,338 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:35:44,339 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,339 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,567 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803333686980368 to PingRequest (1aa6e664230)
2025-04-24 14:35:44,567 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:35:44,568 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,568 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,718 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:35:44,719 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: hi nanna mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 79, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485545, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:35:44,719 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:35:44,720 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803334299122928 to SearchRequest (1aa6e8310a0)
2025-04-24 14:35:44,720 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:35:44,721 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,721 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,761 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496803333686980368
2025-04-24 14:35:44,761 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:44,980 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803334299122928
2025-04-24 14:35:44,981 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:44,981 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803335342544676 to MsgsAck (1aa6e664230)
2025-04-24 14:35:44,981 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:44,982 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,982 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,982 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803335346611144 to MsgsAck (1aa6e80f050)
2025-04-24 14:35:44,982 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 44 bytes for sending
2025-04-24 14:35:44,983 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:44,984 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,984 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:44,984 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803335354628684 to SearchRequest (1aa6e832600)
2025-04-24 14:35:44,984 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:35:44,985 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:44,985 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:45,187 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803335354628684
2025-04-24 14:35:45,187 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:35:45,188 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803336464628936 to MsgsAck (1aa6e832390)
2025-04-24 14:35:45,188 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:45,189 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:45,189 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:45,189 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803336468476060 to MsgsAck (1aa6e833b60)
2025-04-24 14:35:45,189 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:35:45,190 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:35:45,190 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:35:45,191 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:35:45,191 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:35:45,568 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:35:45,569 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'hi nanna' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 80, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485546, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:35:45,569 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:35:48,389 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:35:48,390 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:35:48,390 - telegram._bot - DEBUG - []
2025-04-24 14:35:48,390 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:35:48,390 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:35:58,573 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:35:58,574 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:35:58,575 - telegram._bot - DEBUG - []
2025-04-24 14:35:58,575 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:35:58,575 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:36:08,772 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:36:08,772 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:36:08,773 - telegram._bot - DEBUG - []
2025-04-24 14:36:08,773 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:36:08,773 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:36:18,952 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:36:18,953 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:36:18,953 - telegram._bot - DEBUG - []
2025-04-24 14:36:18,954 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:36:18,954 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:36:26,823 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:36:26,824 - telegram._bot - DEBUG - Getting updates: [954247036]
2025-04-24 14:36:26,825 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001AA6E690100>]
2025-04-24 14:36:26,825 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:36:26,826 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:36:26,827 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247036, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Batman', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 81, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485587, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 14:36:26,827 - __main__ - INFO - Received message: batman
2025-04-24 14:36:26,828 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:36:27,699 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:36:27,700 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:batman', 'text': 'Movie'}, {'callback_data': 'series:batman', 'text': 'Series'}, {'callback_data': 'pdf:batman', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'batman' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 82, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485588, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:36:27,701 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:36:31,094 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:36:31,095 - telegram._bot - DEBUG - Getting updates: [954247037]
2025-04-24 14:36:31,095 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001AA6E692500>]
2025-04-24 14:36:31,095 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:36:31,095 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:36:31,096 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:batman', 'text': 'Movie'}, {'callback_data': 'series:batman', 'text': 'Series'}, {'callback_data': 'pdf:batman', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'batman' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 82, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485588, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488947085284651', 'data': 'movie:batman', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247037}
2025-04-24 14:36:31,096 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 14:36:31,479 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 14:36:31,479 - telegram._bot - DEBUG - True
2025-04-24 14:36:31,479 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 14:36:31,479 - __main__ - INFO - Searching movie: batman
2025-04-24 14:36:31,480 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=batman&page=1&include_adult=false
2025-04-24 14:36:31,483 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:36:31,769 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=batman&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 14:36:31,771 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 14:36:31,771 - __main__ - INFO - TMDB found 3 results for batman
2025-04-24 14:36:31,773 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 14:36:32,519 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=batman+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 14:36:32,522 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 14:36:32,701 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 14:36:33,387 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 14:36:33,983 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 14:36:33,985 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 14:36:33,985 - __main__ - INFO - Discovering groups across Telegram...
2025-04-24 14:36:33,986 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:36:34,380 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:36:34,381 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Entire Telegram lo groups chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 84, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485595, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:36:34,381 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:36:34,392 - __main__ - INFO - Loaded 2 cached groups
2025-04-24 14:36:34,392 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803547732811444 to SearchRequest (1aa6ea005c0)
2025-04-24 14:36:34,392 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:36:34,393 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:34,394 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:34,699 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803547732811444
2025-04-24 14:36:34,700 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:34,700 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803548964774604 to MsgsAck (1aa6ea005f0)
2025-04-24 14:36:34,700 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:34,701 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:34,701 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:34,701 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803548968966956 to MsgsAck (1aa6e79dd30)
2025-04-24 14:36:34,701 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:34,702 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:34,702 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:34,703 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:35,697 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803553248865244 to SearchRequest (1aa6e79de50)
2025-04-24 14:36:35,698 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:36:35,700 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:35,700 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:35,913 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803553248865244
2025-04-24 14:36:35,913 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:35,914 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803554116863368 to MsgsAck (1aa6cf71a60)
2025-04-24 14:36:35,914 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:35,914 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:35,914 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:35,914 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803554116863372 to MsgsAck (1aa6ea00620)
2025-04-24 14:36:35,914 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:35,915 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:35,915 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:35,915 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:37,927 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803562757184388 to SearchRequest (1aa6cf71a60)
2025-04-24 14:36:37,928 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:36:37,929 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:37,931 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:38,121 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803562757184388
2025-04-24 14:36:38,121 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:38,121 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803563829434400 to MsgsAck (1aa6e4e91f0)
2025-04-24 14:36:38,122 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:38,122 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:38,123 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:38,123 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803563837437632 to MsgsAck (1aa6e6f5df0)
2025-04-24 14:36:38,123 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:38,123 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:38,124 - __main__ - ERROR - Failed to search movies after 3 attempts
2025-04-24 14:36:38,124 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:38,124 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:38,124 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803563841445928 to SearchRequest (1aa6e4e91f0)
2025-04-24 14:36:38,124 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:36:38,125 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:38,125 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:38,329 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803563841445928
2025-04-24 14:36:38,329 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:38,330 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803564665689472 to MsgsAck (1aa6e6f6330)
2025-04-24 14:36:38,330 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:38,331 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:38,331 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:38,331 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803564671735768 to MsgsAck (1aa6ea002f0)
2025-04-24 14:36:38,331 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:38,333 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:38,333 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:38,333 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:39,342 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803569009685164 to SearchRequest (1aa6e6f6330)
2025-04-24 14:36:39,342 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:36:39,343 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:39,345 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:39,553 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803569009685164
2025-04-24 14:36:39,553 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:39,554 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803569858513480 to MsgsAck (1aa6ea005f0)
2025-04-24 14:36:39,554 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:39,554 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:39,554 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:39,554 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803569858513484 to MsgsAck (1aa6ea000e0)
2025-04-24 14:36:39,554 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:39,555 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:39,555 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:39,555 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:41,293 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:36:41,294 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:36:41,294 - telegram._bot - DEBUG - []
2025-04-24 14:36:41,294 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:36:41,294 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:36:41,561 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803578475864300 to SearchRequest (1aa6e80fdd0)
2025-04-24 14:36:41,561 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:36:41,562 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:41,562 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:41,763 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803578475864300
2025-04-24 14:36:41,763 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:41,763 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803579283577808 to MsgsAck (1aa6ea006b0)
2025-04-24 14:36:41,764 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:41,764 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:41,764 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:41,764 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803579287608992 to MsgsAck (1aa6ea01be0)
2025-04-24 14:36:41,764 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:41,765 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:41,765 - __main__ - ERROR - Failed to search series after 3 attempts
2025-04-24 14:36:41,765 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:41,765 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:41,766 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803579295605552 to SearchRequest (1aa6ea00050)
2025-04-24 14:36:41,766 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:36:41,766 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:41,766 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:41,996 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803579295605552
2025-04-24 14:36:41,996 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:41,996 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803580214033016 to MsgsAck (1aa6ea00440)
2025-04-24 14:36:41,997 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:41,997 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:41,997 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:41,997 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803580218039404 to MsgsAck (1aa6ea006e0)
2025-04-24 14:36:41,997 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:41,998 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:41,998 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:41,998 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:43,000 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803584818931712 to SearchRequest (1aa6ea00440)
2025-04-24 14:36:43,000 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:36:43,000 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:43,000 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:43,219 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803584818931712
2025-04-24 14:36:43,219 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:43,219 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803585695476664 to MsgsAck (1aa6ea006b0)
2025-04-24 14:36:43,219 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:43,220 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:43,220 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:43,221 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803585703446520 to MsgsAck (1aa6e80faa0)
2025-04-24 14:36:43,221 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:43,221 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:43,222 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:43,222 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:44,580 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803591434279220 to PingRequest (1aa6e4e8fe0)
2025-04-24 14:36:44,580 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:36:44,581 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:44,582 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:44,777 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496803591434279220
2025-04-24 14:36:44,777 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:45,235 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803594352708240 to SearchRequest (1aa6e80fad0)
2025-04-24 14:36:45,235 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:36:45,236 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:45,236 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:45,237 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803594360698124 to MsgsAck (1aa6e4e8fe0)
2025-04-24 14:36:45,237 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:45,238 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:45,238 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:45,539 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803594352708240
2025-04-24 14:36:45,540 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:45,540 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803595571211236 to MsgsAck (1aa6e80dee0)
2025-04-24 14:36:45,540 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:45,541 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:45,541 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:45,541 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803595574833292 to MsgsAck (1aa6e80e120)
2025-04-24 14:36:45,541 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:45,541 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:45,542 - __main__ - ERROR - Failed to search pdf after 3 attempts
2025-04-24 14:36:45,542 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:45,542 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:45,542 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803595578794856 to SearchRequest (1aa6e80f410)
2025-04-24 14:36:45,542 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:45,543 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:45,543 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:45,838 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803595578794856
2025-04-24 14:36:45,838 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:45,838 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803596763979336 to MsgsAck (1aa6e80e1e0)
2025-04-24 14:36:45,838 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:45,840 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:45,840 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:45,840 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803596770500560 to MsgsAck (1aa6e80ea20)
2025-04-24 14:36:45,840 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:45,840 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:45,842 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:45,842 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:46,848 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803601097517988 to SearchRequest (1aa6e79dd30)
2025-04-24 14:36:46,848 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:46,849 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:46,850 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:47,066 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803601097517988
2025-04-24 14:36:47,066 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:47,067 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803602267006540 to MsgsAck (1aa6e80f380)
2025-04-24 14:36:47,067 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:47,068 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:47,068 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:47,068 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803602271072052 to MsgsAck (1aa6e80fcb0)
2025-04-24 14:36:47,068 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:47,069 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:47,069 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:47,069 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:49,079 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803610905616668 to SearchRequest (1aa6ea00620)
2025-04-24 14:36:49,080 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:49,081 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:49,081 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:49,820 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803610905616668
2025-04-24 14:36:49,821 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:49,821 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803613873935608 to MsgsAck (1aa6e80fda0)
2025-04-24 14:36:49,821 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:49,822 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:49,822 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:49,822 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803613877914336 to MsgsAck (1aa6e80f2c0)
2025-04-24 14:36:49,823 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:49,823 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:49,824 - __main__ - ERROR - Failed to search telugu movies after 3 attempts
2025-04-24 14:36:49,824 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:49,824 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:49,824 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803613885924248 to SearchRequest (1aa6e6f5df0)
2025-04-24 14:36:49,824 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:49,825 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:49,826 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:50,128 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803613885924248
2025-04-24 14:36:50,128 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:50,128 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803615398103268 to MsgsAck (1aa6e80f740)
2025-04-24 14:36:50,128 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:50,129 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:50,129 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:50,130 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803615402102976 to MsgsAck (1aa6e80d910)
2025-04-24 14:36:50,130 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:50,130 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:50,131 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:50,131 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:51,134 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803619715912972 to SearchRequest (1aa6ea002f0)
2025-04-24 14:36:51,134 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:51,135 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:51,135 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:51,412 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803619715912972
2025-04-24 14:36:51,412 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:51,412 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803620829201852 to MsgsAck (1aa6e80f050)
2025-04-24 14:36:51,412 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:51,413 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:51,413 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:51,413 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803620833198700 to MsgsAck (1aa6e80de80)
2025-04-24 14:36:51,413 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:51,414 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:51,414 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:51,414 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:51,503 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:36:51,504 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:36:51,504 - telegram._bot - DEBUG - []
2025-04-24 14:36:51,504 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:36:51,504 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:36:53,424 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803629467832960 to SearchRequest (1aa6e80e5d0)
2025-04-24 14:36:53,424 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:53,425 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:53,425 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:53,622 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803629467832960
2025-04-24 14:36:53,622 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:53,623 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803630261038220 to MsgsAck (1aa6e80e030)
2025-04-24 14:36:53,623 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:53,623 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:53,624 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:53,624 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803630264645972 to MsgsAck (1aa6e80ddf0)
2025-04-24 14:36:53,624 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:53,624 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:53,625 - __main__ - ERROR - Failed to search english movies after 3 attempts
2025-04-24 14:36:53,625 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:53,625 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:53,625 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803630268625656 to SearchRequest (1aa6ea01be0)
2025-04-24 14:36:53,625 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:53,626 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:53,626 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:53,831 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803630268625656
2025-04-24 14:36:53,831 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:53,832 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803631100249684 to MsgsAck (1aa6e80e750)
2025-04-24 14:36:53,832 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:53,833 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:53,833 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:53,833 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803631104259884 to MsgsAck (1aa6e80e6f0)
2025-04-24 14:36:53,833 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:53,835 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:53,835 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:53,835 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:54,849 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803635462698976 to SearchRequest (1aa6ea006e0)
2025-04-24 14:36:54,850 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:54,850 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:54,850 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:55,041 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803635462698976
2025-04-24 14:36:55,042 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:55,042 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803636528730076 to MsgsAck (1aa6e80f140)
2025-04-24 14:36:55,042 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:55,043 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:55,043 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:55,043 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803636532679240 to MsgsAck (1aa6e80d640)
2025-04-24 14:36:55,043 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:55,044 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:55,044 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:55,044 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:57,057 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803645176874088 to SearchRequest (1aa6e80e810)
2025-04-24 14:36:57,057 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:57,058 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:57,058 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:57,261 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803645176874088
2025-04-24 14:36:57,262 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:57,262 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803645997120784 to MsgsAck (1aa6e80c9e0)
2025-04-24 14:36:57,262 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:57,263 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:57,263 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:57,263 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803646000678944 to MsgsAck (1aa6e80dd00)
2025-04-24 14:36:57,263 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:57,264 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:57,264 - __main__ - ERROR - Failed to search hindi movies after 3 attempts
2025-04-24 14:36:57,264 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:57,264 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:57,264 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803646004682468 to SearchRequest (1aa6e4e8fe0)
2025-04-24 14:36:57,264 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:57,265 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:57,266 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:57,473 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803646004682468
2025-04-24 14:36:57,473 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:57,473 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803646840660976 to MsgsAck (1aa6e80efc0)
2025-04-24 14:36:57,473 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:57,474 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:57,474 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:57,474 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803646844663548 to MsgsAck (1aa6e80e750)
2025-04-24 14:36:57,474 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:57,474 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:57,475 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:57,475 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:58,482 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803651171838332 to SearchRequest (1aa6e80eae0)
2025-04-24 14:36:58,483 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:36:58,484 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:58,484 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:58,681 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803651171838332
2025-04-24 14:36:58,682 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:36:58,682 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803651971766044 to MsgsAck (1aa6e80e030)
2025-04-24 14:36:58,682 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:58,683 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:58,683 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:36:58,683 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803651975768616 to MsgsAck (1aa6e80f0b0)
2025-04-24 14:36:58,683 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:36:58,684 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:36:58,684 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:36:58,684 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:00,699 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803660632160000 to SearchRequest (1aa6e79c0b0)
2025-04-24 14:37:00,699 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:00,701 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:00,701 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:00,892 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803660632160000
2025-04-24 14:37:00,893 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:00,893 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803661408680732 to MsgsAck (1aa6e80d760)
2025-04-24 14:37:00,893 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:00,894 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:00,894 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:00,894 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803661412686164 to MsgsAck (1aa6e80ef60)
2025-04-24 14:37:00,894 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:00,895 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:00,895 - __main__ - ERROR - Failed to search tamil movies after 3 attempts
2025-04-24 14:37:00,895 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:00,895 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:00,895 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803661416671568 to SearchRequest (1aa6ea00380)
2025-04-24 14:37:00,895 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:00,896 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:00,896 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:01,111 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803661416671568
2025-04-24 14:37:01,112 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:01,112 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803662577461656 to MsgsAck (1aa6e80fe30)
2025-04-24 14:37:01,112 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:01,113 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:01,113 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:01,113 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803662581457552 to MsgsAck (1aa6e80e120)
2025-04-24 14:37:01,113 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:01,113 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:01,114 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:01,114 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:01,693 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:37:01,694 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:37:01,694 - telegram._bot - DEBUG - []
2025-04-24 14:37:01,695 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:37:01,695 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:37:02,121 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803666910423336 to SearchRequest (1aa6e831b20)
2025-04-24 14:37:02,121 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:02,122 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:02,123 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:02,321 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803666910423336
2025-04-24 14:37:02,321 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:02,321 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803667710472164 to MsgsAck (1aa6e80cef0)
2025-04-24 14:37:02,321 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:02,322 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:02,322 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:02,322 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803667714470920 to MsgsAck (1aa6e80eab0)
2025-04-24 14:37:02,322 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:02,323 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:02,323 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:02,323 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:04,329 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803676329795184 to SearchRequest (1aa6ea007d0)
2025-04-24 14:37:04,329 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:04,330 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:04,330 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:04,525 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803676329795184
2025-04-24 14:37:04,526 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:04,526 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803677117278400 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:04,526 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:04,526 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:04,526 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:04,526 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803677120878520 to MsgsAck (1aa6e80c9e0)
2025-04-24 14:37:04,526 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:04,527 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:04,527 - __main__ - ERROR - Failed to search web series after 3 attempts
2025-04-24 14:37:04,527 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:04,527 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:04,527 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803677124886812 to SearchRequest (1aa6e80de80)
2025-04-24 14:37:04,528 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:37:04,528 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:04,528 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:04,730 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803677124886812
2025-04-24 14:37:04,731 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:04,731 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803677940589252 to MsgsAck (1aa6e80ede0)
2025-04-24 14:37:04,731 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:04,731 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:04,731 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:04,731 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803677940589256 to MsgsAck (1aa6e80cef0)
2025-04-24 14:37:04,732 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:04,732 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:04,732 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:04,732 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:05,721 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803682194101280 to SearchRequest (1aa6ea00350)
2025-04-24 14:37:05,721 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:37:05,722 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:05,722 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:05,921 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803682194101280
2025-04-24 14:37:05,923 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:05,923 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803683000089592 to MsgsAck (1aa6e80ede0)
2025-04-24 14:37:05,923 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:05,924 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:05,924 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:05,924 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803683004153196 to MsgsAck (1aa6e8337a0)
2025-04-24 14:37:05,924 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:05,924 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:05,925 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:05,925 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:07,927 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803691608060072 to SearchRequest (1aa6e80e6f0)
2025-04-24 14:37:07,927 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 14:37:07,928 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:07,929 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:08,261 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803691608060072
2025-04-24 14:37:08,261 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:08,261 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803693237134768 to MsgsAck (1aa6e80ede0)
2025-04-24 14:37:08,261 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:08,263 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:08,263 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:08,263 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803693245135140 to MsgsAck (1aa6e830680)
2025-04-24 14:37:08,263 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:08,264 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:08,264 - __main__ - ERROR - Failed to search books after 3 attempts
2025-04-24 14:37:08,264 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:08,264 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:08,265 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803693249976944 to SearchRequest (1aa6e80d640)
2025-04-24 14:37:08,265 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:08,266 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:08,266 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:08,582 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803693249976944
2025-04-24 14:37:08,583 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:08,583 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803694526645492 to MsgsAck (1aa6e80ede0)
2025-04-24 14:37:08,583 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:08,584 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:08,584 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:08,584 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803694531327080 to MsgsAck (1aa6e8309b0)
2025-04-24 14:37:08,584 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:08,585 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:08,585 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:08,585 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:09,590 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803698848734332 to SearchRequest (1aa6e80dd00)
2025-04-24 14:37:09,590 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:09,591 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:09,591 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:09,787 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803698848734332
2025-04-24 14:37:09,787 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:09,787 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803699636447384 to MsgsAck (1aa6e80ede0)
2025-04-24 14:37:09,787 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:09,787 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:09,787 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:09,788 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803699640446140 to MsgsAck (1aa6e830650)
2025-04-24 14:37:09,788 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:09,788 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:09,788 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:09,788 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:11,800 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803708278546052 to SearchRequest (1aa6e80e750)
2025-04-24 14:37:11,800 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:11,800 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:11,800 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:11,902 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:37:11,903 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:37:11,903 - telegram._bot - DEBUG - []
2025-04-24 14:37:11,903 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:37:11,903 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:37:12,034 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803708278546052
2025-04-24 14:37:12,034 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:12,034 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803709508926712 to MsgsAck (1aa6e830230)
2025-04-24 14:37:12,034 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:12,035 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:12,035 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:12,035 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803709512928328 to MsgsAck (1aa6e830560)
2025-04-24 14:37:12,035 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:12,036 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:12,036 - __main__ - ERROR - Failed to search medical books after 3 attempts
2025-04-24 14:37:12,036 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:12,036 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:12,036 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803709516951880 to SearchRequest (1aa6e80f0b0)
2025-04-24 14:37:12,036 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:12,037 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:12,037 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:12,251 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803709516951880
2025-04-24 14:37:12,251 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:12,251 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803710377393088 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:12,251 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:12,252 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:12,252 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:12,252 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803710381372772 to MsgsAck (1aa6e830e30)
2025-04-24 14:37:12,252 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:12,252 - __main__ - ERROR - Telethon search error for inception: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:12,253 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:12,253 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:13,253 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803714681093180 to SearchRequest (1aa6e80ef60)
2025-04-24 14:37:13,253 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:13,253 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:13,253 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:13,506 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803714681093180
2025-04-24 14:37:13,506 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:13,506 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803715695505104 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:13,506 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:13,507 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:13,507 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:13,507 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803715699496232 to MsgsAck (1aa6e831ac0)
2025-04-24 14:37:13,507 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:13,507 - __main__ - ERROR - Telethon search error for inception: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:13,507 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:13,507 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:15,524 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803724355868544 to SearchRequest (1aa6e80e120)
2025-04-24 14:37:15,524 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:15,525 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:15,525 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:15,721 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803724355868544
2025-04-24 14:37:15,721 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:15,722 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803725144174780 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:15,722 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:15,722 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:15,722 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:15,722 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803725146279540 to MsgsAck (1aa6e8324e0)
2025-04-24 14:37:15,722 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:15,722 - __main__ - ERROR - Telethon search error for inception: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:15,722 - __main__ - ERROR - Failed to search inception after 3 attempts
2025-04-24 14:37:15,723 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:15,723 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:15,723 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803725150536744 to SearchRequest (1aa6e80eab0)
2025-04-24 14:37:15,723 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:15,723 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:15,723 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:15,963 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803725150536744
2025-04-24 14:37:15,963 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:15,963 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803726112785544 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:15,963 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:15,963 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:15,964 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:15,964 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803726116733756 to MsgsAck (1aa6e831b80)
2025-04-24 14:37:15,964 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:15,964 - __main__ - ERROR - Telethon search error for breaking bad: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:15,964 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:15,964 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:16,978 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803730465202184 to SearchRequest (1aa6e80c9e0)
2025-04-24 14:37:16,978 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:16,979 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:16,979 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:17,191 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803730465202184
2025-04-24 14:37:17,192 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:17,192 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803731616981956 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:17,192 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:17,192 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:17,192 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:17,193 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803731620615456 to MsgsAck (1aa6e832000)
2025-04-24 14:37:17,193 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:17,193 - __main__ - ERROR - Telethon search error for breaking bad: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:17,193 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:17,193 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:19,195 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803740220932700 to SearchRequest (1aa6e80cef0)
2025-04-24 14:37:19,195 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:19,196 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:19,196 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:19,976 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803740220932700
2025-04-24 14:37:19,976 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:19,977 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803743343211864 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:19,977 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:19,977 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:19,977 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:19,978 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803743350792624 to MsgsAck (1aa6e831a90)
2025-04-24 14:37:19,978 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:19,978 - __main__ - ERROR - Telethon search error for breaking bad: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:19,978 - __main__ - ERROR - Failed to search breaking bad after 3 attempts
2025-04-24 14:37:19,979 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:19,979 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:19,979 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803743354812360 to SearchRequest (1aa6e80f560)
2025-04-24 14:37:19,979 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 44 bytes for sending
2025-04-24 14:37:19,980 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:19,980 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:20,382 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803743354812360
2025-04-24 14:37:20,382 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:20,383 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803745265122752 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:20,383 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:20,383 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:20,384 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:20,384 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803745269093852 to MsgsAck (1aa6e830da0)
2025-04-24 14:37:20,384 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:20,384 - __main__ - ERROR - Telethon search error for robbins pathology: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:20,385 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:20,385 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:21,387 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803749575708372 to SearchRequest (1aa6e80f5f0)
2025-04-24 14:37:21,388 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 44 bytes for sending
2025-04-24 14:37:21,389 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:21,389 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:21,580 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803749575708372
2025-04-24 14:37:21,581 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:21,581 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803750352592448 to MsgsAck (1aa6e80d730)
2025-04-24 14:37:21,581 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:21,581 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:21,581 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:21,581 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803750352592452 to MsgsAck (1aa6e8313d0)
2025-04-24 14:37:21,582 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:21,582 - __main__ - ERROR - Telethon search error for robbins pathology: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:21,582 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:21,582 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:22,097 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:37:22,097 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:37:22,098 - telegram._bot - DEBUG - []
2025-04-24 14:37:22,098 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:37:22,098 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:37:23,597 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803759009428248 to SearchRequest (1aa6e80d7f0)
2025-04-24 14:37:23,598 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 44 bytes for sending
2025-04-24 14:37:23,599 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:23,599 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:23,802 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803759009428248
2025-04-24 14:37:23,804 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:23,804 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803759834823832 to MsgsAck (1aa6e80e000)
2025-04-24 14:37:23,805 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:23,805 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:23,805 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:23,805 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803759837593304 to MsgsAck (1aa6e80f3e0)
2025-04-24 14:37:23,805 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:23,806 - __main__ - ERROR - Telethon search error for robbins pathology: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:23,806 - __main__ - ERROR - Failed to search robbins pathology after 3 attempts
2025-04-24 14:37:23,806 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:23,807 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:23,807 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803759847845300 to SearchRequest (1aa6e80e4b0)
2025-04-24 14:37:23,807 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:23,808 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:23,808 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:24,010 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803759847845300
2025-04-24 14:37:24,011 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:24,011 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803760959643232 to MsgsAck (1aa6e80d100)
2025-04-24 14:37:24,011 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:24,012 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:24,012 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:24,012 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803760963570464 to MsgsAck (1aa6e80daf0)
2025-04-24 14:37:24,012 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:24,013 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:24,013 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:24,013 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:25,021 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803765295041552 to SearchRequest (1aa6e80da90)
2025-04-24 14:37:25,021 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:25,023 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:25,023 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:25,312 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803765295041552
2025-04-24 14:37:25,312 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:25,312 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803766457986344 to MsgsAck (1aa6e80eea0)
2025-04-24 14:37:25,313 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:25,313 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:25,313 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:25,313 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803766462098588 to MsgsAck (1aa6e80ce60)
2025-04-24 14:37:25,314 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:25,314 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:25,314 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:25,315 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:27,326 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803775104251616 to SearchRequest (1aa6e80da60)
2025-04-24 14:37:27,326 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:27,327 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:27,327 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:27,521 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803775104251616
2025-04-24 14:37:27,521 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:27,521 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803775883990996 to MsgsAck (1aa6e80fa40)
2025-04-24 14:37:27,521 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:27,523 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:27,523 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:27,523 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803775890118356 to MsgsAck (1aa6e80e390)
2025-04-24 14:37:27,523 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:27,524 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:27,524 - __main__ - ERROR - Failed to search movie download after 3 attempts
2025-04-24 14:37:27,525 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:27,525 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:27,525 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803775898200744 to SearchRequest (1aa6e80d340)
2025-04-24 14:37:27,525 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:27,526 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:27,526 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:27,732 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803775898200744
2025-04-24 14:37:27,732 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:27,732 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803776726781600 to MsgsAck (1aa6e80d130)
2025-04-24 14:37:27,732 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:27,733 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:27,733 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:27,733 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803776730813736 to MsgsAck (1aa6e80e4e0)
2025-04-24 14:37:27,733 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:27,734 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:27,734 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:27,735 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:28,744 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803781071480152 to SearchRequest (1aa6e80fad0)
2025-04-24 14:37:28,744 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:28,745 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:28,745 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:28,955 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803781071480152
2025-04-24 14:37:28,956 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:28,956 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803781916757940 to MsgsAck (1aa6e80f2c0)
2025-04-24 14:37:28,956 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:28,957 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:28,957 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:28,957 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803781922830936 to MsgsAck (1aa6e6f6330)
2025-04-24 14:37:28,957 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:28,958 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:28,958 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:28,958 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:30,962 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803790530453324 to SearchRequest (1aa6e6f5df0)
2025-04-24 14:37:30,962 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 14:37:30,962 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:30,962 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:31,163 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803790530453324
2025-04-24 14:37:31,163 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:31,164 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803791634400608 to MsgsAck (1aa6e80fcb0)
2025-04-24 14:37:31,164 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:31,165 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:31,165 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:31,165 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803791638412716 to MsgsAck (1aa6e80ee40)
2025-04-24 14:37:31,165 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:31,166 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:31,166 - __main__ - ERROR - Failed to search series download after 3 attempts
2025-04-24 14:37:31,166 - __main__ - INFO - Total groups: 2
2025-04-24 14:37:31,167 - __main__ - INFO - Searching files for query: batman, types: ['.mp4', '.mkv'], groups: 2
2025-04-24 14:37:31,167 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:37:31,169 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:31,169 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:31,949 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:37:31,950 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: batman...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 85, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485652, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:37:31,950 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:37:31,951 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803794782037024 to SearchRequest (1aa6ea00650)
2025-04-24 14:37:31,951 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 14:37:31,952 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:31,952 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,141 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803794782037024
2025-04-24 14:37:32,142 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:32,142 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803795841987496 to MsgsAck (1aa6e80de20)
2025-04-24 14:37:32,142 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:32,143 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,143 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,143 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803795845966228 to MsgsAck (1aa6e80f2f0)
2025-04-24 14:37:32,143 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:32,144 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:32,145 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,145 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,145 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803795853558428 to SearchRequest (1aa6e80de20)
2025-04-24 14:37:32,145 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 14:37:32,146 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,146 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,272 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:37:32,272 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:37:32,273 - telegram._bot - DEBUG - []
2025-04-24 14:37:32,273 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:37:32,273 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:37:32,351 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803795853558428
2025-04-24 14:37:32,351 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:32,351 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803796677167780 to MsgsAck (1aa6ea03ec0)
2025-04-24 14:37:32,351 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:32,352 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,352 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,352 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803796681168444 to MsgsAck (1aa6ea01970)
2025-04-24 14:37:32,352 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:32,352 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:32,353 - __main__ - INFO - Searching files for query: batman movie, types: ['.mp4', '.mkv'], groups: 2
2025-04-24 14:37:32,353 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:37:32,353 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,353 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,716 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:37:32,717 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: batman movie...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 86, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485653, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:37:32,717 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:37:32,718 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803798146476632 to SearchRequest (1aa6ea03b60)
2025-04-24 14:37:32,718 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:37:32,719 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,719 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,928 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803798146476632
2025-04-24 14:37:32,928 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:32,928 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803798987080460 to MsgsAck (1aa6ea01340)
2025-04-24 14:37:32,928 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:32,929 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,929 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,929 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803798991167908 to MsgsAck (1aa6ea01670)
2025-04-24 14:37:32,929 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:32,930 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:32,930 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,931 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:32,931 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803798999173052 to SearchRequest (1aa6ea01340)
2025-04-24 14:37:32,931 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 92 bytes for sending
2025-04-24 14:37:32,932 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:32,932 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:33,127 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803798999173052
2025-04-24 14:37:33,128 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:33,128 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803800081717024 to MsgsAck (1aa6ea034d0)
2025-04-24 14:37:33,128 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:33,128 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:33,128 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:33,128 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803800081717028 to MsgsAck (1aa6ea03e00)
2025-04-24 14:37:33,128 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:33,130 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:33,130 - __main__ - INFO - Searching files for query: batman mp4, types: ['.mp4', '.mkv'], groups: 2
2025-04-24 14:37:33,130 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:37:33,131 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:33,131 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:33,502 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:37:33,502 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Files lo chusthunna: batman mp4...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 87, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485654, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:37:33,503 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:37:33,503 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803801582204352 to SearchRequest (1aa6ea01a90)
2025-04-24 14:37:33,503 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:37:33,503 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:33,503 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:33,689 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803801582204352
2025-04-24 14:37:33,689 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:33,689 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803802326587208 to MsgsAck (1aa6ea03e90)
2025-04-24 14:37:33,690 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:33,691 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:33,691 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:33,691 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803802334585676 to MsgsAck (1aa6ea02a50)
2025-04-24 14:37:33,691 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:33,692 - __main__ - ERROR - File search error in group -100123456789: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:33,692 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:33,693 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:33,693 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803802342603216 to SearchRequest (1aa6ea03e90)
2025-04-24 14:37:33,693 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 88 bytes for sending
2025-04-24 14:37:33,693 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:33,693 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:33,892 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496803802342603216
2025-04-24 14:37:33,892 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:33,892 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803803138445384 to MsgsAck (1aa6ea024b0)
2025-04-24 14:37:33,892 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:33,893 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:33,893 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:33,893 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803803140571124 to MsgsAck (1aa6ea03c80)
2025-04-24 14:37:33,893 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:37:33,893 - __main__ - ERROR - File search error in group -100987654321: The key is not registered in the system (caused by SearchRequest)
2025-04-24 14:37:33,893 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 14:37:33,895 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:33,895 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:34,265 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 14:37:34,266 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Files em levu for 'batman' in Telegram groups, checking external sources...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 88, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745485655, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 14:37:34,267 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 14:37:42,453 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:37:42,454 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:37:42,455 - telegram._bot - DEBUG - []
2025-04-24 14:37:42,455 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:37:42,455 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:37:44,588 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496803849166930588 to PingRequest (1aa6ea006b0)
2025-04-24 14:37:44,589 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:37:44,590 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:37:44,590 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:37:44,775 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496803849166930588
2025-04-24 14:37:44,775 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 14:37:52,633 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:37:52,633 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:37:52,634 - telegram._bot - DEBUG - []
2025-04-24 14:37:52,634 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:37:52,634 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:38:02,829 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:38:02,830 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:38:02,830 - telegram._bot - DEBUG - []
2025-04-24 14:38:02,830 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:38:02,830 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:38:13,009 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:38:13,009 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:38:13,010 - telegram._bot - DEBUG - []
2025-04-24 14:38:13,010 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:38:13,010 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:38:23,190 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:38:23,191 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:38:23,191 - telegram._bot - DEBUG - []
2025-04-24 14:38:23,191 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:38:23,191 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:38:33,370 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:38:33,370 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:38:33,371 - telegram._bot - DEBUG - []
2025-04-24 14:38:33,371 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:38:33,371 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:38:43,553 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 14:38:43,554 - telegram._bot - DEBUG - No new updates found.
2025-04-24 14:38:43,555 - telegram._bot - DEBUG - []
2025-04-24 14:38:43,555 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 14:38:43,555 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 14:38:44,613 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496804106965349248 to PingRequest (1aa6e80fce0)
2025-04-24 14:38:44,613 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 14:38:44,614 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:38:44,614 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:38:44,615 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496804106973409704 to MsgsAck (1aa6ea006b0)
2025-04-24 14:38:44,615 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 14:38:44,616 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 14:38:44,616 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 14:38:44,820 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496804106965349248
2025-04-24 14:38:44,820 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:00:11,194 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 15:00:11,198 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 15:00:12,154 - __main__ - INFO - Bot polling started...
2025-04-24 15:00:12,157 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 15:00:12,878 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 15:00:12,880 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 15:00:12,880 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 15:00:12,881 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 15:00:12,881 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 15:00:12,882 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 15:00:12,882 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 15:00:12,883 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 15:00:13,071 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 15:00:13,072 - telegram._bot - DEBUG - True
2025-04-24 15:00:13,073 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 15:00:13,074 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 15:00:13,074 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 15:00:13,075 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 15:00:13,076 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 15:00:13,076 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:00:13,078 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 15:00:13,079 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 15:00:13,079 - telegram.ext._application - INFO - Application started
2025-04-24 15:00:13,080 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 15:00:13,080 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 15:00:23,647 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:00:23,648 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:00:23,650 - telegram._bot - DEBUG - []
2025-04-24 15:00:23,650 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:00:23,651 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:00:33,825 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:00:33,827 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:00:33,828 - telegram._bot - DEBUG - []
2025-04-24 15:00:33,828 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:00:33,829 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:00:44,009 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:00:44,010 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:00:44,012 - telegram._bot - DEBUG - []
2025-04-24 15:00:44,012 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:00:44,013 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:00:54,224 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:00:54,225 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:00:54,227 - telegram._bot - DEBUG - []
2025-04-24 15:00:54,227 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:00:54,227 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:01:04,404 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:01:04,405 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:01:04,406 - telegram._bot - DEBUG - []
2025-04-24 15:01:04,406 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:01:04,407 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:01:14,589 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:01:14,590 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:01:14,591 - telegram._bot - DEBUG - []
2025-04-24 15:01:14,592 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:01:14,592 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:01:24,784 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:01:24,785 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:01:24,786 - telegram._bot - DEBUG - []
2025-04-24 15:01:24,786 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:01:24,787 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:01:38,202 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 15:01:38,205 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 15:01:39,141 - __main__ - INFO - Bot polling started...
2025-04-24 15:01:39,141 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 15:01:39,850 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 15:01:39,851 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 15:01:39,851 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 15:01:39,851 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 15:01:39,851 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 15:01:39,852 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 15:01:39,852 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 15:01:39,852 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 15:01:40,042 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 15:01:40,043 - telegram._bot - DEBUG - True
2025-04-24 15:01:40,043 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 15:01:40,044 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 15:01:40,044 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 15:01:40,044 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 15:01:40,044 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 15:01:40,044 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:01:40,046 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 15:01:40,046 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 15:01:40,046 - telegram.ext._application - INFO - Application started
2025-04-24 15:01:40,047 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 15:01:40,047 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 15:01:50,629 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:01:50,630 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:01:50,630 - telegram._bot - DEBUG - []
2025-04-24 15:01:50,630 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:01:50,630 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:02:00,813 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:02:00,814 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:02:00,814 - telegram._bot - DEBUG - []
2025-04-24 15:02:00,815 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:02:00,815 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:02:11,032 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:02:11,033 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:02:11,034 - telegram._bot - DEBUG - []
2025-04-24 15:02:11,034 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:02:11,034 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:02:21,236 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:02:21,238 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:02:21,238 - telegram._bot - DEBUG - []
2025-04-24 15:02:21,238 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:02:21,238 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:02:31,434 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:02:31,434 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:02:31,434 - telegram._bot - DEBUG - []
2025-04-24 15:02:31,434 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:02:31,434 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:02:41,613 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:02:41,614 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:02:41,615 - telegram._bot - DEBUG - []
2025-04-24 15:02:41,615 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:02:41,615 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:02:51,812 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:02:51,814 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:02:51,814 - telegram._bot - DEBUG - []
2025-04-24 15:02:51,814 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:02:51,814 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:03:01,998 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:03:02,000 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:03:02,000 - telegram._bot - DEBUG - []
2025-04-24 15:03:02,000 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:03:02,001 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:03:12,194 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:03:12,194 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:03:12,194 - telegram._bot - DEBUG - []
2025-04-24 15:03:12,194 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:03:12,194 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:03:20,290 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:03:20,291 - telegram._bot - DEBUG - Getting updates: [954247038]
2025-04-24 15:03:20,292 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000144B4323580>]
2025-04-24 15:03:20,292 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:03:20,292 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:03:20,293 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247038, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 89, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487201, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 15:03:20,294 - __main__ - INFO - Received /start command
2025-04-24 15:03:20,294 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:03:21,210 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:03:21,211 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 167}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 90, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487202, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:03:21,212 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:03:30,491 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:03:30,492 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:03:30,492 - telegram._bot - DEBUG - []
2025-04-24 15:03:30,492 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:03:30,492 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:03:33,639 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:03:33,640 - telegram._bot - DEBUG - Getting updates: [954247039]
2025-04-24 15:03:33,640 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000144B4323340>]
2025-04-24 15:03:33,640 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:03:33,640 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:03:33,641 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247039, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Salaar', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 91, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487214, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 15:03:33,642 - __main__ - INFO - Received message: salaar
2025-04-24 15:03:33,644 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:03:34,441 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:03:34,442 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:salaar', 'text': 'Movie'}, {'callback_data': 'series:salaar', 'text': 'Series'}, {'callback_data': 'pdf:salaar', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'salaar' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 92, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487215, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:03:34,442 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:03:37,032 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:03:37,033 - telegram._bot - DEBUG - Getting updates: [954247040]
2025-04-24 15:03:37,033 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000144B43219C0>]
2025-04-24 15:03:37,034 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:03:37,034 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:03:37,035 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:salaar', 'text': 'Movie'}, {'callback_data': 'series:salaar', 'text': 'Series'}, {'callback_data': 'pdf:salaar', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'salaar' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 92, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487215, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488949656312865', 'data': 'movie:salaar', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247040}
2025-04-24 15:03:37,036 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 15:03:37,386 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 15:03:37,387 - telegram._bot - DEBUG - True
2025-04-24 15:03:37,387 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 15:03:37,387 - __main__ - INFO - Searching movie: salaar
2025-04-24 15:03:37,387 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=salaar&page=1&include_adult=false
2025-04-24 15:03:37,389 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:03:37,922 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=salaar&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 15:03:37,927 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 15:03:37,927 - __main__ - INFO - TMDB found 4 results for salaar
2025-04-24 15:03:37,929 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 15:03:38,666 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=salaar+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 15:03:38,671 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:03:38,816 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 15:03:40,582 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 15:03:42,099 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 15:03:42,121 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 15:03:42,121 - __main__ - INFO - Discovering groups across Telegram...
2025-04-24 15:03:42,121 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 15:03:42,121 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 15:03:42,122 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 15:03:42,293 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 15:03:42,293 - telethon.network.mtprotosender - DEBUG - New auth_key attempt 1...
2025-04-24 15:03:45,359 - telethon.network.mtprotosender - DEBUG - auth_key generation success!
2025-04-24 15:03:45,359 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 15:03:45,359 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 15:03:45,359 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 15:03:45,367 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:45,368 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810548433497532 to InvokeWithLayerRequest (144b444f0b0)
2025-04-24 15:03:45,368 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 15:03:45,369 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:45,369 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:45,369 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:45,552 - telethon.network.mtprotostate - DEBUG - Updated time offset (old offset 0, bad 7496810549172194584, good 7496810554061795329, new 1)
2025-04-24 15:03:45,552 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496810548433497532
2025-04-24 15:03:45,552 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 15:03:45,552 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:45,552 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810553467161880 to InvokeWithLayerRequest (144b444f0b0)
2025-04-24 15:03:45,552 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 15:03:45,553 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:45,553 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:45,553 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810553471056684 to MsgsAck (144b4423740)
2025-04-24 15:03:45,553 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:45,554 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:45,554 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:45,712 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 15:03:45,713 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 15:03:45,713 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496810553467161880]
2025-04-24 15:03:45,713 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:45,779 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810553467161880
2025-04-24 15:03:45,779 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:45,779 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810554374425636 to GetUsersRequest (144b4423860)
2025-04-24 15:03:45,779 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:03:45,780 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:45,780 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:45,780 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810554378445372 to MsgsAck (144b4423b90)
2025-04-24 15:03:45,780 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 15:03:45,781 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:45,781 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:46,017 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810554374425636
2025-04-24 15:03:46,018 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:46,018 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810555625161516 to MsgsAck (144b444e9c0)
2025-04-24 15:03:46,018 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:46,019 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:46,019 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:46,019 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810555629227032 to MsgsAck (144b444c7a0)
2025-04-24 15:03:46,019 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:46,020 - __main__ - INFO - Client connected successfully
2025-04-24 15:03:46,020 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:03:46,021 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:46,022 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:46,387 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:03:46,387 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Entire Telegram lo groups chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 94, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487227, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:03:46,388 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:03:46,388 - __main__ - INFO - Loaded 0 cached groups
2025-04-24 15:03:46,388 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810557106288300 to SearchRequest (144b444f350)
2025-04-24 15:03:46,389 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:03:46,390 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:46,390 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:46,659 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810557106288300
2025-04-24 15:03:46,661 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:46,661 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810558194773068 to MsgsAck (144b444c860)
2025-04-24 15:03:46,661 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:46,662 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:46,662 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:46,662 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810558198878636 to MsgsAck (144b444c050)
2025-04-24 15:03:46,662 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:46,662 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:03:46,663 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:46,663 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:47,232 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:03:47,233 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:03:47,233 - telegram._bot - DEBUG - []
2025-04-24 15:03:47,234 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:03:47,234 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:03:47,663 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810562497706404 to SearchRequest (144b444fc80)
2025-04-24 15:03:47,663 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:03:47,664 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:47,664 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:47,836 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810562497706404
2025-04-24 15:03:47,836 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:47,837 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810563195483200 to MsgsAck (144b444f9b0)
2025-04-24 15:03:47,837 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:47,837 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:47,837 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:47,837 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810563195483204 to MsgsAck (144b444f650)
2025-04-24 15:03:47,837 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:47,838 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:03:47,838 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:47,838 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:49,848 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810571828092808 to SearchRequest (144b444fcb0)
2025-04-24 15:03:49,848 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:03:49,849 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:49,849 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:50,151 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810571828092808
2025-04-24 15:03:50,151 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:50,152 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810573338692544 to MsgsAck (144b444fe30)
2025-04-24 15:03:50,152 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:50,152 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:50,152 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:50,153 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810573342678900 to MsgsAck (144b444fd70)
2025-04-24 15:03:50,153 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:50,153 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:03:50,154 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:50,154 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:54,159 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810590547394164 to SearchRequest (144b444f830)
2025-04-24 15:03:54,159 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:03:54,160 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:54,160 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:54,344 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810590547394164
2025-04-24 15:03:54,345 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:03:54,345 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810591290476208 to MsgsAck (144b444faa0)
2025-04-24 15:03:54,345 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:54,346 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:54,346 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:54,346 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810591296563512 to MsgsAck (144b444fd40)
2025-04-24 15:03:54,346 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:03:54,347 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:03:54,347 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:03:54,347 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:03:57,429 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:03:57,430 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:03:57,430 - telegram._bot - DEBUG - []
2025-04-24 15:03:57,430 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:03:57,430 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:04:02,363 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810625725109484 to SearchRequest (144b4460980)
2025-04-24 15:04:02,364 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:04:02,364 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:02,364 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:02,640 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810625725109484
2025-04-24 15:04:02,641 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:02,641 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810626835957908 to MsgsAck (144b4460470)
2025-04-24 15:04:02,641 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:02,641 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:02,642 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:02,642 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810626839956664 to MsgsAck (144b4461190)
2025-04-24 15:04:02,642 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:02,643 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:02,643 - __main__ - ERROR - Failed to search movies after 5 attempts
2025-04-24 15:04:02,643 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:02,644 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:02,644 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810626847966576 to SearchRequest (144b4461d00)
2025-04-24 15:04:02,644 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:04:02,645 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:02,645 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:02,845 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810626847966576
2025-04-24 15:04:02,846 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:02,846 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810627654317284 to MsgsAck (144b44614f0)
2025-04-24 15:04:02,846 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:02,847 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:02,847 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:02,847 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810627660847092 to MsgsAck (144b4461df0)
2025-04-24 15:04:02,847 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:02,848 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:02,848 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:02,848 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:03,856 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810631989766148 to SearchRequest (144b4460e00)
2025-04-24 15:04:03,857 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:04:03,857 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:03,858 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:04,036 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810631989766148
2025-04-24 15:04:04,037 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:04,037 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810633009504944 to MsgsAck (144b4461130)
2025-04-24 15:04:04,037 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:04,038 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:04,038 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:04,038 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810633013549476 to MsgsAck (144b44611c0)
2025-04-24 15:04:04,038 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:04,039 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:04,039 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:04,040 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:06,055 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810641672974500 to SearchRequest (144b44620c0)
2025-04-24 15:04:06,055 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:04:06,056 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:06,056 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:06,247 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810641672974500
2025-04-24 15:04:06,247 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:06,247 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810642440814888 to MsgsAck (144b4461cd0)
2025-04-24 15:04:06,247 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:06,248 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:06,248 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:06,248 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810642444820320 to MsgsAck (144b44623c0)
2025-04-24 15:04:06,248 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:06,249 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:06,250 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:06,250 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:07,611 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:04:07,612 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:04:07,612 - telegram._bot - DEBUG - []
2025-04-24 15:04:07,612 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:04:07,613 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:04:10,259 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810659669198436 to SearchRequest (144b4460e90)
2025-04-24 15:04:10,259 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:04:10,260 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:10,261 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:10,527 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810659669198436
2025-04-24 15:04:10,527 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:10,528 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810660745717448 to MsgsAck (144b4461ca0)
2025-04-24 15:04:10,528 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:10,528 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:10,528 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:10,528 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810660745717452 to MsgsAck (144b4462030)
2025-04-24 15:04:10,528 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:10,529 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:10,529 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:10,529 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:17,805 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:04:17,806 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:04:17,806 - telegram._bot - DEBUG - []
2025-04-24 15:04:17,806 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:04:17,807 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:04:18,544 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810695166991652 to SearchRequest (144b4462570)
2025-04-24 15:04:18,544 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:04:18,545 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:18,545 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:18,754 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810695166991652
2025-04-24 15:04:18,755 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:18,755 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810696010211408 to MsgsAck (144b4461730)
2025-04-24 15:04:18,755 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:18,755 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:18,755 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:18,755 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810696012605132 to MsgsAck (144b4461280)
2025-04-24 15:04:18,755 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:18,756 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:18,756 - __main__ - ERROR - Failed to search series after 5 attempts
2025-04-24 15:04:18,756 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:18,756 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:18,756 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810696016013564 to SearchRequest (144b444c7a0)
2025-04-24 15:04:18,756 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:04:18,757 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:18,757 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:18,996 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810696016013564
2025-04-24 15:04:18,997 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:18,997 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810696978958548 to MsgsAck (144b4462600)
2025-04-24 15:04:18,997 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:18,998 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:18,998 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:18,998 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810696982952536 to MsgsAck (144b4462a80)
2025-04-24 15:04:18,998 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:18,998 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:18,999 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:18,999 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:20,001 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810701587568944 to SearchRequest (144b444c050)
2025-04-24 15:04:20,001 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:04:20,003 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:20,003 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:20,191 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810701587568944
2025-04-24 15:04:20,191 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:20,192 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810702348759360 to MsgsAck (144b44628a0)
2025-04-24 15:04:20,192 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:20,192 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:20,193 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:20,193 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810702352807708 to MsgsAck (144b4462990)
2025-04-24 15:04:20,193 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:20,194 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:20,194 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:20,195 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:22,199 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810710966133068 to SearchRequest (144b444f650)
2025-04-24 15:04:22,199 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:04:22,200 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:22,200 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:22,415 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810710966133068
2025-04-24 15:04:22,416 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:22,416 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810711835412928 to MsgsAck (144b4462780)
2025-04-24 15:04:22,416 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:22,416 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:22,416 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:22,416 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810711835412932 to MsgsAck (144b4462840)
2025-04-24 15:04:22,416 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:22,416 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:22,417 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:22,417 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:26,430 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810729072255572 to SearchRequest (144b444fce0)
2025-04-24 15:04:26,430 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:04:26,431 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:26,431 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:26,654 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810729072255572
2025-04-24 15:04:26,654 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:26,654 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810729966319520 to MsgsAck (144b4462ba0)
2025-04-24 15:04:26,655 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:26,655 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:26,655 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:26,656 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810729974328476 to MsgsAck (144b44625d0)
2025-04-24 15:04:26,656 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:26,657 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:26,657 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:26,657 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:27,993 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:04:27,994 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:04:27,994 - telegram._bot - DEBUG - []
2025-04-24 15:04:27,994 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:04:27,994 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:04:34,681 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810764435894468 to SearchRequest (144b44632c0)
2025-04-24 15:04:34,682 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:04:34,682 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:34,682 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:34,858 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810764435894468
2025-04-24 15:04:34,858 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:34,858 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810765143795468 to MsgsAck (144b44614c0)
2025-04-24 15:04:34,858 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:34,859 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:34,859 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:34,860 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810765151620364 to MsgsAck (144b4462600)
2025-04-24 15:04:34,860 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:34,861 - __main__ - ERROR - Telethon search error for pdf: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:34,861 - __main__ - ERROR - Failed to search pdf after 5 attempts
2025-04-24 15:04:34,861 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:34,862 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:34,862 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810765159611204 to SearchRequest (144b4463440)
2025-04-24 15:04:34,862 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:34,863 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:34,863 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:35,058 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810765159611204
2025-04-24 15:04:35,060 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:35,061 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810766250759224 to MsgsAck (144b44633b0)
2025-04-24 15:04:35,061 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:35,062 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:35,062 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:35,063 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810766258759596 to MsgsAck (144b4463380)
2025-04-24 15:04:35,063 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:35,063 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:35,064 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:35,064 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:36,071 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810770585645420 to SearchRequest (144b44633e0)
2025-04-24 15:04:36,071 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:36,072 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:36,073 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:36,269 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810770585645420
2025-04-24 15:04:36,269 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:36,270 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810771376173716 to MsgsAck (144b4463800)
2025-04-24 15:04:36,270 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:36,271 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:36,271 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:36,271 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810771384195072 to MsgsAck (144b44638c0)
2025-04-24 15:04:36,272 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:36,273 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:36,273 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:36,274 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:38,223 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:04:38,224 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:04:38,225 - telegram._bot - DEBUG - []
2025-04-24 15:04:38,225 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:04:38,225 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:04:38,281 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810780013809192 to SearchRequest (144b4463ef0)
2025-04-24 15:04:38,281 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:38,283 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:38,283 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:38,529 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810780013809192
2025-04-24 15:04:38,529 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:38,530 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810781010031688 to MsgsAck (144b4461df0)
2025-04-24 15:04:38,530 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:38,531 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:38,531 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:38,531 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810781014019952 to MsgsAck (144b4463650)
2025-04-24 15:04:38,531 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:38,532 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:38,533 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:38,533 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:42,548 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810798263610360 to SearchRequest (144b444cf80)
2025-04-24 15:04:42,548 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:42,549 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:42,549 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:42,807 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810798263610360
2025-04-24 15:04:42,807 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:42,808 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810799301513192 to MsgsAck (144b4463dd0)
2025-04-24 15:04:42,808 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:42,809 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:42,809 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:42,809 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810799305557724 to MsgsAck (144b4463fe0)
2025-04-24 15:04:42,809 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:42,810 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:42,810 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:42,810 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:46,039 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810813406692508 to PingRequest (144b444e4e0)
2025-04-24 15:04:46,039 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:04:46,040 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:46,040 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:46,216 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496810813406692508
2025-04-24 15:04:46,216 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:48,431 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:04:48,432 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:04:48,432 - telegram._bot - DEBUG - []
2025-04-24 15:04:48,432 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:04:48,433 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:04:50,819 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810833707273972 to SearchRequest (144b4624bf0)
2025-04-24 15:04:50,819 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:50,820 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:50,820 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:50,820 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810833711217416 to MsgsAck (144b44638f0)
2025-04-24 15:04:50,821 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:50,822 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:50,822 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:51,009 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810833707273972
2025-04-24 15:04:51,009 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:51,009 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810834760138648 to MsgsAck (144b4461280)
2025-04-24 15:04:51,010 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:51,011 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:51,011 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:51,011 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810834768140928 to MsgsAck (144b444e4e0)
2025-04-24 15:04:51,011 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:51,012 - __main__ - ERROR - Telethon search error for telugu movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:51,012 - __main__ - ERROR - Failed to search telugu movies after 5 attempts
2025-04-24 15:04:51,012 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:51,012 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:51,012 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810834772136824 to SearchRequest (144b4462a80)
2025-04-24 15:04:51,013 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:51,013 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:51,013 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:51,217 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810834772136824
2025-04-24 15:04:51,217 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:51,217 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810835593064444 to MsgsAck (144b444e9c0)
2025-04-24 15:04:51,217 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:51,218 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:51,218 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:51,218 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810835597041264 to MsgsAck (144b4461280)
2025-04-24 15:04:51,218 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:51,219 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:51,219 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:51,219 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:52,227 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810839927576800 to SearchRequest (144b4462990)
2025-04-24 15:04:52,227 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:52,228 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:52,229 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:52,437 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810839927576800
2025-04-24 15:04:52,437 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:52,437 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810840766680496 to MsgsAck (144b444e9c0)
2025-04-24 15:04:52,438 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:52,439 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:52,439 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:52,439 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810840774709480 to MsgsAck (144b4624f80)
2025-04-24 15:04:52,439 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:52,440 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:52,441 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:52,441 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:54,452 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810849418194792 to SearchRequest (144b4462840)
2025-04-24 15:04:54,452 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:54,453 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:54,453 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:54,616 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810849418194792
2025-04-24 15:04:54,617 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:54,617 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810850077088380 to MsgsAck (144b444e9c0)
2025-04-24 15:04:54,618 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:54,618 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:54,619 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:54,619 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810850085086844 to MsgsAck (144b4624f20)
2025-04-24 15:04:54,619 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:54,619 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:54,620 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:54,620 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:58,625 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810867289807828 to SearchRequest (144b44625d0)
2025-04-24 15:04:58,625 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:04:58,626 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:58,626 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:58,667 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:04:58,668 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:04:58,668 - telegram._bot - DEBUG - []
2025-04-24 15:04:58,668 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:04:58,669 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:04:58,856 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810867289807828
2025-04-24 15:04:58,856 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:04:58,856 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810868213200124 to MsgsAck (144b4625160)
2025-04-24 15:04:58,856 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:58,857 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:58,857 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:04:58,857 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810868217194112 to MsgsAck (144b4624c50)
2025-04-24 15:04:58,858 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:04:58,859 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:04:58,859 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:04:58,859 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:06,868 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810902621624520 to SearchRequest (144b4462600)
2025-04-24 15:05:06,868 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:06,869 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:06,870 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:07,057 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810902621624520
2025-04-24 15:05:07,058 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:07,058 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810903677802256 to MsgsAck (144b46258e0)
2025-04-24 15:05:07,058 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:07,059 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:07,059 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:07,059 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810903682123356 to MsgsAck (144b4625880)
2025-04-24 15:05:07,059 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:07,060 - __main__ - ERROR - Telethon search error for english movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:07,060 - __main__ - ERROR - Failed to search english movies after 5 attempts
2025-04-24 15:05:07,061 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:07,061 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:07,061 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810903689660244 to SearchRequest (144b4463380)
2025-04-24 15:05:07,061 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:07,062 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:07,062 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:07,261 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810903689660244
2025-04-24 15:05:07,261 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:07,261 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810904489309484 to MsgsAck (144b4625cd0)
2025-04-24 15:05:07,261 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:07,262 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:07,262 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:07,262 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810904493322544 to MsgsAck (144b4625c70)
2025-04-24 15:05:07,262 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:07,263 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:07,263 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:07,263 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:08,268 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810908811981016 to SearchRequest (144b44638c0)
2025-04-24 15:05:08,268 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:08,269 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:08,269 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:08,461 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810908811981016
2025-04-24 15:05:08,461 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:08,462 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810909587909516 to MsgsAck (144b4625f40)
2025-04-24 15:05:08,462 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:08,462 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:08,462 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:08,463 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810909591912084 to MsgsAck (144b4625d60)
2025-04-24 15:05:08,463 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:08,463 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:08,464 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:08,464 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:08,871 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:05:08,872 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:05:08,872 - telegram._bot - DEBUG - []
2025-04-24 15:05:08,872 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:05:08,872 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:05:10,462 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810918178138792 to SearchRequest (144b46264b0)
2025-04-24 15:05:10,462 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:10,463 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:10,463 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:10,659 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810918178138792
2025-04-24 15:05:10,659 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:10,659 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810918964486180 to MsgsAck (144b4625c10)
2025-04-24 15:05:10,659 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:10,660 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:10,660 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:10,660 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810918968499244 to MsgsAck (144b4625ac0)
2025-04-24 15:05:10,661 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:10,661 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:10,662 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:10,662 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:14,675 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810936208140916 to SearchRequest (144b4463fe0)
2025-04-24 15:05:14,675 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:14,676 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:14,677 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:14,863 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810936208140916
2025-04-24 15:05:14,864 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:14,864 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810936965200968 to MsgsAck (144b4626a50)
2025-04-24 15:05:14,864 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:14,865 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:14,865 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:14,865 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810936969210216 to MsgsAck (144b46269f0)
2025-04-24 15:05:14,865 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:14,866 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:14,866 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:14,866 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:19,483 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:05:19,483 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:05:19,483 - telegram._bot - DEBUG - []
2025-04-24 15:05:19,484 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:05:19,484 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:05:22,863 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810971323506920 to SearchRequest (144b43d9f70)
2025-04-24 15:05:22,864 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:22,864 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:22,864 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:23,056 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810971323506920
2025-04-24 15:05:23,057 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:23,057 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810972390771120 to MsgsAck (144b4463470)
2025-04-24 15:05:23,057 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:23,057 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:23,057 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:23,057 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810972392987460 to MsgsAck (144b4463650)
2025-04-24 15:05:23,057 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:23,059 - __main__ - ERROR - Telethon search error for hindi movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:23,059 - __main__ - ERROR - Failed to search hindi movies after 5 attempts
2025-04-24 15:05:23,060 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:23,060 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:23,060 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810972403178424 to SearchRequest (144b4462a80)
2025-04-24 15:05:23,060 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:23,061 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:23,061 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:23,248 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810972403178424
2025-04-24 15:05:23,248 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:23,249 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810973160974708 to MsgsAck (144b44625d0)
2025-04-24 15:05:23,249 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:23,250 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:23,250 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:23,250 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810973165514200 to MsgsAck (144b4463380)
2025-04-24 15:05:23,250 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:23,251 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:23,251 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:23,251 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:24,266 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810977525401920 to SearchRequest (144b4463e60)
2025-04-24 15:05:24,266 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:24,267 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:24,268 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:24,454 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810977525401920
2025-04-24 15:05:24,455 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:24,455 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810978280059668 to MsgsAck (144b4463aa0)
2025-04-24 15:05:24,455 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:24,456 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:24,456 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:24,456 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810978283949704 to MsgsAck (144b4463c80)
2025-04-24 15:05:24,457 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:24,457 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:24,458 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:24,458 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:26,468 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810986921191312 to SearchRequest (144b4463d70)
2025-04-24 15:05:26,468 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:26,469 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:26,469 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:26,649 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496810986921191312
2025-04-24 15:05:26,649 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:26,650 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810987645262812 to MsgsAck (144b44638c0)
2025-04-24 15:05:26,650 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:26,650 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:26,650 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:26,650 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496810987649279688 to MsgsAck (144b4463c50)
2025-04-24 15:05:26,651 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:26,651 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:26,652 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:26,652 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:29,670 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:05:29,672 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:05:29,672 - telegram._bot - DEBUG - []
2025-04-24 15:05:29,672 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:05:29,672 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:05:30,656 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811004853310212 to SearchRequest (144b44632c0)
2025-04-24 15:05:30,656 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:30,657 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:30,657 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:30,843 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811004853310212
2025-04-24 15:05:30,843 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:30,843 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811005600601776 to MsgsAck (144b44632f0)
2025-04-24 15:05:30,843 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:30,843 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:30,844 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:30,844 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811005604693992 to MsgsAck (144b44637d0)
2025-04-24 15:05:30,844 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:30,844 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:30,845 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:30,845 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:38,845 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811039969783428 to SearchRequest (144b4462e70)
2025-04-24 15:05:38,845 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:05:38,846 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:38,846 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:39,234 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811039969783428
2025-04-24 15:05:39,234 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:39,234 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811041820312744 to MsgsAck (144b44630b0)
2025-04-24 15:05:39,234 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:39,235 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:39,236 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:39,236 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811041828519112 to MsgsAck (144b4461040)
2025-04-24 15:05:39,236 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:39,237 - __main__ - ERROR - Telethon search error for tamil movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:39,237 - __main__ - ERROR - Failed to search tamil movies after 5 attempts
2025-04-24 15:05:39,237 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:39,237 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:39,237 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811041832324272 to SearchRequest (144b4462540)
2025-04-24 15:05:39,237 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:39,238 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:39,239 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:39,526 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811041832324272
2025-04-24 15:05:39,527 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:39,527 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811042991483932 to MsgsAck (144b4463440)
2025-04-24 15:05:39,528 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:39,529 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:39,529 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:39,529 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811042999483352 to MsgsAck (144b4462e40)
2025-04-24 15:05:39,529 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:39,530 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:39,531 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:39,531 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:39,864 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:05:39,864 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:05:39,864 - telegram._bot - DEBUG - []
2025-04-24 15:05:39,864 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:05:39,864 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:05:40,540 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811047340016252 to SearchRequest (144b44624b0)
2025-04-24 15:05:40,541 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:40,541 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:40,541 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:40,709 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811047340016252
2025-04-24 15:05:40,710 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:40,710 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811048018216976 to MsgsAck (144b4461970)
2025-04-24 15:05:40,710 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:40,711 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:40,711 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:40,711 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811048022210964 to MsgsAck (144b44626f0)
2025-04-24 15:05:40,711 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:40,712 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:40,712 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:40,712 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:42,716 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811056633265628 to SearchRequest (144b44616d0)
2025-04-24 15:05:42,716 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:42,717 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:42,717 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:42,896 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811056633265628
2025-04-24 15:05:42,896 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:42,896 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811057353221072 to MsgsAck (144b4462390)
2025-04-24 15:05:42,897 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:42,897 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:42,898 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:42,898 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811057361223352 to MsgsAck (144b44615e0)
2025-04-24 15:05:42,899 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:42,899 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:42,899 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:42,900 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:46,059 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811071183649680 to PingRequest (144b4461df0)
2025-04-24 15:05:46,059 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:05:46,059 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:46,060 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:46,234 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496811071183649680
2025-04-24 15:05:46,235 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:46,904 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811074563881536 to SearchRequest (144b4462870)
2025-04-24 15:05:46,904 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:46,905 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:46,905 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:46,905 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811074567956588 to MsgsAck (144b4460260)
2025-04-24 15:05:46,905 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:46,906 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:46,906 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:47,075 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811074563881536
2025-04-24 15:05:47,075 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:47,075 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811075545647884 to MsgsAck (144b44612e0)
2025-04-24 15:05:47,075 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:47,076 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:47,076 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:47,076 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811075549640916 to MsgsAck (144b4460920)
2025-04-24 15:05:47,076 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:47,077 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:47,077 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:47,077 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:50,051 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:05:50,052 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:05:50,053 - telegram._bot - DEBUG - []
2025-04-24 15:05:50,053 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:05:50,053 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:05:55,089 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811109960264484 to SearchRequest (144b4462090)
2025-04-24 15:05:55,090 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:55,090 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:55,091 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:55,294 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811109960264484
2025-04-24 15:05:55,294 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:55,294 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811110778384488 to MsgsAck (144b4461c40)
2025-04-24 15:05:55,294 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:55,295 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:55,295 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:55,296 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811110786454480 to MsgsAck (144b4462390)
2025-04-24 15:05:55,296 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:55,297 - __main__ - ERROR - Telethon search error for web series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:55,297 - __main__ - ERROR - Failed to search web series after 5 attempts
2025-04-24 15:05:55,297 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:55,298 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:55,298 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811110794041912 to SearchRequest (144b4461340)
2025-04-24 15:05:55,298 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:05:55,299 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:55,299 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:55,505 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811110794041912
2025-04-24 15:05:55,506 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:55,506 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811111627712528 to MsgsAck (144b44622d0)
2025-04-24 15:05:55,506 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:55,507 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:55,507 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:55,507 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811111632198612 to MsgsAck (144b4460bc0)
2025-04-24 15:05:55,508 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:55,510 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:55,510 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:55,511 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:55,845 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:05:55,846 - telegram._bot - DEBUG - Getting updates: [954247041]
2025-04-24 15:05:55,847 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000144B4323700>]
2025-04-24 15:05:55,847 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:05:55,847 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:05:56,517 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811115964980048 to SearchRequest (144b4460c50)
2025-04-24 15:05:56,517 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:05:56,518 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:56,518 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:56,700 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811115964980048
2025-04-24 15:05:56,700 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:56,700 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811116697306556 to MsgsAck (144b4461d00)
2025-04-24 15:05:56,700 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:56,701 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:56,701 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:56,702 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811116701294824 to MsgsAck (144b4461cd0)
2025-04-24 15:05:56,702 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:56,703 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:56,704 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:56,704 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:58,706 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811125312064340 to SearchRequest (144b4460530)
2025-04-24 15:05:58,706 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:05:58,707 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:58,707 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:58,875 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811125312064340
2025-04-24 15:05:58,875 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:05:58,875 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811125988643812 to MsgsAck (144b44604a0)
2025-04-24 15:05:58,875 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:58,875 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:58,875 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:05:58,875 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811125988643816 to MsgsAck (144b44605c0)
2025-04-24 15:05:58,875 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:05:58,876 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:05:58,876 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:05:58,876 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:02,886 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811143214098628 to SearchRequest (144b4460d10)
2025-04-24 15:06:02,887 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:06:02,887 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:02,887 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:03,117 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811143214098628
2025-04-24 15:06:03,117 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:03,117 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811144433240236 to MsgsAck (144b44604d0)
2025-04-24 15:06:03,118 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:03,118 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:03,118 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:03,119 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811144440843880 to MsgsAck (144b44608f0)
2025-04-24 15:06:03,119 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:03,119 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:03,120 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:03,120 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:06,049 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:06:06,049 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:06:06,049 - telegram._bot - DEBUG - []
2025-04-24 15:06:06,049 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:06:06,049 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:06:11,120 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811178801762896 to SearchRequest (144b444fe00)
2025-04-24 15:06:11,120 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:06:11,121 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:11,121 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:11,294 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811178801762896
2025-04-24 15:06:11,295 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:11,295 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811179504803020 to MsgsAck (144b4460890)
2025-04-24 15:06:11,295 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:11,295 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:11,296 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:11,296 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811179508791284 to MsgsAck (144b44611f0)
2025-04-24 15:06:11,296 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:11,297 - __main__ - ERROR - Telethon search error for books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:11,297 - __main__ - ERROR - Failed to search books after 5 attempts
2025-04-24 15:06:11,298 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:11,298 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:11,298 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811179513452844 to SearchRequest (144b4460ce0)
2025-04-24 15:06:11,298 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:11,298 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:11,298 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:11,484 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811179513452844
2025-04-24 15:06:11,484 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:11,484 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811180259224252 to MsgsAck (144b4460890)
2025-04-24 15:06:11,485 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:11,485 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:11,485 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:11,485 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811180263223012 to MsgsAck (144b4460da0)
2025-04-24 15:06:11,485 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:11,485 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:11,486 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:11,486 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:12,500 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811184619708020 to SearchRequest (144b44626f0)
2025-04-24 15:06:12,500 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:12,502 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:12,502 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:12,713 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811184619708020
2025-04-24 15:06:12,714 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:12,714 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811185473645172 to MsgsAck (144b4460890)
2025-04-24 15:06:12,714 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:12,715 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:12,715 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:12,715 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811185477714500 to MsgsAck (144b4462e40)
2025-04-24 15:06:12,715 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:12,716 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:12,716 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:12,716 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:14,730 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811194125945296 to SearchRequest (144b44615e0)
2025-04-24 15:06:14,730 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:14,731 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:14,731 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:14,963 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811194125945296
2025-04-24 15:06:14,963 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:14,963 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811195058082784 to MsgsAck (144b4460890)
2025-04-24 15:06:14,963 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:14,964 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:14,964 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:14,964 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811195064136708 to MsgsAck (144b444c890)
2025-04-24 15:06:14,964 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:14,965 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:14,965 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:14,965 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:16,241 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:06:16,242 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:06:16,242 - telegram._bot - DEBUG - []
2025-04-24 15:06:16,242 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:06:16,242 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:06:17,020 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:06:17,021 - telegram._bot - DEBUG - Getting updates: [954247042]
2025-04-24 15:06:17,021 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000144B4323C40>]
2025-04-24 15:06:17,021 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:06:17,021 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:06:18,305 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:06:18,306 - telegram._bot - DEBUG - Getting updates: [954247043]
2025-04-24 15:06:18,306 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000144B4322F80>]
2025-04-24 15:06:18,307 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:06:18,307 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:06:18,969 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811212265052532 to SearchRequest (144b46246b0)
2025-04-24 15:06:18,969 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:18,971 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:18,971 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:19,229 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811212265052532
2025-04-24 15:06:19,229 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:19,230 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811213601436948 to MsgsAck (144b444f5c0)
2025-04-24 15:06:19,230 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:19,231 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:19,231 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:19,231 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811213605052328 to MsgsAck (144b444f3e0)
2025-04-24 15:06:19,231 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:19,232 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:19,233 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:19,233 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:27,236 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811247981427544 to SearchRequest (144b4460920)
2025-04-24 15:06:27,236 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:27,243 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:27,243 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:27,423 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811247981427544
2025-04-24 15:06:27,423 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:27,423 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811248733809824 to MsgsAck (144b444f5c0)
2025-04-24 15:06:27,423 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:27,424 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:27,424 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:27,424 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811248737808580 to MsgsAck (144b444f560)
2025-04-24 15:06:27,424 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:27,425 - __main__ - ERROR - Telethon search error for medical books: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:27,425 - __main__ - ERROR - Failed to search medical books after 5 attempts
2025-04-24 15:06:27,425 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:27,425 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:27,425 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811248741808288 to SearchRequest (144b4462390)
2025-04-24 15:06:27,425 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:27,426 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:27,426 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:27,600 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811248741808288
2025-04-24 15:06:27,600 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:27,600 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811249443504684 to MsgsAck (144b444f5c0)
2025-04-24 15:06:27,600 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:27,600 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:27,600 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:27,600 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811249443504688 to MsgsAck (144b444fe60)
2025-04-24 15:06:27,600 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:27,602 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:27,603 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:27,603 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:28,489 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:06:28,490 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:06:28,490 - telegram._bot - DEBUG - []
2025-04-24 15:06:28,490 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:06:28,491 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:06:28,612 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811253783669468 to SearchRequest (144b4624e60)
2025-04-24 15:06:28,612 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:28,612 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:28,612 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:28,793 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811253783669468
2025-04-24 15:06:28,793 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:28,793 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811254510558124 to MsgsAck (144b4625760)
2025-04-24 15:06:28,793 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:28,794 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:28,794 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:28,794 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811254514601704 to MsgsAck (144b4625f10)
2025-04-24 15:06:28,794 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:28,794 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:28,795 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:28,795 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:30,796 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811263110920192 to SearchRequest (144b4461cd0)
2025-04-24 15:06:30,796 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:30,797 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:30,797 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:30,982 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811263110920192
2025-04-24 15:06:30,982 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:30,982 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811263855836156 to MsgsAck (144b4624bc0)
2025-04-24 15:06:30,983 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:30,983 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:30,983 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:30,983 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811263859843492 to MsgsAck (144b4624980)
2025-04-24 15:06:30,983 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:30,984 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:30,984 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:30,984 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:35,000 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811281400619876 to SearchRequest (144b44605c0)
2025-04-24 15:06:35,000 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:35,000 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:35,000 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:35,173 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811281400619876
2025-04-24 15:06:35,174 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:35,174 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811282098197352 to MsgsAck (144b4624170)
2025-04-24 15:06:35,174 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:35,174 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:35,174 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:35,174 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811282098197356 to MsgsAck (144b4624920)
2025-04-24 15:06:35,174 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:35,175 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:35,175 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:35,175 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:38,669 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:06:38,670 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:06:38,670 - telegram._bot - DEBUG - []
2025-04-24 15:06:38,670 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:06:38,670 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:06:43,186 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811316506102952 to SearchRequest (144b4627290)
2025-04-24 15:06:43,186 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:43,186 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:43,187 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:43,377 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811316506102952
2025-04-24 15:06:43,377 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:43,377 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811317271935852 to MsgsAck (144b4624860)
2025-04-24 15:06:43,377 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:43,379 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:43,379 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:43,379 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811317275957496 to MsgsAck (144b4624b30)
2025-04-24 15:06:43,379 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:43,379 - __main__ - ERROR - Telethon search error for movie download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:43,379 - __main__ - ERROR - Failed to search movie download after 5 attempts
2025-04-24 15:06:43,379 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:43,379 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:43,379 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811317279544264 to SearchRequest (144b44611f0)
2025-04-24 15:06:43,380 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:43,380 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:43,380 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:43,559 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811317279544264
2025-04-24 15:06:43,560 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:43,560 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811318003453644 to MsgsAck (144b4627890)
2025-04-24 15:06:43,560 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:43,561 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:43,561 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:43,561 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811318007044228 to MsgsAck (144b4627830)
2025-04-24 15:06:43,561 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:43,562 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:43,562 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:43,562 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:44,567 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811322324935944 to SearchRequest (144b4460da0)
2025-04-24 15:06:44,567 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:44,568 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:44,568 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:44,769 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811322324935944
2025-04-24 15:06:44,769 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:44,769 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811323133527788 to MsgsAck (144b46240e0)
2025-04-24 15:06:44,769 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:44,770 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:44,770 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:44,770 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811323137887032 to MsgsAck (144b46276e0)
2025-04-24 15:06:44,771 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:44,771 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:44,772 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:44,772 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:46,060 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811328885760584 to PingRequest (144b4462030)
2025-04-24 15:06:46,061 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:06:46,061 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:46,061 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:46,229 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496811328885760584
2025-04-24 15:06:46,229 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:46,788 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811331798645296 to SearchRequest (144b4627740)
2025-04-24 15:06:46,789 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 40 bytes for sending
2025-04-24 15:06:46,789 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:46,790 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:46,790 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811331805747308 to MsgsAck (144b4462030)
2025-04-24 15:06:46,790 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:46,791 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:46,791 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:46,990 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496811331798645296
2025-04-24 15:06:46,991 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:06:46,991 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811332609768188 to MsgsAck (144b444c890)
2025-04-24 15:06:46,991 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:46,992 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:46,992 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:06:46,992 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496811332614116944 to MsgsAck (144b4461970)
2025-04-24 15:06:46,992 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:06:46,993 - __main__ - ERROR - Telethon search error for series download: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:06:46,993 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:06:46,993 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:09:51,609 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 15:09:51,610 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 15:09:52,542 - __main__ - INFO - Bot polling started...
2025-04-24 15:09:52,542 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 15:09:53,220 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 15:09:53,220 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 15:09:53,221 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 15:09:53,221 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 15:09:53,221 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 15:09:53,221 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 15:09:53,221 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 15:09:53,221 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 15:09:53,398 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 15:09:53,399 - telegram._bot - DEBUG - True
2025-04-24 15:09:53,399 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 15:09:53,399 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 15:09:53,399 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 15:09:53,399 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 15:09:53,399 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 15:09:53,399 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:09:53,400 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 15:09:53,401 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 15:09:53,401 - telegram.ext._application - INFO - Application started
2025-04-24 15:09:53,401 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 15:09:53,402 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 15:10:02,425 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:10:02,426 - telegram._bot - DEBUG - Getting updates: [954247044]
2025-04-24 15:10:02,426 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000194E00AE140>]
2025-04-24 15:10:02,426 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:10:02,427 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:10:02,428 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247044, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 95, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487603, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 15:10:02,428 - __main__ - INFO - Received /start command
2025-04-24 15:10:02,428 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:10:03,184 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:10:03,186 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 180}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 96, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487604, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:10:03,187 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:10:12,619 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:10:12,620 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:10:12,620 - telegram._bot - DEBUG - []
2025-04-24 15:10:12,620 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:10:12,620 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:10:14,214 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:10:14,214 - telegram._bot - DEBUG - Getting updates: [954247045]
2025-04-24 15:10:14,215 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000194E00AE740>]
2025-04-24 15:10:14,215 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:10:14,215 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:10:14,217 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247045, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Inception', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 97, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487615, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 15:10:14,218 - __main__ - INFO - Received message: inception
2025-04-24 15:10:14,219 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:10:14,946 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:10:14,947 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:inception', 'text': 'Movie'}, {'callback_data': 'series:inception', 'text': 'Series'}, {'callback_data': 'pdf:inception', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'inception' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 98, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487615, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:10:14,948 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:10:24,394 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:10:24,395 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:10:24,395 - telegram._bot - DEBUG - []
2025-04-24 15:10:24,396 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:10:24,396 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:10:34,163 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:10:34,164 - telegram._bot - DEBUG - Getting updates: [954247046]
2025-04-24 15:10:34,164 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000194E00AEA40>]
2025-04-24 15:10:34,164 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:10:34,164 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:10:34,165 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:inception', 'text': 'Movie'}, {'callback_data': 'series:inception', 'text': 'Series'}, {'callback_data': 'pdf:inception', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'inception' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 98, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487615, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488945900215262', 'data': 'movie:inception', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247046}
2025-04-24 15:10:34,166 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 15:10:34,923 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 15:10:34,924 - telegram._bot - DEBUG - True
2025-04-24 15:10:34,924 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 15:10:34,924 - __main__ - INFO - Searching movie: inception
2025-04-24 15:10:34,924 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=inception&page=1&include_adult=false
2025-04-24 15:10:34,926 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:10:35,139 - __main__ - ERROR - TMDB request error on attempt 1: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2025-04-24 15:10:36,142 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:10:36,287 - __main__ - ERROR - TMDB request error on attempt 2: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2025-04-24 15:10:38,304 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:10:38,517 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=inception&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 15:10:38,518 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 15:10:38,518 - __main__ - INFO - TMDB found 2 results for inception
2025-04-24 15:10:38,520 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 15:10:39,238 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=inception+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 15:10:39,240 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:10:39,363 - __main__ - WARNING - Genre fetch failed, retrying 1...
2025-04-24 15:10:41,363 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:10:41,482 - __main__ - WARNING - Genre fetch failed, retrying 2...
2025-04-24 15:10:43,488 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:10:43,580 - __main__ - WARNING - Genre fetch failed, retrying 3...
2025-04-24 15:10:44,354 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:10:44,355 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:10:44,355 - telegram._bot - DEBUG - []
2025-04-24 15:10:44,355 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:10:44,355 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:10:46,133 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 15:10:47,213 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 15:10:47,228 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 15:10:47,228 - __main__ - INFO - Discovering groups across Telegram...
2025-04-24 15:10:47,229 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 15:10:47,229 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 15:10:47,229 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 15:10:47,408 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 15:10:47,409 - telethon.network.mtprotosender - DEBUG - New auth_key attempt 1...
2025-04-24 15:10:49,006 - telethon.network.mtprotosender - DEBUG - auth_key generation success!
2025-04-24 15:10:49,006 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 15:10:49,006 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 15:10:49,006 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 15:10:49,014 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:49,015 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812368088639368 to InvokeWithLayerRequest (194e02327e0)
2025-04-24 15:10:49,015 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 15:10:49,016 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:49,016 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:49,016 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:49,637 - telethon.network.mtprotostate - DEBUG - Updated time offset (old offset 0, bad 7496812370576307404, good 7496812375501858817, new 1)
2025-04-24 15:10:49,638 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496812368088639368
2025-04-24 15:10:49,638 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 15:10:49,638 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:49,638 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812374875245800 to InvokeWithLayerRequest (194e02327e0)
2025-04-24 15:10:49,638 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 15:10:49,639 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:49,639 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:49,639 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812374879323712 to MsgsAck (194e02328d0)
2025-04-24 15:10:49,639 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:49,640 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:49,640 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:49,815 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 15:10:49,815 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 15:10:49,815 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496812374875245800]
2025-04-24 15:10:49,815 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:49,865 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496812374875245800
2025-04-24 15:10:49,865 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:49,866 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812375787165396 to GetUsersRequest (194e0231850)
2025-04-24 15:10:49,866 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:10:49,866 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:49,866 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:49,866 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812375787165400 to MsgsAck (194de989640)
2025-04-24 15:10:49,866 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 15:10:49,867 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:49,867 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:50,090 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496812375787165396
2025-04-24 15:10:50,091 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:50,091 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812376982718820 to MsgsAck (194e0233440)
2025-04-24 15:10:50,091 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:50,092 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:50,092 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:50,092 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812376986719484 to MsgsAck (194e0232330)
2025-04-24 15:10:50,092 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:50,093 - __main__ - INFO - Client connected successfully
2025-04-24 15:10:50,093 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:10:50,094 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:50,094 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:50,445 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:10:50,446 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Entire Telegram lo groups chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 100, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745487651, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:10:50,447 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:10:50,447 - __main__ - INFO - Loaded 0 cached groups
2025-04-24 15:10:50,447 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812378408122412 to SearchRequest (194e0233a70)
2025-04-24 15:10:50,447 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:10:50,448 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:50,448 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:50,694 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496812378408122412
2025-04-24 15:10:50,694 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:50,695 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812379397473684 to MsgsAck (194de6c5e80)
2025-04-24 15:10:50,695 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:50,695 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:50,696 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:50,696 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812379401653640 to MsgsAck (194e0233b90)
2025-04-24 15:10:50,696 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:50,697 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:10:50,697 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:50,697 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:51,704 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812383731033320 to SearchRequest (194de6c5e80)
2025-04-24 15:10:51,704 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:10:51,705 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:51,705 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:52,047 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496812383731033320
2025-04-24 15:10:52,047 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:52,048 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812385402496932 to MsgsAck (194e0233a10)
2025-04-24 15:10:52,048 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:52,049 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:52,049 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:52,049 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812385406492828 to MsgsAck (194e0232300)
2025-04-24 15:10:52,049 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:52,050 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:10:52,050 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:52,050 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:54,058 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812394029254796 to SearchRequest (194e0233a10)
2025-04-24 15:10:54,058 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:10:54,059 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:54,059 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:54,234 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496812394029254796
2025-04-24 15:10:54,234 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:54,234 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812394732855680 to MsgsAck (194e0233c80)
2025-04-24 15:10:54,234 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:54,235 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:54,235 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:54,235 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812394736860160 to MsgsAck (194e00ec290)
2025-04-24 15:10:54,235 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:54,236 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:10:54,236 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:54,236 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:54,524 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:10:54,525 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:10:54,525 - telegram._bot - DEBUG - []
2025-04-24 15:10:54,525 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:10:54,525 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:10:58,249 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812411973444352 to SearchRequest (194e02505f0)
2025-04-24 15:10:58,249 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:10:58,250 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:58,250 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:58,434 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496812411973444352
2025-04-24 15:10:58,434 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:10:58,435 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812412719170940 to MsgsAck (194e00ec830)
2025-04-24 15:10:58,435 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:58,436 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:58,436 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:10:58,436 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812412721652400 to MsgsAck (194e00ec620)
2025-04-24 15:10:58,436 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:10:58,437 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:10:58,437 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:10:58,438 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:11:04,728 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:11:04,729 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:11:04,729 - telegram._bot - DEBUG - []
2025-04-24 15:11:04,730 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:11:04,730 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:11:06,457 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812447165357024 to SearchRequest (194e0251310)
2025-04-24 15:11:06,457 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:11:06,457 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:11:06,457 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:11:06,632 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496812447165357024
2025-04-24 15:11:06,632 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:11:06,632 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812447866684348 to MsgsAck (194e02507d0)
2025-04-24 15:11:06,632 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:11:06,633 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:11:06,633 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:11:06,633 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496812447869006544 to MsgsAck (194e0250530)
2025-04-24 15:11:06,633 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:11:06,633 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:11:06,633 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:11:06,633 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:37,115 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 15:16:37,116 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 15:16:38,060 - __main__ - INFO - Bot polling started...
2025-04-24 15:16:38,060 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 15:16:38,747 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 15:16:38,748 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 15:16:38,748 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 15:16:38,748 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 15:16:38,748 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 15:16:38,748 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 15:16:38,748 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 15:16:38,748 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 15:16:38,921 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 15:16:38,922 - telegram._bot - DEBUG - True
2025-04-24 15:16:38,922 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 15:16:38,922 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 15:16:38,922 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 15:16:38,922 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 15:16:38,922 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 15:16:38,922 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:16:38,923 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 15:16:38,923 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 15:16:38,923 - telegram.ext._application - INFO - Application started
2025-04-24 15:16:38,923 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 15:16:38,923 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 15:16:50,479 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:16:50,480 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:16:50,480 - telegram._bot - DEBUG - []
2025-04-24 15:16:50,480 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:16:50,480 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:16:50,659 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:16:50,660 - telegram._bot - DEBUG - Getting updates: [954247047]
2025-04-24 15:16:50,660 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C11729A80>]
2025-04-24 15:16:50,661 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:16:50,661 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:16:50,662 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247047, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Devara', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 101, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745488011, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 15:16:50,663 - __main__ - INFO - Received message: devara
2025-04-24 15:16:50,664 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:16:51,431 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:16:51,433 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 102, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745488012, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:16:51,433 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:16:54,185 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:16:54,186 - telegram._bot - DEBUG - Getting updates: [954247048]
2025-04-24 15:16:54,186 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C1172A680>]
2025-04-24 15:16:54,187 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:16:54,187 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:16:54,188 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 102, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745488012, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488946845620073', 'data': 'movie:devara', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247048}
2025-04-24 15:16:54,188 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 15:16:54,550 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 15:16:54,551 - telegram._bot - DEBUG - True
2025-04-24 15:16:54,551 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 15:16:54,551 - __main__ - INFO - Searching movie: devara
2025-04-24 15:16:54,551 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false
2025-04-24 15:16:54,553 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:16:54,701 - __main__ - ERROR - TMDB request error on attempt 1: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2025-04-24 15:16:55,715 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:16:55,924 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 15:16:55,925 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 15:16:55,925 - __main__ - INFO - TMDB found 12 results for devara
2025-04-24 15:16:55,927 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 15:16:56,674 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=devara+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 15:16:56,677 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 15:16:56,803 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 15:16:57,359 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 15:16:58,134 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 15:16:58,147 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 15:16:58,147 - __main__ - INFO - Discovering groups across Telegram...
2025-04-24 15:16:58,148 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 15:16:58,148 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 15:16:58,148 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 15:16:58,333 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 15:16:58,333 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 15:16:58,333 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 15:16:58,333 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 15:16:58,342 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:58,343 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813954240489592 to InvokeWithLayerRequest (10c11732b40)
2025-04-24 15:16:58,343 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 15:16:58,344 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:58,344 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:58,344 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:16:58,539 - telethon.network.mtprotostate - DEBUG - Updated time offset (old offset 0, bad 7496813955028042424, good 7496813959905723393, new 1)
2025-04-24 15:16:58,539 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496813954240489592
2025-04-24 15:16:58,539 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 15:16:58,539 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:16:58,540 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813959326993216 to InvokeWithLayerRequest (10c11732b40)
2025-04-24 15:16:58,540 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 15:16:58,541 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:58,541 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:58,541 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813959330985300 to MsgsAck (10c7f231880)
2025-04-24 15:16:58,541 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:16:58,542 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:58,542 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:58,723 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 15:16:58,723 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 15:16:58,723 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496813959326993216]
2025-04-24 15:16:58,723 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:16:58,754 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496813959326993216
2025-04-24 15:16:58,755 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:16:58,755 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813960187130204 to GetUsersRequest (10c1187cb30)
2025-04-24 15:16:58,755 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:16:58,755 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:58,756 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:58,756 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813960191123236 to MsgsAck (10c100ddb80)
2025-04-24 15:16:58,756 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 15:16:58,756 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:58,756 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:58,941 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496813960187130204
2025-04-24 15:16:58,943 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:16:58,943 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813960937212220 to MsgsAck (10c7fa4cd70)
2025-04-24 15:16:58,943 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:16:58,944 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:58,944 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:58,944 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813960941163292 to MsgsAck (10c118a44d0)
2025-04-24 15:16:58,944 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:16:58,945 - __main__ - INFO - Client connected successfully
2025-04-24 15:16:58,945 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:16:58,947 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:58,947 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:59,365 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:16:59,366 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Entire Telegram lo groups chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 104, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745488020, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:16:59,366 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:16:59,366 - __main__ - INFO - Loaded 0 cached groups
2025-04-24 15:16:59,366 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813962924941892 to SearchRequest (10c118a5190)
2025-04-24 15:16:59,366 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:16:59,366 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:59,366 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:59,546 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496813962924941892
2025-04-24 15:16:59,546 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:16:59,546 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813963647167080 to MsgsAck (10c7f7a69f0)
2025-04-24 15:16:59,546 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:16:59,547 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:59,547 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:16:59,547 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813963651509160 to MsgsAck (10c118a40e0)
2025-04-24 15:16:59,547 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:16:59,548 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:16:59,548 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:16:59,548 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:00,556 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813967978994840 to SearchRequest (10c7f7a69f0)
2025-04-24 15:17:00,557 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:17:00,558 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:00,558 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:00,779 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496813967978994840
2025-04-24 15:17:00,779 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:17:00,779 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813968873906608 to MsgsAck (10c118a50a0)
2025-04-24 15:17:00,780 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:00,780 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:00,780 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:00,780 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813968877954000 to MsgsAck (10c118a5160)
2025-04-24 15:17:00,781 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:00,782 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:17:00,782 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:00,782 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:02,789 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813977504515408 to SearchRequest (10c118a4710)
2025-04-24 15:17:02,789 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:17:02,790 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:02,790 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:02,984 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496813977504515408
2025-04-24 15:17:02,985 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:17:02,985 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813978288408996 to MsgsAck (10c118a5460)
2025-04-24 15:17:02,985 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:02,986 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:02,986 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:02,986 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813978292158840 to MsgsAck (10c118a54c0)
2025-04-24 15:17:02,986 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:02,987 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:17:02,987 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:02,988 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:04,378 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:04,379 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:17:04,379 - telegram._bot - DEBUG - []
2025-04-24 15:17:04,379 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:04,379 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:07,000 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813995822783360 to SearchRequest (10c118a5c10)
2025-04-24 15:17:07,001 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:17:07,002 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:07,003 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:07,207 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496813995822783360
2025-04-24 15:17:07,207 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:17:07,208 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813996648023496 to MsgsAck (10c118a5070)
2025-04-24 15:17:07,208 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:07,208 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:07,208 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:07,208 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496813996652004132 to MsgsAck (10c118a5670)
2025-04-24 15:17:07,209 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:07,209 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:17:07,209 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:07,210 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:14,558 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:14,559 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:17:14,559 - telegram._bot - DEBUG - []
2025-04-24 15:17:14,559 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:14,559 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:15,212 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814031030705360 to SearchRequest (10c118a6660)
2025-04-24 15:17:15,213 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:17:15,214 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:15,214 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:15,407 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496814031030705360
2025-04-24 15:17:15,407 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:17:15,407 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814031808075816 to MsgsAck (10c118a5ca0)
2025-04-24 15:17:15,407 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:15,408 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:15,408 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:15,408 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814031812075524 to MsgsAck (10c118a60f0)
2025-04-24 15:17:15,408 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:15,408 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:17:15,409 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:15,409 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:24,760 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:24,761 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:17:24,761 - telegram._bot - DEBUG - []
2025-04-24 15:17:24,761 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:24,761 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:31,425 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814100600410408 to SearchRequest (10c118a7080)
2025-04-24 15:17:31,425 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:17:31,426 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:31,426 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:31,656 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496814100600410408
2025-04-24 15:17:31,657 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:17:31,657 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814101527871076 to MsgsAck (10c118a64b0)
2025-04-24 15:17:31,657 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:31,658 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:31,658 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:31,658 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814101531508392 to MsgsAck (10c118a6720)
2025-04-24 15:17:31,658 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:17:31,659 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:17:31,659 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:31,659 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:34,961 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:34,962 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:17:34,962 - telegram._bot - DEBUG - []
2025-04-24 15:17:34,962 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:34,962 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:37,044 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:37,045 - telegram._bot - DEBUG - Getting updates: [954247049]
2025-04-24 15:17:37,045 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C1172BF40>]
2025-04-24 15:17:37,046 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:37,046 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:46,512 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:46,513 - telegram._bot - DEBUG - Getting updates: [954247050]
2025-04-24 15:17:46,514 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C11729F00>]
2025-04-24 15:17:46,514 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:46,514 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:48,476 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:48,477 - telegram._bot - DEBUG - Getting updates: [954247051]
2025-04-24 15:17:48,477 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C1172B400>]
2025-04-24 15:17:48,477 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:48,478 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:50,693 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:50,694 - telegram._bot - DEBUG - Getting updates: [954247052]
2025-04-24 15:17:50,694 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C1172BE80>]
2025-04-24 15:17:50,695 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:50,695 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:52,057 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:17:52,057 - telegram._bot - DEBUG - Getting updates: [954247053]
2025-04-24 15:17:52,058 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C1172AD40>]
2025-04-24 15:17:52,058 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:17:52,058 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:17:58,974 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814218759749300 to PingRequest (10c11732b40)
2025-04-24 15:17:58,974 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:17:58,975 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:17:58,975 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:17:59,248 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496814218759749300
2025-04-24 15:17:59,249 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:18:02,256 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:18:02,256 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:18:02,256 - telegram._bot - DEBUG - []
2025-04-24 15:18:02,257 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:18:02,257 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:03,668 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814239011784572 to SearchRequest (10c1187df70)
2025-04-24 15:18:03,669 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:18:03,669 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:18:03,669 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:18:03,669 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814239014034288 to MsgsAck (10c11732b40)
2025-04-24 15:18:03,669 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:18:03,670 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:18:03,670 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:18:03,857 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496814239011784572
2025-04-24 15:18:03,858 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:18:03,858 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814239772222536 to MsgsAck (10c118a4170)
2025-04-24 15:18:03,858 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:18:03,859 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:18:03,859 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:18:03,859 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814239775839824 to MsgsAck (10c118a4650)
2025-04-24 15:18:03,859 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:18:03,859 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:18:03,860 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:18:03,860 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:18:12,439 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:18:12,440 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:18:12,440 - telegram._bot - DEBUG - []
2025-04-24 15:18:12,440 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:18:12,441 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:22,642 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:18:22,644 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:18:22,644 - telegram._bot - DEBUG - []
2025-04-24 15:18:22,644 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:18:22,644 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:32,838 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:18:32,839 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:18:32,839 - telegram._bot - DEBUG - []
2025-04-24 15:18:32,839 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:18:32,839 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:43,035 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:18:43,036 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:18:43,036 - telegram._bot - DEBUG - []
2025-04-24 15:18:43,036 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:18:43,036 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:55,044 - telegram.ext._updater - DEBUG - Timed out getting Updates: Timed out
2025-04-24 15:18:55,044 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:55,048 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:18:55,049 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:18:56,055 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:56,058 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:18:56,058 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:18:57,567 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:57,573 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:18:57,574 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:18:58,993 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814476532295728 to PingRequest (10c1187e5d0)
2025-04-24 15:18:58,993 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 15:18:58,994 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:18:58,995 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:18:59,837 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:18:59,840 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:18:59,841 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:19:03,224 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:19:03,227 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:19:03,227 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:19:07,871 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814514699730084 to SearchRequest (10c1187daf0)
2025-04-24 15:19:07,871 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:19:07,872 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:19:07,872 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:19:08,306 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:19:08,310 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:19:08,311 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:19:15,918 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:19:15,921 - telegram.ext._updater - ERROR - Error while getting Updates: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:19:15,921 - __main__ - ERROR - Update None caused error: httpx HTTPError: [Errno 11001] getaddrinfo failed
2025-04-24 15:19:18,355 - telethon.network.connection.connection - WARNING - Server closed the connection: [WinError 121] The semaphore timeout period has expired
2025-04-24 15:19:18,356 - telethon.network.mtprotosender - INFO - Connection closed while receiving data: [WinError 121] The semaphore timeout period has expired
2025-04-24 15:19:18,356 - telethon.network.mtprotosender - INFO - Closing current connection to begin reconnect...
2025-04-24 15:19:18,356 - telethon.network.connection.connection - INFO - <class 'OSError'> during disconnect: [WinError 121] The semaphore timeout period has expired
2025-04-24 15:19:18,357 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 15:19:18,357 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 15:19:18,360 - telethon.network.mtprotosender - WARNING - Attempt 1 at connecting failed: OSError: [WinError 1232] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 15:19:19,366 - telethon.network.mtprotosender - DEBUG - Connection attempt 2...
2025-04-24 15:19:19,367 - telethon.network.mtprotosender - WARNING - Attempt 2 at connecting failed: OSError: [WinError 1232] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 15:19:20,381 - telethon.network.mtprotosender - DEBUG - Connection attempt 3...
2025-04-24 15:19:20,382 - telethon.network.mtprotosender - WARNING - Attempt 3 at connecting failed: OSError: [WinError 1232] The network location cannot be reached. For information about network troubleshooting, see Windows Help
2025-04-24 15:19:21,385 - telethon.network.mtprotosender - DEBUG - Connection attempt 4...
2025-04-24 15:19:21,570 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 15:19:21,570 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 15:19:21,571 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 15:19:21,571 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 15:19:21,571 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:19:21,571 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814573629903748 to PingRequest (10c1187e5d0)
2025-04-24 15:19:21,571 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814573629903752 to SearchRequest (10c1187daf0)
2025-04-24 15:19:21,571 - telethon.network.mtprotosender - DEBUG - Encrypting 2 message(s) in 84 bytes for sending
2025-04-24 15:19:21,572 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:19:21,572 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:19:21,572 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:19:21,573 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814573637905076 to GetUsersRequest (10c118a5880)
2025-04-24 15:19:21,573 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 15:19:21,574 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:19:21,574 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:19:21,771 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 15:19:21,771 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 15:19:21,771 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496814573629903748
2025-04-24 15:19:21,771 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496814573629903752]
2025-04-24 15:19:21,771 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:19:21,840 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 15:19:21,840 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496814573629903752
2025-04-24 15:19:21,840 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496814573637905076]
2025-04-24 15:19:21,842 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:19:21,842 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814574714395480 to MsgsAck (10c1187d1f0)
2025-04-24 15:19:21,842 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 15:19:21,842 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:19:21,842 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:19:21,843 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814574718479112 to MsgsAck (10c1187e5d0)
2025-04-24 15:19:21,843 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 15:19:21,843 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 15:19:21,845 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496814573637905076
2025-04-24 15:19:21,845 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 15:19:21,845 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:19:21,846 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:19:21,846 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814574729446368 to MsgsAck (10c100ddb80)
2025-04-24 15:19:21,846 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496814574729446372 to MsgsAck (10c118a6b10)
2025-04-24 15:19:21,846 - telethon.network.mtprotosender - DEBUG - Encrypting 2 message(s) in 96 bytes for sending
2025-04-24 15:19:21,847 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 15:19:21,847 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 15:19:27,323 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:19:27,929 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:19:27,930 - telegram._bot - DEBUG - Getting updates: [954247054]
2025-04-24 15:19:27,930 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C1172B700>]
2025-04-24 15:19:27,931 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:19:27,931 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:19:34,864 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:19:34,865 - telegram._bot - DEBUG - Getting updates: [954247055]
2025-04-24 15:19:34,866 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x0000010C1172AF80>]
2025-04-24 15:19:34,866 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:19:34,866 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:19:53,317 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 15:19:53,318 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 15:19:54,303 - __main__ - INFO - Bot polling started...
2025-04-24 15:19:54,303 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 15:19:54,872 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 15:19:54,874 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 15:19:54,874 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 15:19:54,874 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 15:19:54,874 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 15:19:54,874 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 15:19:54,875 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 15:19:54,875 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 15:19:55,063 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 15:19:55,063 - telegram._bot - DEBUG - True
2025-04-24 15:19:55,064 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 15:19:55,064 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 15:19:55,064 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 15:19:55,064 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 15:19:55,064 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 15:19:55,064 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:19:55,065 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 15:19:55,066 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 15:19:55,066 - telegram.ext._application - INFO - Application started
2025-04-24 15:19:55,066 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 15:19:55,066 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 15:19:55,638 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:19:55,638 - telegram._bot - DEBUG - Getting updates: [954247056]
2025-04-24 15:19:55,639 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x00000249E98D8040>]
2025-04-24 15:19:55,639 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:19:55,639 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:19:55,640 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247056, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 107, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745488196, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 15:19:55,641 - __main__ - INFO - Received /start command
2025-04-24 15:19:55,641 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 15:19:56,003 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 15:19:56,003 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 180}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 108, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745488197, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 15:19:56,003 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 15:20:05,836 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:20:05,837 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:20:05,838 - telegram._bot - DEBUG - []
2025-04-24 15:20:05,838 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:20:05,838 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:20:16,044 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:20:16,045 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:20:16,045 - telegram._bot - DEBUG - []
2025-04-24 15:20:16,045 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:20:16,045 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:20:26,252 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:20:26,253 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:20:26,253 - telegram._bot - DEBUG - []
2025-04-24 15:20:26,253 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:20:26,253 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:20:36,456 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:20:36,457 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:20:36,457 - telegram._bot - DEBUG - []
2025-04-24 15:20:36,457 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:20:36,457 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:20:46,657 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:20:46,658 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:20:46,658 - telegram._bot - DEBUG - []
2025-04-24 15:20:46,658 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:20:46,658 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 15:20:56,855 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 15:20:56,855 - telegram._bot - DEBUG - No new updates found.
2025-04-24 15:20:56,855 - telegram._bot - DEBUG - []
2025-04-24 15:20:56,855 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 15:20:56,855 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:14:25,726 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 17:14:25,730 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 17:14:27,070 - __main__ - INFO - Bot polling started...
2025-04-24 17:14:27,071 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 17:14:27,818 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 17:14:27,819 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 17:14:27,819 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 17:14:27,820 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 17:14:27,820 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 17:14:27,820 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 17:14:27,820 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 17:14:27,820 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 17:14:28,012 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 17:14:28,013 - telegram._bot - DEBUG - True
2025-04-24 17:14:28,013 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 17:14:28,013 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 17:14:28,013 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 17:14:28,013 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 17:14:28,013 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 17:14:28,014 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:14:28,015 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 17:14:28,016 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 17:14:28,016 - telegram.ext._application - INFO - Application started
2025-04-24 17:14:28,016 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 17:14:28,016 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 17:14:28,587 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:14:28,587 - telegram._bot - DEBUG - Getting updates: [954247060]
2025-04-24 17:14:28,588 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001C6A74CC100>]
2025-04-24 17:14:28,588 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:14:28,588 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:14:28,588 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247060, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 119, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745491664, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 17:14:28,591 - __main__ - INFO - Received /start command
2025-04-24 17:14:28,591 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:14:29,559 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:14:29,560 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 180}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 120, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745495070, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:14:29,561 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:14:35,723 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:14:35,724 - telegram._bot - DEBUG - Getting updates: [954247061]
2025-04-24 17:14:35,724 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001C6A74CC1C0>]
2025-04-24 17:14:35,725 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:14:35,725 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:14:35,728 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247061, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 121, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745495076, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 17:14:35,732 - __main__ - INFO - Received /start command
2025-04-24 17:14:35,732 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:14:36,470 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:14:36,474 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 180}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 122, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745495077, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:14:36,476 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:14:45,933 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:14:45,934 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:14:45,934 - telegram._bot - DEBUG - []
2025-04-24 17:14:45,934 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:14:45,934 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:14:47,852 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:14:47,854 - telegram._bot - DEBUG - Getting updates: [954247062]
2025-04-24 17:14:47,854 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001C6A74CE2C0>]
2025-04-24 17:14:47,855 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:14:47,855 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:14:47,863 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247062, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'devara', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 123, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745495088, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 17:14:47,866 - __main__ - INFO - Received message: devara
2025-04-24 17:14:47,875 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:14:48,694 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:14:48,695 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 124, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745495089, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:14:48,695 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:14:52,706 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:14:52,707 - telegram._bot - DEBUG - Getting updates: [954247063]
2025-04-24 17:14:52,708 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001C6A74CE800>]
2025-04-24 17:14:52,708 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:14:52,708 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:14:52,709 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 124, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745495089, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488945565748162', 'data': 'movie:devara', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247063}
2025-04-24 17:14:52,710 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 17:14:53,097 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 17:14:53,099 - telegram._bot - DEBUG - True
2025-04-24 17:14:53,099 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 17:14:53,099 - __main__ - INFO - Searching movie: devara
2025-04-24 17:14:53,099 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false
2025-04-24 17:14:53,104 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 17:14:53,378 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 17:14:53,381 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 17:14:53,382 - __main__ - INFO - TMDB found 12 results for devara
2025-04-24 17:14:53,384 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 17:14:54,137 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=devara+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 17:14:54,142 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 17:14:54,322 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/genre/movie/list?api_key=68ee2f30970c38d0d60ebc9800be7451 HTTP/1.1" 200 None
2025-04-24 17:14:54,913 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:14:54,914 - telegram._bot - DEBUG - Getting updates: [954247064]
2025-04-24 17:14:54,916 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001C6A74CD9C0>]
2025-04-24 17:14:54,916 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:14:54,918 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:14:55,074 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 17:14:55,839 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 17:14:55,901 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 17:14:55,901 - __main__ - INFO - Discovering groups across Telegram...
2025-04-24 17:14:55,902 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 17:14:55,902 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 17:14:55,902 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 17:14:56,078 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 17:14:56,079 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 17:14:56,079 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 17:14:56,079 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 17:14:56,087 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:56,087 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844352998776572 to InvokeWithLayerRequest (1c6a7653440)
2025-04-24 17:14:56,087 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 17:14:56,090 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:56,091 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:56,091 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:14:56,259 - telethon.network.mtprotostate - DEBUG - Updated time offset (old offset 0, bad 7496844353687766208, good 7496844358986591233, new 1)
2025-04-24 17:14:56,260 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496844352998776572
2025-04-24 17:14:56,260 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 17:14:56,260 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:14:56,261 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844357990729112 to InvokeWithLayerRequest (1c6a7653440)
2025-04-24 17:14:56,261 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 17:14:56,263 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:56,263 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:56,263 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844357998695152 to MsgsAck (1c6a7653470)
2025-04-24 17:14:56,263 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:14:56,265 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:56,265 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:56,449 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 17:14:56,450 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 17:14:56,450 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496844357990729112]
2025-04-24 17:14:56,450 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:14:56,457 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844357990729112
2025-04-24 17:14:56,458 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:14:56,458 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844358778686304 to GetUsersRequest (1c6a7653440)
2025-04-24 17:14:56,458 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:14:56,459 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:56,459 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:56,460 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844358786672372 to MsgsAck (1c6a76530b0)
2025-04-24 17:14:56,460 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 17:14:56,461 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:56,461 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:56,644 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844358778686304
2025-04-24 17:14:56,644 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:14:56,644 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844359521047372 to MsgsAck (1c6a76535f0)
2025-04-24 17:14:56,644 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:14:56,645 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:56,645 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:56,645 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844359525054712 to MsgsAck (1c6a7650e60)
2025-04-24 17:14:56,645 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:14:56,646 - __main__ - INFO - Client connected successfully
2025-04-24 17:14:56,646 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:14:56,654 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:56,654 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:57,038 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:14:57,040 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Entire Telegram lo groups chusthunna...', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 126, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745495098, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:14:57,040 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:14:57,041 - __main__ - INFO - Loaded 0 cached groups
2025-04-24 17:14:57,042 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844361408539196 to SearchRequest (1c6a76500b0)
2025-04-24 17:14:57,042 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:14:57,043 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:57,043 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:57,226 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844361408539196
2025-04-24 17:14:57,227 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:14:57,227 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844362146616360 to MsgsAck (1c6a597e9f0)
2025-04-24 17:14:57,227 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:14:57,227 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:57,228 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:57,228 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844362154178996 to MsgsAck (1c6a7653710)
2025-04-24 17:14:57,228 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:14:57,229 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:14:57,229 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:57,230 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:58,240 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844366493745824 to SearchRequest (1c6a597e9f0)
2025-04-24 17:14:58,240 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:14:58,241 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:58,241 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:58,423 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844366493745824
2025-04-24 17:14:58,424 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:14:58,424 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844367229801200 to MsgsAck (1c6a750d880)
2025-04-24 17:14:58,424 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:14:58,425 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:58,426 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:14:58,426 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844367237811112 to MsgsAck (1c6a7653200)
2025-04-24 17:14:58,426 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:14:58,427 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:14:58,428 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:14:58,428 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:00,439 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844375878004340 to SearchRequest (1c6a750d880)
2025-04-24 17:15:00,440 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:15:00,442 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:00,442 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:00,632 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844375878004340
2025-04-24 17:15:00,632 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:15:00,632 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844376653643872 to MsgsAck (1c6a76532c0)
2025-04-24 17:15:00,633 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:15:00,633 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:00,634 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:00,634 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844376661639480 to MsgsAck (1c6a76721b0)
2025-04-24 17:15:00,634 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:15:00,635 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:15:00,636 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:00,636 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:04,643 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844393875329768 to SearchRequest (1c6a76532c0)
2025-04-24 17:15:04,643 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:15:04,644 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:04,644 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:04,826 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844393875329768
2025-04-24 17:15:04,827 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:15:04,827 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844394614603792 to MsgsAck (1c6a7672030)
2025-04-24 17:15:04,827 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:15:04,827 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:04,827 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:04,828 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844394618640696 to MsgsAck (1c6a76722a0)
2025-04-24 17:15:04,828 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:15:04,828 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:15:04,828 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:04,828 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:05,134 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:15:05,134 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:15:05,135 - telegram._bot - DEBUG - []
2025-04-24 17:15:05,135 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:15:05,135 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:15:12,843 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844429035625272 to SearchRequest (1c6a7672870)
2025-04-24 17:15:12,843 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:15:12,844 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:12,844 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:13,159 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844429035625272
2025-04-24 17:15:13,159 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:15:13,160 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844430599255020 to MsgsAck (1c6a76724e0)
2025-04-24 17:15:13,160 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:15:13,160 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:13,161 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:13,161 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844430603246148 to MsgsAck (1c6a7672300)
2025-04-24 17:15:13,161 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:15:13,162 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:15:13,162 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:13,162 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:15,333 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:15:15,334 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:15:15,334 - telegram._bot - DEBUG - []
2025-04-24 17:15:15,334 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:15:15,334 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:15:25,520 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:15:25,524 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:15:25,524 - telegram._bot - DEBUG - []
2025-04-24 17:15:25,524 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:15:25,524 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:15:29,182 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844499405023072 to SearchRequest (1c6a75e2d80)
2025-04-24 17:15:29,182 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:15:29,182 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:29,182 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:29,365 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844499405023072
2025-04-24 17:15:29,365 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:15:29,365 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844500137889360 to MsgsAck (1c6a5db13a0)
2025-04-24 17:15:29,365 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:15:29,366 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:29,367 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:29,367 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844500146045180 to MsgsAck (1c6a75e2e40)
2025-04-24 17:15:29,367 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:15:29,368 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:15:29,368 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:29,368 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:35,722 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:15:35,723 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:15:35,723 - telegram._bot - DEBUG - []
2025-04-24 17:15:35,723 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:15:35,723 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:15:46,000 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:15:46,001 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:15:46,001 - telegram._bot - DEBUG - []
2025-04-24 17:15:46,001 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:15:46,001 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:15:46,459 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:15:46,460 - telegram._bot - DEBUG - Getting updates: [954247065]
2025-04-24 17:15:46,460 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001C6A74CF580>]
2025-04-24 17:15:46,460 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:15:46,460 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:15:56,664 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:15:56,675 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844617344214832 to PingRequest (1c6a7534bf0)
2025-04-24 17:15:56,675 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 17:15:56,682 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:15:56,682 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:15:56,684 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:15:56,684 - telegram._bot - DEBUG - []
2025-04-24 17:15:56,684 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:15:56,692 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:15:56,881 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496844617344214832
2025-04-24 17:15:56,881 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:16:01,373 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844637609874292 to SearchRequest (1c6a761bb30)
2025-04-24 17:16:01,374 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:16:01,378 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:16:01,378 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:16:01,378 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844637629955812 to MsgsAck (1c6a7534bf0)
2025-04-24 17:16:01,379 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:16:01,381 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:16:01,381 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:16:01,628 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844637609874292
2025-04-24 17:16:01,629 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:16:01,629 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844638634192988 to MsgsAck (1c6a761bad0)
2025-04-24 17:16:01,629 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:16:01,631 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:16:01,631 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:16:01,631 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844638641542956 to MsgsAck (1c6a76535f0)
2025-04-24 17:16:01,631 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:16:01,632 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:16:01,632 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:16:01,632 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:16:06,896 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:16:06,897 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:16:06,897 - telegram._bot - DEBUG - []
2025-04-24 17:16:06,898 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:16:06,898 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:16:17,084 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:16:17,085 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:16:17,085 - telegram._bot - DEBUG - []
2025-04-24 17:16:17,085 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:16:17,086 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:16:27,287 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:16:27,288 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:16:27,288 - telegram._bot - DEBUG - []
2025-04-24 17:16:27,288 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:16:27,289 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:16:28,697 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:16:28,698 - telegram._bot - DEBUG - Getting updates: [954247066]
2025-04-24 17:16:28,699 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001C6A74CF7C0>]
2025-04-24 17:16:28,699 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:16:28,699 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:16:38,908 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:16:38,909 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:16:38,909 - telegram._bot - DEBUG - []
2025-04-24 17:16:38,909 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:16:38,910 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:16:49,287 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:16:49,288 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:16:49,288 - telegram._bot - DEBUG - []
2025-04-24 17:16:49,288 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:16:49,288 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:16:56,745 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844875320924808 to PingRequest (1c6a5b57080)
2025-04-24 17:16:56,746 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 17:16:56,747 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:16:56,748 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:16:56,941 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496844875320924808
2025-04-24 17:16:56,942 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:16:59,491 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:16:59,491 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:16:59,491 - telegram._bot - DEBUG - []
2025-04-24 17:16:59,491 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:16:59,492 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:17:05,636 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844913541120244 to SearchRequest (1c6a784be00)
2025-04-24 17:17:05,637 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:17:05,638 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:05,638 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:05,638 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844913549113940 to MsgsAck (1c6a5b57080)
2025-04-24 17:17:05,638 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:05,642 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:05,642 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:05,889 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844913541120244
2025-04-24 17:17:05,890 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:17:05,891 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844914558309268 to MsgsAck (1c6a7652a50)
2025-04-24 17:17:05,891 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:05,892 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:05,893 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:05,893 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844914566384028 to MsgsAck (1c6a76537d0)
2025-04-24 17:17:05,893 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:05,894 - __main__ - ERROR - Telethon search error for movies: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:17:05,895 - __main__ - ERROR - Failed to search movies after 8 attempts
2025-04-24 17:17:05,896 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:05,896 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:05,896 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844914578377436 to SearchRequest (1c6a7650e60)
2025-04-24 17:17:05,896 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:17:05,898 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:05,898 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:06,132 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844914578377436
2025-04-24 17:17:06,133 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:17:06,133 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844915823396040 to MsgsAck (1c6a738bbf0)
2025-04-24 17:17:06,133 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:06,134 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:06,135 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:06,135 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844915831807448 to MsgsAck (1c6a7652a50)
2025-04-24 17:17:06,135 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:06,137 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:17:06,137 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:06,137 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:07,144 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844920162001564 to SearchRequest (1c6a738bbf0)
2025-04-24 17:17:07,145 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:17:07,146 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:07,146 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:07,456 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844920162001564
2025-04-24 17:17:07,456 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:17:07,457 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844921411494212 to MsgsAck (1c6a7653710)
2025-04-24 17:17:07,457 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:07,457 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:07,457 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:07,458 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844921419325784 to MsgsAck (1c6a784b830)
2025-04-24 17:17:07,458 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:07,461 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:17:07,462 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:07,462 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:09,464 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844930032536704 to SearchRequest (1c6a7653200)
2025-04-24 17:17:09,465 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:17:09,466 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:09,466 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:09,641 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844930032536704
2025-04-24 17:17:09,642 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:17:09,642 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844930743432244 to MsgsAck (1c6a7653710)
2025-04-24 17:17:09,642 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:09,643 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:09,643 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:09,643 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844930749954424 to MsgsAck (1c6a784bef0)
2025-04-24 17:17:09,644 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:09,645 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:17:09,645 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:09,646 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:09,687 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:17:09,689 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:17:09,689 - telegram._bot - DEBUG - []
2025-04-24 17:17:09,690 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:17:09,690 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:17:13,654 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844947972752304 to SearchRequest (1c6a78509e0)
2025-04-24 17:17:13,655 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:17:13,656 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:13,657 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:13,859 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844947972752304
2025-04-24 17:17:13,860 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:17:13,860 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844948797038764 to MsgsAck (1c6a784bce0)
2025-04-24 17:17:13,860 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:13,861 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:13,861 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:13,861 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844948801039428 to MsgsAck (1c6a784be30)
2025-04-24 17:17:13,861 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:13,862 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:17:13,862 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:13,862 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:20,003 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:17:20,004 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:17:20,004 - telegram._bot - DEBUG - []
2025-04-24 17:17:20,005 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:17:20,005 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:17:21,871 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844983198230492 to SearchRequest (1c6a78514c0)
2025-04-24 17:17:21,872 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:17:21,875 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:21,876 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:22,153 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496844983198230492
2025-04-24 17:17:22,153 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:17:22,154 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844984628568044 to MsgsAck (1c6a7850aa0)
2025-04-24 17:17:22,154 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:22,155 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:22,155 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:22,155 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496844984632563940 to MsgsAck (1c6a7850a40)
2025-04-24 17:17:22,155 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:22,156 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:17:22,156 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:22,156 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:30,246 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:17:30,247 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:17:30,247 - telegram._bot - DEBUG - []
2025-04-24 17:17:30,247 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:17:30,247 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:17:38,165 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496845053391627696 to SearchRequest (1c6a7851fa0)
2025-04-24 17:17:38,166 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:17:38,170 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:38,171 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:38,400 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496845053391627696
2025-04-24 17:17:38,402 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:17:38,403 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496845054340805436 to MsgsAck (1c6a7851520)
2025-04-24 17:17:38,403 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:38,404 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:38,406 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:38,406 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496845054352619556 to MsgsAck (1c6a78517f0)
2025-04-24 17:17:38,408 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:17:38,409 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:17:38,409 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:38,409 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:40,453 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:17:40,454 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:17:40,455 - telegram._bot - DEBUG - []
2025-04-24 17:17:40,455 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:17:40,455 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:17:50,728 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:17:50,728 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:17:50,728 - telegram._bot - DEBUG - []
2025-04-24 17:17:50,728 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:17:50,728 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:17:56,771 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496845133124913880 to PingRequest (1c6a7672630)
2025-04-24 17:17:56,771 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 28 bytes for sending
2025-04-24 17:17:56,776 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:17:56,777 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:17:56,969 - telethon.network.mtprotosender - DEBUG - Handling pong for message 7496845133124913880
2025-04-24 17:17:56,969 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:18:00,953 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:18:00,954 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:18:00,955 - telegram._bot - DEBUG - []
2025-04-24 17:18:00,955 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:18:00,956 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:18:10,446 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496845191954478720 to SearchRequest (1c6a784b0b0)
2025-04-24 17:18:10,456 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:18:10,479 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:18:10,479 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:18:10,479 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496845192085046272 to MsgsAck (1c6a784b1d0)
2025-04-24 17:18:10,479 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:18:10,484 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:18:10,485 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:18:10,691 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496845191954478720
2025-04-24 17:18:10,692 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:18:10,692 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496845192936495284 to MsgsAck (1c6a784b770)
2025-04-24 17:18:10,694 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:18:10,695 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:18:10,695 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:18:10,695 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496845192948469620 to MsgsAck (1c6a784b5f0)
2025-04-24 17:18:10,695 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:18:10,784 - __main__ - ERROR - Telethon search error for series: The key is not registered in the system (caused by SearchRequest)
2025-04-24 17:18:10,788 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:18:10,788 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:18:11,152 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:18:11,154 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:18:11,155 - telegram._bot - DEBUG - []
2025-04-24 17:18:11,155 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:18:11,156 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:36:55,603 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 17:36:55,606 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 17:36:56,962 - __main__ - INFO - Bot polling started...
2025-04-24 17:36:56,963 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 17:36:57,668 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 17:36:57,668 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 17:36:57,669 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 17:36:57,669 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 17:36:57,669 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 17:36:57,669 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 17:36:57,669 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 17:36:57,670 - telegram.ext._updater - DEBUG - Dropping pending updates from Telegram server
2025-04-24 17:36:57,670 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 17:36:57,871 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 17:36:57,872 - telegram._bot - DEBUG - True
2025-04-24 17:36:57,872 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 17:36:57,872 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 17:36:57,872 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 17:36:57,872 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 17:36:57,872 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 17:36:57,873 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:36:57,875 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 17:36:57,876 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 17:36:57,876 - telegram.ext._application - INFO - Application started
2025-04-24 17:36:57,876 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 17:36:57,877 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 17:37:42,957 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:37:42,959 - telegram._bot - DEBUG - Getting updates: [954247067]
2025-04-24 17:37:42,960 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001E8FFB60040>]
2025-04-24 17:37:42,960 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:37:42,962 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:37:42,967 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247067, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 127, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745496464, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 17:37:42,968 - __main__ - INFO - Received /start command
2025-04-24 17:37:42,968 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:37:43,777 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:37:43,779 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 180}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 128, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745496464, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:37:43,780 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:38:04,451 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:38:04,452 - telegram._bot - DEBUG - Getting updates: [954247068]
2025-04-24 17:38:04,452 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001E8FFB60100>]
2025-04-24 17:38:04,453 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:38:04,453 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:38:04,454 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247068, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 129, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745496485, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 17:38:04,455 - __main__ - INFO - Received /start command
2025-04-24 17:38:04,455 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:38:05,351 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:38:05,352 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 180}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 130, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745496486, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:38:05,352 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:38:10,577 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:38:10,578 - telegram._bot - DEBUG - Getting updates: [954247069]
2025-04-24 17:38:10,579 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001E8FFB61900>]
2025-04-24 17:38:10,579 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:38:10,579 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:38:10,581 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247069, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': 'Devara', 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 131, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745496491, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 17:38:10,582 - __main__ - INFO - Received message: devara
2025-04-24 17:38:10,582 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:38:11,405 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:38:11,406 - telegram._bot - DEBUG - {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 132, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745496492, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:38:11,406 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:38:12,962 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:38:12,963 - telegram._bot - DEBUG - Getting updates: [954247070]
2025-04-24 17:38:12,963 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001E8FFB62EC0>]
2025-04-24 17:38:12,963 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:38:12,963 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:38:12,965 - telegram.ext._application - DEBUG - Processing update {'callback_query': {'message': {'reply_markup': {'inline_keyboard': [[{'callback_data': 'movie:devara', 'text': 'Movie'}, {'callback_data': 'series:devara', 'text': 'Series'}, {'callback_data': 'pdf:devara', 'text': 'PDF'}]]}, 'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Is 'devara' a Movie, Series, or PDF? Select one ra...", 'group_chat_created': False, 'entities': [], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 132, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745496492, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}, 'chat_instance': '-2137169113698463045', 'id': '7177488948787071743', 'data': 'movie:devara', 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}, 'update_id': 954247070}
2025-04-24 17:38:12,966 - telegram._bot - DEBUG - Entering: answer_callback_query
2025-04-24 17:38:13,370 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/answerCallbackQuery "HTTP/1.1 200 OK"
2025-04-24 17:38:13,371 - telegram._bot - DEBUG - True
2025-04-24 17:38:13,371 - telegram._bot - DEBUG - Exiting: answer_callback_query
2025-04-24 17:38:13,371 - __main__ - INFO - Searching movie: devara
2025-04-24 17:38:13,372 - __main__ - DEBUG - TMDB API call: https://api.themoviedb.org/3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false
2025-04-24 17:38:13,374 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 17:38:13,565 - __main__ - ERROR - TMDB request error on attempt 1: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2025-04-24 17:38:14,576 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 17:38:14,670 - __main__ - ERROR - TMDB request error on attempt 2: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2025-04-24 17:38:16,673 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 17:38:16,838 - urllib3.connectionpool - DEBUG - https://api.themoviedb.org:443 "GET /3/search/movie?api_key=68ee2f30970c38d0d60ebc9800be7451&language=en-US&query=devara&page=1&include_adult=false HTTP/1.1" 200 None
2025-04-24 17:38:16,839 - __main__ - DEBUG - TMDB response status: 200
2025-04-24 17:38:16,839 - __main__ - INFO - TMDB found 12 results for devara
2025-04-24 17:38:16,845 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): www.googleapis.com:443
2025-04-24 17:38:17,529 - urllib3.connectionpool - DEBUG - https://www.googleapis.com:443 "GET /youtube/v3/search?part=snippet&q=devara+trailer&key=AIzaSyAnrSzc1SPZet8uAEkNoSAMpmwNhAeBA94 HTTP/1.1" 200 None
2025-04-24 17:38:17,532 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 17:38:17,615 - __main__ - WARNING - Genre fetch failed, retrying 1...
2025-04-24 17:38:19,620 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 17:38:19,795 - __main__ - WARNING - Genre fetch failed, retrying 2...
2025-04-24 17:38:21,800 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.themoviedb.org:443
2025-04-24 17:38:21,921 - __main__ - WARNING - Genre fetch failed, retrying 3...
2025-04-24 17:38:24,603 - telegram._bot - DEBUG - Entering: send_photo
2025-04-24 17:38:25,882 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendPhoto "HTTP/1.1 200 OK"
2025-04-24 17:38:25,909 - telegram._bot - DEBUG - Exiting: send_photo
2025-04-24 17:38:25,909 - __main__ - INFO - Discovering groups for query: devara
2025-04-24 17:38:25,909 - __main__ - DEBUG - Connecting Telethon client...
2025-04-24 17:38:25,909 - telethon.network.mtprotosender - INFO - Connecting to 149.154.167.51:443/TcpFull...
2025-04-24 17:38:25,910 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 17:38:26,085 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 17:38:26,085 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 17:38:26,085 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 17:38:26,085 - telethon.network.mtprotosender - INFO - Connection to 149.154.167.51:443/TcpFull complete!
2025-04-24 17:38:26,092 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:26,092 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850408923959476 to InvokeWithLayerRequest (1e8ffcdeba0)
2025-04-24 17:38:26,092 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 17:38:26,093 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:26,093 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:26,093 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:26,477 - telethon.network.mtprotostate - DEBUG - Updated time offset (old offset 0, bad 7496850410463787780, good 7496850415072992257, new 1)
2025-04-24 17:38:26,477 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496850408923959476
2025-04-24 17:38:26,477 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 17:38:26,477 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:26,477 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850414758755076 to InvokeWithLayerRequest (1e8ffcdeba0)
2025-04-24 17:38:26,479 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 17:38:26,480 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:26,480 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:26,480 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850414768871652 to MsgsAck (1e8ffcdec30)
2025-04-24 17:38:26,480 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:26,481 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:26,481 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:26,684 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 17:38:26,685 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 17:38:26,685 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496850414758755076]
2025-04-24 17:38:26,685 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:26,687 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850414758755076
2025-04-24 17:38:26,687 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:26,687 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850415597638476 to GetUsersRequest (1e8ff5140e0)
2025-04-24 17:38:26,688 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:38:26,688 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:26,688 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:26,688 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850415601637232 to MsgsAck (1e8ffc2fbf0)
2025-04-24 17:38:26,688 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 17:38:26,689 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:26,689 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:26,889 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850415597638476
2025-04-24 17:38:26,889 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:26,890 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850416407947884 to MsgsAck (1e8ffcdea80)
2025-04-24 17:38:26,890 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:26,890 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:26,891 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:26,891 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850416411945688 to MsgsAck (1e8ffcdfb60)
2025-04-24 17:38:26,891 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:26,891 - __main__ - INFO - Client connected successfully
2025-04-24 17:38:26,892 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:26,892 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:26,892 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850416415938720 to GetStateRequest (1e8ffcdf560)
2025-04-24 17:38:26,892 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 20 bytes for sending
2025-04-24 17:38:26,893 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:26,893 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,075 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850416415938720
2025-04-24 17:38:27,076 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:27,076 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850417447787272 to MsgsAck (1e8ffcdfbf0)
2025-04-24 17:38:27,076 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:27,076 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,076 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,077 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850417451815592 to MsgsAck (1e8ffcde870)
2025-04-24 17:38:27,077 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:27,077 - __main__ - WARNING - No OTP found, requesting new OTP
2025-04-24 17:38:27,077 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,077 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,078 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850417455834376 to GetUsersRequest (1e8ffcdfbf0)
2025-04-24 17:38:27,078 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:38:27,078 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,078 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,403 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850417455834376
2025-04-24 17:38:27,405 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:27,405 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850418762481680 to MsgsAck (1e8ffcde600)
2025-04-24 17:38:27,405 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:27,405 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,405 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,405 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850418766094196 to MsgsAck (1e8ffcdf4a0)
2025-04-24 17:38:27,405 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:27,407 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,407 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,407 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850418774081220 to SendCodeRequest (1e8ffcdcfb0)
2025-04-24 17:38:27,407 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 17:38:27,408 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,408 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,606 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850418774081220
2025-04-24 17:38:27,607 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:27,607 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850419573480596 to MsgsAck (1e8ffcdf650)
2025-04-24 17:38:27,608 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:27,608 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,608 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,608 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850419577513684 to MsgsAck (1e8ffcde120)
2025-04-24 17:38:27,608 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:27,609 - telethon.client.users - INFO - Phone migrated to 5
2025-04-24 17:38:27,609 - telethon.client.telegrambaseclient - INFO - Reconnecting to new data center 5
2025-04-24 17:38:27,609 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,609 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,609 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850419581532468 to GetConfigRequest (1e8ffcded50)
2025-04-24 17:38:27,609 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 20 bytes for sending
2025-04-24 17:38:27,611 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:27,611 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:27,813 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850419581532468
2025-04-24 17:38:27,813 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:27,820 - telethon.network.mtprotosender - INFO - Disconnecting from 149.154.167.51:443/TcpFull...
2025-04-24 17:38:27,821 - telethon.network.mtprotosender - DEBUG - Closing current connection...
2025-04-24 17:38:27,821 - telethon.network.mtprotosender - DEBUG - Cancelling 0 pending message(s)...
2025-04-24 17:38:27,821 - telethon.network.mtprotosender - INFO - Disconnection from 149.154.167.51:443/TcpFull complete!
2025-04-24 17:38:27,822 - telethon.network.mtprotosender - INFO - Connecting to 91.108.56.171:443/TcpFull...
2025-04-24 17:38:27,822 - telethon.network.mtprotosender - DEBUG - Connection attempt 1...
2025-04-24 17:38:27,908 - telethon.network.mtprotosender - DEBUG - Connection success!
2025-04-24 17:38:27,910 - telethon.network.mtprotosender - DEBUG - New auth_key attempt 1...
2025-04-24 17:38:29,278 - telethon.network.mtprotosender - DEBUG - auth_key generation success!
2025-04-24 17:38:29,279 - telethon.network.mtprotosender - DEBUG - Starting send loop
2025-04-24 17:38:29,279 - telethon.network.mtprotosender - DEBUG - Starting receive loop
2025-04-24 17:38:29,279 - telethon.network.mtprotosender - INFO - Connection to 91.108.56.171:443/TcpFull complete!
2025-04-24 17:38:29,287 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,287 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850426880631680 to InvokeWithLayerRequest (1e8ffcde2d0)
2025-04-24 17:38:29,287 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850426880631684 to MsgsAck (1e8ffcded50)
2025-04-24 17:38:29,287 - telethon.network.mtprotosender - DEBUG - Encrypting 2 message(s) in 136 bytes for sending
2025-04-24 17:38:29,289 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:29,290 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,290 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:29,390 - telethon.network.mtprotosender - DEBUG - Handling bad salt for message 7496850426880631688
2025-04-24 17:38:29,391 - telethon.network.mtprotosender - DEBUG - 1 message(s) will be resent
2025-04-24 17:38:29,391 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:29,391 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850427298382992 to InvokeWithLayerRequest (1e8ffcde2d0)
2025-04-24 17:38:29,391 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 76 bytes for sending
2025-04-24 17:38:29,392 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:29,392 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,392 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850427302462808 to MsgsAck (1e8fed04fe0)
2025-04-24 17:38:29,392 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:29,393 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:29,393 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,486 - telethon.network.mtprotosender - DEBUG - Handling container
2025-04-24 17:38:29,486 - telethon.network.mtprotosender - DEBUG - Handling new session created
2025-04-24 17:38:29,487 - telethon.network.mtprotosender - DEBUG - Handling acknowledge for [7496850427298382992]
2025-04-24 17:38:29,487 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:29,504 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850427298382992
2025-04-24 17:38:29,504 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:29,504 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850427750853772 to GetUsersRequest (1e8ffcdf860)
2025-04-24 17:38:29,504 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 32 bytes for sending
2025-04-24 17:38:29,504 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:29,504 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,504 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850427750853776 to MsgsAck (1e8ffcdf8c0)
2025-04-24 17:38:29,504 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 60 bytes for sending
2025-04-24 17:38:29,506 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:29,506 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,599 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850427750853772
2025-04-24 17:38:29,600 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:38:29,600 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850428135527844 to MsgsAck (1e8ffcdf920)
2025-04-24 17:38:29,600 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:29,601 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:29,601 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,601 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850428139521832 to MsgsAck (1e8ffcdedb0)
2025-04-24 17:38:29,601 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 36 bytes for sending
2025-04-24 17:38:29,602 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:29,603 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,603 - telethon.extensions.messagepacker - DEBUG - Assigned msg_id = 7496850428147529832 to SendCodeRequest (1e8ffcdcfb0)
2025-04-24 17:38:29,603 - telethon.network.mtprotosender - DEBUG - Encrypting 1 message(s) in 84 bytes for sending
2025-04-24 17:38:29,604 - telethon.network.mtprotosender - DEBUG - Encrypted messages put in a queue to be sent
2025-04-24 17:38:29,604 - telethon.network.mtprotosender - DEBUG - Waiting for messages to send...
2025-04-24 17:38:29,960 - telethon.network.mtprotosender - DEBUG - Handling RPC result for message 7496850428147529832
2025-04-24 17:38:29,960 - telethon.network.mtprotosender - DEBUG - Receiving items from the network...
2025-04-24 17:46:56,767 - asyncio - DEBUG - Using proactor: IocpProactor
2025-04-24 17:46:56,773 - __main__ - INFO - Starting AllInOneBot...
2025-04-24 17:46:59,519 - __main__ - INFO - Bot polling started...
2025-04-24 17:46:59,519 - telegram._bot - DEBUG - Entering: get_me
2025-04-24 17:47:00,626 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getMe "HTTP/1.1 200 OK"
2025-04-24 17:47:00,628 - telegram._bot - DEBUG - {'is_bot': True, 'can_read_all_group_messages': False, 'username': 'allinonehachubot', 'first_name': 'allinone', 'can_join_groups': True, 'supports_inline_queries': False, 'id': 7963951416}
2025-04-24 17:47:00,629 - telegram._bot - DEBUG - Exiting: get_me
2025-04-24 17:47:00,629 - telegram._bot - DEBUG - This Bot is already initialized.
2025-04-24 17:47:00,630 - telegram.ext._updater - DEBUG - Updater started (polling)
2025-04-24 17:47:00,630 - telegram.ext._updater - DEBUG - Start network loop retry bootstrap del webhook
2025-04-24 17:47:00,631 - telegram.ext._updater - DEBUG - Deleting webhook
2025-04-24 17:47:00,633 - telegram.ext._updater - DEBUG - Dropping pending updates from Telegram server
2025-04-24 17:47:00,633 - telegram._bot - DEBUG - Entering: delete_webhook
2025-04-24 17:47:00,829 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/deleteWebhook "HTTP/1.1 200 OK"
2025-04-24 17:47:00,831 - telegram._bot - DEBUG - True
2025-04-24 17:47:00,832 - telegram._bot - DEBUG - Exiting: delete_webhook
2025-04-24 17:47:00,832 - telegram.ext._updater - DEBUG - Bootstrap done
2025-04-24 17:47:00,833 - telegram.ext._updater - DEBUG - Waiting for polling to start
2025-04-24 17:47:00,834 - telegram.ext._updater - DEBUG - Polling updates from Telegram started
2025-04-24 17:47:00,834 - telegram.ext._updater - DEBUG - Start network loop retry getting Updates
2025-04-24 17:47:00,834 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:47:00,838 - apscheduler.scheduler - INFO - Scheduler started
2025-04-24 17:47:00,838 - telegram.ext._application - DEBUG - JobQueue started
2025-04-24 17:47:00,839 - telegram.ext._application - INFO - Application started
2025-04-24 17:47:00,840 - apscheduler.scheduler - DEBUG - Looking for jobs to run
2025-04-24 17:47:00,840 - apscheduler.scheduler - DEBUG - No jobs; waiting until a job is added
2025-04-24 17:47:42,044 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:47:42,045 - telegram._bot - DEBUG - Getting updates: [954247074]
2025-04-24 17:47:42,046 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001CD1A490040>]
2025-04-24 17:47:42,048 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:47:42,049 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:47:42,051 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247074, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 134, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745497063, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 17:47:42,053 - __main__ - INFO - Received /start command
2025-04-24 17:47:42,053 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:47:42,844 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:47:42,846 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 180}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 135, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745497063, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:47:42,851 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:48:32,376 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:48:32,377 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:48:32,377 - telegram._bot - DEBUG - []
2025-04-24 17:48:32,378 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:48:32,378 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:49:22,576 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:49:22,578 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:49:22,579 - telegram._bot - DEBUG - []
2025-04-24 17:49:22,580 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:49:22,580 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:50:12,827 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:50:12,829 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:50:12,830 - telegram._bot - DEBUG - []
2025-04-24 17:50:12,830 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:50:12,830 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:50:49,431 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:50:49,432 - telegram._bot - DEBUG - Getting updates: [954247075]
2025-04-24 17:50:49,433 - telegram._bot - DEBUG - [<telegram._update.Update object at 0x000001CD1A491C00>]
2025-04-24 17:50:49,435 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:50:49,435 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:50:49,436 - telegram.ext._application - DEBUG - Processing update {'update_id': 954247075, 'message': {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': '/start', 'group_chat_created': False, 'entities': [{'length': 6, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 0}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 136, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745497250, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': False, 'first_name': 'Kartheek', 'id': 8113590315, 'language_code': 'en'}}}
2025-04-24 17:50:49,437 - __main__ - INFO - Received /start command
2025-04-24 17:50:49,438 - telegram._bot - DEBUG - Entering: send_message
2025-04-24 17:50:50,381 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/sendMessage "HTTP/1.1 200 OK"
2025-04-24 17:50:50,382 - telegram._bot - DEBUG - {'chat': {'id': 8113590315, 'type': <ChatType.PRIVATE>, 'first_name': 'Kartheek'}, 'text': "Rey mawa, welcome to AllInOneBot! Movies, series, PDFs—entire Telegram lo automatic ga search chesi files pampistha. Ex: 'hi nanna', 'batman', 'breaking bad', 'robbins pathology'. /help cheyyi!", 'group_chat_created': False, 'entities': [{'length': 5, 'type': <MessageEntityType.BOT_COMMAND>, 'offset': 180}], 'new_chat_members': [], 'new_chat_photo': [], 'message_id': 137, 'delete_chat_photo': False, 'caption_entities': [], 'date': 1745497251, 'supergroup_chat_created': False, 'photo': [], 'channel_chat_created': False, 'from': {'is_bot': True, 'username': 'allinonehachubot', 'first_name': 'allinone', 'id': 7963951416}}
2025-04-24 17:50:50,382 - telegram._bot - DEBUG - Exiting: send_message
2025-04-24 17:51:39,769 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:51:39,770 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:51:39,771 - telegram._bot - DEBUG - []
2025-04-24 17:51:39,771 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:51:39,771 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:52:30,043 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:52:30,044 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:52:30,044 - telegram._bot - DEBUG - []
2025-04-24 17:52:30,045 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:52:30,045 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:53:20,427 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:53:20,428 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:53:20,428 - telegram._bot - DEBUG - []
2025-04-24 17:53:20,428 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:53:20,428 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:54:10,629 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:54:10,630 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:54:10,631 - telegram._bot - DEBUG - []
2025-04-24 17:54:10,631 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:54:10,631 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:55:01,184 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:55:01,186 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:55:01,187 - telegram._bot - DEBUG - []
2025-04-24 17:55:01,187 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:55:01,188 - telegram._bot - DEBUG - Entering: get_updates
2025-04-24 17:55:51,389 - httpx._client - DEBUG - HTTP Request: POST https://api.telegram.org/bot7963951416:AAEfYWghOfZc50jxE90exSAgCM_C6TrG-yo/getUpdates "HTTP/1.1 200 OK"
2025-04-24 17:55:51,391 - telegram._bot - DEBUG - No new updates found.
2025-04-24 17:55:51,392 - telegram._bot - DEBUG - []
2025-04-24 17:55:51,392 - telegram._bot - DEBUG - Exiting: get_updates
2025-04-24 17:55:51,392 - telegram._bot - DEBUG - Entering: get_updates
