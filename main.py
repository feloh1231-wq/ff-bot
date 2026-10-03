import telebot
import random

TOKEN = "حط التوكن الجديد هنا"
bot = telebot.TeleBot(TOKEN)

players = []

@bot.message_handler(commands=['join'])
def join(m):
    user = f"@{m.from_user.username}" if m.from_user.username else m.from_user.first_name
    if user not in players:
        players.append(user)
        bot.reply_to(m, f"✅ {user} دخل القايمة - العدد دلوقتي {len(players)}")
    else:
        bot.reply_to(m, "انت دخلت قبل كده!")

@bot.message_handler(commands=['squad5'])
def squad(m):
    if len(players) < 5:
        bot.reply_to(m, f"لسه محتاجين ناس! العدد {len(players)}/5")
        return
    random.shuffle(players)
    text = "🔥 تقسيم السكوادات 🔥\n\n"
    for i in range(0, len(players), 5):
        squad_list = players[i:i+5]
        text += f"سكواد {i//5+1}: {' - '.join(squad_list)}\n"
    bot.send_message(m.chat.id, text)

@bot.message_handler(commands=['clear'])
def clear(m):
    players.clear()
    bot.reply_to(m, "🗑️ القايمة اتمسحت")

@bot.message_handler(commands=['list'])
def list_players(m):
    if not players:
        bot.reply_to(m, "مفيش حد في القايمة")
    else:
        bot.reply_to(m, "اللاعيبة:\n" + "\n".join(players))

bot.polling()
