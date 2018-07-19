<img src="https://github.com/hypar-io/sdk/blob/master/hypar_logo.svg" width="300px" style="display: block;margin-left: auto;margin-right: auto;width: 50%;">

# python-starter
A python starter project for Hypar.

The `python-starter` project is a python 3.6 module which references the [Hypar SDK](https://github.com/hypar-io/sdk) and uses the [Hypar CLI](https://github.com/hypar-io/sdk/tree/master/src/cli) to bootstrap your project.

## Prerequisites
- Install [Python 3.6](https://www.python.org/downloads/release/python-360/).

## Getting Started
- Fork this repository.
- Clone your fork of the repository locally.
- Edit the `hypar.json` to describe your function.

## Test
Although not a strict requirement of Hypar, your code should have tests. The python-starter project uses Python's `unittest` module. To run the tests you can do the following:
```
cd test
python -m unittest
```

## Preview
Hypar functions generate geometry in the form of [glTF](https://www.khronos.org/gltf/) models. One of the tests will generate a `model.glb` at the root of the repository. GlTF models can be previewed using the [online glTF viewer](https://gltf-viewer.donmccurdy.com/) or using the [glTF GitHub Chrome Extension](https://chrome.google.com/webstore/detail/gltf-preview-for-github/cokmplcldeedmnkojcinmmpjkpnalbci) which will show a preview button next to a `.glb` file in your repository.
