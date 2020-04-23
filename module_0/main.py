from statistics import mean

from module_0.algorithm import steps_to_guess

if __name__ == "__main__":
    guess_interval = (1, 100)
    steps = [steps_to_guess(x, guess_interval) for x in range(guess_interval[0], guess_interval[1] + 1)]
    print("Average number of steps for interval %s is %.2f" % (guess_interval, mean(steps)))
