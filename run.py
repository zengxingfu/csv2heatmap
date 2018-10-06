# coding: utf-8
import os
from script.main import HeatmapMaker, ROOT
from config import CONF


def main():
    # workflow
    # 1. 创建实例，读取 data 下的文件
    print('正在创建实例……')
    maker = HeatmapMaker()
    print('csv数量：%d' % len(maker.csv_files))

    for file in maker.csv_files:
        print(file)
    # 2. 生成 json 数据
        print('正在生成json数据文件……')
        csv_path = os.path.join(ROOT, 'data', file)
        json_data = maker.gen_json(csv_path, CONF)
    # 3. 打包
        print('正在打包……')
        maker.pack(file[:-4], json_data, CONF)
    # 4. 归档csv数据
        print('正在归档csv文件……')
        maker.archive_csv(file)
    print('Done!')
    print('热力图在 /dist 目录下')


if __name__ == '__main__':
    main()
