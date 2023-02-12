"""Console script for cheese_course."""

import fire


def help():
    print("cheese_course")
    print("=" * len("cheese_course"))
    print("量化芝识")


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
