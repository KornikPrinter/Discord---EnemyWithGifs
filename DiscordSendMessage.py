import requests
import time
#Paste the channel id into ChannelId var
ChannelId = ''
url = f'https://discord.com/api/v9/channels/{ChannelId}/messages'
gifs = ['https://tenor.com/view/oh-the-misery-cat-gif-25928322', 'https://tenor.com/view/enemy-i-wake-up-to-the-sounds-of-the-silence-that-allows-gif-26060699', 'https://tenor.com/view/for-my-mind-to-run-around-with-my-ear-up-to-the-ground-enemy-gif-26060700', 'https://tenor.com/view/enemy-im-searching-to-behold-the-stories-that-are-told-gif-26060713', 'https://tenor.com/view/when-my-back-is-to-the-world-that-was-smiling-when-i-turned-enemy-gif-26060701', 'https://tenor.com/view/enemy-tell-you-youre-the-greatest-gif-26060714', 'https://tenor.com/view/but-once-you-turn-they-hate-us-enemy-gif-26060702', 'https://tenor.com/view/oh-the-misery-oh-the-misery-everybody-wants-to-be-my-enemy-gif-25368312', 'https://tenor.com/view/everybody-wants-to-be-my-enemy-enemy-gif-26060704', 'https://tenor.com/view/spare-spare-the-sympathy-the-sympathy-wawa-cat-gif-25825252', 'https://tenor.com/view/everybody-wants-to-be-my-enemy-enemy-gif-26060704', 'https://tenor.com/view/oh-the-misery-cat-gif-25928322', 'https://tenor.com/view/my-enemy-enemy-gif-26060859', 'https://tenor.com/view/oh-the-misery-cat-gif-25928322', 'https://tenor.com/view/wawa-cat-wawa-oh-the-misery-oh-the-misery-cat-gif-25978650', 'https://tenor.com/view/your-words-up-on-the-wall-as-youre-praying-for-my-fall-enemy-gif-26060826', 'https://tenor.com/view/and-the-laughter-in-the-halls-and-the-name-that-ive-been-called-enemy-gif-26060827', 'https://tenor.com/view/i-stack-it-in-my-mind-and-im-waiting-for-the-time-enemy-gif-26060828', 'https://tenor.com/view/when-i-show-you-what-its-like-to-be-words-spit-in-a-mic-enemy-gif-26060829', 'https://tenor.com/view/enemy-tell-you-youre-the-greatest-gif-26060714', 'https://tenor.com/view/but-once-you-turn-they-hate-us-enemy-gif-26060702', 'https://tenor.com/view/oh-the-misery-oh-the-misery-everybody-wants-to-be-my-enemy-gif-25368312', 'https://tenor.com/view/everybody-wants-to-be-my-enemy-enemy-gif-26060704', 'https://tenor.com/view/spare-spare-the-sympathy-the-sympathy-wawa-cat-gif-25825252', 'https://tenor.com/view/everybody-wants-to-be-my-enemy-enemy-gif-26060704', 'https://tenor.com/view/oh-the-misery-cat-gif-25928322', 'https://tenor.com/view/my-enemy-enemy-gif-26060859', 'https://tenor.com/view/oh-the-misery-cat-gif-25928322', 'https://tenor.com/view/uh-look-enemy-gif-26060830', 'https://tenor.com/view/okay-im-hoping-somebody-pray-for-me-enemy-gif-26060831', 'https://tenor.com/view/im-praying-that-somebody-hope-for-me-enemy-gif-26060832', 'https://tenor.com/view/eggcat-im-staying-where-nobody-supposed-to-be-gif-25715277', 'https://tenor.com/view/posted-being-a-wreck-of-emotions-enemy-gif-26060846', 'https://tenor.com/view/ready-to-go-whenever-just-let-me-know-enemy-gif-26060847', 'https://tenor.com/view/the-enemy-on-my-trail-my-energy-unavailable-enemy-gif-26060849', 'https://tenor.com/view/ima-tell-em-hasta-luego-enemy-gif-26060850', 'https://tenor.com/view/they-wanna-plot-my-trot-on-the-top-enemy-gif-26060851', 'https://tenor.com/view/ive-been-outta-shape-thinkin-out-the-box-im-an-astronaut-enemy-gif-26060852', 'https://tenor.com/view/oh-the-misery-everybody-wanna-be-my-enemy-cat-gif-25172445', 'https://tenor.com/view/and-it-matters-more-because-i-had-it-not-enemy-gif-26060844', 'https://tenor.com/view/had-i-thought-about-wreaking-havoc-on-an-opposition-enemy-gif-26060845', 'https://tenor.com/view/kinda-shocking-they-wanted-static-with-precision-im-automatic-enemy-gif-26060863', 'https://tenor.com/view/oh-the-misery-everybody-wanna-be-my-enemy-cat-gif-25172445', 'https://tenor.com/view/it-dont-matter-cause-we-at-your-throat-enemy-gif-26060858', 'https://tenor.com/view/everybody-wants-to-be-my-enemy-enemy-gif-26060704', 'https://tenor.com/view/spare-spare-the-sympathy-the-sympathy-wawa-cat-gif-25825252', 'https://tenor.com/view/everybody-wants-to-be-my-enemy-enemy-gif-26060704', 'https://tenor.com/view/oh-the-misery-oh-the-misery-everybody-wants-to-be-my-enemy-gif-25368312', 'https://tenor.com/view/everybody-wants-to-be-my-enemy-enemy-gif-26060704', 'https://tenor.com/view/spare-spare-the-sympathy-the-sympathy-wawa-cat-gif-25825252', 'https://tenor.com/view/everybody-wants-to-be-my-enemy-enemy-gif-26060704', 'https://tenor.com/view/i-swear-that-ill-never-be-saint-wawa-i-swear-ill-never-be-a-saint-gif-26493237', 'https://tenor.com/view/my-enemy-enemy-gif-26060859', 'https://tenor.com/view/i-swear-that-ill-never-be-saint-wawa-i-swear-ill-never-be-a-saint-gif-26493237', 'https://tenor.com/view/oh-the-misery-cat-gif-25928322']
#Paste your discord token into DiscordToken var
DiscordToken=''
myobj = {'somekey': 'somevalue'}
header = {'Authorization': f'{DiscordToken}'}
for i in range(len(gifs)):
    payload = {'content' : f'{gifs[i]}'}
    x = requests.post(url, payload,  headers = header)
    time.sleep(0.5) #I dont recommend setting it much lower as you can get rate limited with >5messages a second
    print(x.text) #'debug' can remove
