#!/bin/bash

if [[ -z $1 ]]; then
    echo Please provide an argument.
    exit 1
fi

filename=$(basename "$1")
filename_without_extension="${filename%.*}"

edge-tts --file "${filename}" --write-media "build/${filename_without_extension}.mp3" --write-subtitles "build/${filename_without_extension}.vtt" --voice zh-CN-XiaoxiaoNeural