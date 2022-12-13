# Lab3_SCV

## Exercici 1:

This exercise is done in "Exercici1.py". In this script I created a HLS transport stream container with one the video 1min_cuttedVideo which is also given in this repository. The ffmpeg command is basically 
reading the input video and resizing it to multiple resolutions, then transcodes the video into multiple bitrates for the HLS packing, an finally created the HLS playlists (m3u8).
If we execute this script (with the 1min_cuttedVideo) we obtain:
  - The master.m3u8 (text)
  - The stream_0.m3u8 (test)
  - The stream_1.m3u8 (text)
  - The stream_3.m3u8 (text)
  
 Together with the 3 folders containing all the .ts files for each stream with different resolutions:
  - stream_0/data00.ts, data01.ts, data02.ts,... (original resolution)
  - stream_1/data00.ts, data01.ts, data02.ts,... (1260x720 resolution)
  - stream_2/data00.ts, data01.ts, data02.ts,... (640x360 resolution)

## Exercici 2:

In this exercise I tried to download the bento4 tools using the following commands with Ubuntu:
```
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh
./vcpkg integrate install
./vcpkg install bento4
```

Once I had this downloaded I tried to create a MPD video file. To do so, the file should follow the next steps: fragment it, encrypt it (type of encryptation) and finally dash it.

## Exercici 3:

This exercise is done in "Exercici3.py". In this script I created a function that directlly calls the ffmpeg command able to livestream locally the input video. Then, I called the function with the 1min_cuttedVideo.mp4 video in order to live stream this video locally from my computer. In order to play the stream, we just need to introduce the following command in another terminal: ffplay rtp.//127.0.0.1:1234.
In this repository, there is also a screenshot called "LiveStreaming_1min_cuttedVideo,PNG" showing the output of the terminal when the live stream had finished.

## Exercici 4:

In this final exercise I opened a livestreaming show in Twitch, because is on of the most famous streaming platforms nowadays, and I tried to look for the protocols and codecs that are used there. To do so, I used Google DevTools to inspect the video that I was watching in Twitch. So I saw all the packages that can be seen in the screenshot "InspectioningNetwork.PNG" and looking more into detail we can see two types, the '.m3u8' which are the parts containing text and the '.ts' which are the parts containing the video. So, we can deduct that this video in Twitch is using HLS.
In the screenshots "Twitch_m3u8_file.PNG" and "Twitch_ts_file.PNG" we can see the specific information of '.m3u8' and '.ts' that I mentioned before.
