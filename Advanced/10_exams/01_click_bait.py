from collections import deque

suggested_links = deque(int(sl) for sl in input().split())
featured_articles = [int(fa) for fa in input().split()]
target_value = int(input())
final_feed_collection = []

while suggested_links and featured_articles:
    sg = suggested_links.popleft()
    fa = featured_articles.pop()
    if fa > sg:
        remainder = fa % sg
        final_feed_collection.append(abs(remainder))
        if remainder != 0:
            featured_articles.append(remainder * 2)
    elif sg > fa:
        remainder = sg % fa
        final_feed_collection.append(-abs(remainder))
        if remainder != 0:
            suggested_links.append(remainder * 2)
    else:
        final_feed_collection.append(0)
print(f"Final Feed: {', '.join(map(str, final_feed_collection))}")

if sum(final_feed_collection) >= target_value:
    print(f"Goal achieved! Engagement Value: {sum(final_feed_collection)}")
else:
    print(f"Goal not achieved! Short by: {target_value - sum(final_feed_collection)}")
