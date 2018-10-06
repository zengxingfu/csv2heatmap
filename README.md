# csv2heatmap

Generate heatmap from csv data.

## Usage

Quick example.

First, Clone or download this repository:

```bash
git clone https://github.com/zengxingfu/csv2heatmap.git
cd csv2heatmap
```

Then, Copy all `csv` files to the `/data` directory:

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
