from pytube import Playlist

playlist = Playlist(
    "https://youtube.com/playlist?list=PLbDRORmj0gydAp_9O0Vc4fq4qE3zmrTdw")
print(f"Downloading: {playlist.title}")
print("Number of videos in playlist: %s" % len(playlist.video_urls))

for video in playlist.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
