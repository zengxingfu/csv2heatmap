# coding: utf-8
import csv
from json import dump
import os
import requests

ROOT = os.getcwd()


def geocode(address):
    api = 'https://restapi.amap.com/v3/geocode/geo'
    payload = {
        'key': '9a61156e93412c9ab957deb1e37da015',
        'address': address
    }
    r = requests.get(api, params=payload)
    return r.json()


def gen_standard_csv(file_name):
    cities_path = os.path.join(ROOT, 'data', 'cities', file_name)
    raw_data = []
    with open(cities_path, mode='r') as raw_file:
        f_csv = csv.DictReader(raw_file)
        for row in f_csv:
            res_data = geocode(row['address'])
            # print(res_data)
            # row['geocode'] = {
            #     'province': res_data['province'],
            #     'citycode': res_data['citycode'],
            #     'city': res_data['city'],
            #     'district': res_data['district'],
            #     'adcode': res_data['adcode'],
            #     'level': res_data['level'],
            #     'location': res_data['location']
            # }
            try:
                location = res_data['geocodes'][0]['location'].split(',')
                print(row['address'], location)
                raw_data.append({
                    'longitude': location[0],
                    'latitude': location[1],
                    'play_count_poi': row['play_count_poi'],
                    'address': row['address']
                })
            except IndexError as e:
                print('ERROR:', e)
                continue
            # print(row)
    with open(os.path.join(ROOT, 'data', file_name), 'w') as f:
        headers = ['longitude', 'latitude', 'play_count_poi', 'address']
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(raw_data)
    print('Done!')
    print('运行 python3 run.py 以生成热力图页面！')
    # return raw_data


def main():
    csv_files = []
    data_path = os.path.join(ROOT, 'data', 'cities')
    for file in os.listdir(data_path):
        if '.csv' in file:
            csv_files.append(file)
    if len(csv_files) == 1:
        gen_standard_csv(csv_files[0])
    elif len(csv_files) > 1:
        print('暂不支持批量处理，请至多保留 /data/cities 目录一个 csv 文件！')
    else:
        pass


if __name__ == '__main__':
    main()
