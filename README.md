# jma-weather-images

基本天気画像の組み合わせによって、すべての気象テロップ番号に対応する画像を生成する例です。

基本天気画像を網羅的に用意することは必須ではありません。例えば、多くのメディアで「霧」は「くもり」と同じマークで表現されていたり、「雨または雪」は単なる雪だるまマークで表現されていたりします。


# ファイル一覧

- `srcimgs/` —- 基本天気画像
  -  `sun.svg` -- 晴れ
  -  `cloud.svg` -- くもり
  -  `rain.svg` -- 雨
  -  `snow.svg` -- 雪
  -  `mist.svg` -- 霧
  -  `rain_and_snow.svg` -- 雨または雪/雪または雨/みぞれ
  -  `fair_night.svg` -- 晴れ (夜)
  -  `rain_heavy.svg` -- 雨強い
  -  `rain_heavy_wind.svg` -- 雨強い 風強い
  -  `snow_heavy.svg` -- 雪強い
  -  `rain_wind.svg` -- 雨 風強い
  -  `snow_wind.svg` -- 雪 風強い
  -  `rain_thunder.svg` -- 雨 雷を伴う
  -  `snow_thunder.svg` -- 雪 雷を伴う
  -  `tr.svg` -- 「のち」サイン
- `codes.json` -- 気象テロップ番号
- `generate.py` -- 生成用プログラム
- `output/` -- 生成された画像データ



# 出力例

凡例:

- `tr`: のち
- `st`: 時々
- `te`: 一時

