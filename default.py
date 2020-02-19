from xbmcswift2 import Plugin, xbmcgui
import requests

plugin = Plugin()

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': "https://manage.kawaaii.moe/radio/8000/test",
            'is_playable': True
        },
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('recent_plays'),
            'is_playable': False
        }
    ]
    return items

@plugin.route('/recent_plays/')
def recent_plays():
    recent_songs = get_recent_plays()
    items = []

    for song in recent_songs:
        items.append({
            'label': song['song']['artist'] + ' - ' + song['song']['title'],
            'thumbnail': song['song']['art'],
            'is_playable': False
        })
    return items

def get_recent_plays():
    response = requests.get('https://manage.kawaaii.moe/api/nowplaying')
    return response.json()[0]['song_history']

if __name__ == '__main__':
    plugin.run()