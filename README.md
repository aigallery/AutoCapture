# Auto capture the scroll screen

## Package the .py to .exe

```shell
pyinstaller --onefile --noconsole your_script.py
```

## MousePositionDisplay

give you the current position x and y of your mouse.

![](https://cdn.staticaly.com/gh/HongdaChen/image-home@master/image.68piuuy8dy40.webp)

## AutoCapture

- fill your interested area left top and right bottom position which can be got by MousePositionDisplay.

- click count means how many "next page button" been clicked before the next capture starting. "next page button" which position is `Click X Position` and `Click Y Position` does not mean realy next page, if it does, then there is no need for click count. 

- button includes left click and right click. always be left, it will be OK for right if you can extend the source code to more complex procedure.

![](https://cdn.staticaly.com/gh/HongdaChen/image-home@master/image.1fztf9qglqzk.webp)


