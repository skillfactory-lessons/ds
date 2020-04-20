
def steps_to_guess(secret, initial_range):
    def guess_range(search_range, step=1):
        guess = int((search_range[0]+search_range[1]) / 2)
        if guess == secret:
            return step

        if guess > secret:
            left_part = (search_range[0], guess - 1)
            return guess_range(left_part, step + 1)
        else:
            right_part = (guess + 1, search_range[1])
            return guess_range(right_part, step + 1)

    return guess_range(initial_range)
