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

