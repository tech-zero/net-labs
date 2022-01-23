# How to switch between alternative Python Versions step by step instrucstions

## ```Step 1```

First step is to check what version python are available on your Ubuntu system.  To do so execute the following command: 

```ls /usr/bin/python*```

## ```Step 2```

Next, check if you already have python alternatives configured.  To do so, run:

```sudo update-alternatives --list python```

## ```Step 3```

In this step we are going to set two Python alternatives, namely it will by Python2 and Python3 alternative. Execute the following commands:

```linux
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 2
```

## ```Step 4```

Confirm that both alternatives are ready to be used:

```linux
sudo update-alternatives --list python
```

## ```Step 5``` 

Change to alternative python version. For example to change to Python 2 execute the following command:

```linux
sudo update-alternatives --config python
```

## ```Step 6```

Check your python version:

```linux
python -V
```

To switch to Python3 alternative ```Step 5``` and enter the selection number appropriate to your desired python version.
