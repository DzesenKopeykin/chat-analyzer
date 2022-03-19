#!/usr/bin/env python
import json


def analyze():
    with open("statistics/sticker_statistics.json", "r") as f:
        sticker_statistics = json.load(f)

    analyzed_stats = {}

    for sticker in sticker_statistics:
        emoji = sticker["sticker"]
        author = sticker["author"]

        if author not in analyzed_stats:
            analyzed_stats[author] = {}
        if emoji not in analyzed_stats[author]:
            analyzed_stats[author][emoji] = 0
        analyzed_stats[author][emoji] += 1

    analyzed_stats = {}
    for author in analyzed_stats.keys():
        analyzed_stats[author] = list(analyzed_stats[author].items())
        analyzed_stats[author].sort(key=lambda e: e[1], reverse=True)

    for author in analyzed_stats.keys():
        print(author, "-" * 100)
        print(analyzed_stats[author])

    with open("statistics/analyzed_stats.json", "w") as f:
        json.dump(analyzed_stats, f)


if __name__ == "__main__":
    analyze()
