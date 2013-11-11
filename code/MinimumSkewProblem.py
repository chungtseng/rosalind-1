import sys


def get_min_skew(sequence):
    skew = 0
    min_skew =0
    min_skew_poses = []
    for pos, base in enumerate(sequence):
        skew = skew - (base == "C") + (base == "G")
        if skew == min_skew:
            min_skew_poses.append(str(pos + 1))
        elif skew < min_skew:
            min_skew = skew
            min_skew_poses = [str(pos + 1)]
        else:
            pass
    return min_skew_poses


def main():
    f = open(sys.argv[1])
    sequence = f.readline().strip()
    min_skew_poses = get_min_skew(sequence)
    print ' '.join(min_skew_poses)
if __name__ == '__main__':
    main()