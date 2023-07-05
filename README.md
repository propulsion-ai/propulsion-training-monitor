
# Propulsion Training Monitor

## Introduction

Propulsion Training Monitor is a Python library designed to help machine learning practitioners keep track of their model's training status. It provides a simple and intuitive interface for monitoring the progress of your model training, allowing you to stay updated on the performance of your model throughout the training process.

## Installation
*Private access only as of now.*
```python
pip install git+ssh://git@github.com/propulsion-ai/propulsion-training-monitor.git#egg=propulsion_training_monitor
```

## Examples

Here are some examples of how you can use the Propulsion Training Monitor:

### Webhook
Supports POST requests.
```python
from propulsion_training_monitor import webhook_sender

@webhook_sender(webhook_url="Your url")
def train(params):
    import time
    time.sleep(10000)
    return {'loss': 0.9} # Optional return value
```

## Contributions

We welcome contributions from the community. If you have a feature request, bug report, or proposal for improving Propulsion Training Monitor, please open an issue on our GitHub page. For significant changes, please open a pull request so we can discuss the potential impact and benefits. Please make sure to update tests as appropriate.

## Inspirations

The Propulsion Training Monitor was majorly inspired by the [Knock Knock](https://github.com/huggingface/knockknock/tree/master) library. We noticed the need for a more streamlined and intuitive way for machine learning practitioners to monitor their model's training status. This tool aims to fill that gap, providing a simple interface for tracking the progress of your model training.

## License

Propulsion Training Monitor is released under the Apache 2.0 License. See [LICENSE](https://github.com/propulsion-ai/propulsion-training-monitor/blob/main/LICENSE) for more information.