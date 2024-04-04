def solution(genres, plays):
    answer = []
    genre_play = {}
    genre_total_play = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre_play.keys():
            genre_play[genre].append((idx, play))
            genre_total_play[genre] += play
        else:
            genre_play[genre]= [(idx, play)]
            genre_total_play[genre] = play
    for key, value in sorted(genre_total_play.items(), key=lambda item: item[1], reverse=True):
        items = genre_play[key]
        for idx, ans in enumerate(sorted(items, key=lambda x: x[1], reverse=True)):
            if idx > 1: break
            answer.append(ans[0])
    return answer