# fitbit-file-saver
A Python server that saves files from a Fitbit OS app.

A phone-based server is used to receive the files. This avoids the need to use `https`, which can be difficult to set up on a LAN.

This demonstration transfers accelerometer data, which is probably the most demanding use case. The same architecture should be fine for streaming heart rate, step count, *etc*.
## Architecture
This repository consists of two main components:
* `fitbit`. This is a Fitbit OS app comprising a device (watch) component and a companion (phone) component. Accelerometer data is passed from the device to the companion using file transfer. The companion then uses `fetch()` to `POST` each file to the `server` component. `GET` requests are used to pass server control commands.
* `server`. An HTTP server (written in Python) is used to receive files `POST`ed from the Fitbit companion and save them on the phone. `GET` requests are also decoded but are not used.

## Usage
### Installation and Configuration
#### Fitbit
* Download or clone the `fitbit` app’s files.
* In `companion/index.js`, verify that `httpURL` is appropriate to your phone. (The default should be fine on Android.)
* Build the app (named `File Saver`) using the Fitbit development CLI.
* Install the app onto a watch (although it can also run on the Fitbit Simulator).
#### Server
* Install a Python 3.5+ execution environment on the phone on which the Fitbit companion component (*ie*, Fitbit mobile app) will run. For Android, you can use [pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3). For iOS, [Pythonista 3](http://omz-software.com/pythonista/index.html) might work (untested).
* In `file-saver.py`, set the port specified in the `HTTPServer` call to match that specified in `companion/index.js`’s `httpURL`.
* Copy `server/file-saver.py` to a directory on your phone from which Python can run it.

### Start-up
* Using Python on your phone, run `file-saver.py`.
* On your watch, run the `File Saver` app.

### Running
* Use the `File Saver` app on the watch to record some accelerometer data, and then transfer it to the phone.
* You can monitor the transfers on the watch or the companion settings page.
* After transfer, files should be available on the phone in the same directory as `file-saver.py`.

## Issues
* Python’s `HTTP.server` and this repository’s `file-saver.py` are insecure. Use at your own risk.
* There is minimal error checking or recovery.
* Python’s `HTTP.server` is slow (but should be able to keep up with Fitbit’s file transfer).
* If you restart either component, connection(s) may not automatically reopen. You may need to restart the other component.
* In this demonstration, binary messages are used for watch-to-companion file transfers, because the watch-to-companion connection (in particular) can be slow. Using text (string) files should be possible but will take longer to transfer (conceivably by a factor of 10). If you use text files, be aware that the server won’t attempt to convert end-of-line characters.
* The `server` should save files without changing their content or format, so the use of binary or text files should be possible (untested).
* File transfer and `fetch()` aren't well-suited to streaming data in real-time. For streaming, use WebSockets. See the [fitbit-stream-bridge](https://github.com/gondwanasoft/fitbit-stream-bridge) repository for an example.
* The Fitbit component is based on [fitbit-accel-fetcher](https://github.com/gondwanasoft/fitbit-accel-fetcher), and probably contains some irrelevant artefacts. Please see the `README` there for more information.
* The server doesn't attempt to combine (*ie*, merge or append) files even when they represent successive sets of readings. You could implement this on receipt of an HTTP `GET` command.
* If you don't want to install Python, [android-fitbit-fetcher](https://github.com/gondwanasoft/android-fitbit-fetcher) provides source code for a native Java server than runs on Android.

## Acknowledgements

*  `file-saver.py` contains snippets from [realpython](https://realpython.com/python-http-server/).
* `File Saver`’s icon was adapted from [friconix](https://friconix.com/icon/fi-xtluxl-file-thin/).