# для страницы
u_admins = [626727521]
bot_id = 626727521
u_token = '066ad48c26dc8670613faf1f7346bcdde58be3977080ca63027199037ccd9e58bf1be38c3029c9aa655e1'

# для группы
g_admins = []
group_id = 0
g_token = ''

# комнады
hate = ['+хейт', '+hate']
unhate = ['-хейт', '-hate']
cooldown = ['!кд', '!cd']

# префиксы
hate_message_prefix = ['текст', 'text']
hate_photo_prefix = ['фото', 'photo']

# варианты сообщений
MESSAGE_VARIANTS = ["Я твой рот ебал", "Пошел нахуй", "Соси мой пайтонский член", "Маме своей так скажи",
                    "Ты быканул или мне показалось", "Не пиши мне, педик", "Ясно гей", "Пидорас ебаный", "Хуй из пасти вытащи и потом говори",
                    "Я вертел тебя на своем цифрововм хуе", "Ну и хули ты высрал", "Тебе уебать или дать пососать", "Нихуя ты умный", "Хорошо сосешь",
                    "А почему рот в говне", "Хуя ты сказанул", "От такой речи мне аж захотелось въебать тебе", "Ну и что ты мне сделаешь",
                    "Пососи ок", "Помойся, воняешь", "Нихуя ты заглотнул", "Готовь очко", "Сын шлюхи", "Вижу тебе понравилось как я тебя ебу",
                    "Лох ебаный", "Иди мамке поплачься", "В школе расскажешь", "Маме привет", "Шароеб ебаный", "Я твой рот ебал",
                    "На, хуй соси и не скули, пока я твою мать не начал ебать", "Че ты на мой хуй садишься как муха на говно",
                    "Сука, ты заебал мне яйца носом щекотать, соси аккуратно", "Прикол, твоя мать шлюха обоссаная", "Ты хули такой токсик, отчим в детстве выебал?",
                    "Оккупировал твое очко", "Ты че там кони двинул, сын пидораса", "Ты че заикаться то начал, хуеглот",
                    "Мамку твою ебал, что на это скажешь?", "Ты на кого выебываешься, фиксик ебаный", "Вхахахава, нихуя ты сказанул, чехол для хуя",
                    "От тебя говном воняет", "От таких слов даже твой батя в гробу перевернулся", "Ну как там с деньгами, еблан?",
                    "Нихуя тебе пердак разорвало", "Чет твой батя не постарался, сливаешься как говно", "Маму ебал", "Все ясно, автор пидорас",
                    "Расширил твое очко до размеров созвездия Гидры", "В палату быстро, долбоеб", "А когда я тебя ебал ты друое орал", "Как уебу тебе залупой по лбу", "Че ты высрал, подзалупник",
                    "Поешь говна", "10 iq ответ", "Завали ебало, уёбище безмозглое, сука я бы тебя закопал", "Хватит ныть как дешевая шлюха при виде огромного члена, твои выпуки читать все равно никто не будет",
                    "Молодец, а теперь отсоси так же, только с заглотом", "Девочка слитая, иди поплачься бате в хуй", "Ебало оффни, подзалупный творог",
                    "Сказал ты, сглотнув сперму своего бати", "Единственное,что отличает тебя от остальных маленьких хуеглотов, это твое оригинальное имя. Передай своим родителям, что они достаточно творческие хуеплеты.",
                    "Я тебе тут ебучку в моче ополаскиваю, нравится?", "Ебашу тебя хуем по лбу", "Обкончал тебя и твою дохлую мамашу", "haha", "『o』『t』『v』『e』『z』 『t』『v』『o』『u』 『m』『a』『t』 『n』『a』 『t』『r』『u』『p』『o』『v』『o』『z』『k』『e』 『v』 『b』『o』『r』『d』『e』『l』",
                    "еz søsе kаk bеглыŭ =D", "sаsеш tu kаk членаглаtаtель uллюzøрныŭ =D", "еz еz søsала tы mну kаk vzbалmøшныŭ =D", "хуŭøk ŋøsаsuvøеш bømш ŋøряdøчныŭ =D",
                    "ꍟꌃꍏꌗꃅꀎ ᐯꍏꌗ ꈤꍏ ꀤꁴꀤ", "🅴🅱🅰🆂🅷🆄 🆅🅰🆂 🅽🅰 🅸🆉🅸", "ꂦꋪꀘꍏꀎ ꈤꍟ ꀘꀎꌗꍏꀤ ꃅꀎꀤ", "ꍟꌃꍏꌗꃅꀎ ꓄ꌩꍏ ꈤꍏ ꀤꁴꌩꍏꃅ", "『h』『v』『a』『t』『i』『t』 『s』『v』『o』『i』『m』 『y』『a』『z』『y』『k』『o』『m』 『l』『i』『s』『a』『t』 『m』『o』『u』 『o』『b』『u』『v』", "ｈａｒｅ　ｎａ　ｍｏｅｍ　ｈｕｅ　ｏｒａｔ,　ｇｏｌｏｖａ　ｂｏｌｉｔ", "ꌗ꒒ꀤᐯꍏꀎ ꓄ꌩꍏ", "🆂🅻🅸🆅🅰🆄 🆃🆈🅰", "『s』『l』『i』『v』『a』『u』 『t』『y』『a』", "ｓｌｉｖａｕ　ｔｙａ",
                    "ꃅꍏꃅꍏꃅꍏꃅꍏꃅꍏꃅꍏꃅꍏꃅꍏ ꌗ꒒ꀤ꓄ ꎭꂦꍟꎭꀎ 4꒒ꍟꈤꀎ", "🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰 🆂🅻🅸🆃 🅼🅾🅴🅼🆄 4🅻🅴🅽🆄", "『h』『a』『h』『a』『h』『a』『h』『a』『h』『a』『h』『a』『h』『a』『h』『a』 『s』『l』『i』『t』 『m』『o』『e』『m』『u』 『4』『l』『e』『n』『u』", "ｈａｈａｈａｈａｈａｈａｈａｈａ　ｓｌｉｔ　ｍｏｅｍｕ　４ｌｅｎｕ",
                    "ᐯꌃꀤ꒒ ᐯ ꓄ᐯꂦꀎ ꎭꍏ꓄ ꁅᐯꂦꁴꀸ, ᖘꂦᐯꍟꌗꀤ꒒ ꈤꍏ ꌗ꓄ꍟꈤꍟ ꀤ ꒒ꀎꌃꀎꀎꌗ ꍟꀤ ꀘꍏꀘ ꀘꍏꋪ꓄ꀤꈤꂦꀤ", "🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰 🆂🅻🅸🆃 🅼🅾🅴🅼🆄 4🅻🅴🅽🆄", "『h』『a』『h』『a』『h』『a』『h』『a』『h』『a』『h』『a』『h』『a』『h』『a』 『s』『l』『i』『t』 『m』『o』『e』『m』『u』 『4』『l』『e』『n』『u』", "ｈａｈａｈａｈａｈａｈａｈａｈａ　ｓｌｉｔ　ｍｏｅｍｕ　４ｌｅｎｕ",
                    "ꂦ꓄ᐯꍟꁴ ꓄ᐯꂦꀎ ꎭꍏ꓄ ᐯ ꌃꂦꋪꀸꍟ꒒ ᐯꎭꍟꌗ꓄ꂦ ꎭꂦꋪꁅꍏ", "🅾🆃🆅🅴🆉 🆃🆅🅾🆄 🅼🅰🆃 🆅 🅱🅾🆁🅳🅴🅻 🆅🅼🅴🆂🆃🅾 🅼🅾🆁🅶🅰", "『o』『t』『v』『e』『z』 『t』『v』『o』『u』 『m』『a』『t』 『v』 『b』『o』『r』『d』『e』『l』 『v』『m』『e』『s』『t』『o』 『m』『o』『r』『g』『a』", "ｏｔｖｅｚ　ｔｖｏｕ　ｍａｔ　ｖ　ｂｏｒｄｅｌ　ｖｍｅｓｔｏ　ｍｏｒｇａ",
                    "ｏｔｖｅｚ　ｔｖｏｕ　ｍａｔ　ｖ　ｂｏｒｄｅｌ　ｖｍｅｓｔｏ　ｍｏｒｇａꀤ ꍟꌃꀎ ꍟꍟ ꓄ꍏꎭ", "ꌗꂦꋪꌩꍏꈤ ꈤꂦ ꓄ꌩ 🅾🅿🅴🆁 🅿🆁🅾🆃🅸🆅 🅼🅴🅽🆈🅰『i』 『t』『e』『p』『e』『r』 『p』『i』『s』『t』『o』『l』『e』『t』 『u』 『t』『v』『o』『e』『g』『o』 『v』『i』『s』『k』『a』", "slishkom izevo slilsa mne(REPORT LES)", "🅢🅛🅘🅢🅗🅚🅞🅜 🅘🅩🅔🅥🅞 🅢🅛🅘🅛🅢🅐 🅜🅝🅔(🅡🅔🅟🅞🅡🅣 🅛🅔🅢)", "丂ㄥ丨丂卄Ҝㄖ爪 丨乙乇ᐯㄖ 丂ㄥ丨ㄥ丂卂 爪几乇(尺乇卩ㄖ尺ㄒ ㄥ乇丂)",
                    "РЕПОРТ ЛЕС ИДЕТ ЕБАШИТЬ", "РЕПОРТ ЛЕС РАСКАТАЛ ТВОЮ МАТЬ ПО ПОЛУ", "РЕПОРТ ЛЕС РАЗЬЕБАЛ ТУПУЮ ЛОХУШКУ", "РЕПОРТ ЛЕС ИДЕТ ВАС ЕБАТЬ", "РЕПОРТ ЛЕС ВЫЕБАЛ ВСЕ ЧТО ДВИЖЕТСЯ А ЧТО НЕ ДВИЖЕТСЯ НАЧАЛ ДВИГАТЬ И ТОЖЕ ВЫЕБАЛ",
                    "ꌗ꒒ꀤꌗꃅꀘꂦꎭ ꀤꁴꍟᐯꂦ ꌗ꒒ꀤ꒒ꌗꍏ ꎭꈤꍟ(ꋪꍟᖘꂦꋪ꓄ ꒒ꍟꌗ)", "🆂🅻🅸🆂🅷🅺🅾🅼 🅸🆉🅴🆅🅾 🆂🅻🅸🅻🆂🅰 🅼🅽🅴(🆁🅴🅿🅾🆁🆃 🅻🅴🆂)", "『s』『l』『i』『s』『h』『k』『o』『m』 『i』『z』『e』『v』『o』 『s』『l』『i』『l』『s』『a』 『m』『n』『e』(『R』『E』『P』『O』『R』『T』 『L』『E』『S』)", "ｓｌｉｓｈｋｏｍ　ｉｚｅｖｏ　ｓｌｉｌｓａ　ｍｎｅ(ＲＥＰＯＲＴ　ＬＥＳ)", "haha slil tya petuha", "𝖍𝖆𝖍𝖆 𝖘𝖑𝖎𝖑 𝖙𝖞𝖆 𝖕𝖊𝖙𝖚𝖍𝖆", "Ⱨ₳Ⱨ₳ ₴ⱠłⱠ ₮Ɏ₳ ₱Ɇ₮ɄⱧ₳", "𝓱𝓪𝓱𝓪 𝓼𝓵𝓲𝓵 𝓽𝔂𝓪 𝓹𝓮𝓽𝓾𝓱𝓪", "『h』『a』『h』『a』 『s』『l』『i』『l』 『t』『y』『a』 『p』『e』『t』『u』『h』『a』", "ｈａｈａ　ｓｌｉｌ　ｔｙａ　ｐｅｔｕｈａ", "卄卂卄卂 丂ㄥ丨ㄥ ㄒㄚ卂 卩乇ㄒㄩ卄卂",
                    "𝖊𝖇𝖆𝖘𝖍𝖚 𝖙𝖚𝖕𝖆", "Ɇ฿₳₴ⱧɄ ₮Ʉ₱₳", "𝓮𝓫𝓪𝓼𝓱𝓾 𝓽𝓾𝓹𝓪", "『e』『b』『a』『s』『h』『u』 『t』『u』『p』『a』", "ｅｂａｓｈｕ　ｔｕｐａ", "乇乃卂丂卄ㄩ ㄒㄩ卩卂", "𝖛𝖟𝖇𝖔𝖑𝖙𝖆𝖑 𝖙𝖞𝖆 𝖍𝖚𝖊𝖒", "VⱫ฿ØⱠ₮₳Ⱡ ₮Ɏ₳ ⱧɄɆ₥", "𝓿𝔃𝓫𝓸𝓵𝓽𝓪𝓵 𝓽𝔂𝓪 𝓱𝓾𝓮𝓶", "『v』『z』『b』『o』『l』『t』『a』『l』 『t』『y』『a』 『h』『u』『e』『m』", "ｖｚｂｏｌｔａｌ　ｔｙａ　ｈｕｅｍ", "ᐯ乙乃ㄖㄥㄒ卂ㄥ ㄒㄚ卂 卄ㄩ乇爪", "𝖘𝖔𝖘𝖊𝖘𝖍 𝖒𝖓𝖊 𝖘 𝖟𝖆𝖌𝖑𝖔𝖙𝖔𝖒", "₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ ₴ Ⱬ₳₲ⱠØ₮Ø₥", "𝓼𝓸𝓼𝓮𝓼𝓱 𝓶𝓷𝓮 𝓼 𝔃𝓪𝓰𝓵𝓸𝓽𝓸𝓶", "『s』『o』『s』『e』『s』『h』 『m』『n』『e』 『s』 『z』『a』『g』『l』『o』『t』『o』『m』", "ｖｚｂｏｌｔａｌ　ｔｙａ　ｈｕｅｍ", "ᐯ乙乃ㄖㄥㄒ卂ㄥ ㄒㄚ卂 卄ㄩ乇爪", 
                    "𝖊𝖇𝖚 𝖙𝖛𝖔𝖚 𝖒𝖆𝖙 𝖒𝖓𝖊 𝖘𝖐𝖚𝖘𝖍𝖓𝖔 𝖍𝖏𝖈𝖍𝖊𝖙𝖘𝖆 𝖘𝖕𝖆𝖙", "Ɇ฿Ʉ ₮VØɄ ₥₳₮ ₥₦Ɇ ₴₭Ʉ₴Ⱨ₦Ø ⱧJ₵ⱧɆ₮₴₳ ₴₱₳₮", "𝓮𝓫𝓾 𝓽𝓿𝓸𝓾 𝓶𝓪𝓽 𝓶𝓷𝓮 𝓼𝓴𝓾𝓼𝓱𝓷𝓸 𝓱𝓳𝓬𝓱𝓮𝓽𝓼𝓪 𝓼𝓹𝓪𝓽", "『e』『b』『u』 『t』『v』『o』『u』 『m』『a』『t』 『m』『n』『e』 『s』『k』『u』『s』『h』『n』『o』 『h』『j』『c』『h』『e』『t』『s』『a』 『s』『p』『a』『t』", "ｅｂｕ　ｔｖｏｕ　ｍａｔ　ｍｎｅ　ｓｋｕｓｈｎｏ　ｈｊｃｈｅｔｓａ　ｓｐａｔ", "乇乃ㄩ ㄒᐯㄖㄩ 爪卂ㄒ 爪几乇 丂Ҝㄩ丂卄几ㄖ 卄ﾌ匚卄乇ㄒ丂卂 丂卩卂ㄒ",
                    "𝖎𝖟𝖛𝖎𝖓𝖎 𝖊𝖇𝖞 𝖙𝖞𝖆", "łⱫVł₦ł Ɇ฿Ɏ ₮Ɏ₳", "𝓲𝔃𝓿𝓲𝓷𝓲 𝓮𝓫𝔂 𝓽𝔂𝓪", "『i』『z』『v』『i』『n』『i』 『e』『b』『y』 『t』『y』『a』", "ｉｚｖｉｎｉ　ｅｂｙ　ｔｙａ", "丨乙ᐯ丨几丨 乇乃ㄚ ㄒㄚ卂", "", "", "", "", "", "", 
                    "𝖊𝖇𝖚 𝖙𝖞𝖆 𝖔𝖙𝖛𝖊𝖗𝖙𝖐𝖆𝖎", "Ɇ฿Ʉ ₮Ɏ₳ Ø₮VɆⱤ₮₭₳ł", "𝓮𝓫𝓾 𝓽𝔂𝓪 𝓸𝓽𝓿𝓮𝓻𝓽𝓴𝓪𝓲", "『e』『b』『u』 『t』『y』『a』 『o』『t』『v』『e』『r』『t』『k』『a』『i』", "ｅｂｕ　ｔｙａ　ｏｔｖｅｒｔｋａｉ", "乇乃ㄩ ㄒㄚ卂 ㄖㄒᐯ乇尺ㄒҜ卂丨",
                    "𝖚𝖊𝖇𝖚 𝖙𝖊𝖇𝖞𝖆 𝖟𝖆𝖑𝖚𝖕𝖆𝖎 𝖐𝖗𝖆𝖘𝖎𝖛𝖆", "ɄɆ฿Ʉ ₮Ɇ฿Ɏ₳ Ⱬ₳ⱠɄ₱₳ł ₭Ɽ₳₴łV₳", "𝓾𝓮𝓫𝓾 𝓽𝓮𝓫𝔂𝓪 𝔃𝓪𝓵𝓾𝓹𝓪𝓲 𝓴𝓻𝓪𝓼𝓲𝓿𝓪", "『u』『e』『b』『u』 『t』『e』『b』『y』『a』 『z』『a』『l』『u』『p』『a』『i』 『k』『r』『a』『s』『i』『v』『a』", "ｕｅｂｕ　ｔｅｂｙａ　ｚａｌｕｐａｉ　ｋｒａｓｉｖａ", "ㄩ乇乃ㄩ ㄒ乇乃ㄚ卂 乙卂ㄥㄩ卩卂丨 Ҝ尺卂丂丨ᐯ卂",
                    "𝖍𝖚𝖞𝖆𝖗𝖚 𝖙𝖊𝖇𝖞𝖆 𝖆𝖍𝖚𝖊𝖓𝖔", "ⱧɄɎ₳ⱤɄ ₮Ɇ฿Ɏ₳ ₳ⱧɄɆ₦Ø", "𝓱𝓾𝔂𝓪𝓻𝓾 𝓽𝓮𝓫𝔂𝓪 𝓪𝓱𝓾𝓮𝓷𝓸", "『h』『u』『y』『a』『r』『u』 『t』『e』『b』『y』『a』 『a』『h』『u』『e』『n』『o』", "ｈｕｙａｒｕ　ｔｅｂｙａ　ａｈｕｅｎｏ", "卄ㄩㄚ卂尺ㄩ ㄒ乇乃ㄚ卂 卂卄ㄩ乇几ㄖ",
                    "𝖆𝖍𝖊𝖗𝖊𝖓𝖆 𝖛𝖟'𝖊𝖇𝖆𝖑 𝖙𝖞𝖆 =𝕯", "₳ⱧɆⱤɆ₦₳ VⱫ'Ɇ฿₳Ⱡ ₮Ɏ₳ =Đ", "𝓪𝓱𝓮𝓻𝓮𝓷𝓪 𝓿𝔃'𝓮𝓫𝓪𝓵 𝓽𝔂𝓪 =𝓓", "『a』『h』『e』『r』『e』『n』『a』 『v』『z』'『e』『b』『a』『l』 『t』『y』『a』 =『D』", "ａｈｅｒｅｎａ　ｖｚ'ｅｂａｌ　ｔｙａ　=Ｄ", "卂卄乇尺乇几卂 ᐯ乙'乇乃卂ㄥ ㄒㄚ卂 =ᗪ",
                    "𝖞𝖆 𝖕𝖔𝖛𝖊𝖘𝖎𝖑 𝖙𝖊𝖇𝖞𝖆 𝖓𝖆 𝖐𝖎𝖘𝖍𝖐𝖆𝖍 𝖙𝖛𝖔𝖊𝖎 𝖒𝖆𝖙𝖊𝖗𝖎 𝖎 𝖓𝖆𝖘𝖗𝖆𝖑 𝖙𝖛𝖔𝖊𝖒𝖚 𝖔𝖙𝖈𝖚 𝖛 𝖒𝖔𝖟𝖌", "Ɏ₳ ₱ØVɆ₴łⱠ ₮Ɇ฿Ɏ₳ ₦₳ ₭ł₴Ⱨ₭₳Ⱨ ₮VØɆł ₥₳₮ɆⱤł ł ₦₳₴Ɽ₳Ⱡ ₮VØɆ₥Ʉ Ø₮₵Ʉ V ₥ØⱫ₲", "𝔂𝓪 𝓹𝓸𝓿𝓮𝓼𝓲𝓵 𝓽𝓮𝓫𝔂𝓪 𝓷𝓪 𝓴𝓲𝓼𝓱𝓴𝓪𝓱 𝓽𝓿𝓸𝓮𝓲 𝓶𝓪𝓽𝓮𝓻𝓲 𝓲 𝓷𝓪𝓼𝓻𝓪𝓵 𝓽𝓿𝓸𝓮𝓶𝓾 𝓸𝓽𝓬𝓾 𝓿 𝓶𝓸𝔃𝓰", "『y』『a』 『p』『o』『v』『e』『s』『i』『l』 『t』『e』『b』『y』『a』 『n』『a』 『k』『i』『s』『h』『k』『a』『h』 『t』『v』『o』『e』『i』 『m』『a』『t』『e』『r』『i』 『i』 『n』『a』『s』『r』『a』『l』 『t』『v』『o』『e』『m』『u』 『o』『t』『c』『u』 『v』 『m』『o』『z』『g』", "ｙａ　ｐｏｖｅｓｉｌ　ｔｅｂｙａ　ｎａ　ｋｉｓｈｋａｈ　ｔｖｏｅｉ　ｍａｔｅｒｉ　ｉ　ｎａｓｒａｌ　ｔｖｏｅｍｕ　ｏｔｃｕ　ｖ　ｍｏｚｇ", "ㄚ卂 卩ㄖᐯ乇丂丨ㄥ ㄒ乇乃ㄚ卂 几卂 Ҝ丨丂卄Ҝ卂卄 ㄒᐯㄖ乇丨 爪卂ㄒ乇尺丨 丨 几卂丂尺卂ㄥ ㄒᐯㄖ乇爪ㄩ ㄖㄒ匚ㄩ ᐯ 爪ㄖ乙Ꮆ",
                    "𝖉𝖎𝖐𝖆 𝖆𝖙𝖘𝖆𝖘𝖆𝖑 𝖒𝖓𝖊 𝖕𝖔𝖉 𝖙𝖗𝖊𝖐 𝖒𝖔𝖗𝖌𝖊𝖓𝖘𝖍𝖙𝖊𝖗𝖓𝖆", "Đł₭₳ ₳₮₴₳₴₳Ⱡ ₥₦Ɇ ₱ØĐ ₮ⱤɆ₭ ₥ØⱤ₲Ɇ₦₴Ⱨ₮ɆⱤ₦₳", "𝓭𝓲𝓴𝓪 𝓪𝓽𝓼𝓪𝓼𝓪𝓵 𝓶𝓷𝓮 𝓹𝓸𝓭 𝓽𝓻𝓮𝓴 𝓶𝓸𝓻𝓰𝓮𝓷𝓼𝓱𝓽𝓮𝓻𝓷𝓪", "『d』『i』『k』『a』 『a』『t』『s』『a』『s』『a』『l』 『m』『n』『e』 『p』『o』『d』 『t』『r』『e』『k』 『m』『o』『r』『g』『e』『n』『s』『h』『t』『e』『r』『n』『a』", "ｄｉｋａ　ａｔｓａｓａｌ　ｍｎｅ　ｐｏｄ　ｔｒｅｋ　ｍｏｒｇｅｎｓｈｔｅｒｎａ", "ᗪ丨Ҝ卂 卂ㄒ丂卂丂卂ㄥ 爪几乇 卩ㄖᗪ ㄒ尺乇Ҝ 爪ㄖ尺Ꮆ乇几丂卄ㄒ乇尺几卂",
                    "𝖟𝖆𝖐𝖗𝖔𝖎 𝖗𝖔𝖙 𝖕𝖔𝖐𝖆 𝖞𝖆 𝖙𝖛𝖔𝖚 𝖒𝖆𝖙' 𝖓𝖊 𝖛𝖞𝖊𝖇𝖆𝖑 𝖘𝖓𝖔𝖛𝖆", "Ⱬ₳₭ⱤØł ⱤØ₮ ₱Ø₭₳ Ɏ₳ ₮VØɄ ₥₳₮' ₦Ɇ VɎɆ฿₳Ⱡ ₴₦ØV₳", "𝔃𝓪𝓴𝓻𝓸𝓲 𝓻𝓸𝓽 𝓹𝓸𝓴𝓪 𝔂𝓪 𝓽𝓿𝓸𝓾 𝓶𝓪𝓽' 𝓷𝓮 𝓿𝔂𝓮𝓫𝓪𝓵 𝓼𝓷𝓸𝓿𝓪", "『z』『a』『k』『r』『o』『i』 『r』『o』『t』 『p』『o』『k』『a』 『y』『a』 『t』『v』『o』『u』 『m』『a』『t』' 『n』『e』 『v』『y』『e』『b』『a』『l』 『s』『n』『o』『v』『a』", "ｚａｋｒｏｉ　ｒｏｔ　ｐｏｋａ　ｙａ　ｔｖｏｕ　ｍａｔ'　ｎｅ　ｖｙｅｂａｌ　ｓｎｏｖａ", "乙卂Ҝ尺ㄖ丨 尺ㄖㄒ 卩ㄖҜ卂 ㄚ卂 ㄒᐯㄖㄩ 爪卂ㄒ' 几乇 ᐯㄚ乇乃卂ㄥ 丂几ㄖᐯ卂",
                    "𝖕𝖔𝖈𝖍𝖊𝖒𝖚 𝖓𝖔𝖊𝖘𝖍, 𝖔𝖕𝖞𝖆𝖙' 𝖒𝖔𝖊𝖌𝖔 𝖍𝖚𝖞𝖆 𝖓𝖊 𝖉𝖔𝖘𝖙𝖆𝖑𝖔𝖘?", "₱Ø₵ⱧɆ₥Ʉ ₦ØɆ₴Ⱨ, Ø₱Ɏ₳₮' ₥ØɆ₲Ø ⱧɄɎ₳ ₦Ɇ ĐØ₴₮₳ⱠØ₴?", "𝓹𝓸𝓬𝓱𝓮𝓶𝓾 𝓷𝓸𝓮𝓼𝓱, 𝓸𝓹𝔂𝓪𝓽' 𝓶𝓸𝓮𝓰𝓸 𝓱𝓾𝔂𝓪 𝓷𝓮 𝓭𝓸𝓼𝓽𝓪𝓵𝓸𝓼?", "『p』『o』『c』『h』『e』『m』『u』 『n』『o』『e』『s』『h』, 『o』『p』『y』『a』『t』' 『m』『o』『e』『g』『o』 『h』『u』『y』『a』 『n』『e』 『d』『o』『s』『t』『a』『l』『o』『s』?", "ｐｏｃｈｅｍｕ　ｎｏｅｓｈ,　ｏｐｙａｔ'　ｍｏｅｇｏ　ｈｕｙａ　ｎｅ　ｄｏｓｔａｌｏｓ?", "卩ㄖ匚卄乇爪ㄩ 几ㄖ乇丂卄, ㄖ卩ㄚ卂ㄒ' 爪ㄖ乇Ꮆㄖ 卄ㄩㄚ卂 几乇 ᗪㄖ丂ㄒ卂ㄥㄖ丂?",
                    "𝖙𝖞 𝖟𝖆𝖈𝖍𝖊𝖒 𝖔𝖙 𝖒𝖔𝖊𝖌𝖔 𝖍𝖚𝖞𝖆 𝖛 𝖘𝖙𝖗𝖆𝖍𝖊 𝖇𝖊𝖟𝖍𝖎𝖘𝖍, 𝖓𝖆𝖕𝖚𝖌𝖆𝖓 𝖌𝖎𝖌𝖆𝖓𝖙𝖘𝖐𝖎𝖒𝖎 𝖗𝖆𝖟𝖒𝖊𝖗𝖆𝖒𝖎 𝖈𝖍𝖙𝖔𝖑𝖎?", "₮Ɏ Ⱬ₳₵ⱧɆ₥ Ø₮ ₥ØɆ₲Ø ⱧɄɎ₳ V ₴₮Ɽ₳ⱧɆ ฿ɆⱫⱧł₴Ⱨ, ₦₳₱Ʉ₲₳₦ ₲ł₲₳₦₮₴₭ł₥ł Ɽ₳Ⱬ₥ɆⱤ₳₥ł ₵Ⱨ₮ØⱠł?", "𝓽𝔂 𝔃𝓪𝓬𝓱𝓮𝓶 𝓸𝓽 𝓶𝓸𝓮𝓰𝓸 𝓱𝓾𝔂𝓪 𝓿 𝓼𝓽𝓻𝓪𝓱𝓮 𝓫𝓮𝔃𝓱𝓲𝓼𝓱, 𝓷𝓪𝓹𝓾𝓰𝓪𝓷 𝓰𝓲𝓰𝓪𝓷𝓽𝓼𝓴𝓲𝓶𝓲 𝓻𝓪𝔃𝓶𝓮𝓻𝓪𝓶𝓲 𝓬𝓱𝓽𝓸𝓵𝓲?", "『t』『y』 『z』『a』『c』『h』『e』『m』 『o』『t』 『m』『o』『e』『g』『o』 『h』『u』『y』『a』 『v』 『s』『t』『r』『a』『h』『e』 『b』『e』『z』『h』『i』『s』『h』, 『n』『a』『p』『u』『g』『a』『n』 『g』『i』『g』『a』『n』『t』『s』『k』『i』『m』『i』 『r』『a』『z』『m』『e』『r』『a』『m』『i』 『c』『h』『t』『o』『l』『i』?", "ｔｙ　ｚａｃｈｅｍ　ｏｔ　ｍｏｅｇｏ　ｈｕｙａ　ｖ　ｓｔｒａｈｅ　ｂｅｚｈｉｓｈ,　ｎａｐｕｇａｎ　ｇｉｇａｎｔｓｋｉｍｉ　ｒａｚｍｅｒａｍｉ　ｃｈｔｏｌｉ?", "ㄒㄚ 乙卂匚卄乇爪 ㄖㄒ 爪ㄖ乇Ꮆㄖ 卄ㄩㄚ卂 ᐯ 丂ㄒ尺卂卄乇 乃乇乙卄丨丂卄, 几卂卩ㄩᎶ卂几 Ꮆ丨Ꮆ卂几ㄒ丂Ҝ丨爪丨 尺卂乙爪乇尺卂爪丨 匚卄ㄒㄖㄥ丨?",
                    "𝖐𝖆𝖐 𝖟𝖍𝖊 𝖘𝖑𝖆𝖉𝖐𝖔 𝖛𝖞𝖊𝖇𝖆𝖑 𝖙𝖛𝖔𝖚 𝖒𝖆𝖙' 𝖛𝖈𝖍𝖊𝖗𝖆, 𝖔𝖓𝖆 𝖙𝖆𝖐 𝖘𝖙𝖔𝖓𝖆𝖑𝖆, 𝖒𝖓𝖊 𝖉𝖆𝖟𝖍𝖊 𝖟𝖍𝖆𝖑𝖐𝖔 𝖊𝖊 𝖘𝖙𝖆𝖑𝖔, 𝖟𝖍𝖆𝖑 𝖈𝖍𝖙𝖔 𝖞𝖆 𝖘𝖑𝖚𝖈𝖍𝖆𝖎𝖓𝖔 𝖚𝖇𝖎𝖑 𝖊𝖊 𝖘𝖛𝖔𝖎𝖒 𝖍𝖚𝖊𝖒", "₭₳₭ ⱫⱧɆ ₴Ⱡ₳Đ₭Ø VɎɆ฿₳Ⱡ ₮VØɄ ₥₳₮' V₵ⱧɆⱤ₳, Ø₦₳ ₮₳₭ ₴₮Ø₦₳Ⱡ₳, ₥₦Ɇ Đ₳ⱫⱧɆ ⱫⱧ₳Ⱡ₭Ø ɆɆ ₴₮₳ⱠØ, ⱫⱧ₳Ⱡ ₵Ⱨ₮Ø Ɏ₳ ₴ⱠɄ₵Ⱨ₳ł₦Ø Ʉ฿łⱠ ɆɆ ₴VØł₥ ⱧɄɆ₥", "𝓴𝓪𝓴 𝔃𝓱𝓮 𝓼𝓵𝓪𝓭𝓴𝓸 𝓿𝔂𝓮𝓫𝓪𝓵 𝓽𝓿𝓸𝓾 𝓶𝓪𝓽' 𝓿𝓬𝓱𝓮𝓻𝓪, 𝓸𝓷𝓪 𝓽𝓪𝓴 𝓼𝓽𝓸𝓷𝓪𝓵𝓪, 𝓶𝓷𝓮 𝓭𝓪𝔃𝓱𝓮 𝔃𝓱𝓪𝓵𝓴𝓸 𝓮𝓮 𝓼𝓽𝓪𝓵𝓸, 𝔃𝓱𝓪𝓵 𝓬𝓱𝓽𝓸 𝔂𝓪 𝓼𝓵𝓾𝓬𝓱𝓪𝓲𝓷𝓸 𝓾𝓫𝓲𝓵 𝓮𝓮 𝓼𝓿𝓸𝓲𝓶 𝓱𝓾𝓮𝓶", "『k』『a』『k』 『z』『h』『e』 『s』『l』『a』『d』『k』『o』 『v』『y』『e』『b』『a』『l』 『t』『v』『o』『u』 『m』『a』『t』' 『v』『c』『h』『e』『r』『a』, 『o』『n』『a』 『t』『a』『k』 『s』『t』『o』『n』『a』『l』『a』, 『m』『n』『e』 『d』『a』『z』『h』『e』 『z』『h』『a』『l』『k』『o』 『e』『e』 『s』『t』『a』『l』『o』, 『z』『h』『a』『l』 『c』『h』『t』『o』 『y』『a』 『s』『l』『u』『c』『h』『a』『i』『n』『o』 『u』『b』『i』『l』 『e』『e』 『s』『v』『o』『i』『m』 『h』『u』『e』『m』", "ｋａｋ　ｚｈｅ　ｓｌａｄｋｏ　ｖｙｅｂａｌ　ｔｖｏｕ　ｍａｔ'　ｖｃｈｅｒａ,　ｏｎａ　ｔａｋ　ｓｔｏｎａｌａ,　ｍｎｅ　ｄａｚｈｅ　ｚｈａｌｋｏ　ｅｅ　ｓｔａｌｏ,　ｚｈａｌ　ｃｈｔｏ　ｙａ　ｓｌｕｃｈａｉｎｏ　ｕｂｉｌ　ｅｅ　ｓｖｏｉｍ　ｈｕｅｍ", "Ҝ卂Ҝ 乙卄乇 丂ㄥ卂ᗪҜㄖ ᐯㄚ乇乃卂ㄥ ㄒᐯㄖㄩ 爪卂ㄒ' ᐯ匚卄乇尺卂, ㄖ几卂 ㄒ卂Ҝ 丂ㄒㄖ几卂ㄥ卂, 爪几乇 ᗪ卂乙卄乇 乙卄卂ㄥҜㄖ 乇乇 丂ㄒ卂ㄥㄖ, 乙卄卂ㄥ 匚卄ㄒㄖ ㄚ卂 丂ㄥㄩ匚卄卂丨几ㄖ ㄩ乃丨ㄥ 乇乇 丂ᐯㄖ丨爪 卄ㄩ乇爪",
                    "𝖒𝖆𝖒𝖚 𝖙𝖛𝖔𝖞𝖚 𝖊𝖇𝖆𝖑 𝖑𝖊𝖌𝖐𝖔)", "₥₳₥Ʉ ₮VØɎɄ Ɇ฿₳Ⱡ ⱠɆ₲₭Ø)", "𝓶𝓪𝓶𝓾 𝓽𝓿𝓸𝔂𝓾 𝓮𝓫𝓪𝓵 𝓵𝓮𝓰𝓴𝓸)", "『m』『a』『m』『u』 『t』『v』『o』『y』『u』 『e』『b』『a』『l』 『l』『e』『g』『k』『o』)", "ｍａｍｕ　ｔｖｏｙｕ　ｅｂａｌ　ｌｅｇｋｏ)", "爪卂爪ㄩ ㄒᐯㄖㄚㄩ 乇乃卂ㄥ ㄥ乇ᎶҜㄖ)",
                    "𝖍𝖚𝖊𝖘𝖔𝖘 𝖞𝖆 𝖙𝖛𝖔𝖞𝖚 𝖒𝖆𝖒𝖐𝖚 𝖘𝖔𝖙𝖓𝖎 𝖗𝖆𝖟 𝖕𝖊𝖗𝖊𝖊𝖇𝖆𝖑 𝖓𝖆 𝖕𝖔𝖘𝖙𝖊𝖑𝖊 𝖌𝖉𝖊 𝖙𝖎 𝖘𝖕𝖎𝖘𝖍)", "ⱧɄɆ₴Ø₴ Ɏ₳ ₮VØɎɄ ₥₳₥₭Ʉ ₴Ø₮₦ł Ɽ₳Ⱬ ₱ɆⱤɆɆ฿₳Ⱡ ₦₳ ₱Ø₴₮ɆⱠɆ ₲ĐɆ ₮ł ₴₱ł₴Ⱨ)", "𝓱𝓾𝓮𝓼𝓸𝓼 𝔂𝓪 𝓽𝓿𝓸𝔂𝓾 𝓶𝓪𝓶𝓴𝓾 𝓼𝓸𝓽𝓷𝓲 𝓻𝓪𝔃 𝓹𝓮𝓻𝓮𝓮𝓫𝓪𝓵 𝓷𝓪 𝓹𝓸𝓼𝓽𝓮𝓵𝓮 𝓰𝓭𝓮 𝓽𝓲 𝓼𝓹𝓲𝓼𝓱)", "『h』『u』『e』『s』『o』『s』 『y』『a』 『t』『v』『o』『y』『u』 『m』『a』『m』『k』『u』 『s』『o』『t』『n』『i』 『r』『a』『z』 『p』『e』『r』『e』『e』『b』『a』『l』 『n』『a』 『p』『o』『s』『t』『e』『l』『e』 『g』『d』『e』 『t』『i』 『s』『p』『i』『s』『h』)", "ｈｕｅｓｏｓ　ｙａ　ｔｖｏｙｕ　ｍａｍｋｕ　ｓｏｔｎｉ　ｒａｚ　ｐｅｒｅｅｂａｌ　ｎａ　ｐｏｓｔｅｌｅ　ｇｄｅ　ｔｉ　ｓｐｉｓｈ)", "卄ㄩ乇丂ㄖ丂 ㄚ卂 ㄒᐯㄖㄚㄩ 爪卂爪Ҝㄩ 丂ㄖㄒ几丨 尺卂乙 卩乇尺乇乇乃卂ㄥ 几卂 卩ㄖ丂ㄒ乇ㄥ乇 Ꮆᗪ乇 ㄒ丨 丂卩丨丂卄)",
                    "𝖙𝖛𝖔𝖊𝖌𝖔 𝖔𝖙𝖈𝖍𝖎𝖒𝖆 𝖓𝖆 𝖟𝖔𝖓𝖚 𝖔𝖙𝖕𝖗𝖆𝖛𝖎𝖑 𝖌𝖉𝖊 𝖊𝖌𝖔 𝖊𝖇𝖆𝖑𝖎 𝖐𝖆𝖐 𝖙𝖛𝖔𝖞𝖚 𝖒𝖆𝖙`", "₮VØɆ₲Ø Ø₮₵Ⱨł₥₳ ₦₳ ⱫØ₦Ʉ Ø₮₱Ɽ₳VłⱠ ₲ĐɆ Ɇ₲Ø Ɇ฿₳Ⱡł ₭₳₭ ₮VØɎɄ ₥₳₮`", "𝓽𝓿𝓸𝓮𝓰𝓸 𝓸𝓽𝓬𝓱𝓲𝓶𝓪 𝓷𝓪 𝔃𝓸𝓷𝓾 𝓸𝓽𝓹𝓻𝓪𝓿𝓲𝓵 𝓰𝓭𝓮 𝓮𝓰𝓸 𝓮𝓫𝓪𝓵𝓲 𝓴𝓪𝓴 𝓽𝓿𝓸𝔂𝓾 𝓶𝓪𝓽`", "『t』『v』『o』『e』『g』『o』 『o』『t』『c』『h』『i』『m』『a』 『n』『a』 『z』『o』『n』『u』 『o』『t』『p』『r』『a』『v』『i』『l』 『g』『d』『e』 『e』『g』『o』 『e』『b』『a』『l』『i』 『k』『a』『k』 『t』『v』『o』『y』『u』 『m』『a』『t』`", "ｔｖｏｅｇｏ　ｏｔｃｈｉｍａ　ｎａ　ｚｏｎｕ　ｏｔｐｒａｖｉｌ　ｇｄｅ　ｅｇｏ　ｅｂａｌｉ　ｋａｋ　ｔｖｏｙｕ　ｍａｔ`", "ㄒᐯㄖ乇Ꮆㄖ ㄖㄒ匚卄丨爪卂 几卂 乙ㄖ几ㄩ ㄖㄒ卩尺卂ᐯ丨ㄥ Ꮆᗪ乇 乇Ꮆㄖ 乇乃卂ㄥ丨 Ҝ卂Ҝ ㄒᐯㄖㄚㄩ 爪卂ㄒ`",
                    "𝖘𝖔𝖘𝖊𝖘𝖍 𝖒𝖓𝖊 𝖘 𝖐𝖆𝖎𝖋𝖆𝖒𝖎", "₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ ₴ ₭₳ł₣₳₥ł", "𝓼𝓸𝓼𝓮𝓼𝓱 𝓶𝓷𝓮 𝓼 𝓴𝓪𝓲𝓯𝓪𝓶𝓲", "『s』『o』『s』『e』『s』『h』 『m』『n』『e』 『s』 『k』『a』『i』『f』『a』『m』『i』", "ｓｏｓｅｓｈ　ｍｎｅ　ｓ　ｋａｉｆａｍｉ", "丂ㄖ丂乇丂卄 爪几乇 丂 Ҝ卂丨千卂爪丨",
                    "Ⱬ₳₮Ɽ₳Ⱨ₳Ⱡ ĐØ ₴₥ɆⱤ₮ł ₮VØɄ ₥₳₮'", "𝔃𝓪𝓽𝓻𝓪𝓱𝓪𝓵 𝓭𝓸 𝓼𝓶𝓮𝓻𝓽𝓲 𝓽𝓿𝓸𝓾 𝓶𝓪𝓽'", "『z』『a』『t』『r』『a』『h』『a』『l』 『d』『o』 『s』『m』『e』『r』『t』『i』 『t』『v』『o』『u』 『m』『a』『t』'", "ｚａｔｒａｈａｌ　ｄｏ　ｓｍｅｒｔｉ　ｔｖｏｕ　ｍａｔ'", "乙卂ㄒ尺卂卄卂ㄥ ᗪㄖ 丂爪乇尺ㄒ丨 ㄒᐯㄖㄩ 爪卂ㄒ'",
                    "ĐØ ₱Ø₴ł₦Ɇ₦łɎ₳ Ɇ฿Ʉ ₮Ɇ฿Ɏ₳", "𝓭𝓸 𝓹𝓸𝓼𝓲𝓷𝓮𝓷𝓲𝔂𝓪 𝓮𝓫𝓾 𝓽𝓮𝓫𝔂𝓪", "『d』『o』 『p』『o』『s』『i』『n』『e』『n』『i』『y』『a』 『e』『b』『u』 『t』『e』『b』『y』『a』", "ｄｏ　ｐｏｓｉｎｅｎｉｙａ　ｅｂｕ　ｔｅｂｙａ", "ᗪㄖ 卩ㄖ丂丨几乇几丨ㄚ卂 乇乃ㄩ ㄒ乇乃ㄚ卂",
                    "₴Ⱡł₴Ⱨ₭Ø₥ ₭ⱤɄ₮Ø ₳₮₴₳₴₳Ⱡ ₥₦Ɇ", "𝓼𝓵𝓲𝓼𝓱𝓴𝓸𝓶 𝓴𝓻𝓾𝓽𝓸 𝓪𝓽𝓼𝓪𝓼𝓪𝓵 𝓶𝓷𝓮", "『s』『l』『i』『s』『h』『k』『o』『m』 『k』『r』『u』『t』『o』 『a』『t』『s』『a』『s』『a』『l』 『m』『n』『e』", "ｓｌｉｓｈｋｏｍ　ｋｒｕｔｏ　ａｔｓａｓａｌ　ｍｎｅ", "丂ㄥ丨丂卄Ҝㄖ爪 Ҝ尺ㄩㄒㄖ 卂ㄒ丂卂丂卂ㄥ 爪几乇",
                    "VɎɆ฿₳Ⱡ ₮VØɄ ₥₳₮' VɆ₮₭Øł", "🆅🆈🅴🅱🅰🅻 🆃🆅🅾🆄 🅼🅰🆃' 🆅🅴🆃🅺🅾🅸", "『v』『y』『e』『b』『a』『l』 『t』『v』『o』『u』 『m』『a』『t』' 『v』『e』『t』『k』『o』『i』", "ｖｙｅｂａｌ　ｔｖｏｕ　ｍａｔ'　ｖｅｔｋｏｉ", "ᐯㄚ乇乃卂ㄥ ㄒᐯㄖㄩ 爪卂ㄒ' ᐯ乇ㄒҜㄖ丨",
                    "Ⱬ₳₴Ʉ₦ɄⱠ V ₮VØɆ Ø₵Ⱨ₭Ø ₳Ɽ₥₳₮ɄⱤɄ", "🆉🅰🆂🆄🅽🆄🅻 🆅 🆃🆅🅾🅴 🅾🅲🅷🅺🅾 🅰🆁🅼🅰🆃🆄🆁🆄", "『z』『a』『s』『u』『n』『u』『l』 『v』 『t』『v』『o』『e』 『o』『c』『h』『k』『o』 『a』『r』『m』『a』『t』『u』『r』『u』", "ｚａｓｕｎｕｌ　ｖ　ｔｖｏｅ　ｏｃｈｋｏ　ａｒｍａｔｕｒｕ", "乙卂丂ㄩ几ㄩㄥ ᐯ ㄒᐯㄖ乇 ㄖ匚卄Ҝㄖ 卂尺爪卂ㄒㄩ尺ㄩ",
                    "Ɇ฿₳₴ⱧɄ ₮Ɇ฿Ɏ₳ ₱Ø₭₳ ₮Ɏ ₴₱ł₴Ⱨ ₦₳ ₥ØɆ₥ ⱧɄɆ, ₴ØⱤⱤɎ ₦Ø Ɏ₳ Ʉ฿łⱠ ₮VØɆ₲Ø Ø₮₵₳", "🅴🅱🅰🆂🅷🆄 🆃🅴🅱🆈🅰 🅿🅾🅺🅰 🆃🆈 🆂🅿🅸🆂🅷 🅽🅰 🅼🅾🅴🅼 🅷🆄🅴, 🆂🅾🆁🆁🆈 🅽🅾 🆈🅰 🆄🅱🅸🅻 🆃🆅🅾🅴🅶🅾 🅾🆃🅲🅰", "『e』『b』『a』『s』『h』『u』 『t』『e』『b』『y』『a』 『p』『o』『k』『a』 『t』『y』 『s』『p』『i』『s』『h』 『n』『a』 『m』『o』『e』『m』 『h』『u』『e』, 『s』『o』『r』『r』『y』 『n』『o』 『y』『a』 『u』『b』『i』『l』 『t』『v』『o』『e』『g』『o』 『o』『t』『c』『a』", "ｅｂａｓｈｕ　ｔｅｂｙａ　ｐｏｋａ　ｔｙ　ｓｐｉｓｈ　ｎａ　ｍｏｅｍ　ｈｕｅ,　ｓｏｒｒｙ　ｎｏ　ｙａ　ｕｂｉｌ　ｔｖｏｅｇｏ　ｏｔｃａ", "乇乃卂丂卄ㄩ ㄒ乇乃ㄚ卂 卩ㄖҜ卂 ㄒㄚ 丂卩丨丂卄 几卂 爪ㄖ乇爪 卄ㄩ乇, 丂ㄖ尺尺ㄚ 几ㄖ ㄚ卂 ㄩ乃丨ㄥ ㄒᐯㄖ乇Ꮆㄖ ㄖㄒ匚卂",
                    "₴Ø₴ɆⱧ ₭₳₭ ₦Ɇ₱Ɽł₦ɄⱫⱧ₣Ɇ₦₦Ɏł", "🆂🅾🆂🅴🅷 🅺🅰🅺 🅽🅴🅿🆁🅸🅽🆄🆉🅷🅵🅴🅽🅽🆈🅸", "『s』『o』『s』『e』『h』 『k』『a』『k』 『n』『e』『p』『r』『i』『n』『u』『z』『h』『f』『e』『n』『n』『y』『i』", "ｓｏｓｅｈ　ｋａｋ　ｎｅｐｒｉｎｕｚｈｆｅｎｎｙｉ", "丂ㄖ丂乇卄 Ҝ卂Ҝ 几乇卩尺丨几ㄩ乙卄千乇几几ㄚ丨",
                    "₮Ɏ ₦₳ ₥ØɆ₥ ⱧɄɄ ₱Ø₮ɆɆ₴Ⱨ ₭₳₭ Ɇ฿Ⱡ₳₦", "🆃🆈 🅽🅰 🅼🅾🅴🅼 🅷🆄🆄 🅿🅾🆃🅴🅴🆂🅷 🅺🅰🅺 🅴🅱🅻🅰🅽", "『t』『y』 『n』『a』 『m』『o』『e』『m』 『h』『u』『u』 『p』『o』『t』『e』『e』『s』『h』 『k』『a』『k』 『e』『b』『l』『a』『n』", "ｔｙ　ｎａ　ｍｏｅｍ　ｈｕｕ　ｐｏｔｅｅｓｈ　ｋａｋ　ｅｂｌａｎ", "ㄒㄚ 几卂 爪ㄖ乇爪 卄ㄩㄩ 卩ㄖㄒ乇乇丂卄 Ҝ卂Ҝ 乇乃ㄥ卂几",
                    "₴ØⱤⱤɎ Ʉ฿łⱠ ₮VØɄ ĐɆVɄ₴Ⱨ₭Ʉ ⱠØ₱₳₮₳ł", "🆂🅾🆁🆁🆈 🆄🅱🅸🅻 🆃🆅🅾🆄 🅳🅴🆅🆄🆂🅷🅺🆄 🅻🅾🅿🅰🆃🅰🅸", "『s』『o』『r』『r』『y』 『u』『b』『i』『l』 『t』『v』『o』『u』 『d』『e』『v』『u』『s』『h』『k』『u』 『l』『o』『p』『a』『t』『a』『i』", "ｓｏｒｒｙ　ｕｂｉｌ　ｔｖｏｕ　ｄｅｖｕｓｈｋｕ　ｌｏｐａｔａｉ", "丂ㄖ尺尺ㄚ ㄩ乃丨ㄥ ㄒᐯㄖㄩ ᗪ乇ᐯㄩ丂卄Ҝㄩ ㄥㄖ卩卂ㄒ卂丨",
                    "₴ØⱤⱤɎ ₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ ₭₳₭ ĐɆ฿", "🆂🅾🆁🆁🆈 🆂🅾🆂🅴🆂🅷 🅼🅽🅴 🅺🅰🅺 🅳🅴🅱", "『s』『o』『r』『r』『y』 『s』『o』『s』『e』『s』『h』 『m』『n』『e』 『k』『a』『k』 『d』『e』『b』", "ｓｏｒｒｙ　ｓｏｓｅｓｈ　ｍｎｅ　ｋａｋ　ｄｅｂ", "丂ㄖ尺尺ㄚ 丂ㄖ丂乇丂卄 爪几乇 Ҝ卂Ҝ ᗪ乇乃",
                    "₴ⱠłⱠ₴₳ ₥₦Ɇ ₭₳₭ Ⱬ₳ⱠɄ₱₳)", "🆂🅻🅸🅻🆂🅰 🅼🅽🅴 🅺🅰🅺 🆉🅰🅻🆄🅿🅰)", "『s』『l』『i』『l』『s』『a』 『m』『n』『e』 『k』『a』『k』 『z』『a』『l』『u』『p』『a』)", "ｓｌｉｌｓａ　ｍｎｅ　ｋａｋ　ｚａｌｕｐａ)", "丂ㄥ丨ㄥ丂卂 爪几乇 Ҝ卂Ҝ 乙卂ㄥㄩ卩卂)",
                    "₮ɆⱤ₱łⱠ₦Ø ₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ", "🆃🅴🆁🅿🅸🅻🅽🅾 🆂🅾🆂🅴🆂🅷 🅼🅽🅴", "『t』『e』『r』『p』『i』『l』『n』『o』 『s』『o』『s』『e』『s』『h』 『m』『n』『e』", "ｔｅｒｐｉｌｎｏ　ｓｏｓｅｓｈ　ｍｎｅ", "ㄒ乇尺卩丨ㄥ几ㄖ 丂ㄖ丂乇丂卄 爪几乇",
                    "РЕПОРТ ЛЕС ОТХУЯРИЛ ТЕБЯ ДО ПОТЕРИ СОЗНАНИЯ", "ТЕРПИЛЬНО ДРЮЧИШЬ МОЙ ХУЙ", "ТЕРПИЛЬНО АТСАСЫВАЕШЬ С ЗАГЛОТОМ", "СЛИШКОМ ИЗЕВА ТРАХНУЛ ТЕБЯ", "СЛИШКОМ ИЗЕВО ВЫЕБАЛ ТВОЮ МАМАНЬКУ",
                    "Ⱨ₳Ⱨ₳Ⱨ₳Ⱨ₳ Ɽ₳ⱫɆ฿₳Ⱡ ₮Ɏ₳ ₦₳ łⱫł", "🅷🅰🅷🅰🅷🅰🅷🅰 🆁🅰🆉🅴🅱🅰🅻 🆃🆈🅰 🅽🅰 🅸🆉🅸", "『H』『A』『H』『A』『H』『A』『H』『A』 『R』『A』『Z』『E』『B』『A』『L』 『T』『Y』『A』 『N』『A』 『I』『Z』『I』", "ＨＡＨＡＨＡＨＡ　ＲＡＺＥＢＡＬ　ＴＹＡ　ＮＡ　ＩＺＩ", "卄卂卄卂卄卂卄卂 尺卂乙乇乃卂ㄥ ㄒㄚ卂 几卂 丨乙丨",
                    "฿ɆⱫⱧł₴Ⱨ Ø₮ ₥ØɆ₲Ø ⱧɄɎ₳ V ₴₮Ɽ₳ⱧɆ", "🅱🅴🆉🅷🅸🆂🅷 🅾🆃 🅼🅾🅴🅶🅾 🅷🆄🆈🅰 🆅 🆂🆃🆁🅰🅷🅴", "『B』『E』『Z』『H』『I』『S』『H』 『O』『T』 『M』『O』『E』『G』『O』 『H』『U』『Y』『A』 『V』 『S』『T』『R』『A』『H』『E』", "ＢＥＺＨＩＳＨ　ＯＴ　ＭＯＥＧＯ　ＨＵＹＡ　Ｖ　ＳＴＲＡＨＥ", "乃乇乙卄丨丂卄 ㄖㄒ 爪ㄖ乇Ꮆㄖ 卄ㄩㄚ卂 ᐯ 丂ㄒ尺卂卄乇",
                    "Ⱬ₳₵ⱧɆ₥ ₮Ɏ ₥₦Ɇ Ɏ₳ł₵₳ ₦Ø₴Ø₥ ₴ⱧɆ₭Ø₵ⱧɆ₴Ⱨ, ₳ ₦Ʉ Đ₳V₳ł ₳₭₭ɄⱤ₳₮₦ɆɆ ₦₳Ɏ₳ⱤłV₳ł, ₱Ø₭₳ ⱫɄ฿Ɏ ₮Ɇ฿Ɇ ⱧɄɆ₥ ₦Ɇ ₴₦Ɇ₴, ₵ⱧɆ₱ɄⱧ₳ Ɇ฿₳₦₦₳Ɏ₳", "🆉🅰🅲🅷🅴🅼 🆃🆈 🅼🅽🅴 🆈🅰🅸🅲🅰 🅽🅾🆂🅾🅼 🆂🅷🅴🅺🅾🅲🅷🅴🆂🅷, 🅰 🅽🆄 🅳🅰🆅🅰🅸 🅰🅺🅺🆄🆁🅰🆃🅽🅴🅴 🅽🅰🆈🅰🆁🅸🆅🅰🅸, 🅿🅾🅺🅰 🆉🆄🅱🆈 🆃🅴🅱🅴 🅷🆄🅴🅼 🅽🅴 🆂🅽🅴🆂, 🅲🅷🅴🅿🆄🅷🅰 🅴🅱🅰🅽🅽🅰🆈🅰", "『Z』『A』『C』『H』『E』『M』 『T』『Y』 『M』『N』『E』 『Y』『A』『I』『C』『A』 『N』『O』『S』『O』『M』 『S』『H』『E』『K』『O』『C』『H』『E』『S』『H』, 『A』 『N』『U』 『D』『A』『V』『A』『I』 『A』『K』『K』『U』『R』『A』『T』『N』『E』『E』 『N』『A』『Y』『A』『R』『I』『V』『A』『I』, 『P』『O』『K』『A』 『Z』『U』『B』『Y』 『T』『E』『B』『E』 『H』『U』『E』『M』 『N』『E』 『S』『N』『E』『S』, 『C』『H』『E』『P』『U』『H』『A』 『E』『B』『A』『N』『N』『A』『Y』『A』", "ＺＡＣＨＥＭ　ＴＹ　ＭＮＥ　ＹＡＩＣＡ　ＮＯＳＯＭ　ＳＨＥＫＯＣＨＥＳＨ,　Ａ　ＮＵ　ＤＡＶＡＩ　ＡＫＫＵＲＡＴＮＥＥ　ＮＡＹＡＲＩＶＡＩ,　ＰＯＫＡ　ＺＵＢＹ　ＴＥＢＥ　ＨＵＥＭ　ＮＥ　ＳＮＥＳ,　ＣＨＥＰＵＨＡ　ＥＢＡＮＮＡＹＡ", "乙卂匚卄乇爪 ㄒㄚ 爪几乇 ㄚ卂丨匚卂 几ㄖ丂ㄖ爪 丂卄乇Ҝㄖ匚卄乇丂卄, 卂 几ㄩ ᗪ卂ᐯ卂丨 卂ҜҜㄩ尺卂ㄒ几乇乇 几卂ㄚ卂尺丨ᐯ卂丨, 卩ㄖҜ卂 乙ㄩ乃ㄚ ㄒ乇乃乇 卄ㄩ乇爪 几乇 丂几乇丂, 匚卄乇卩ㄩ卄卂 乇乃卂几几卂ㄚ卂",
                    "₵Ⱨ₱Ø₭₳Ʉ ₮Ɇ฿Ɏ₳ ₦₳ ₭ⱤØV₳₮ł ₮VØłⱧ ⱤØĐł₮ɆⱠɆł", "🅲🅷🅿🅾🅺🅰🆄 🆃🅴🅱🆈🅰 🅽🅰 🅺🆁🅾🆅🅰🆃🅸 🆃🆅🅾🅸🅷 🆁🅾🅳🅸🆃🅴🅻🅴🅸", "『C』『H』『P』『O』『K』『A』『U』 『T』『E』『B』『Y』『A』 『N』『A』 『K』『R』『O』『V』『A』『T』『I』 『T』『V』『O』『I』『H』 『R』『O』『D』『I』『T』『E』『L』『E』『I』", "ＣＨＰＯＫＡＵ　ＴＥＢＹＡ　ＮＡ　ＫＲＯＶＡＴＩ　ＴＶＯＩＨ　ＲＯＤＩＴＥＬＥＩ", "匚卄卩ㄖҜ卂ㄩ ㄒ乇乃ㄚ卂 几卂 Ҝ尺ㄖᐯ卂ㄒ丨 ㄒᐯㄖ丨卄 尺ㄖᗪ丨ㄒ乇ㄥ乇丨",
                    "Ⱨ₳Ⱨ₳Ⱨ₳Ⱨ₳Ⱨ₳Ⱨ₳ Ʉ ₮Ɇ฿Ɏ₳ VØ Ɽ₮Ʉ ₵Ʉ₥ ₵ØⱠⱠɆ₵₮łØ₦, ĐɎ₳ĐɎ₳, ₳ ₦Ʉ Đ₳V₳ł ₵Ⱨł₴₮ł ₥Øł ฿Ø₮ł₦₭ł ₴VØł₥ Ɏ₳ⱫɎ₭Ø₥, ₱Ø₭₳ Ɏ₳ ₮VØɄ ₥₳₮ ₦Ɇ Ɽ₳₴₴Ⱨ₳₮₳Ⱡ ₴VØł₥ ⱧɄɆ₥, ₵Ⱨ₮Ø฿Ɏ Ɇł ₴₮₳ⱠØ ₱ⱠØⱧØ", "🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰 🆄 🆃🅴🅱🆈🅰 🆅🅾 🆁🆃🆄 🅲🆄🅼 🅲🅾🅻🅻🅴🅲🆃🅸🅾🅽, 🅳🆈🅰🅳🆈🅰, 🅰 🅽🆄 🅳🅰🆅🅰🅸 🅲🅷🅸🆂🆃🅸 🅼🅾🅸 🅱🅾🆃🅸🅽🅺🅸 🆂🆅🅾🅸🅼 🆈🅰🆉🆈🅺🅾🅼, 🅿🅾🅺🅰 🆈🅰 🆃🆅🅾🆄 🅼🅰🆃 🅽🅴 🆁🅰🆂🆂🅷🅰🆃🅰🅻 🆂🆅🅾🅸🅼 🅷🆄🅴🅼, 🅲🅷🆃🅾🅱🆈 🅴🅸 🆂🆃🅰🅻🅾 🅿🅻🅾🅷🅾", "『H』『A』『H』『A』『H』『A』『H』『A』『H』『A』『H』『A』 『U』 『T』『E』『B』『Y』『A』 『V』『O』 『R』『T』『U』 『C』『U』『M』 『C』『O』『L』『L』『E』『C』『T』『I』『O』『N』, 『D』『Y』『A』『D』『Y』『A』, 『A』 『N』『U』 『D』『A』『V』『A』『I』 『C』『H』『I』『S』『T』『I』 『M』『O』『I』 『B』『O』『T』『I』『N』『K』『I』 『S』『V』『O』『I』『M』 『Y』『A』『Z』『Y』『K』『O』『M』, 『P』『O』『K』『A』 『Y』『A』 『T』『V』『O』『U』 『M』『A』『T』 『N』『E』 『R』『A』『S』『S』『H』『A』『T』『A』『L』 『S』『V』『O』『I』『M』 『H』『U』『E』『M』, 『C』『H』『T』『O』『B』『Y』 『E』『I』 『S』『T』『A』『L』『O』 『P』『L』『O』『H』『O』", "ＨＡＨＡＨＡＨＡＨＡＨＡ　Ｕ　ＴＥＢＹＡ　ＶＯ　ＲＴＵ　ＣＵＭ　ＣＯＬＬＥＣＴＩＯＮ,　ＤＹＡＤＹＡ,　Ａ　ＮＵ　ＤＡＶＡＩ　ＣＨＩＳＴＩ　ＭＯＩ　ＢＯＴＩＮＫＩ　ＳＶＯＩＭ　ＹＡＺＹＫＯＭ,　ＰＯＫＡ　ＹＡ　ＴＶＯＵ　ＭＡＴ　ＮＥ　ＲＡＳＳＨＡＴＡＬ　ＳＶＯＩＭ　ＨＵＥＭ,　ＣＨＴＯＢＹ　ＥＩ　ＳＴＡＬＯ　ＰＬＯＨＯ", "卄卂卄卂卄卂卄卂卄卂卄卂 ㄩ ㄒ乇乃ㄚ卂 ᐯㄖ 尺ㄒㄩ 匚ㄩ爪 匚ㄖㄥㄥ乇匚ㄒ丨ㄖ几, ᗪㄚ卂ᗪㄚ卂, 卂 几ㄩ ᗪ卂ᐯ卂丨 匚卄丨丂ㄒ丨 爪ㄖ丨 乃ㄖㄒ丨几Ҝ丨 丂ᐯㄖ丨爪 ㄚ卂乙ㄚҜㄖ爪, 卩ㄖҜ卂 ㄚ卂 ㄒᐯㄖㄩ 爪卂ㄒ 几乇 尺卂丂丂卄卂ㄒ卂ㄥ 丂ᐯㄖ丨爪 卄ㄩ乇爪, 匚卄ㄒㄖ乃ㄚ 乇丨 丂ㄒ卂ㄥㄖ 卩ㄥㄖ卄ㄖ",
                    "₱ⱤɎ₳₵ⱧɆ₴Ⱨ₴₳ ₱ØĐ ₥Øł₥ ⱧɄɆ₥ ₭₳₭ ₴₳₴₳Ⱡ₴Ⱨł₭", "🅿🆁🆈🅰🅲🅷🅴🆂🅷🆂🅰 🅿🅾🅳 🅼🅾🅸🅼 🅷🆄🅴🅼 🅺🅰🅺 🆂🅰🆂🅰🅻🆂🅷🅸🅺", "『P』『R』『Y』『A』『C』『H』『E』『S』『H』『S』『A』 『P』『O』『D』 『M』『O』『I』『M』 『H』『U』『E』『M』 『K』『A』『K』 『S』『A』『S』『A』『L』『S』『H』『I』『K』", "ＰＲＹＡＣＨＥＳＨＳＡ　ＰＯＤ　ＭＯＩＭ　ＨＵＥＭ　ＫＡＫ　ＳＡＳＡＬＳＨＩＫ", "卩尺ㄚ卂匚卄乇丂卄丂卂 卩ㄖᗪ 爪ㄖ丨爪 卄ㄩ乇爪 Ҝ卂Ҝ 丂卂丂卂ㄥ丂卄丨Ҝ",
                    "ⱧV₳₮ł₮ ₦Ɏ₮, ₱Ø₭₳ Ɏ₳ ₮Ɇ฿Ɇ ₭ł₴Ⱨ₭ł ⱧɄɆ₥ ₦Ɇ VɎⱤV₳Ⱡ", "🅷🆅🅰🆃🅸🆃 🅽🆈🆃, 🅿🅾🅺🅰 🆈🅰 🆃🅴🅱🅴 🅺🅸🆂🅷🅺🅸 🅷🆄🅴🅼 🅽🅴 🆅🆈🆁🆅🅰🅻", "『H』『V』『A』『T』『I』『T』 『N』『Y』『T』, 『P』『O』『K』『A』 『Y』『A』 『T』『E』『B』『E』 『K』『I』『S』『H』『K』『I』 『H』『U』『E』『M』 『N』『E』 『V』『Y』『R』『V』『A』『L』", "ＨＶＡＴＩＴ　ＮＹＴ,　ＰＯＫＡ　ＹＡ　ＴＥＢＥ　ＫＩＳＨＫＩ　ＨＵＥＭ　ＮＥ　ＶＹＲＶＡＬ", "卄ᐯ卂ㄒ丨ㄒ 几ㄚㄒ, 卩ㄖҜ卂 ㄚ卂 ㄒ乇乃乇 Ҝ丨丂卄Ҝ丨 卄ㄩ乇爪 几乇 ᐯㄚ尺ᐯ卂ㄥ",
                    "Ɇ฿₳₦ɄⱠ ₮VØɆł ₥₳₮ɄⱧɆ ₱Ø ₵ⱧɆⱠɄⱧɆ, ₮Ɇ₱ɆⱤ ɆɆ ₵ⱧɆⱠɄⱧ₳ ⱠɆ₮₳Ɇ₮ V Đ₳ⱠɆ₭Øł ₲₳Ⱡ₳₭₮ł₭Ɇ, ₦Ʉ ł ₱Ø₮Ø₥ ₭Ø₦Ɇ₵Ⱨ₦Ø ₦₳₴₴₳Ⱡ Ɇł V ₮ⱤɄ₱ ł ₴ⱫⱧɆ₲ ₦₳ⱧɄł ฿ⱠɎ₳Đł₦Ʉ", "🅴🅱🅰🅽🆄🅻 🆃🆅🅾🅴🅸 🅼🅰🆃🆄🅷🅴 🅿🅾 🅲🅷🅴🅻🆄🅷🅴, 🆃🅴🅿🅴🆁 🅴🅴 🅲🅷🅴🅻🆄🅷🅰 🅻🅴🆃🅰🅴🆃 🆅 🅳🅰🅻🅴🅺🅾🅸 🅶🅰🅻🅰🅺🆃🅸🅺🅴, 🅽🆄 🅸 🅿🅾🆃🅾🅼 🅺🅾🅽🅴🅲🅷🅽🅾 🅽🅰🆂🆂🅰🅻 🅴🅸 🆅 🆃🆁🆄🅿 🅸 🆂🆉🅷🅴🅶 🅽🅰🅷🆄🅸 🅱🅻🆈🅰🅳🅸🅽🆄", "『E』『B』『A』『N』『U』『L』 『T』『V』『O』『E』『I』 『M』『A』『T』『U』『H』『E』 『P』『O』 『C』『H』『E』『L』『U』『H』『E』, 『T』『E』『P』『E』『R』 『E』『E』 『C』『H』『E』『L』『U』『H』『A』 『L』『E』『T』『A』『E』『T』 『V』 『D』『A』『L』『E』『K』『O』『I』 『G』『A』『L』『A』『K』『T』『I』『K』『E』, 『N』『U』 『I』 『P』『O』『T』『O』『M』 『K』『O』『N』『E』『C』『H』『N』『O』 『N』『A』『S』『S』『A』『L』 『E』『I』 『V』 『T』『R』『U』『P』 『I』 『S』『Z』『H』『E』『G』 『N』『A』『H』『U』『I』 『B』『L』『Y』『A』『D』『I』『N』『U』", "ＥＢＡＮＵＬ　ＴＶＯＥＩ　ＭＡＴＵＨＥ　ＰＯ　ＣＨＥＬＵＨＥ,　ＴＥＰＥＲ　ＥＥ　ＣＨＥＬＵＨＡ　ＬＥＴＡＥＴ　Ｖ　ＤＡＬＥＫＯＩ　ＧＡＬＡＫＴＩＫＥ,　ＮＵ　Ｉ　ＰＯＴＯＭ　ＫＯＮＥＣＨＮＯ　ＮＡＳＳＡＬ　ＥＩ　Ｖ　ＴＲＵＰ　Ｉ　ＳＺＨＥＧ　ＮＡＨＵＩ　ＢＬＹＡＤＩＮＵ", "乇乃卂几ㄩㄥ ㄒᐯㄖ乇丨 爪卂ㄒㄩ卄乇 卩ㄖ 匚卄乇ㄥㄩ卄乇, ㄒ乇卩乇尺 乇乇 匚卄乇ㄥㄩ卄卂 ㄥ乇ㄒ卂乇ㄒ ᐯ ᗪ卂ㄥ乇Ҝㄖ丨 Ꮆ卂ㄥ卂Ҝㄒ丨Ҝ乇, 几ㄩ 丨 卩ㄖㄒㄖ爪 Ҝㄖ几乇匚卄几ㄖ 几卂丂丂卂ㄥ 乇丨 ᐯ ㄒ尺ㄩ卩 丨 丂乙卄乇Ꮆ 几卂卄ㄩ丨 乃ㄥㄚ卂ᗪ丨几ㄩ",
                    "Ʉ₱łⱫĐØⱧ₳Ⱡ ₮Ɇ฿Ɏ₳ ⱧɄɆ₥, ₦Ɇ ₱Ⱡ₳₵Ⱨ ĐɆ₮₭₳", "🆄🅿🅸🆉🅳🅾🅷🅰🅻 🆃🅴🅱🆈🅰 🅷🆄🅴🅼, 🅽🅴 🅿🅻🅰🅲🅷 🅳🅴🆃🅺🅰", "『U』『P』『I』『Z』『D』『O』『H』『A』『L』 『T』『E』『B』『Y』『A』 『H』『U』『E』『M』, 『N』『E』 『P』『L』『A』『C』『H』 『D』『E』『T』『K』『A』", "ＵＰＩＺＤＯＨＡＬ　ＴＥＢＹＡ　ＨＵＥＭ,　ＮＥ　ＰＬＡＣＨ　ＤＥＴＫＡ", "ㄩ卩丨乙ᗪㄖ卄卂ㄥ ㄒ乇乃ㄚ卂 卄ㄩ乇爪, 几乇 卩ㄥ卂匚卄 ᗪ乇ㄒҜ卂",
                    "₦Ɇ ₦Øł ₣₳₦₳₮₭₳ ₥ØɆ₲Ø ⱧɄɎ₳", "🅽🅴 🅽🅾🅸 🅵🅰🅽🅰🆃🅺🅰 🅼🅾🅴🅶🅾 🅷🆄🆈🅰", "『N』『E』 『N』『O』『I』 『F』『A』『N』『A』『T』『K』『A』 『M』『O』『E』『G』『O』 『H』『U』『Y』『A』", "ＮＥ　ＮＯＩ　ＦＡＮＡＴＫＡ　ＭＯＥＧＯ　ＨＵＹＡ", "几乇 几ㄖ丨 千卂几卂ㄒҜ卂 爪ㄖ乇Ꮆㄖ 卄ㄩㄚ卂",
                    "Ⱬ₳ ฿Ɇ₴₱Ⱡ₳₮₦Ø Ɇ฿Ʉ ₮Ɇ฿Ɏ₳", "🆉🅰 🅱🅴🆂🅿🅻🅰🆃🅽🅾 🅴🅱🆄 🆃🅴🅱🆈🅰", "『Z』『A』 『B』『E』『S』『P』『L』『A』『T』『N』『O』 『E』『B』『U』 『T』『E』『B』『Y』『A』", "ＺＡ　ＢＥＳＰＬＡＴＮＯ　ＥＢＵ　ＴＥＢＹＡ", "乙卂 乃乇丂卩ㄥ卂ㄒ几ㄖ 乇乃ㄩ ㄒ乇乃ㄚ卂",
                    "ɄɆ฿₳Ⱡ ₮Ɏ₳ Ⱬ₳ⱠɄ₱₳ł ₭Ɽ₳₴łV₳", "🆄🅴🅱🅰🅻 🆃🆈🅰 🆉🅰🅻🆄🅿🅰🅸 🅺🆁🅰🆂🅸🆅🅰", "『U』『E』『B』『A』『L』 『T』『Y』『A』 『Z』『A』『L』『U』『P』『A』『I』 『K』『R』『A』『S』『I』『V』『A』", "ＵＥＢＡＬ　ＴＹＡ　ＺＡＬＵＰＡＩ　ＫＲＡＳＩＶＡ", "ㄩ乇乃卂ㄥ ㄒㄚ卂 乙卂ㄥㄩ卩卂丨 Ҝ尺卂丂丨ᐯ卂",
                    "₦Ɇ ₴Ø฿łⱤ₳ł ₴VØł₥ Ɏ₳ⱫɎ₭Ø₥ ₴₱ɆⱤ₥Ʉ ₴ ₱ØⱠ₳", "🅽🅴 🆂🅾🅱🅸🆁🅰🅸 🆂🆅🅾🅸🅼 🆈🅰🆉🆈🅺🅾🅼 🆂🅿🅴🆁🅼🆄 🆂 🅿🅾🅻🅰", "『N』『E』 『S』『O』『B』『I』『R』『A』『I』 『S』『V』『O』『I』『M』 『Y』『A』『Z』『Y』『K』『O』『M』 『S』『P』『E』『R』『M』『U』 『S』 『P』『O』『L』『A』", "ＮＥ　ＳＯＢＩＲＡＩ　ＳＶＯＩＭ　ＹＡＺＹＫＯＭ　ＳＰＥＲＭＵ　Ｓ　ＰＯＬＡ", "几乇 丂ㄖ乃丨尺卂丨 丂ᐯㄖ丨爪 ㄚ卂乙ㄚҜㄖ爪 丂卩乇尺爪ㄩ 丂 卩ㄖㄥ卂",
                    "₦₳ ɆⱫ ɆⱫ ₱₳₴₳₴₳Ⱡ ₥₦Ɇ ₴Ø ₴VØɆł ₥₳₮ɄⱧØł ₴ⱧⱠɄⱧØł", "🅽🅰 🅴🆉 🅴🆉 🅿🅰🆂🅰🆂🅰🅻 🅼🅽🅴 🆂🅾 🆂🆅🅾🅴🅸 🅼🅰🆃🆄🅷🅾🅸 🆂🅷🅻🆄🅷🅾🅸", "『N』『A』 『E』『Z』 『E』『Z』 『P』『A』『S』『A』『S』『A』『L』 『M』『N』『E』 『S』『O』 『S』『V』『O』『E』『I』 『M』『A』『T』『U』『H』『O』『I』 『S』『H』『L』『U』『H』『O』『I』", "ＮＡ　ＥＺ　ＥＺ　ＰＡＳＡＳＡＬ　ＭＮＥ　ＳＯ　ＳＶＯＥＩ　ＭＡＴＵＨＯＩ　ＳＨＬＵＨＯＩ", "几卂 乇乙 乇乙 卩卂丂卂丂卂ㄥ 爪几乇 丂ㄖ 丂ᐯㄖ乇丨 爪卂ㄒㄩ卄ㄖ丨 丂卄ㄥㄩ卄ㄖ丨",
                    "Ⱨ₳Ⱨ₳Ⱨ₳Ⱨ₳Ⱨ₳ Ɇ฿Ʉ ₮Ɇ฿Ɏ₳ ₴Ⱡł₮Ɏ₴Ⱨ ĐØ ₮₳₭Øł ₴₮Ɇ₱Ɇ₦ł, ₵Ⱨ₮Ø Ø₮₴Ø₴₳Ⱡ ₥₦Ɇ ₴ ₮₳₭ł₥ Ⱬ₳₲ⱠØ₮Ø₥, ł Ɇ₴ⱧɆ ₱Ø₴₭₳₭₳Ⱡ ₦₳ ₥ØɆ₥ ⱧɄɆ ₴Øł₥ Ø₵Ⱨ₭Ø₥, Ɏ₳ ₮₳₭ ⱤⱫⱧ₳Ⱡ VɆ₴ ĐɆ₦ ₭₳₭Øł ⱫⱧɆ ₮Ɏ ₦ł₵Ⱨ₮ØⱫⱧ₦Ɏł ₴Ɏ₦ ₱ØⱤ₮ØVØł ₴ⱧⱠɄⱧł ł ₱łĐØⱤ₳₴₳", "🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰 🅴🅱🆄 🆃🅴🅱🆈🅰 🆂🅻🅸🆃🆈🆂🅷 🅳🅾 🆃🅰🅺🅾🅸 🆂🆃🅴🅿🅴🅽🅸, 🅲🅷🆃🅾 🅾🆃🆂🅾🆂🅰🅻 🅼🅽🅴 🆂 🆃🅰🅺🅸🅼 🆉🅰🅶🅻🅾🆃🅾🅼, 🅸 🅴🆂🅷🅴 🅿🅾🆂🅺🅰🅺🅰🅻 🅽🅰 🅼🅾🅴🅼 🅷🆄🅴 🆂🅾🅸🅼 🅾🅲🅷🅺🅾🅼, 🆈🅰 🆃🅰🅺 🆁🆉🅷🅰🅻 🆅🅴🆂 🅳🅴🅽 🅺🅰🅺🅾🅸 🆉🅷🅴 🆃🆈 🅽🅸🅲🅷🆃🅾🆉🅷🅽🆈🅸 🆂🆈🅽 🅿🅾🆁🆃🅾🆅🅾🅸 🆂🅷🅻🆄🅷🅸 🅸 🅿🅸🅳🅾🆁🅰🆂🅰", "『H』『A』『H』『A』『H』『A』『H』『A』『H』『A』 『E』『B』『U』 『T』『E』『B』『Y』『A』 『S』『L』『I』『T』『Y』『S』『H』 『D』『O』 『T』『A』『K』『O』『I』 『S』『T』『E』『P』『E』『N』『I』, 『C』『H』『T』『O』 『O』『T』『S』『O』『S』『A』『L』 『M』『N』『E』 『S』 『T』『A』『K』『I』『M』 『Z』『A』『G』『L』『O』『T』『O』『M』, 『I』 『E』『S』『H』『E』 『P』『O』『S』『K』『A』『K』『A』『L』 『N』『A』 『M』『O』『E』『M』 『H』『U』『E』 『S』『O』『I』『M』 『O』『C』『H』『K』『O』『M』, 『Y』『A』 『T』『A』『K』 『R』『Z』『H』『A』『L』 『V』『E』『S』 『D』『E』『N』 『K』『A』『K』『O』『I』 『Z』『H』『E』 『T』『Y』 『N』『I』『C』『H』『T』『O』『Z』『H』『N』『Y』『I』 『S』『Y』『N』 『P』『O』『R』『T』『O』『V』『O』『I』 『S』『H』『L』『U』『H』『I』 『I』 『P』『I』『D』『O』『R』『A』『S』『A』", "ＨＡＨＡＨＡＨＡＨＡ　ＥＢＵ　ＴＥＢＹＡ　ＳＬＩＴＹＳＨ　ＤＯ　ＴＡＫＯＩ　ＳＴＥＰＥＮＩ,　ＣＨＴＯ　ＯＴＳＯＳＡＬ　ＭＮＥ　Ｓ　ＴＡＫＩＭ　ＺＡＧＬＯＴＯＭ,　Ｉ　ＥＳＨＥ　ＰＯＳＫＡＫＡＬ　ＮＡ　ＭＯＥＭ　ＨＵＥ　ＳＯＩＭ　ＯＣＨＫＯＭ,　ＹＡ　ＴＡＫ　ＲＺＨＡＬ　ＶＥＳ　ＤＥＮ　ＫＡＫＯＩ　ＺＨＥ　ＴＹ　ＮＩＣＨＴＯＺＨＮＹＩ　ＳＹＮ　ＰＯＲＴＯＶＯＩ　ＳＨＬＵＨＩ　Ｉ　ＰＩＤＯＲＡＳＡ", "卄卂卄卂卄卂卄卂卄卂 乇乃ㄩ ㄒ乇乃ㄚ卂 丂ㄥ丨ㄒㄚ丂卄 ᗪㄖ ㄒ卂Ҝㄖ丨 丂ㄒ乇卩乇几丨, 匚卄ㄒㄖ ㄖㄒ丂ㄖ丂卂ㄥ 爪几乇 丂 ㄒ卂Ҝ丨爪 乙卂Ꮆㄥㄖㄒㄖ爪, 丨 乇丂卄乇 卩ㄖ丂Ҝ卂Ҝ卂ㄥ 几卂 爪ㄖ乇爪 卄ㄩ乇 丂ㄖ丨爪 ㄖ匚卄Ҝㄖ爪, ㄚ卂 ㄒ卂Ҝ 尺乙卄卂ㄥ ᐯ乇丂 ᗪ乇几 Ҝ卂Ҝㄖ丨 乙卄乇 ㄒㄚ 几丨匚卄ㄒㄖ乙卄几ㄚ丨 丂ㄚ几 卩ㄖ尺ㄒㄖᐯㄖ丨 丂卄ㄥㄩ卄丨 丨 卩丨ᗪㄖ尺卂丂卂",
                    "Ʉ₱₴ Ɇ฿₦ɄⱠ ₮Ɇ฿Ɏ₳ ₱₳Ⱡ₭Øł ₴ⱠɄ₵Ⱨ₳ł₦Ø", "🆄🅿🆂 🅴🅱🅽🆄🅻 🆃🅴🅱🆈🅰 🅿🅰🅻🅺🅾🅸 🆂🅻🆄🅲🅷🅰🅸🅽🅾", "『u』『p』『s』 『e』『b』『n』『u』『l』 『t』『e』『b』『y』『a』 『p』『a』『l』『k』『o』『i』 『s』『l』『u』『c』『h』『a』『i』『n』『o』", "ｕｐｓ　ｅｂｎｕｌ　ｔｅｂｙａ　ｐａｌｋｏｉ　ｓｌｕｃｈａｉｎｏ", "ㄩ卩丂 乇乃几ㄩㄥ ㄒ乇乃ㄚ卂 卩卂ㄥҜㄖ丨 丂ㄥㄩ匚卄卂丨几ㄖ",
                    "Ʉ₱₴ Ɇ฿₦ɄⱠ ₮Ɇ฿Ɏ₳ ₴VØł₥ ₳₲ⱤɆ₲₳₮Ø₥ ₴ⱠɄ₵Ⱨ₳ł₦Ø", "🆄🅿🆂 🅴🅱🅽🆄🅻 🆃🅴🅱🆈🅰 🆂🆅🅾🅸🅼 🅰🅶🆁🅴🅶🅰🆃🅾🅼 🆂🅻🆄🅲🅷🅰🅸🅽🅾", "『u』『p』『s』 『e』『b』『n』『u』『l』 『t』『e』『b』『y』『a』 『s』『v』『o』『i』『m』 『a』『g』『r』『e』『g』『a』『t』『o』『m』 『s』『l』『u』『c』『h』『a』『i』『n』『o』", "ｕｐｓ　ｅｂｎｕｌ　ｔｅｂｙａ　ｓｖｏｉｍ　ａｇｒｅｇａｔｏｍ　ｓｌｕｃｈａｉｎｏ", "ㄩ卩丂 乇乃几ㄩㄥ ㄒ乇乃ㄚ卂 丂ᐯㄖ丨爪 卂Ꮆ尺乇Ꮆ卂ㄒㄖ爪 丂ㄥㄩ匚卄卂丨几ㄖ",
                    "₱łⱫⱫⱧɄ ₮Ɇ฿Ɏ₳ ₭ɄⱠ₳₭₳₥ł Ⱬ₳ ⱧɄɆVɎł ₥ł₦Ɇ₮", "🅿🅸🆉🆉🅷🆄 🆃🅴🅱🆈🅰 🅺🆄🅻🅰🅺🅰🅼🅸 🆉🅰 🅷🆄🅴🆅🆈🅸 🅼🅸🅽🅴🆃", "『p』『i』『z』『z』『h』『u』 『t』『e』『b』『y』『a』 『k』『u』『l』『a』『k』『a』『m』『i』 『z』『a』 『h』『u』『e』『v』『y』『i』 『m』『i』『n』『e』『t』", "ｐｉｚｚｈｕ　ｔｅｂｙａ　ｋｕｌａｋａｍｉ　ｚａ　ｈｕｅｖｙｉ　ｍｉｎｅｔ", "卩丨乙乙卄ㄩ ㄒ乇乃ㄚ卂 Ҝㄩㄥ卂Ҝ卂爪丨 乙卂 卄ㄩ乇ᐯㄚ丨 爪丨几乇ㄒ",
                    "Ʉ₱₴ Ɏ₳ ₱ɆⱤɆ₭₳₴₳Ɇ฿łⱠ ₮VØɆ₲Ø Ø₮₵Ⱨł₥₳", "🆄🅿🆂 🆈🅰 🅿🅴🆁🅴🅺🅰🆂🅰🅴🅱🅸🅻 🆃🆅🅾🅴🅶🅾 🅾🆃🅲🅷🅸🅼🅰", "『u』『p』『s』 『y』『a』 『p』『e』『r』『e』『k』『a』『s』『a』『e』『b』『i』『l』 『t』『v』『o』『e』『g』『o』 『o』『t』『c』『h』『i』『m』『a』", "ｕｐｓ　ｙａ　ｐｅｒｅｋａｓａｅｂｉｌ　ｔｖｏｅｇｏ　ｏｔｃｈｉｍａ", "ㄩ卩丂 ㄚ卂 卩乇尺乇Ҝ卂丂卂乇乃丨ㄥ ㄒᐯㄖ乇Ꮆㄖ ㄖㄒ匚卄丨爪卂",
                    "ⱧɎ₳ⱤɄ ฿ɆⱫ ₱ⱤØɆ฿ØV ", "🅷🆈🅰🆁🆄 🅱🅴🆉 🅿🆁🅾🅴🅱🅾🆅 ", "『h』『y』『a』『r』『u』 『b』『e』『z』 『p』『r』『o』『e』『b』『o』『v』 ", "ｈｙａｒｕ　ｂｅｚ　ｐｒｏｅｂｏｖ　", "卄ㄚ卂尺ㄩ 乃乇乙 卩尺ㄖ乇乃ㄖᐯ ",
                    "₮Ʉ₴ⱧłⱠ Ø฿ ₭Ⱡł₮ØⱤ ₮VØɆł ₥₳₮ɆⱤł ฿Ɏ₵Ⱨ₭ł", "🆃🆄🆂🅷🅸🅻 🅾🅱 🅺🅻🅸🆃🅾🆁 🆃🆅🅾🅴🅸 🅼🅰🆃🅴🆁🅸 🅱🆈🅲🅷🅺🅸", "『t』『u』『s』『h』『i』『l』 『o』『b』 『k』『l』『i』『t』『o』『r』 『t』『v』『o』『e』『i』 『m』『a』『t』『e』『r』『i』 『b』『y』『c』『h』『k』『i』", "ｔｕｓｈｉｌ　ｏｂ　ｋｌｉｔｏｒ　ｔｖｏｅｉ　ｍａｔｅｒｉ　ｂｙｃｈｋｉ", "ㄒㄩ丂卄丨ㄥ ㄖ乃 Ҝㄥ丨ㄒㄖ尺 ㄒᐯㄖ乇丨 爪卂ㄒ乇尺丨 乃ㄚ匚卄Ҝ丨",
                    "₵₳₵Ɇ₩ Ⱬ₳ 100Ɽ", "🅲🅰🅲🅴🆆 🆉🅰 100🆁", "『c』『a』『c』『e』『w』 『z』『a』 『1』『0』『0』『r』", "ｃａｃｅｗ　ｚａ　１００ｒ", "匚卂匚乇山 乙卂 100尺",
                    "₮Ɏ ⱫⱧ₳ⱠØ₭", "🆃🆈 🆉🅷🅰🅻🅾🅺", "『t』『y』 『z』『h』『a』『l』『o』『k』", "ｔｙ　ｚｈａｌｏｋ", "ㄒㄚ 乙卄卂ㄥㄖҜ",
                    "VɆⱤ₦ɄⱠ₴₳ łⱫ ₳Đ₳ ₵Ⱨ₮Ø฿Ɏ Ɇ฿₳₴Ⱨł₮ ₮Ɇ฿Ɏ₳", "🆅🅴🆁🅽🆄🅻🆂🅰 🅸🆉 🅰🅳🅰 🅲🅷🆃🅾🅱🆈 🅴🅱🅰🆂🅷🅸🆃 🆃🅴🅱🆈🅰", "『v』『e』『r』『n』『u』『l』『s』『a』 『i』『z』 『a』『d』『a』 『c』『h』『t』『o』『b』『y』 『e』『b』『a』『s』『h』『i』『t』 『t』『e』『b』『y』『a』", "ｖｅｒｎｕｌｓａ　ｉｚ　ａｄａ　ｃｈｔｏｂｙ　ｅｂａｓｈｉｔ　ｔｅｂｙａ", "ᐯ乇尺几ㄩㄥ丂卂 丨乙 卂ᗪ卂 匚卄ㄒㄖ乃ㄚ 乇乃卂丂卄丨ㄒ ㄒ乇乃ㄚ卂",
                    "₴₦łⱫØ₴ⱧɆⱠ ₵Ⱨ₮Ø฿Ɏ Ø₮ⱧɄɎ₳Ɽł₮ ₮Ɇ฿Ɏ₳", "🆂🅽🅸🆉🅾🆂🅷🅴🅻 🅲🅷🆃🅾🅱🆈 🅾🆃🅷🆄🆈🅰🆁🅸🆃 🆃🅴🅱🆈🅰", "『s』『n』『i』『z』『o』『s』『h』『e』『l』 『c』『h』『t』『o』『b』『y』 『o』『t』『h』『u』『y』『a』『r』『i』『t』 『t』『e』『b』『y』『a』", "ｓｎｉｚｏｓｈｅｌ　ｃｈｔｏｂｙ　ｏｔｈｕｙａｒｉｔ　ｔｅｂｙａ", "丂几丨乙ㄖ丂卄乇ㄥ 匚卄ㄒㄖ乃ㄚ ㄖㄒ卄ㄩㄚ卂尺丨ㄒ ㄒ乇乃ㄚ卂",
                    "₭₳₭ ⱫⱧɆ ⱫⱧ₳Ⱡ₭Ø ₮Ɇ฿Ɏ₳, ₴₮Øł₴Ⱨ ₱ⱤØ₮łV ₥Ɇ₦Ɏ₳, ₦Ɇ ฿Øł₴Ⱨ₴₳ ₵Ⱨ₮Ø Ɏ₳ ₮Ɇ฿Ɏ₳ ₱ɆⱤɆɆ฿₳₴ⱧɄ?)", "🅺🅰🅺 🆉🅷🅴 🆉🅷🅰🅻🅺🅾 🆃🅴🅱🆈🅰, 🆂🆃🅾🅸🆂🅷 🅿🆁🅾🆃🅸🆅 🅼🅴🅽🆈🅰, 🅽🅴 🅱🅾🅸🆂🅷🆂🅰 🅲🅷🆃🅾 🆈🅰 🆃🅴🅱🆈🅰 🅿🅴🆁🅴🅴🅱🅰🆂🅷🆄?)", "『k』『a』『k』 『z』『h』『e』 『z』『h』『a』『l』『k』『o』 『t』『e』『b』『y』『a』, 『s』『t』『o』『i』『s』『h』 『p』『r』『o』『t』『i』『v』 『m』『e』『n』『y』『a』, 『n』『e』 『b』『o』『i』『s』『h』『s』『a』 『c』『h』『t』『o』 『y』『a』 『t』『e』『b』『y』『a』 『p』『e』『r』『e』『e』『b』『a』『s』『h』『u』?)", "ｋａｋ　ｚｈｅ　ｚｈａｌｋｏ　ｔｅｂｙａ,　ｓｔｏｉｓｈ　ｐｒｏｔｉｖ　ｍｅｎｙａ,　ｎｅ　ｂｏｉｓｈｓａ　ｃｈｔｏ　ｙａ　ｔｅｂｙａ　ｐｅｒｅｅｂａｓｈｕ?)", "Ҝ卂Ҝ 乙卄乇 乙卄卂ㄥҜㄖ ㄒ乇乃ㄚ卂, 丂ㄒㄖ丨丂卄 卩尺ㄖㄒ丨ᐯ 爪乇几ㄚ卂, 几乇 乃ㄖ丨丂卄丂卂 匚卄ㄒㄖ ㄚ卂 ㄒ乇乃ㄚ卂 卩乇尺乇乇乃卂丂卄ㄩ?)",
                    "₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ ₭₳₭ ฿Ɇ₴ⱧɆ₦Ɏ", "🆂🅾🆂🅴🆂🅷 🅼🅽🅴 🅺🅰🅺 🅱🅴🆂🅷🅴🅽🆈", "『s』『o』『s』『e』『s』『h』 『m』『n』『e』 『k』『a』『k』 『b』『e』『s』『h』『e』『n』『y』", "ｓｏｓｅｓｈ　ｍｎｅ　ｋａｋ　ｂｅｓｈｅｎｙ", "丂ㄖ丂乇丂卄 爪几乇 Ҝ卂Ҝ 乃乇丂卄乇几ㄚ",
                    "₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ ₭₳₭ Ø฿Ɇ₴₱Ø₭ØɆ₦Ɏ", "🆂🅾🆂🅴🆂🅷 🅼🅽🅴 🅺🅰🅺 🅾🅱🅴🆂🅿🅾🅺🅾🅴🅽🆈", "『s』『o』『s』『e』『s』『h』 『m』『n』『e』 『k』『a』『k』 『o』『b』『e』『s』『p』『o』『k』『o』『e』『n』『y』", "ｓｏｓｅｓｈ　ｍｎｅ　ｋａｋ　ｏｂｅｓｐｏｋｏｅｎｙ", "丂ㄖ丂乇丂卄 爪几乇 Ҝ卂Ҝ ㄖ乃乇丂卩ㄖҜㄖ乇几ㄚ",
                    "₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ ₭₳₭ ₦ɆɄ₲Ø₥Ø₦₦Ɏ", "🆂🅾🆂🅴🆂🅷 🅼🅽🅴 🅺🅰🅺 🅽🅴🆄🅶🅾🅼🅾🅽🅽🆈", "『s』『o』『s』『e』『s』『h』 『m』『n』『e』 『k』『a』『k』 『n』『e』『u』『g』『o』『m』『o』『n』『n』『y』", "ｓｏｓｅｓｈ　ｍｎｅ　ｋａｋ　ｎｅｕｇｏｍｏｎｎｙ", "丂ㄖ丂乇丂卄 爪几乇 Ҝ卂Ҝ 几乇ㄩᎶㄖ爪ㄖ几几ㄚ",
                    "₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ ₭₳₭ ₮VØɎ₳ ₥₳₮", "🆂🅾🆂🅴🆂🅷 🅼🅽🅴 🅺🅰🅺 🆃🆅🅾🆈🅰 🅼🅰🆃", "『s』『o』『s』『e』『s』『h』 『m』『n』『e』 『k』『a』『k』 『t』『v』『o』『y』『a』 『m』『a』『t』", "ｓｏｓｅｓｈ　ｍｎｅ　ｋａｋ　ｔｖｏｙａ　ｍａｔ", "𝖘𝖔𝖘𝖊𝖘𝖍 𝖒𝖓𝖊 𝖐𝖆𝖐 𝖙𝖛𝖔𝖞𝖆 𝖒𝖆𝖙",
                    "₮VØɎ₳ ₥₳₮ ₱ⱤɎ₲₳Ɇ₮ ₦₳ ₥ØɆ₥ ⱧɄɆ", "🆃🆅🅾🆈🅰 🅼🅰🆃 🅿🆁🆈🅶🅰🅴🆃 🅽🅰 🅼🅾🅴🅼 🅷🆄🅴", "『t』『v』『o』『y』『a』 『m』『a』『t』 『p』『r』『y』『g』『a』『e』『t』 『n』『a』 『m』『o』『e』『m』 『h』『u』『e』", "ｔｖｏｙａ　ｍａｔ　ｐｒｙｇａｅｔ　ｎａ　ｍｏｅｍ　ｈｕｅ", "𝖙𝖛𝖔𝖞𝖆 𝖒𝖆𝖙 𝖕𝖗𝖞𝖌𝖆𝖊𝖙 𝖓𝖆 𝖒𝖔𝖊𝖒 𝖍𝖚𝖊",
                    "₭₳₭ ₥₳ⱠɆ₦₭₳Ɏ₳ ĐɆVØ₵Ⱨ₭₳ Ø₮ ₥ØɆ₲Ø ⱧɄɎ₳ Ø₮VØⱤ₳₵ⱧłV₳Ɇ₴Ⱨ₴₳, ฿ɄĐ ₴Ø฿Øł ₦₳Ɏ₳ⱤłV₳ł ₭₳₭ Ʉ₥ɆɆ₴Ⱨ", "🅺🅰🅺 🅼🅰🅻🅴🅽🅺🅰🆈🅰 🅳🅴🆅🅾🅲🅷🅺🅰 🅾🆃 🅼🅾🅴🅶🅾 🅷🆄🆈🅰 🅾🆃🆅🅾🆁🅰🅲🅷🅸🆅🅰🅴🆂🅷🆂🅰, 🅱🆄🅳 🆂🅾🅱🅾🅸 🅽🅰🆈🅰🆁🅸🆅🅰🅸 🅺🅰🅺 🆄🅼🅴🅴🆂🅷", "『k』『a』『k』 『m』『a』『l』『e』『n』『k』『a』『y』『a』 『d』『e』『v』『o』『c』『h』『k』『a』 『o』『t』 『m』『o』『e』『g』『o』 『h』『u』『y』『a』 『o』『t』『v』『o』『r』『a』『c』『h』『i』『v』『a』『e』『s』『h』『s』『a』, 『b』『u』『d』 『s』『o』『b』『o』『i』 『n』『a』『y』『a』『r』『i』『v』『a』『i』 『k』『a』『k』 『u』『m』『e』『e』『s』『h』", "ｋａｋ　ｍａｌｅｎｋａｙａ　ｄｅｖｏｃｈｋａ　ｏｔ　ｍｏｅｇｏ　ｈｕｙａ　ｏｔｖｏｒａｃｈｉｖａｅｓｈｓａ,　ｂｕｄ　ｓｏｂｏｉ　ｎａｙａｒｉｖａｉ　ｋａｋ　ｕｍｅｅｓｈ", "𝖐𝖆𝖐 𝖒𝖆𝖑𝖊𝖓𝖐𝖆𝖞𝖆 𝖉𝖊𝖛𝖔𝖈𝖍𝖐𝖆 𝖔𝖙 𝖒𝖔𝖊𝖌𝖔 𝖍𝖚𝖞𝖆 𝖔𝖙𝖛𝖔𝖗𝖆𝖈𝖍𝖎𝖛𝖆𝖊𝖘𝖍𝖘𝖆, 𝖇𝖚𝖉 𝖘𝖔𝖇𝖔𝖎 𝖓𝖆𝖞𝖆𝖗𝖎𝖛𝖆𝖎 𝖐𝖆𝖐 𝖚𝖒𝖊𝖊𝖘𝖍",
                    "Ɽ₳₴₴ⱧłⱤłⱠ ₮VØɆ Ø₵Ⱨ₭Ø ĐØ Ɽ₳Ⱬ₥ɆⱤØV ₴ØⱫVɆⱫĐł₳ ₲ɎĐⱤɎ", "🆁🅰🆂🆂🅷🅸🆁🅸🅻 🆃🆅🅾🅴 🅾🅲🅷🅺🅾 🅳🅾 🆁🅰🆉🅼🅴🆁🅾🆅 🆂🅾🆉🆅🅴🆉🅳🅸🅰 🅶🆈🅳🆁🆈", "『r』『a』『s』『s』『h』『i』『r』『i』『l』 『t』『v』『o』『e』 『o』『c』『h』『k』『o』 『d』『o』 『r』『a』『z』『m』『e』『r』『o』『v』 『s』『o』『z』『v』『e』『z』『d』『i』『a』 『G』『y』『d』『r』『y』", "ｒａｓｓｈｉｒｉｌ　ｔｖｏｅ　ｏｃｈｋｏ　ｄｏ　ｒａｚｍｅｒｏｖ　ｓｏｚｖｅｚｄｉａ　Ｇｙｄｒｙ", "𝖗𝖆𝖘𝖘𝖍𝖎𝖗𝖎𝖑 𝖙𝖛𝖔𝖊 𝖔𝖈𝖍𝖐𝖔 𝖉𝖔 𝖗𝖆𝖟𝖒𝖊𝖗𝖔𝖛 𝖘𝖔𝖟𝖛𝖊𝖟𝖉𝖎𝖆 𝕲𝖞𝖉𝖗𝖞",
                    "₮VØɎ₳ ₥₳₮ Ʉ₭Ɽ₳Ⱡ₳ ₥Øł ⱧɄł ₴VØł₥ Ɽ₮Ø₥", "🆃🆅🅾🆈🅰 🅼🅰🆃 🆄🅺🆁🅰🅻🅰 🅼🅾🅸 🅷🆄🅸 🆂🆅🅾🅸🅼 🆁🆃🅾🅼", "『t』『v』『o』『y』『a』 『m』『a』『t』 『u』『k』『r』『a』『l』『a』 『m』『o』『i』 『h』『u』『i』 『s』『v』『o』『i』『m』 『r』『t』『o』『m』", "ｔｖｏｙａ　ｍａｔ　ｕｋｒａｌａ　ｍｏｉ　ｈｕｉ　ｓｖｏｉｍ　ｒｔｏｍ", "𝖙𝖛𝖔𝖞𝖆 𝖒𝖆𝖙 𝖚𝖐𝖗𝖆𝖑𝖆 𝖒𝖔𝖎 𝖍𝖚𝖎 𝖘𝖛𝖔𝖎𝖒 𝖗𝖙𝖔𝖒",
                    "₴₳₴Ɇ₴Ⱨ ฿ɆⱫ ₣łⱠ₮Ɽ₳", "🆂🅰🆂🅴🆂🅷 🅱🅴🆉 🅵🅸🅻🆃🆁🅰", "『s』『a』『s』『e』『s』『h』 『b』『e』『z』 『f』『i』『l』『t』『r』『a』", "ｓａｓｅｓｈ　ｂｅｚ　ｆｉｌｔｒａ", "𝖘𝖆𝖘𝖊𝖘𝖍 𝖇𝖊𝖟 𝖋𝖎𝖑𝖙𝖗𝖆",
                    "ⱧɄł ₴Ø₴ł", "🅷🆄🅸 🆂🅾🆂🅸", "『h』『u』『i』 『s』『o』『s』『i』", "ｈｕｉ　ｓｏｓｉ", "𝖍𝖚𝖎 𝖘𝖔𝖘𝖎",
                    "Ʉ₱₴ ɄɆ฿₳Ⱡ ₮Ɇ฿Ɏ₳ ฿ł₮Øł", "🆄🅿🆂 🆄🅴🅱🅰🅻 🆃🅴🅱🆈🅰 🅱🅸🆃🅾🅸", "『u』『p』『s』 『u』『e』『b』『a』『l』 『t』『e』『b』『y』『a』 『b』『i』『t』『o』『i』", "ｕｐｓ　ｕｅｂａｌ　ｔｅｂｙａ　ｂｉｔｏｉ", "𝖚𝖕𝖘 𝖚𝖊𝖇𝖆𝖑 𝖙𝖊𝖇𝖞𝖆 𝖇𝖎𝖙𝖔𝖎",
                    "Ʉ₱₴ ₴ⱠØ₥₳Ⱡ ₮VØɆ Ⱡł₵Ø ⱧɄɆ₥", "🆄🅿🆂 🆂🅻🅾🅼🅰🅻 🆃🆅🅾🅴 🅻🅸🅲🅾 🅷🆄🅴🅼", "『u』『p』『s』 『s』『l』『o』『m』『a』『l』 『t』『v』『o』『e』 『l』『i』『c』『o』 『h』『u』『e』『m』", "ｕｐｓ　ｓｌｏｍａｌ　ｔｖｏｅ　ｌｉｃｏ　ｈｕｅｍ", "𝖚𝖕𝖘 𝖘𝖑𝖔𝖒𝖆𝖑 𝖙𝖛𝖔𝖊 𝖑𝖎𝖈𝖔 𝖍𝖚𝖊𝖒",
                    "Ⱨ₳Ⱨ₳Ⱨ₳Ⱨ₳ⱧⱧ₳Ⱨ₳Ⱨ₳Ⱨ₳ⱧⱧ₳Ⱨ₳Ⱨ₳Ⱨ₳Ⱨ₳ⱧⱧ₳ ØⱤɄ ₴ ₮Ɇ฿Ɏ₳ ₮Ɏ ₮₳₭ØɆ ₥ɄĐØɆ฿ł₴ⱧɆ ₴Ø₴Ɇ₴Ⱨ ₥₦Ɇ Đł₭Ø ₳ Ⱬ₳₵ⱧɆ₥ Ɇ₴Ⱡł Ɏ₳ ₮Ɇ฿Ɏ₳ ⱧɄɎ₳ⱤɄ ĐØ ₮₳₭Øł ₴₮Ɇ₱Ɇ₦ł ₵Ⱨ₮Ø ₮Ɏ ɄⱫⱧɆ Ʉ₥łⱤ₳Ɇ₴Ⱨ ł ₥Ɏ₵Ⱨł₴Ⱨ ₦₳ ₥ØɆ₥ ⱧɄɆ, ₦₳VɆⱤ₦ØɆ ₦Ɇ ⱧØ₵ⱧɆ₴Ⱨ ĐØ₱Ʉ₴₮ł₮₮₳₭ØɆ ₴Ø ₴VØɆł ₥₳₥₳₴ⱧɆł, ₦Ø ₮Ɏ Ø₱ØⱫĐ₳Ⱡ, Ɏ₳ Ɇł Ɇ₮Ø ĐɆⱠ₳Ⱡ ₴Ø₮₦ł Ɽ₳Ⱬ, Ɇ₴Ⱡł ₦Ɇ ₮Ɏ₴Ɏ₳₵Ⱨł...", "🅷🅰🅷🅰🅷🅰🅷🅰🅷🅷🅰🅷🅰🅷🅰🅷🅰🅷🅷🅰🅷🅰🅷🅰🅷🅰🅷🅰🅷🅷🅰 🅾🆁🆄 🆂 🆃🅴🅱🆈🅰 🆃🆈 🆃🅰🅺🅾🅴 🅼🆄🅳🅾🅴🅱🅸🆂🅷🅴 🆂🅾🆂🅴🆂🅷 🅼🅽🅴 🅳🅸🅺🅾 🅰 🆉🅰🅲🅷🅴🅼 🅴🆂🅻🅸 🆈🅰 🆃🅴🅱🆈🅰 🅷🆄🆈🅰🆁🆄 🅳🅾 🆃🅰🅺🅾🅸 🆂🆃🅴🅿🅴🅽🅸 🅲🅷🆃🅾 🆃🆈 🆄🆉🅷🅴 🆄🅼🅸🆁🅰🅴🆂🅷 🅸 🅼🆈🅲🅷🅸🆂🅷 🅽🅰 🅼🅾🅴🅼 🅷🆄🅴, 🅽🅰🆅🅴🆁🅽🅾🅴 🅽🅴 🅷🅾🅲🅷🅴🆂🅷 🅳🅾🅿🆄🆂🆃🅸🆃🆃🅰🅺🅾🅴 🆂🅾 🆂🆅🅾🅴🅸 🅼🅰🅼🅰🆂🅷🅴🅸, 🅽🅾 🆃🆈 🅾🅿🅾🆉🅳🅰🅻, 🆈🅰 🅴🅸 🅴🆃🅾 🅳🅴🅻🅰🅻 🆂🅾🆃🅽🅸 🆁🅰🆉, 🅴🆂🅻🅸 🅽🅴 🆃🆈🆂🆈🅰🅲🅷🅸...", "『H』『A』『H』『A』『H』『A』『H』『A』『H』『H』『A』『H』『A』『H』『A』『H』『A』『H』『H』『A』『H』『A』『H』『A』『H』『A』『H』『A』『H』『H』『A』 『O』『R』『U』 『S』 『T』『E』『B』『Y』『A』 『T』『Y』 『T』『A』『K』『O』『E』 『M』『U』『D』『O』『E』『B』『I』『S』『H』『E』 『S』『O』『S』『E』『S』『H』 『M』『N』『E』 『D』『I』『K』『O』 『A』 『Z』『A』『C』『H』『E』『M』 『E』『S』『L』『I』 『Y』『A』 『T』『E』『B』『Y』『A』 『H』『U』『Y』『A』『R』『U』 『D』『O』 『T』『A』『K』『O』『I』 『S』『T』『E』『P』『E』『N』『I』 『C』『H』『T』『O』 『T』『Y』 『U』『Z』『H』『E』 『U』『M』『I』『R』『A』『E』『S』『H』 『I』 『M』『Y』『C』『H』『I』『S』『H』 『N』『A』 『M』『O』『E』『M』 『H』『U』『E』, 『N』『A』『V』『E』『R』『N』『O』『E』 『N』『E』 『H』『O』『C』『H』『E』『S』『H』 『D』『O』『P』『U』『S』『T』『I』『T』『T』『A』『K』『O』『E』 『S』『O』 『S』『V』『O』『E』『I』 『M』『A』『M』『A』『S』『H』『E』『I』, 『N』『O』 『T』『Y』 『O』『P』『O』『Z』『D』『A』『L』, 『Y』『A』 『E』『I』 『E』『T』『O』 『D』『E』『L』『A』『L』 『S』『O』『T』『N』『I』 『R』『A』『Z』, 『E』『S』『L』『I』 『N』『E』 『T』『Y』『S』『Y』『A』『C』『H』『I』...", "ＨＡＨＡＨＡＨＡＨＨＡＨＡＨＡＨＡＨＨＡＨＡＨＡＨＡＨＡＨＨＡ　ＯＲＵ　Ｓ　ＴＥＢＹＡ　ＴＹ　ＴＡＫＯＥ　ＭＵＤＯＥＢＩＳＨＥ　ＳＯＳＥＳＨ　ＭＮＥ　ＤＩＫＯ　Ａ　ＺＡＣＨＥＭ　ＥＳＬＩ　ＹＡ　ＴＥＢＹＡ　ＨＵＹＡＲＵ　ＤＯ　ＴＡＫＯＩ　ＳＴＥＰＥＮＩ　ＣＨＴＯ　ＴＹ　ＵＺＨＥ　ＵＭＩＲＡＥＳＨ　Ｉ　ＭＹＣＨＩＳＨ　ＮＡ　ＭＯＥＭ　ＨＵＥ,　ＮＡＶＥＲＮＯＥ　ＮＥ　ＨＯＣＨＥＳＨ　ＤＯＰＵＳＴＩＴＴＡＫＯＥ　ＳＯ　ＳＶＯＥＩ　ＭＡＭＡＳＨＥＩ,　ＮＯ　ＴＹ　ＯＰＯＺＤＡＬ,　ＹＡ　ＥＩ　ＥＴＯ　ＤＥＬＡＬ　ＳＯＴＮＩ　ＲＡＺ,　ＥＳＬＩ　ＮＥ　ＴＹＳＹＡＣＨＩ...", "𝕳𝕬𝕳𝕬𝕳𝕬𝕳𝕬𝕳𝕳𝕬𝕳𝕬𝕳𝕬𝕳𝕬𝕳𝕳𝕬𝕳𝕬𝕳𝕬𝕳𝕬𝕳𝕬𝕳𝕳𝕬 𝕺𝕽𝖀 𝕾 𝕿𝕰𝕭𝖄𝕬 𝕿𝖄 𝕿𝕬𝕶𝕺𝕰 𝕸𝖀𝕯𝕺𝕰𝕭𝕴𝕾𝕳𝕰 𝕾𝕺𝕾𝕰𝕾𝕳 𝕸𝕹𝕰 𝕯𝕴𝕶𝕺 𝕬 𝖅𝕬𝕮𝕳𝕰𝕸 𝕰𝕾𝕷𝕴 𝖄𝕬 𝕿𝕰𝕭𝖄𝕬 𝕳𝖀𝖄𝕬𝕽𝖀 𝕯𝕺 𝕿𝕬𝕶𝕺𝕴 𝕾𝕿𝕰𝕻𝕰𝕹𝕴 𝕮𝕳𝕿𝕺 𝕿𝖄 𝖀𝖅𝕳𝕰 𝖀𝕸𝕴𝕽𝕬𝕰𝕾𝕳 𝕴 𝕸𝖄𝕮𝕳𝕴𝕾𝕳 𝕹𝕬 𝕸𝕺𝕰𝕸 𝕳𝖀𝕰, 𝕹𝕬𝖁𝕰𝕽𝕹𝕺𝕰 𝕹𝕰 𝕳𝕺𝕮𝕳𝕰𝕾𝕳 𝕯𝕺𝕻𝖀𝕾𝕿𝕴𝕿𝕿𝕬𝕶𝕺𝕰 𝕾𝕺 𝕾𝖁𝕺𝕰𝕴 𝕸𝕬𝕸𝕬𝕾𝕳𝕰𝕴, 𝕹𝕺 𝕿𝖄 𝕺𝕻𝕺𝖅𝕯𝕬𝕷, 𝖄𝕬 𝕰𝕴 𝕰𝕿𝕺 𝕯𝕰𝕷𝕬𝕷 𝕾𝕺𝕿𝕹𝕴 𝕽𝕬𝖅, 𝕰𝕾𝕷𝕴 𝕹𝕰 𝕿𝖄𝕾𝖄𝕬𝕮𝕳𝕴...",
                    "Ⱨ₳Ⱨ₳ ØⱤ₦ɄⱠ ₴ ₮Ɇ฿Ɏ₳ ₭Ø₲Đ₳ ₮Ʉ ₥Øł ⱧɄł Ⱬ₳ Ø฿Ɇ ₴ⱧɆ₭ł Ʉ₱ⱠɆ₮₳Ⱡ", "🅷🅰🅷🅰 🅾🆁🅽🆄🅻 🆂 🆃🅴🅱🆈🅰 🅺🅾🅶🅳🅰 🆃🆄 🅼🅾🅸 🅷🆄🅸 🆉🅰 🅾🅱🅴 🆂🅷🅴🅺🅸 🆄🅿🅻🅴🆃🅰🅻", "『h』『a』『h』『a』 『o』『r』『n』『u』『l』 『s』 『t』『e』『b』『y』『a』 『k』『o』『g』『d』『a』 『t』『u』 『m』『o』『i』 『h』『u』『i』 『z』『a』 『o』『b』『e』 『s』『h』『e』『k』『i』 『u』『p』『l』『e』『t』『a』『l』", "ｈａｈａ　ｏｒｎｕｌ　ｓ　ｔｅｂｙａ　ｋｏｇｄａ　ｔｕ　ｍｏｉ　ｈｕｉ　ｚａ　ｏｂｅ　ｓｈｅｋｉ　ｕｐｌｅｔａｌ", "卄卂卄卂 ㄖ尺几ㄩㄥ 丂 ㄒ乇乃ㄚ卂 ҜㄖᎶᗪ卂 ㄒㄩ 爪ㄖ丨 卄ㄩ丨 乙卂 ㄖ乃乇 丂卄乇Ҝ丨 ㄩ卩ㄥ乇ㄒ卂ㄥ",
                    "Че ты мне сделаешь, сын портовой шлюхи?", "ꌗꂦꌗꍟꌗꃅ", "『m』『a』『m』『u』 『e』『b』『a』『l』", "『h』『a』『h』 『o』『r』『u』 『s』 『t』『e』『b』『y』『a』", "꒒ꍏ꒒ꀘꍏ", "🆂🅾🆂🅴🆂🅷 🅼🅽🅴 🅳🅸🅺🅾", "ｅｓｔｅｔｉｃｈｎｏ　ｅｂｕ　ｔｅｂｙａ", "ꃅꍏꃅꍏ ꂦꋪꀎ ꀘꍏꀘꂦꀤ ꁴꃅꍟ ꓄ꌩ ꈤꀤꉓꃅ꓄ꂦꁴꃅꈤꌩꀤ"]

