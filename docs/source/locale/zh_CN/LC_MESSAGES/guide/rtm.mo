Þ                         ì   /   í   &        D  *   M  1   x     ª     ³     ¿     Ñ     n  j   ö  N   a    °  +   =  -   i       (     $   Ç     ì     õ               ¡  y   %  Q      And Here is the rtm loop above working sample:: Basically, rtm.loop contains 3 stages: Examples Here is a sample rtm loop implementation:: Provides handful helpers for rtm message parsing. RTM Loop RTM Message Real Time Message To achive more flexible usage, BearyChat.py won't provide any implementations for rtm.loop. You can use examples/rtm_loop below as implementation reference. loop: Subscribe to websocket's message event and consume the message comes from the server. You can use RTMMessage for message parsing. ping: Keep sending type=ping message to server after connected. Pinging interval with 5000ms is suggested. rtm.start: Use rtm token to authenticate user and open a websocket connection. Project-Id-Version: bearychat.py 0.0.1
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2017-01-03 09:51+0800
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: zh_Hans_CN
Language-Team: zh_Hans_CN <LL@li.org>
Plural-Forms: nplurals=1; plural=0
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.3.4
 è¿æ¯ä¸é¢ rtm loop çå·¥ä½æµç¤ºä¾ :: ç®åæ¥è¯´ï¼rtm.loop åå« 3 ä¸ªé¶æ®µï¼ ä¾å­ è¿æ¯ä¸ä¸ªç®åç rtm loop å®ç° :: æä¾æ¹ä¾¿çrtmæ¶æ¯è§£æå½æ° RTM Loop RTM Message Real Time Message ä¸ºäºæä¾æ´å çµæ´»çåè½ï¼BearyChat.py ä¸ä¼æä¾ rtm.loop çå®ç°ãä½ å¯ä»¥ä½¿ç¨ä¸é¢ç examples/rtm_loop ä½ä¸ºåèã loop: è®¢é websocket è¿æ¥çæ¶æ¯äºä»¶ãæ¶å°æ¥èªæå¡å¨çæ¶æ¯åå¯ä»¥ éè¿ rtm.messsage æ¥è§£æå¤çæ¶æ¯ã ping: å¨è¿æ¥ä¸æå¡å¨ä¹åï¼éè¦æç»­åé type=ping çæ¶æ¯æ¥ä¿æè¿æ¥ã å»ºè®®åéé´éä¸º 5000ms rtm.start: ä½¿ç¨ RTM token æ¥è¿è¡è®¤è¯ï¼å¹¶è·å¾ websocket è¿æ¥å°åã 