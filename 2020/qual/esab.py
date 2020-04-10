import logging

MAX_QUERIES = 150


def solve(n):
    speaker = Speaker()
    left = []
    right = []
    even = []  # indexes where symmetrical bits are the same
    odd = []  # indexes where symmetrical bits are different
    i = 0
    read_left = True
    while i < n//2 and speaker.get_n_queries() <= MAX_QUERIES:
        if not speaker.get_n_queries() % 10 and i > 0:
            logging.warning("Quantum fluctuation happened")
            if not read_left:
                read_left = True  # Because we cannot know what happened to the bit if it symmetric is unknown
                left = left[:-1]
            # Complement indexes if first bit changed (sorry, proof why this works not available here)
            if even and speaker.get_int(even[0] + 1) != left[even[0]]:
                for e in even:
                    left[e] = int(not left[e])
                    right[e] = int(not right[e])
            if odd and speaker.get_int(odd[0] + 1) != left[odd[0]]:
                for o in odd:
                    left[o] = int(not left[o])
                    right[o] = int(not right[o])
        else:
            if read_left:
                left.append(speaker.get_int(i + 1))
            else:
                right.append(speaker.get_int(B - i))
                if left[i] == right[i]:
                    even.append(i)
                else:
                    odd.append(i)
                i += 1

            read_left = not read_left

        logging.warning("%s | %s" % (left, right[::-1]))

    output = left + right[::-1]
    output_str = "".join([str(i) for i in output])
    logging.warning("answer: %s" % output_str)
    res = speaker.get(output_str)
    if res != "Y":
        raise Exception("Wrong answer")


class Speaker:

    def __init__(self):
        self._n_queries = 0
        self.verbose = True

    def get(self, n):
        self.send(n)
        return self.receive()

    def get_int(self, n):
        return int(self.get(n))

    def get_n_queries(self):
        return self._n_queries

    def receive(self):
        x = input()
        if self.verbose:
            logging.warning("Received '%s'" % x)
        return x

    def send(self, n):
        self._n_queries += 1
        if self.verbose:
            logging.warning("Request number %d: '%s'" % (self._n_queries, n))
        if self._n_queries > MAX_QUERIES:
            raise Exception("Max queries reached")
        print(n, flush=True)


if __name__ == "__main__":
    T, B = [int(i) for i in input().split()]
    for t in range(T):
        logging.warning(">>> Case #%s" % (t + 1))
        solve(B)
