def solution(participant, completion):
    participant.sort()
    print(participant)
    completion.sort()
    print(completion)
    for c in range(len(completion)):
        if participant[c] != completion[c]:
            return participant[c]
    return participant[c+1]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

solution