|code|description|instruction|img|
|:-:|---|---|:-:|
| 100 | 晴れ | sun   | <img width="50" src="./output_refs/100.png" /> |
| 101 | 晴れ時々くもり | sun st cloud | <img width="50" src="./output_refs/101.png" /> |
| 102 | 晴れ一時雨 | sun te rain | <img width="50" src="./output_refs/102.png" /> |
| 103 | 晴れ時々雨 | sun st rain | <img width="50" src="./output_refs/103.png" /> |
| 104 | 晴れ一時雪 | sun te snow | <img width="50" src="./output_refs/104.png" /> |
| 105 | 晴れ時々雪 | sun st snow | <img width="50" src="./output_refs/105.png" /> |
| 106 | 晴れ一時雨か雪 | sun te rain_or_snow | <img width="50" src="./output_refs/106.png" /> |
| 107 | 晴れ時々雨か雪 | sun st rain_or_snow | <img width="50" src="./output_refs/107.png" /> |
| 108 | 晴れ一時雨か雷雨 | sun te rain_thunder | <img width="50" src="./output_refs/108.png" /> |
| 110 | 晴れのち時々くもり | sun trst cloud | <img width="50" src="./output_refs/110.png" /> |
| 111 | 晴れのちくもり | sun tr cloud | <img width="50" src="./output_refs/111.png" /> |
| 112 | 晴れのち一時雨 | sun trst rain | <img width="50" src="./output_refs/112.png" /> |
| 113 | 晴れのち時々雨 | sun trte rain | <img width="50" src="./output_refs/113.png" /> |
| 114 | 晴れのち雨 | sun tr rain | <img width="50" src="./output_refs/114.png" /> |
| 115 | 晴れのち一時雪 | sun trte snow | <img width="50" src="./output_refs/115.png" /> |
| 116 | 晴れのち時々雪 | sun trst snow | <img width="50" src="./output_refs/116.png" /> |
| 117 | 晴れのち雪 | sun tr snow | <img width="50" src="./output_refs/117.png" /> |
| 118 | 晴れのち雨か雪 | sun tr rain_or_snow | <img width="50" src="./output_refs/118.png" /> |
| 119 | 晴れのち雨か雷雨 | sun tr rain_thunder | <img width="50" src="./output_refs/119.png" /> |
| 120 | 晴れ朝夕一時雨 | sun te rain | <img width="50" src="./output_refs/120.png" /> |
| 121 | 晴れ朝の内一時雨 | sun te rain | <img width="50" src="./output_refs/121.png" /> |
| 122 | 晴れ夕方一時雨 | sun te rain | <img width="50" src="./output_refs/122.png" /> |
| 123 | 晴れ山沿い雷雨 | sun   | <img width="50" src="./output_refs/123.png" /> |
| 124 | 晴れ山沿い雪 | sun   | <img width="50" src="./output_refs/124.png" /> |
| 125 | 晴れ午後は雷雨 | sun tr rain_thunder | <img width="50" src="./output_refs/125.png" /> |
| 126 | 晴れ昼頃から雨 | sun tr rain | <img width="50" src="./output_refs/126.png" /> |
| 127 | 晴れ夕方から雨 | sun tr rain | <img width="50" src="./output_refs/127.png" /> |
| 128 | 晴れ夜は雨 | sun tr rain | <img width="50" src="./output_refs/128.png" /> |
| 129 | 晴れ夜半から雨 | sun tr rain | <img width="50" src="./output_refs/129.png" /> |
| 130 | 朝の内霧後晴れ | mist tr sun | <img width="50" src="./output_refs/130.png" /> |
| 131 | 晴れ明け方霧 | sun tr mist | <img width="50" src="./output_refs/131.png" /> |
| 132 | 晴れ朝夕くもり | sun st cloud | <img width="50" src="./output_refs/132.png" /> |
| 140 | 晴れ時々雨で雷を伴う | sun st rain_thunder | <img width="50" src="./output_refs/140.png" /> |
| 160 | 晴れ一時雪か雨 | sun te snow_or_rain | <img width="50" src="./output_refs/160.png" /> |
| 170 | 晴れ時々雪か雨 | sun st snow_or_rain | <img width="50" src="./output_refs/170.png" /> |
| 181 | 晴れのち雪か雨 | sun tr snow_or_rain | <img width="50" src="./output_refs/181.png" /> |
| 200 | くもり | cloud   | <img width="50" src="./output_refs/200.png" /> |
| 201 | くもり時々晴 | cloud st sun | <img width="50" src="./output_refs/201.png" /> |
| 202 | くもり一時雨 | cloud te rain | <img width="50" src="./output_refs/202.png" /> |
| 203 | くもり時々雨 | cloud st rain | <img width="50" src="./output_refs/203.png" /> |
| 204 | くもり一時雪 | cloud te snow | <img width="50" src="./output_refs/204.png" /> |
| 205 | くもり時々雪 | cloud st snow | <img width="50" src="./output_refs/205.png" /> |
| 206 | くもり一時雨か雪 | cloud te rain_or_snow | <img width="50" src="./output_refs/206.png" /> |
| 207 | くもり時々雨か雪 | cloud st rain_or_snow | <img width="50" src="./output_refs/207.png" /> |
| 208 | くもり一時雨か雷雨 | cloud te rain_thunder | <img width="50" src="./output_refs/208.png" /> |
| 209 | 霧 | mist   | <img width="50" src="./output_refs/209.png" /> |
| 210 | くもりのち時々晴れ | cloud trst sun | <img width="50" src="./output_refs/210.png" /> |
| 211 | くもりのち晴れ | cloud tr sun | <img width="50" src="./output_refs/211.png" /> |
| 212 | くもりのち一時雨 | cloud trte rain | <img width="50" src="./output_refs/212.png" /> |
| 213 | くもりのち時々雨 | cloud trst rain | <img width="50" src="./output_refs/213.png" /> |
| 214 | くもりのち雨 | cloud tr rain | <img width="50" src="./output_refs/214.png" /> |
| 215 | くもりのち一時雪 | cloud trte snow | <img width="50" src="./output_refs/215.png" /> |
| 216 | くもりのち時々雪 | cloud trst snow | <img width="50" src="./output_refs/216.png" /> |
| 217 | くもりのち雪 | cloud tr snow | <img width="50" src="./output_refs/217.png" /> |
| 218 | くもりのち雨か雪 | cloud tr rain | <img width="50" src="./output_refs/218.png" /> |
| 219 | くもりのち雨か雷雨 | cloud tr rain | <img width="50" src="./output_refs/219.png" /> |
| 220 | くもり朝夕一時雨 | cloud te rain | <img width="50" src="./output_refs/220.png" /> |
| 221 | くもり朝の内一時雨 | cloud te rain | <img width="50" src="./output_refs/221.png" /> |
| 222 | くもり夕方一時雨 | cloud te rain | <img width="50" src="./output_refs/222.png" /> |
| 223 | くもり日中時々晴れ | cloud st sun | <img width="50" src="./output_refs/223.png" /> |
| 224 | くもり昼頃から雨 | cloud tr rain | <img width="50" src="./output_refs/224.png" /> |
| 225 | くもり夕方から雨 | cloud tr rain | <img width="50" src="./output_refs/225.png" /> |
| 226 | くもり夜は雨 | cloud tr rain | <img width="50" src="./output_refs/226.png" /> |
| 227 | くもり夜半から雨 | cloud tr rain | <img width="50" src="./output_refs/227.png" /> |
| 228 | くもり昼頃から雪 | cloud tr snow | <img width="50" src="./output_refs/228.png" /> |
| 229 | くもり夕方から雪 | cloud tr snow | <img width="50" src="./output_refs/229.png" /> |
| 230 | くもり夜は雪 | cloud tr snow | <img width="50" src="./output_refs/230.png" /> |
| 231 | くもり海上海岸は霧か霧雨 | cloud   | <img width="50" src="./output_refs/231.png" /> |
| 240 | くもり時々雨で雷を伴う | cloud te rain_thunder | <img width="50" src="./output_refs/240.png" /> |
| 250 | くもり時々雪で雷を伴う | cloud st snow_thunder | <img width="50" src="./output_refs/250.png" /> |
| 260 | くもり一時雪か雨 | cloud te snow_or_rain | <img width="50" src="./output_refs/260.png" /> |
| 270 | くもり時々雪か雨 | cloud st snow_or_rain | <img width="50" src="./output_refs/270.png" /> |
| 281 | くもりのち雪か雨 | cloud tr snow_or_rain | <img width="50" src="./output_refs/281.png" /> |
| 300 | 雨 | rain   | <img width="50" src="./output_refs/300.png" /> |
| 301 | 雨時々晴れ | rain st sun | <img width="50" src="./output_refs/301.png" /> |
| 302 | 雨時々止む | rain st cloud | <img width="50" src="./output_refs/302.png" /> |
| 303 | 雨時々雪 | rain st snow | <img width="50" src="./output_refs/303.png" /> |
| 304 | 雨か雪 | rain_or_snow   | <img width="50" src="./output_refs/304.png" /> |
| 306 | 大雨 | rain_heavy   | <img width="50" src="./output_refs/306.png" /> |
| 307 | 風雨共に強い | rain_heavy_wind   | <img width="50" src="./output_refs/307.png" /> |
| 308 | 雨で暴風を伴う | rain_wind   | <img width="50" src="./output_refs/308.png" /> |
| 309 | 雨一時雪 | rain te snow | <img width="50" src="./output_refs/309.png" /> |
| 311 | 雨のち晴れ | rain tr sun | <img width="50" src="./output_refs/311.png" /> |
| 313 | 雨のちくもり | rain tr cloud | <img width="50" src="./output_refs/313.png" /> |
| 314 | 雨のち時々雪 | rain trst snow | <img width="50" src="./output_refs/314.png" /> |
| 315 | 雨のち雪 | rain tr snow | <img width="50" src="./output_refs/315.png" /> |
| 316 | 雨か雪のち晴れ | rain_or_snow tr sun | <img width="50" src="./output_refs/316.png" /> |
| 317 | 雨か雪のちくもり | rain_or_snow tr cloud | <img width="50" src="./output_refs/317.png" /> |
| 320 | 朝の内雨のち晴れ | rain tr sun | <img width="50" src="./output_refs/320.png" /> |
| 321 | 朝の内雨のちくもり | rain tr cloud | <img width="50" src="./output_refs/321.png" /> |
| 322 | 雨朝晩一時雪 | rain te snow | <img width="50" src="./output_refs/322.png" /> |
| 323 | 雨昼頃から晴れ | rain tr sun | <img width="50" src="./output_refs/323.png" /> |
| 324 | 雨夕方から晴れ | rain tr sun | <img width="50" src="./output_refs/324.png" /> |
| 325 | 雨夜は晴 | rain tr sun | <img width="50" src="./output_refs/325.png" /> |
| 326 | 雨夕方から雪 | rain tr snow | <img width="50" src="./output_refs/326.png" /> |
| 327 | 雨夜は雪 | rain tr snow | <img width="50" src="./output_refs/327.png" /> |
| 328 | 雨一時強く降る | rain te rain_heavy | <img width="50" src="./output_refs/328.png" /> |
| 329 | 雨一時みぞれ | rain te rain_and_snow | <img width="50" src="./output_refs/329.png" /> |
| 340 | 雪か雨 | snow_or_rain   | <img width="50" src="./output_refs/340.png" /> |
| 350 | 雨で雷を伴う | rain_thunder   | <img width="50" src="./output_refs/350.png" /> |
| 361 | 雪か雨のち晴れ | snow_or_rain tr sun | <img width="50" src="./output_refs/361.png" /> |
| 371 | 雪か雨のちくもり | snow_or_rain tr cloud | <img width="50" src="./output_refs/371.png" /> |
| 400 | 雪 | snow   | <img width="50" src="./output_refs/400.png" /> |
| 401 | 雪時々晴れ | snow st sun | <img width="50" src="./output_refs/401.png" /> |
| 402 | 雪時々止む | snow st cloud | <img width="50" src="./output_refs/402.png" /> |
| 403 | 雪時々雨 | snow st rain | <img width="50" src="./output_refs/403.png" /> |
| 405 | 大雪 | snow_heavy   | <img width="50" src="./output_refs/405.png" /> |
| 406 | 風雪強い | snow_wind   | <img width="50" src="./output_refs/406.png" /> |
| 407 | 暴風雪 | snow_wind   | <img width="50" src="./output_refs/407.png" /> |
| 409 | 雪一時雨 | snow te rain | <img width="50" src="./output_refs/409.png" /> |
| 411 | 雪のち晴れ | snow tr sun | <img width="50" src="./output_refs/411.png" /> |
| 413 | 雪のちくもり | snow tr cloud | <img width="50" src="./output_refs/413.png" /> |
| 414 | 雪のち雨 | snow tr rain | <img width="50" src="./output_refs/414.png" /> |
| 420 | 朝の内雪のち晴れ | snow tr sun | <img width="50" src="./output_refs/420.png" /> |
| 421 | 朝の内雪のちくもり | snow tr cloud | <img width="50" src="./output_refs/421.png" /> |
| 422 | 雪昼頃から雨 | snow tr rain | <img width="50" src="./output_refs/422.png" /> |
| 423 | 雪夕方から雨 | snow tr rain | <img width="50" src="./output_refs/423.png" /> |
| 424 | 雪夜半から雨 | snow tr rain | <img width="50" src="./output_refs/424.png" /> |
| 425 | 雪一時強く降る | snow te snow_heavy | <img width="50" src="./output_refs/425.png" /> |
| 426 | 雪のちみぞれ | snow tr rain_and_snow | <img width="50" src="./output_refs/426.png" /> |
| 427 | 雪一時みぞれ | snow te rain_and_snow | <img width="50" src="./output_refs/427.png" /> |
| 450 | 雪で雷を伴う | snow_thunder   | <img width="50" src="./output_refs/450.png" /> |
| 700 |  | night_fair   | <img width="50" src="./output_refs/700.png" /> |
| 701 |  | night_fair st cloud | <img width="50" src="./output_refs/701.png" /> |
| 702 |  | night_fair te rain | <img width="50" src="./output_refs/702.png" /> |
| 703 |  | night_fair st rain | <img width="50" src="./output_refs/703.png" /> |
| 704 |  | night_fair te snow | <img width="50" src="./output_refs/704.png" /> |
| 705 |  | night_fair st snow | <img width="50" src="./output_refs/705.png" /> |
| 706 |  | night_fair te rain_or_snow | <img width="50" src="./output_refs/706.png" /> |
| 707 |  | night_fair st rain_or_snow | <img width="50" src="./output_refs/707.png" /> |
| 708 |  | night_fair te rain_thunder | <img width="50" src="./output_refs/708.png" /> |
| 710 |  | night_fair trst cloud | <img width="50" src="./output_refs/710.png" /> |
| 711 |  | night_fair tr cloud | <img width="50" src="./output_refs/711.png" /> |
| 712 |  | night_fair trst rain | <img width="50" src="./output_refs/712.png" /> |
| 713 |  | night_fair trte rain | <img width="50" src="./output_refs/713.png" /> |
| 714 |  | night_fair tr rain | <img width="50" src="./output_refs/714.png" /> |
| 715 |  | night_fair trte snow | <img width="50" src="./output_refs/715.png" /> |
| 716 |  | night_fair trst snow | <img width="50" src="./output_refs/716.png" /> |
| 717 |  | night_fair tr snow | <img width="50" src="./output_refs/717.png" /> |
| 718 |  | night_fair tr rain_or_snow | <img width="50" src="./output_refs/718.png" /> |
| 719 |  | night_fair tr rain_thunder | <img width="50" src="./output_refs/719.png" /> |
| 720 |  | night_fair te rain | <img width="50" src="./output_refs/720.png" /> |
| 721 |  | night_fair te rain | <img width="50" src="./output_refs/721.png" /> |
| 722 |  | night_fair te rain | <img width="50" src="./output_refs/722.png" /> |
| 723 |  | night_fair   | <img width="50" src="./output_refs/723.png" /> |
| 724 |  | night_fair   | <img width="50" src="./output_refs/724.png" /> |
| 725 |  | night_fair tr rain_thunder | <img width="50" src="./output_refs/725.png" /> |
| 726 |  | night_fair tr rain | <img width="50" src="./output_refs/726.png" /> |
| 727 |  | night_fair tr rain | <img width="50" src="./output_refs/727.png" /> |
| 728 |  | night_fair tr rain | <img width="50" src="./output_refs/728.png" /> |
| 729 |  | night_fair tr rain | <img width="50" src="./output_refs/729.png" /> |
| 730 |  | mist tr sun | <img width="50" src="./output_refs/730.png" /> |
| 731 |  | night_fair tr mist | <img width="50" src="./output_refs/731.png" /> |
| 732 |  | night_fair st cloud | <img width="50" src="./output_refs/732.png" /> |
| 740 |  | night_fair st rain_thunder | <img width="50" src="./output_refs/740.png" /> |
| 760 |  | night_fair te snow_or_rain | <img width="50" src="./output_refs/760.png" /> |
| 770 |  | night_fair st snow_or_rain | <img width="50" src="./output_refs/770.png" /> |
| 781 |  | night_fair tr snow_or_rain | <img width="50" src="./output_refs/781.png" /> |
