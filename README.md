# Bitbar Memrise

This application for Bitbar allows for you to see on the Menubar of your mac the amount of that are available for you to water on Memrise. The application is lightweight (I hope) and is something that should be easily installable.

What is BitBar? BitBar is a Mac application that allows for you to create programs in Ruby, Python or Shell and display informtion on your Menubar without requiring to create an Mac Application for it. Its very lightweight and versatile, check it [here](https://getbitbar.com/).

**WARNING**

Using a script like this, without a timeout ended up having a `Login Required` show up everytime I attempt to ping via this given script. This may be due to the lack of a client requesting the content, yet I dont use Memrise as often as I once did and this script no longer is being maintained by me.


# Install

1. Clone/Fork the repository.
2. Drag `memrise.py` to your `bitbar_plugins` folder.
3. Open Bitbar and press CMD + R.
4. **NOTE** [You must follow setup, instructions below.](#setup)

# Contribute

1. Fork repo.
2. Edit code.
3. Make a PR.
4. Submit said PR.

# Setup

You must have logged into Memrise prior to the setup of this script or the information will not be stored in your cookies as of yet.

**Note** I'm detailing the setup of this application inside of Chrome more specifically at this stage Chrome Canary, you may be able to do this with other browsers but I simply don't care to show how to do so.

1. Type in the omnibox `chrome://settings` (Or click [here](chrome://settings)).
2. Find `Content Settings` under `Advanced` or `Privacy and Security`, Click on `Cookies`
3. Inside of `All Cookies and Data` search for `memrise`
4. Grab the `CSRF` & `sessionid` values from `www.memrise.com` **NOT** `memrise.com`
5. Substitute those two values into the memrise.py script.
6. Poke around on endpoints until you find your COURSEID, a list of which can be found [here](https://github.com/carpiediem/memrise-enhancement-suite/wiki/Unofficial-Documentation-for-the-Memrise-API)

Theres no easy way to (or I was unable to at the time that I created this script) find your COURSEID that I could find quickly, the one however for Japanese i'm aware is `665`. 

# License

A copy of the MIT license can be found in `LICENSE.md`.

# Disclaimer

The reason this isn't on the main Bitbar repo is due to the nature of setup that it requires. It simply wouldn't have been done justice being placed in the main repo and left many people confused. Also the following..

- Yes, I know this is hacky and very bodged together.
- Yes, I realise that the API isn't public for a reason.
- Yes, this code is pretty poor and i'm using requests instead of aiohttp.

Therefore I am not responsible for any harm to your Memrise account as a result of this.
