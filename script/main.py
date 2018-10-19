# coding: utf-8
import csv
from json import dumps
import os
import shutil
from config import CONF

ROOT = os.getcwd()


class HeatmapMaker(object):

    def __init__(self):
        data_path = os.path.join(ROOT, 'data')
        for file in os.listdir(data_path):
            if '.csv' in file:
                self.csv_files.append(file)

    csv_files = []

    def gen_json(self, csv_file, config):
        data = []
        with open(csv_file, 'r', encoding='utf-8') as cf:
            reader = csv.reader(cf)
            for row in reader:
                if row[2] == config['poi']:
                    continue
                # print(row)
                data.append({
                    'lng': row[0],
                    'lat': row[1],
                    'count': int(row[2])
                })
        # archive_path = os.path.join(ROOT, 'data', 'archive')
        return data

    def pack(self, page_name, data, config):
        # 复制模板文件
        dist_path = os.path.join(ROOT, 'dist', page_name)
        template_path = os.path.join(ROOT, 'template')
        shutil.copytree(template_path, dist_path)

        # 写入 data.js
        json_path = os.path.join(dist_path, 'data.js')
        with open(json_path, 'w') as jf:
            # dump(data, jf)
            jf.write('var heatmapData = ')
            jf.write(dumps(data))

        # 写入 config.js
        conf_path = os.path.join(dist_path, 'config.js')
        with open(conf_path, 'w') as cf:
            cf.write('var CONF = ')
            cf.write(dumps(config))

        # 写入 style.css
        style_path = os.path.join(dist_path, 'style.css')
        with open(style_path, 'w') as sf:
            if CONF['hide_map_element']:
                sf.write(
                    '''#container > div.amap-maps > div > div.amap-layers > canvas.amap-layer,#container > div.amap-maps > div > div.amap-layers > canvas.amap-labels { display: none !important; }
                    ''')
            else:
                sf.write('''#container > div.amap-maps > div > div.amap-layers > canvas.amap-layer,#container > div.amap-maps > div > div.amap-layers > canvas.amap-labels { }
                ''')
        # print(json_file, 'generated!')

    def archive_csv(self, csv_file):
        csv_path = os.path.join(ROOT, 'data', csv_file)
        dst_path = os.path.join(ROOT, 'data', 'archive', csv_file)
        shutil.move(csv_path, dst_path)


def main():
    # from configparser import ConfigParser
    # cf = ConfigParser()
    # cf.read('config.ini')
    # print(cf.get('data', 'poi'))

    # csv_path = os.path.join(ROOT, 'data', 'shenzhen.csv')
    # pack('ohoho', gen_json(csv_path))
    pass


if __name__ == '__main__':
    main()
