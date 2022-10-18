import argparse
from itertools import repeat
from multiprocessing.pool import ThreadPool
from pathlib import Path
from tarfile import TarFile
from zipfile import ZipFile

import torch


def parse_args():
    parser = argparse.ArgumentParser(
        description='Download datasets for training')
    parser.add_argument(
        '--dataset-name', type=str, help='dataset name', default='coco2017')
    parser.add_argument(
        '--save-dir',
        type=str,
        help='the dir to save dataset',
        default='data/COCO')
    parser.add_argument(
        '--delete',
        action='store_true',
        help='delete the download zipped files')
    parser.add_argument(
        '--threads', type=int, help='number of threading', default=4)
    args = parser.parse_args()
    return args


def download(url, dir, unzip=True, delete=False, threads=1):

    def download_one(url, dir):
        f = dir / Path(url).name
        if Path(url).is_file():
            Path(url).rename(f)
        elif not f.exists():
            print('Downloading {} to {}'.format(url, f))
            torch.hub.download_url_to_file(url, f, progress=True)
        if unzip and f.suffix in ('.zip', '.tar'):
            print('Unzipping {}'.format(f.name))
            if f.suffix == '.zip':
                ZipFile(f).extractall(path=dir)
            elif f.suffix == '.tar':
                TarFile(f).extractall(path=dir)
            if delete:
                f.unlink()
                print('Delete {}'.format(f))

    dir = Path(dir)
    if threads > 1:
        pool = ThreadPool(threads)
        pool.imap(lambda x: download_one(*x), zip(url, repeat(dir)))
        pool.close()
        pool.join()
    else:
        for u in [url] if isinstance(url, (str, Path)) else url:
            download_one(u, dir)


def download_data():
    args = parse_args()

    path = Path(args.save_dir)
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    data2url = dict(
        # TODO: Support for downloading Panoptic Segmentation of COCO
        coco2017=[
            'http://images.cocodataset.org/zips/train2017.zip',
            'http://images.cocodataset.org/zips/val2017.zip',
            # 'http://images.cocodataset.org/zips/test2017.zip',
            'http://images.cocodataset.org/annotations/' + 'annotations_trainval2017.zip'
        ])
    url = data2url.get('coco2017', None)
    if url is None:
        print('Only support COCO now!')
        return
    download(url, dir=path, unzip=True, delete=args.delete, threads=args.threads)


if __name__ == '__main__':
    download_data()
