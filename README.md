# csv2heatmap

Generate heatmap from csv data.

## Usage

Quick example.

First, clone or download this repository:

```bash
git clone https://github.com/zengxingfu/csv2heatmap.git
cd csv2heatmap
```

Then, copy all `csv` files to the `/data` directory:

⚠️The header of the csv file needs to be defined like this: `longitude,latitude,play_count_poi`.

```bash
cp **/*.csv /data/*.csv
```

And now, you can run the script:

```bash
python3 run.py
```

All processes will be completed automatically. The csv file that has been processed will be archived to the `/data/archive` directory.

## Config

Of course, you can also modify the following configuration (`config.py`) as needed.

```python
# coding: utf-8

CONF = {
    # 取值变量
    'poi': 'play_count_poi',

    # 地图样式、中心点、缩放级别
    'amap': {
        'mapStyle': 'amap://styles/dark',
        'resizeEnable': True,
        'center': [108.9398400000, 34.3412700000],
        'zoom': 5  # 若为城市，建议值为11
    },

    # 热力图设置
    'heatmap': {
        'radius': 35,
        'opacity': [0, 0.8]
        # 'gradient': {
        #     0.5: 'blue',
        #     0.65: 'rgb(117,211,248)',
        #     0.7: 'rgb(0, 255, 0)',
        #     0.9: '#ffea00',
        #     1.0: 'red'
        # }
    },
    # 最大值（体现为红色）
    'max': 5000000
}
```

## Toolkit

### geocode

Copy the original csv file to the `/data/cities` directory.

⚠️The header of the csv file needs to be defined like this: `address,play_count_poi`.

```bash
python3 script/geo.py
```

The new standard csv file will be saved in the `/data/` directory.

Example:

| **longitude**  | **latitude** | **play_count_poi** | **address** |
| -------------- | ------------ | ------------------ | ----------- |
| **95.595761**  | 31.412405    | 181963             | 丁青县      |
| **105.305138** | 27.298494    | 5842683            | 七星关区    |
| **110.317826** | 25.252701    | 1741160            | 七星区      |
| ……             |              |                    |             |

Just run:

```bash
python3 run.py
```
