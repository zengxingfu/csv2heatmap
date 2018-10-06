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
