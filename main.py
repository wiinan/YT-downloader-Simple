import pytube
import os
from pytube import Playlist
from pytube import YouTube

def downloadURL(url):
    youtube = YouTube(url)
    i = 1
    for lista in youtube.streams.order_by('resolution'):
        try:
            print(lista)
            i += 1
        except:
            pass
        video = youtube.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').last()
        title = video.title
        print('Start: ' + str(title))
        video.download('YT-down')

def downloadPlaylist(url_playlist):
    pl = Playlist(url_playlist)
    i = 1
    print('Iniciando Playlist')
    for video in pl.videos:
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').get_highest_resolution().download('TY-play')
        try:
            title = video.title
            print('Iniciando download ' + str(i) + ': ' + str(title))
            i += 1
        except:
            pass

def download_mp3(url_audio):
    audio = YouTube(url_audio)
    i = 1
    for list in audio.streams.order_by('resolution'):
        try:
            print(list)
            i += 1
        except:
            pass
        audio_conv = audio.streams.filter(only_audio=True).first()
        title = audio_conv.title
        print('Start: ' + str(title))
        destination = 'YT-audio'
        out_file = audio_conv.download(output_path=destination)
        try:
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            os.remove(out_file)
        except:
            pass

enter = 's'
while(enter != 'n'):
    retorno = int(input('1 - video, 2 - mp3, 3 - playlist => '))
    if retorno == 1:
        link_solo = input('url - solo: ')
        downloadURL(link_solo)
    if retorno == 2:
        link_mp3 = input('url do Audio: ')
        download_mp3(link_mp3)
    if retorno == 3:
        link = input('Url: ')
        downloadPlaylist(link)
    enter = input('continuar? s/n ')

