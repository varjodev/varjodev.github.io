:: Decodes and encodes a file to webm for smaller size and ease of html integration with ffmpeg
ffmpeg -i %1 -vcodec libvpx-vp9 -crf 10 -b:v 1M -an %~n1.webm