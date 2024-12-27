# [assistant-tgbot](https://github.com/bishalqx980/assistant-tgbot) <img src="https://i.ibb.co/h7bL5bn/download.png" width="20px">

This is a Telegram bot designed to maintain the owner's anonymity (optional) by forwarding received messages directly to the owner. It also includes additional features such as broadcasting messages to all active users, retrieving user IDs and information, and more. The bot is developed using the `python-telegram-bot` library (v21.9).

**A simple assistant telegram bot**
- **This bot can be found as [Eva](https://t.me/EvaTheLovebot) on Telegram.**

**Looking for Ultimate All-in-one Telegram Bot?**
- **Checkout [tgbot](https://github.com/bishalqx980/tgbot)**

## How to deploy 🚀

<h3>Setup 📦</h3>

- Download & rename `sample_config.py` to `config.py` then fillup `config.py` file value's

<h6>⚠️ Don't share or upload the `config.py` any public place or repository</h6>

- `BOT_TOKEN` Get from [https://t.me/BotFather](https://t.me/BotFather) E.g. `123456:abcdefGHIJK...`
- `OWNER_ID` Get from bot by /id command E.g. `2134776547`
- `OWNER_USERNAME` Your Username E.g. paste like ✅ `bishalqx980` not ❌ `@bishalqx980`
- `MONGODB_URI` Get from [https://www.mongodb.com/](https://www.mongodb.com/) (Check Below for instruction)
- `DB_NAME` anything E.g. `MissCiri_db`
- `SERVER_URL` Remember this needs to be fill up after deployment ⚠️ (otherwise bot will goto sleep)

<h3>Creating MongoDB URI</h3>

- Signin/Signup on [MongoDB](https://www.mongodb.com/)
- on [MongoDB Atlas](https://cloud.mongodb.com/) create `New Project`
- After creating click on the project to access
- on the left side list, click on `Clusters` > create a `cluster`
- After creating again on the left side list, `Database Access` click on `ADD NEW DATABASE USER`

1. `Authentication Method`: `Password`

2. `Password Authentication`: give `username` and `password` (remember that)

3. on `Database User Privileges` section

4. `Built-in Role`: `Atlas admin`

5. Finally click on `Add User`

6. Now again goto `cluster` section and click on `connect`

7. `Connect to your application` section `Drivers`

8. `Connecting with MongoDB Driver` section `3. Add your connection string into your application code`

9. Here you can see something like `mongodb+srv://something:<db_password>@cluster9800.AA11.mongodb.net/?retryWrites=true&w=majority&appName=Cluster9800`

10. Remove the `<db_password>` from that URI and add your password which one you gave on `2. 'Password Authentication'`

🥳 Done you have created your `MongoDB_URI` successfully...

> **Note:** One last thing, on the left side list click on `Network Access` section click on `ADD IP ADDRESS` and set ip to `0.0.0.0/0` (Its important to access database without network restriction)


<h3>Deploy Section 🎯</h3>

<center><h3>🖥️ <u>Local deploy</u></h3></center>

----- **Windows** -----
- Required `python 3.11` or later
- Open `assistant-tgbot` directory on cmd
- Run on cmd `pip install -r requirements.txt`
- Finally `python main.py`

----- **Linux** -----
- Required `python 3.11` or later
- Open `assistant-tgbot` directory on shell
- Run on shell `pip install -r requirements.txt`
- Finally `python main.py`

<center><h3>📡 <u>Render deploy</u></h3></center>

- Signin/Signup on [Render](https://render.com/)
- Goto dashboard & create a New `Web Service`
- Select `Public Git repository` > `https://github.com/bishalqx980/tgbot`

- Then 👇
```
> Language: Docker
> Branch: main
> Instance Type: Free [or paid]
```

- Advanced option 👇
```
> Secret Files ⬇️
> Filename: 'config.py'
> File Contents: paste all content from 'sample_config.py' (make sure you filled up everything)
```

> **Note:** _If you face anyproblem accessing `Advanced option` then just click on `Create Web Service` then from `Environment` > `Secret Files` add the `config.py` values. Then restart/redeploy the web service._

> **Important:** _After deployment complete go to [Render Dashboard](https://dashboard.render.com/) and open your service then you can see service url on top left corner [https://example.onrender.com]() copy that and go to `Environment` on the left side list then `Secret Files` section and `Edit` the `SERVER_URL` with your service url. (**So that bot won't go to sleep**)_

**D.O.N.E 🥳**

## License 📝

_GPL-3.0_

<br>

_Original Creator_ - [@bishalqx980](https://t.me/bishalqx980)

```
𝓐 𝓹𝓻𝓸𝓳𝓮𝓬𝓽 𝓸𝓯

 ▄▄▄▄    ██▓  ██████  ██░ ██  ▄▄▄       ██▓    
▓█████▄ ▓██▒▒██    ▒ ▓██░ ██▒▒████▄    ▓██▒    
▒██▒ ▄██▒██▒░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒██░    
▒██░█▀  ░██░  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██░    
░▓█  ▀█▓░██░▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██████▒
░▒▓███▀▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░
▒░▒   ░  ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░
 ░    ░  ▒ ░░  ░  ░   ░  ░░ ░  ░   ▒     ░ ░   
 ░       ░        ░   ░  ░  ░      ░  ░    ░  ░
      ░                                        
                            based on python-telegram-bot lib
```
