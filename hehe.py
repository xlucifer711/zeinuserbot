from userbot.utils import admin_cmd as a
#sleep how many times after each edit in 'lol' 
EDIT_SLEEP = 1
#edit how many times in 'lol' 
EDIT_TIMES = 19


lol_ani = [ 
            "WOW AB BOHOT MAJA AANE WALA HAI TO READY HO ZAO",
            "1..",
            "2...",
            "3....",
            " π°π½π³ πππ°πππ΄π³ ", 
            " β° *ππ°π°π·* β°     [γ€](https://telegra.ph/file/a19b0bf4760fca85bd961.png) ",
            " β° *π»πΎπ»* β°      [γ€](https://telegra.ph/file/ed23819c84bab66e7d92f.png) ",
            " β° *π΄π»π΄π²πππΈπ² π±πΈπ»π» πΊπΎπ½ π±π·π°ππ΄πΆπ°* β°  [γ€](https://telegra.ph/file/53c85b5b354212496746f.png) ",
            " β° *πΉπ·πΈπ½πΆπ° π»π°π»π°* β°    [γ€](https://telegra.ph/file/1379a8c9ea40eaa463fd8.png) ",
            " β° *π½πΈπ½πΉπ° ππ΄π²π·π½πΈπππ΄* β°    [γ€](https://telegra.ph/file/891a05f03399fb48f40f3.png) ",
            " β° *πππΈπ²πΊπ΄π π²π·πΎπ* β°    [γ€](https://telegra.ph/file/542a1f433c263e4f3f984.png)",
            " β° *ππ°π°π π³π°ππ³* β°    [γ€](https://telegra.ph/file/bfa114bbd4b2044cf5933.png)",
            " β° *πππ°π³ π°π°ππ°* β°    [γ€](https://telegra.ph/file/3830d44f9333e3c21b2cd.png)",
            " β° *πΊπ°π°πΌ ππ°πΌπ°πΌ* β°    [γ€](https://telegra.ph/file/ececebb55e5f29be0afcf.png)",
            " β° *πΉπ°π»π΄π±πΈ πΊπ·π°ππΈ* β°    [γ€](https://telegra.ph/file/389a857af3bf833d3ccb2.png)",
            " β° *πΌπΎππ΄ πΎππ* β°    [γ€](https://telegra.ph/file/2a30a5514b022120a82b9.png)",
           
            " β° *πππ³π·π°π πΉπ°* β°    [γ€](https://telegra.ph/file/c5cd50018e304056484f2.png)",
            " β° *π³πΎπ½π π³πΎ πΌπ°πππΈ* β°    [γ€](https://telegra.ph/file/455b959424b17f9fb570e.png)",
            " β° *π²π·π°πΏπΏπ°π» ππ°π* β°    [γ€](https://telegra.ph/file/a0fad91da8b4556c67a2d.png)"
]
@borg.on(a(pattern=r"hehe"))
async def LEGENDX (event):
  msg = await event.edit('DEKHNA AAB MAJA AAEGA π')
    for x in range(EDIT_TIMES):
        msg.edit_text(lol_ani[x%19],parse_mode='markdown')
        time.sleep(5)
    msg.edit_text('*MAJA AAYA KYA π*[γ€](https://telegra.ph/file/381dd2ea242e0bd292434.png) *AGAR HA THEN MAKE* [merissa πππ΄ππ±πΎπ](t.me/q_k_2)  ',parse_mode='markdown')
