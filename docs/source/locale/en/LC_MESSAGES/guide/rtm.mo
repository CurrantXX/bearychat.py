��          �               �   /   �   &        D  *   M  1   x     �     �     �  �   �  �   n  j   �  N   a  �  �  /   4  &   d     �  *   �  1   �     �     �       �     �   �  j   =  N   �   And Here is the rtm loop above working sample:: Basically, rtm.loop contains 3 stages: Examples Here is a sample rtm loop implementation:: Provides handful helpers for rtm message parsing. RTM Loop RTM Message Real Time Message To achive more flexible usage, BearyChat.py won't provide any implementations for rtm.loop. You can use examples/rtm_loop below as implementation reference. loop: Subscribe to websocket's message event and consume the message comes from the server. You can use RTMMessage for message parsing. ping: Keep sending type=ping message to server after connected. Pinging interval with 5000ms is suggested. rtm.start: Use rtm token to authenticate user and open a websocket connection. Project-Id-Version: bearychat.py 0.0.1
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2017-01-03 09:51+0800
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: en
Language-Team: en <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.3.4
 And Here is the rtm loop above working sample:: Basically, rtm.loop contains 3 stages: Examples Here is a sample rtm loop implementation:: Provides handful helpers for rtm message parsing. RTM Loop RTM Message Real Time Message To achive more flexible usage, BearyChat.py won't provide any implementations for rtm.loop. You can use examples/rtm_loop below as implementation reference. loop: Subscribe to websocket's message event and consume the message comes from the server. You can use RTMMessage for message parsing. ping: Keep sending type=ping message to server after connected. Pinging interval with 5000ms is suggested. rtm.start: Use rtm token to authenticate user and open a websocket connection. 