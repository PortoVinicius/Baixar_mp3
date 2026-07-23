import yt_dlp
import os

pasta_destino = "musicas"

if not os.path.exists(pasta_destino):
	os.makedirs(pasta_destino)

url = input("Cole o Link do video: ")

opcoes = {
	"format": "bestaudio/best",
	"outtmpl": f"{pasta_destino}/%(title)s.%(ext)s",
	"noplaylist": True,
	"postprocessors": [
		{
			"key": "FFmpegExtractAudio",
			"preferredcodec": "mp3",
			"preferredquality": "192",
		}
	],
}

with yt_dlp.YoutubeDL(opcoes) as ydl:
	ydl.download([url])

print("Download concluido!")
