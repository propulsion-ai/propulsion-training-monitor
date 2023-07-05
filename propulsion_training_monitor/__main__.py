import argparse
import subprocess

from propulsion_training_monitor import (
    webhook_sender,
    )

def main():
    parser = argparse.ArgumentParser(
        description="KnockKnock - Be notified when your training is complete.")
    parser.add_argument("--verbose", required=False, action="store_true",
                        help="Show full command in notification.")
    subparsers = parser.add_subparsers()

    # Webhook
    webhook_parser = subparsers.add_parser(
        name="webhook", description="Send a POST before and after function " +
        "execution, with start and end status (sucessfully or crashed).")
    webhook_parser.add_argument(
        "--webhook-url", type=lambda s: s.split(","), required=True,
        help="The webhook url to notify")
    webhook_parser.set_defaults(sender_func=webhook_sender)

    args, remaining_args = parser.parse_known_args()
    args = vars(args)

    sender_func = args.pop("sender_func", None)

    if sender_func is None:
        parser.print_help()
        exit(1)

    verbose = args.pop("verbose")

    def run_func(): return subprocess.run(remaining_args, check=True)
    run_func.__name__ = " ".join(
        remaining_args) if verbose else remaining_args[0]

    sender_func(**args)(run_func)()


if __name__ == "__main__":
    main()