# варианты фото
PHOTO_VARIANTS = ["photo-198847189_457239017", "photo-198847189_457239018", "photo-198847189_457239019", "photo-198847189_457239021", "photo-198847189_457239023",
                  "photo-198847189_457239024", "photo-198847189_457239025", "photo-198847189_457239027", "photo-198847189_457239030", "photo-198847189_457239031",
                  "photo-198847189_457239033", "photo-198847189_457239034", "photo-198847189_457239035", "photo-198847189_457239036", "photo-198847189_457239037",
                  "photo-198847189_457239038", "photo-198847189_457239039", "photo-198847189_457239040", "photo-198847189_457239041", "photo-198847189_457239049",
                  "photo-198847189_457239050", "photo-198847189_457239051", "photo-198847189_457239052", "photo-198847189_457239053", "photo-198847189_457239054",
                  "photo-198847189_457239055", "photo-198847189_457239056", "photo-198847189_457239057", "photo-198847189_457239058", "photo-198847189_457239059",
                  "photo-198847189_457239060", "photo-198847189_457239061", "photo-198847189_457239062", "photo-198847189_457239063", "photo-198847189_457239064",
                  "photo-198847189_457239065", "photo-198847189_457239066", "photo-198847189_457239067", "photo-198847189_457239068", "photo-198847189_457239069",
                  "photo-198847189_457239070", "photo-198847189_457239071", "photo-198847189_457239072", "photo-198847189_457239073", "photo-198847189_457239074",
                  "photo-198847189_457239075", "photo-198847189_457239076", "photo-198847189_457239077", "photo-198847189_457239078", "photo-198847189_457239079",
                  "photo-198847189_457239080", "photo-198847189_457239081", "photo-198847189_457239083", "photo-198847189_457239084", "photo-198847189_457239085",
                  "photo-198847189_457239086", "photo-198847189_457239087", "photo-198847189_457239088", "photo-198847189_457239089", "photo-198847189_457239090",
                  "photo-198847189_457239091", "photo-198847189_457239092", "photo-198847189_457239093", "photo-198847189_457239094", "photo-198847189_457239095",
                  "photo-198847189_457239096"]

# варианты ошибок доступа
ERRORS = "купи админку у @id626727521 за 100р/нед и я подумаю"

