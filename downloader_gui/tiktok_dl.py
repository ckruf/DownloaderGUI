import random


def download_from_tiktok(query: str) -> bool:
    """
    Mock download function. Simulates a download function which returns True if successful and False otherwise.

    :param query: keyword for searching videos
    :return: True if successful, False otherwise
    """
    print(f"Downloading videos for term '{query}'...")
    if random.randint(0, 1):
        print("download successful")
        return True
    else:
        print("download failed")
        return False
