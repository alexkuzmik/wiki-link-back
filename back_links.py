import argparse
import os

from concurrent.futures import ProcessPoolExecutor, as_completed
from urllib.parse import urljoin

from wiki_link_back.profiling import timeit
from wiki_link_back.link_processing import get_wiki_links


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url", type=str, help="URL address to wikipedia article"
    )
    parser.add_argument(
        "--workers",
        "-w",
        type=int,
        default=os.cpu_count()*2,
        help="Amount of worker processes to parallelize computations."
    )

    return parser.parse_args()


def is_back_link_task(url: str, src_url: str, baseurl: str) -> tuple[bool, str]:
    wiki_links = get_wiki_links(url, baseurl)
    return src_url in wiki_links, url


@timeit
def analyze_link() -> None:
    args = parse_arguments()
    src_url = args.url
    workers = args.workers

    baseurl = urljoin(src_url, '..')
    wiki_links = get_wiki_links(src_url, baseurl)

    with ProcessPoolExecutor(workers) as pool:
        is_back_link_futures = [
            pool.submit(
                is_back_link_task,
                wiki_link,
                src_url,
                baseurl
            )
            for wiki_link in wiki_links
        ]

        for is_back_link_future in as_completed(is_back_link_futures):
            is_back, url = is_back_link_future.result()
            if is_back:
                print(url)
            

if __name__ == '__main__':
    analyze_link()